FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Joni-Userbot https://github.com/jookalem/Joni-Userbot /home/Joni-Userbot/ \
    && chmod 777 /home/Joni-Userbot \
    && mkdir /home/Joni-Userbot/bin/
WORKDIR /home/Joni-Userbot/
COPY ./sample_config.env ./config.env* /home/Joni-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
