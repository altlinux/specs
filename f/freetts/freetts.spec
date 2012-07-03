
Name: freetts
Version: 1.2.1
Release: alt3
BuildArch: noarch
License: Custom, see license.terms for further information
Group: Development/Java
Summary: Text-to-Speech engine written on Java and based on Flite speech synthesizer
Packager: Michael Pozhidaev <msp@altlinux.ru>

Requires: jsapi

Source: %name-%version-src.zip
Source1: jsapi_license.txt

Patch0: %name-1.2.1-alt-confirm.patch

# Automatically added by buildreq on Thu Sep 11 2008
BuildRequires: ant jakarta-commons-logging log4j sharutils unzip xalan-j2

BuildRequires: java-devel-default

# Tool script contains the stupid reference to non-existing file /tmp/foo.sh:
%add_findreq_skiplist /usr/share/freetts/tools/ArcticToFreeTTS/ArcticToFreeTTS.sh

%description
FreeTTS is a speech synthesis system written entirely in the Java programming language. It is based upon Flite, a small, fast, run-time speech
synthesis engine, which in turn is based upon University of Edinburgh's
Festival Speech Synthesis System and Carnegie Mellon University's
FestVox project.

%package javadoc
Group: Development/Java
Summary: javadoc documentation for FreeTTS

%description javadoc
javadoc documentation for FreeTTS speech system.

%package demo
Group: Development/Java
Requires: %name
Summary: Demos for FreeTTS

%description demo
Demos for FreeTTS speech synthesizer.

%package -n jsapi
Group: Development/Java
Summary: Java Speech API
License: Sun Binary Code License
URL: http://java.sun.com/products/java-media/speech/

%Description -n jsapi
With the Java Speech API you can incorporate speech
technology into user interfaces for your applets and
applications based on Java technology.

%prep
rm -rf ./META-INF

%setup -q 
%patch0 -p1
%build
cd lib
chmod 755 jsapi.sh
./jsapi.sh
cd ..
ant jars
rm -f docs/Makefile
cp %SOURCE1 lib/LICENSE

%install
install -d -m 755 %buildroot%_javadir
cd lib
install -pD -m 644 *.jar %buildroot%_javadir/ 
cd ..

install -d -m 755 %buildroot%_javadocdir/%name
cd javadoc
cp -r ./* %buildroot%_javadocdir/%name/
cd ..

install -d -m 755 %buildroot%_datadir/%name/demo
cd demo
cp -r ./* %buildroot%_datadir/%name/demo/
cd ..

install -d -m 755 %buildroot%_datadir/%name/tools
cd tools
cp -r ./* %buildroot%_datadir/%name/tools/
cd ..

%files
%doc acknowledgments.txt ANNOUNCE.txt docs index.html license.terms overview.html README.txt RELEASE_NOTES
%_javadir/cmudict04.jar
%_javadir/cmulex.jar
%_javadir/cmu_time_awb.jar
%_javadir/cmutimelex.jar
%_javadir/cmu_us_kal.jar
%_javadir/en_us.jar
%_javadir/freetts.jar
%dir %_datadir/%name
%_datadir/%name/tools

%files javadoc
%_javadocdir/%name

%files demo
%_datadir/%name/demo

%files -n jsapi
%_javadir/jsapi.jar
%doc lib/LICENSE



%changelog
* Mon Oct 27 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.1-alt3
- Added java-devel-default

* Fri Sep 12 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.1-alt2
- Added tools

* Wed Sep 10 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.1-alt1
- Initial RPM

