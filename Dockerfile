# 设置基础镜像
FROM continuumio/miniconda3:latest

# 设置工作目录
WORKDIR /app

# 复制应用程序代码到容器中
COPY ./model .
COPY ./src .

# 安装依赖项
RUN conda create --name myenv python=3.9 \
    && echo "conda activate myenv" > ~/.bashrc \
    && source ~/.bashrc \

# 暴露端口号
EXPOSE 2333

# 启动应用程序
CMD [ "bash", "-c", "source ~/.bashrc && python ./src/test_server.py" ]