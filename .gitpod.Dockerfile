FROM gitpod/workspace-full:latest
USER gitpod
RUN pip3 install pytest==4.4.2 pytest-testdox mock
RUN npm i -g @learnpack/learnpack@2.1.20 && learnpack plugins:install @learnpack/python@1.0.0
FROM gitpod/workspace-python

RUN pyenv install 3.8 \
    && pyenv global 3.8