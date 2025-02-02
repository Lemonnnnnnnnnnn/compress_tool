import os
import subprocess
import platform
from src.logger import logger
from src.utils import get_resource_path, get_size

def get_7z_command():
    """获取对应平台的7z命令"""
    system = platform.system().lower()
    if system == 'windows':
        # Windows下使用打包的7z.exe
        seven_zip_path = get_resource_path(os.path.join('resources', '7z.exe'))
        if not os.path.exists(seven_zip_path):
            raise FileNotFoundError("未找到7z.exe，请确保它在resources目录中")
        return seven_zip_path
    elif system == 'darwin':
        # macOS通常通过brew安装p7zip
        return '7za'
    else:
        # Linux通常通过包管理器安装p7zip-full
        return '7z'

def compress_with_7z(source_path, output_path, password, volume_size=None):
    """使用7z进行压缩，可选分卷大小"""
    try:
        seven_zip_cmd = get_7z_command()
        
        cmd = [
            seven_zip_cmd,
            'a',
            '-t7z',
            f'-p{password}',
            '-mhe=on',
        ]

        if volume_size:
            cmd.append(f'-v{volume_size}')

        cmd.extend([output_path, source_path])
        
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            raise Exception(f"7z压缩失败: {stderr}")
        
        logger.info(f"成功使用7z压缩: {output_path}")
        return True
    except Exception as e:
        logger.error(f"7z压缩失败: {str(e)}")
        raise

def compress_item(item_path, output_path, password, password2):
    try:
        logger.info(f"开始压缩: {item_path}")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        size = get_size(item_path)
        TWO_GB = 2 * 1024 * 1024 * 1024
        
        output_base = output_path.rsplit('.', 1)[0] + '.7z'
        
        if size >= TWO_GB:
            logger.info(f"文件大小超过2GB，使用分卷压缩: {size/1024/1024/1024:.2f}GB")
            compress_with_7z(item_path, output_base, password, volume_size="2g")
        else:
            logger.info(f"文件大小小于2GB，使用双层压缩: {size/1024/1024:.2f}MB")
            
            temp_path = output_base + '.temp'
            compress_with_7z(item_path, temp_path, password)
            
            compress_with_7z(temp_path, output_base, password2)
            
            try:
                os.remove(temp_path)
            except Exception as e:
                logger.warning(f"删除临时文件失败: {str(e)}")
        
        logger.info(f"成功压缩: {output_base}")
    except Exception as e:
        logger.error(f"压缩失败: {item_path} -> {output_base}")
        logger.error(f"错误详情: {str(e)}")
        temp_path = output_base + '.temp'
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except:
                pass
        raise 