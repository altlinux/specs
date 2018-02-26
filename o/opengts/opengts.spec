Name: opengts
Version: 2.2.8
Release: alt4

Summary: Open GPS Tracking System
License: ASL 2.0
Group: Networking/Other
Url: http://www.opengts.org/

Source: %name-%version.tar

#barbarian method
Patch0: %name-2.2.8-alt-build.patch

Patch1: %name-2.2.8-alt-interface.patch
Patch2: %name-2.2.8-alt-query.patch

Requires: tomcat6 MySQL-server mysql-connector-java classpathx-mail java-1.6.0-sun-devel

BuildArch: noarch

BuildRequires(pre): /proc rpm-build-java
BuildRequires: ant tomcat6 classpathx-mail

%description
OpenGTS (Open Source GPS Tracking System) is intended to provide a generic
back-end web-based service for querying and viewing GPS related data

%package doc
Summary: Documentation for %name
Group: Development/Documentation

%description doc
Documentation for %name

%prep
%setup

%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
export CATALINA_HOME="/usr/share/tomcat6"
%ant all
%ant track
%ant track.war

%install
install -d -m 755 %buildroot/usr/share/opengts
install -d -m 755 %buildroot/usr/share/opengts/bin
install -d -m 755 %buildroot/usr/share/opengts/build
cp -pr bin/*.sh bin/*.pl %buildroot/usr/share/opengts/bin/
cp -p build/track.war %buildroot/usr/share/opengts/build/
cp -pr build/lib %buildroot/usr/share/opengts/build/
cp -pr sampleData %buildroot/usr/share/opengts/
cp -p *conf* %buildroot/usr/share/opengts/
cp -p *xml* %buildroot/usr/share/opengts/
cp -p *dtd* %buildroot/usr/share/opengts/
install -d -m 755 %buildroot/usr/share/tomcat6/webapps
ln -s /usr/share/opengts/build/track.war %buildroot/usr/share/tomcat6/webapps/track.war

%files
%doc CHANGELOG.txt LICENSE.txt README.txt
/usr/share/opengts
/usr/share/tomcat6/webapps/track.war

%files doc
%doc OpenGTS_Config.pdf

%changelog
* Mon Mar 21 2011 Timur Aitov <timonbl4@altlinux.org> 2.2.8-alt4
- Fixed build

* Mon Jan 31 2011 Timur Aitov <timonbl4@altlinux.org> 2.2.8-alt3
- Added dependences

* Mon Nov 29 2010 Timur Aitov <timonbl4@altlinux.org> 2.2.8-alt2
- modification in interface

* Tue Nov 16 2010 Timur Aitov <timonbl4@altlinux.org> 2.2.8-alt1
- initial build for ALT

