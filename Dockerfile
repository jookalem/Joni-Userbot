# Using Python Slim-Buster
FROM kyyex/kyy-userbot:busterv2
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Joni-Userbot ━━━━━

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
RUN git clone -b Joni-Userbot https://github.com/jookalem/Joni-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/jookalem/joni-Userbot/Joni-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
