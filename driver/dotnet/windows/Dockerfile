FROM mcr.microsoft.com/windows/servercore:ltsc2019

ADD https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe C:\\tmp\\python-3.9.0.exe
RUN C:\\tmp\\python-3.9.0.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

ENV PYTHON=python3
ENV DOTNET_DRIVER_USING_LOCAL_SERVER=true
ENV TEST_NEO4J_USING_TESTKIT=true
