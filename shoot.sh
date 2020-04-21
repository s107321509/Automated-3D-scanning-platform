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
    # 照片命名
    gphoto2 --capture-image --filename $IMG
};
capture # 持續拍照
