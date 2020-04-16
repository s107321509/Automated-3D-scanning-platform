#/bin/bash

#BASENAME=$(date +%s_%F_%H:%M:%S_%N)

BASEDIR="/tmp/"
EXTENTION="jpg"

#repeat() {while true ;do $@; done;};
capture() {
    FOLDER="${BASEDIR}./$(date +%F/%H/%M)" && \
    IMG="$(date +%F_%H:%M:%S).${EXTENTION}"
    mkdir -p $FOLDER
    echo @___folder: [$FOLDER]
    echo @____image: [$IMG]
    # 照相命名并分类保存
    gphoto2 --capture-image --filename $IMG
    # echo  'hello(date +%s)' > $IMG && mv $IMG $FOLDER
    #read -t 1 || return
    # echo sleep 3 seconds && sleep 3 && echo sleep done
};

capture # 持续拍照
