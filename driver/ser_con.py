import serial

class SerialBase(object):

    def __init__(self, con_type, baud, time_out=1):
        """实例化串口对象"""
        self.ser = serial.Serial(con_type, baud, time_out)

    def get_info(self):
        """获得一些串口初始化信息"""
        return f"{self.ser.name}:{self.ser.port}"

    def open_ser(self):
        """打开端口"""
        self.ser.open()

    def read_data(self, length):
        """指定读取字符"""
        return self.ser.read(length)

    def write_data(self, data):
        """写入数据"""
        recv = self.ser.write(data)
        if recv == len(data):
            return True
        else:
            return False


    def close_con(self):
        """关闭连接"""
        self.ser.close()