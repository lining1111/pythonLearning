import os
import subprocess
import psutil
import time
import platform


def is_process_running(process_name):
    """
    检查指定名称的进程是否正在运行
    :param process_name: 进程名称（不含扩展名）
    :return: 如果进程正在运行，则返回True；否则返回False
    """
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def start_process(executable_path):
    """
    启动指定的可执行文件
    :param executable_path: 可执行文件的路径
    """
    try:
        subprocess.Popen(executable_path)
        print(f"{executable_path} 已启动。")
    except Exception as e:
        print(f"无法启动 {executable_path}。错误: {e}")


list = [{'name': 'helloworld', 'path': 'helloworld'},
        {'name': 'helloworld1', 'path': 'helloworld1'}]


def chdir():
    # 获取当前脚本文件的绝对路径
    script_path = os.path.abspath(__file__)

    # 获取脚本文件所在的目录
    script_dir = os.path.dirname(script_path)

    # 打印脚本文件所在的目录
    print(f"脚本文件所在的目录是: {script_dir}")

    # 改变当前工作目录到脚本文件所在的目录
    os.chdir(script_dir)


def main():
    # 进入文件所在目录
    chdir()
    while True:
        for k, v in enumerate(list):
            if not is_process_running(v['name']):
                start_process(v['path'])
            # 等待一段时间再检查（例如：每5秒检查一次）
            time.sleep(5)


if __name__ == "__main__":
    main()
