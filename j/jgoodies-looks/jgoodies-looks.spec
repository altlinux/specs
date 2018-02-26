
Name: jgoodies-looks
Version: 2.1.4
Release: alt3

License: BSD style
Group: Development/Java
Summary: JGoodies Looks is a library that makes your Swing applications and applets look better

Requires: jgoodies-forms
BuildRequires: rpm-build-java ant unzip jgoodies-forms
BuildRequires: java-devel-default
BuildArch: noarch

Url: http://www.jgoodies.com/downloads/libraries.html
Packager: Michael Pozhidaev <msp@altlinux.ru>

Source: looks-2_1_4.zip

Patch0: looks-2.1.4-alt-build.diff
Patch1: looks-2.1.4-alt-javadoc.diff

%description
JGoodies Looks is a library that makes your Swing applications and applets look better. The package
consists of a Windows look&feel and the Plastic look&feel family. These
have been optimized for readability, precise micro-design and
usability.

%package javadoc
Summary: API documentation for %name
Group: Development/Java
Requires: java-common
%description javadoc
Auto-generated API documentation for the %name.jar.

%prep
%setup -q -n looks-%version
%patch0 -p1
%patch1 -p1
rm -rf ./docs/api
rm -rf lib/forms-1.0.7.jar
ln -s /usr/share/java/jgoodies-forms.jar ./lib/forms.jar

%build
mkdir extracting
mv ./looks-2.1.4.jar ./extracting
cd ./extracting
unzip ./looks-2.1.4.jar
cd ..
mkdir -p './conf/service descriptors'
mv './/extracting/META-INF/services/javax.swing.LookAndFeel' './conf/service descriptors/all.txt'
ant javadoc
ant jar

%install
mkdir -p %buildroot/%_javadir
install -m 644 ./build/looks.jar %buildroot/%_javadir/%name-%version.jar
ln -s %_javadir/%name-%version.jar %buildroot/%_javadir/%name.jar

mkdir -p %buildroot/%_javadocdir/%name
cp -r ./build/docs/api/* %buildroot/%_javadocdir/%name

%files
%_javadir/*
%doc docs/* LICENSE.txt README.html RELEASE-NOTES.txt

%files javadoc
%_javadocdir/*

%changelog
* Wed Sep 23 2009 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt3
- jpackage-utils build req replaced by rpm-build-java (closes: #21517)

* Sun Oct 26 2008 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt2
- Added java-devel-default

* Wed Apr 30 2008 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt1
- Initial RPM.

