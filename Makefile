PKG_NAME := mvn-servlet-api
URL = https://repo1.maven.org/maven2/org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.jar
ARCHIVES = https://repo1.maven.org/maven2/org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.pom :  https://repo1.maven.org/maven2/javax/servlet/servlet-api/2.3/servlet-api-2.3.jar : https://repo1.maven.org/maven2/javax/servlet/servlet-api/2.3/servlet-api-2.3.pom : https://repo.maven.apache.org/maven2/javax/servlet/servlet-api/2.3/servlet-api-2.3.pom : https://repo.maven.apache.org/maven2/javax/servlet/servlet-api/2.3/servlet-api-2.3.jar :

include ../common/Makefile.common
