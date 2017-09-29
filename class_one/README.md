>代码测试环境为Ubuntu14 Python 3.6.1 Keras 2.0.8 TensorFlow 1.3.1 GPU
Python 包环境为Anaconda 4.4，在安装Keras时同时安装了Tensorflow，因为
conda安装和pip可以重复，具体使用的时候并不知道究竟是用的是那个TensorFlow，
希望对后来修改此代码的人有所帮助

# 说明 
本代码是基于FastAI原代码修改而成，主要添加替换已经不在支持的Keras1的相关函数，修改部分参数以适应Keras2和Python3
# 已知bug
代码运行的时候会有警告，虽然能运行出结果。具体原因可能和导入的utils里面的包相关，因为代码的函数很多都是在Keras1下运行的，原因可能处在这个函数里面。我修改了一部分，但是依旧出现错误，希望后来的修改者能帮助改进，同时将修改结果告知我。多谢。
Email:bleedingfight@126.com
