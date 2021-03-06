#!/bin/sh
##SCRIPT DIR
DIR_NAME=`dirname "$0"`
DIR_NAME=`cd "$DIR_NAME"; pwd`
cd "${DIR_NAME}"
TUXNAME=tuxguitar3
##JAVA
if [ -z $JAVA ]; then
    JAVA=${JAVA_HOME}/bin/java
    [ ! -f ${JAVA} ] && JAVA=/usr/bin/java
    [ ! -f ${JAVA} ] && JAVA=java
fi
##MOZILLA_FIVE_HOME
if [ -z $MOZILLA_FIVE_HOME ]; then
    MOZILLA_FIVE_HOME=/usr/lib/firefox
    [ ! -d ${MOZILLA_FIVE_HOME} ] && MOZILLA_FIVE_HOME=/usr/lib/mozilla
    [ ! -d ${MOZILLA_FIVE_HOME} ] && MOZILLA_FIVE_HOME=/usr/lib/iceweasel
fi
##LIBRARY_PATH
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${MOZILLA_FIVE_HOME}
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib64
##CLASSPATH
CLASSPATH=${CLASSPATH}:/usr/share/java/${TUXNAME}/
CLASSPATH=${CLASSPATH}:/usr/share/${TUXNAME}/plugins/
CLASSPATH=${CLASSPATH}:/usr/share/java/${TUXNAME}/tuxguitar.jar
CLASSPATH=${CLASSPATH}:/usr/share/java/${TUXNAME}/tuxguitar-lib.jar
CLASSPATH=${CLASSPATH}:/usr/share/java/${TUXNAME}/tuxguitar-gm-utils.jar
CLASSPATH=${CLASSPATH}:/usr/share/java/${TUXNAME}/tuxguitar-awt-graphics.jar
CLASSPATH=${CLASSPATH}:/usr/share/java/${TUXNAME}/tuxguitar-editor-utils.jar
CLASSPATH=${CLASSPATH}:/usr/share/java/${TUXNAME}/swt.jar
CLASSPATH=${CLASSPATH}:/usr/share/java/${TUXNAME}/itext-pdf.jar
CLASSPATH=${CLASSPATH}:/usr/share/java/${TUXNAME}/itext-xmlworker.jar
##MAINCLASS
MAINCLASS=org.herac.tuxguitar.app.TGMainSingleton
##JVM ARGUMENTS
VM_ARGS="-Xmx512m"
##EXPORT VARS
export CLASSPATH
export LD_LIBRARY_PATH
export MOZILLA_FIVE_HOME

##LAUNCH
${JAVA} ${VM_ARGS} -cp :${CLASSPATH} -Dtuxguitar.share.path="/usr/share/${TUXNAME}" -Djava.library.path="${LD_LIBRARY_PATH}" ${MAINCLASS} "$1" "$2"
