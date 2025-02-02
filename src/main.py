import os
import json
from getpass import getpass
from logger import logger, setup_logging
from compression import compress_item
from utils import hash_filename

def main():
    try:
        setup_logging()
        logger.info("程序启动")
        print("=== 压缩工具配置 ===")
        source_folder = input("请输入源文件夹路径：").strip()
        output_folder = input("请输入输出文件夹路径：").strip()
        
        print("\n=== 第一层加密配置 ===")
        while True:
            password = getpass("请输入第一层压缩密码：").strip()
            confirm_pwd = getpass("请再次输入密码确认：").strip()
            if password == confirm_pwd:
                break
            print("错误：两次输入的密码不一致，请重新输入\n")
        
        print("\n=== 第二层加密配置 ===")
        while True:
            password2 = getpass("请输入第二层压缩密码：").strip()
            confirm_pwd = getpass("请再次输入密码确认：").strip()
            if password2 == confirm_pwd:
                break
            print("错误：两次输入的密码不一致，请重新输入\n")
        
        meta_file = input("\n请输入元数据文件名（默认 meta.json）：").strip() or "meta.json"

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            logger.info(f"创建输出目录: {output_folder}")

        meta_data = {
            "password": password,
            "password2": password2,
            "file_mapping": {}
        }

        logger.info("开始处理文件...")
        if os.path.isfile(source_folder):
            original_name = os.path.basename(source_folder)
            hashed_name = hash_filename(original_name)
            output_zip_path = os.path.join(output_folder, f"{hashed_name}.7z")
            compress_item(source_folder, output_zip_path, password, password2)
            meta_data["file_mapping"][hashed_name] = {
                "original_name": original_name,
                "is_file": True
            }
            logger.debug(f"已处理: {original_name} -> {hashed_name}.7z")
        elif os.path.isdir(source_folder):
            base_path = os.path.abspath(source_folder)
            for item in os.listdir(source_folder):
                full_path = os.path.join(base_path, item)
                hashed_name = hash_filename(item)
                output_zip_path = os.path.join(output_folder, f"{hashed_name}.7z")
                compress_item(full_path, output_zip_path, password, password2)
                meta_data["file_mapping"][hashed_name] = {
                    "original_name": item,
                    "is_file": os.path.isfile(full_path)
                }
                logger.debug(f"已处理: {item} -> {hashed_name}.7z")
        else:
            raise ValueError("输入路径不存在")

        with open(os.path.join(output_folder, meta_file), "w", encoding="utf-8") as f:
            json.dump(meta_data, f, indent=4, ensure_ascii=False)
            logger.info(f"元文件已保存: {meta_file}")

        print(f"\n压缩完成！元文件已保存到 {os.path.join(output_folder, meta_file)}")
        logger.info("程序执行完成")

    except Exception as e:
        logger.error(f"发生错误: {str(e)}", exc_info=True)
        print(f"\n错误发生: {str(e)}")
    
    if os.name == 'nt':
        input("\n按 Enter 键退出...")

if __name__ == "__main__":
    main() 