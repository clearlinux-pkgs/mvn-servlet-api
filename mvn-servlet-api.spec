#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-servlet-api
Version  : 2.5.20081211
Release  : 7
URL      : https://repo1.maven.org/maven2/org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.jar
Source0  : https://repo1.maven.org/maven2/org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.jar
Source1  : https://repo1.maven.org/maven2/org/mortbay/jetty/servlet-api-2.5/6.1.14/servlet-api-2.5-6.1.14.jar
Source2  : https://repo1.maven.org/maven2/org/mortbay/jetty/servlet-api-2.5/6.1.14/servlet-api-2.5-6.1.14.pom
Source3  : https://repo1.maven.org/maven2/org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-servlet-api-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-servlet-api package.
Group: Data

%description data
data components for the mvn-servlet-api package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api/2.5-20081211
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api-2.5/6.1.14
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api-2.5/6.1.14/servlet-api-2.5-6.1.14.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api-2.5/6.1.14
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api-2.5/6.1.14/servlet-api-2.5-6.1.14.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api/2.5-20081211
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api-2.5/6.1.14/servlet-api-2.5-6.1.14.jar
/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api-2.5/6.1.14/servlet-api-2.5-6.1.14.pom
/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.jar
/usr/share/java/.m2/repository/org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.pom
