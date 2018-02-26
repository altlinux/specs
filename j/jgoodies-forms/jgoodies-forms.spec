
Name: jgoodies-forms
Version: 1.2.0
Release: alt3

License: BSD style
Group: Development/Java
Summary: %name is a framework that helps you lay out and implement elegant Swing panels quickly and consistently

Requires: java
BuildRequires: rpm-build-java ant unzip
BuildRequires: java-devel-default
BuildArch: noarch

Url: http://www.jgoodies.com/downloads/libraries.html
Packager: Michael Pozhidaev <msp@altlinux.ru>

Source: forms-1_2_0.zip

%description
%name is a framework that helps you lay out and implement elegant Swing panels quickly and
consistently. Forms makes simple things easy and the hard stuff
possible, the good design easy and the bad difficult.

%package javadoc
Summary: API documentation for %name
Group: Development/Java
Requires: java-common
%description javadoc
Auto-generated API documentation for the %name.jar.

%prep
%setup -q -n forms-%version
#msp:There was problem, javadoc on generation never exits.
#rm -rf ./docs/api
rm -rf ./*.jar

%build
#ant javadoc
ant jar
#rm -rf ./docs/api

%install
mkdir -p %buildroot/%_javadir
install -m 644 ./build/forms.jar %buildroot/%_javadir/%name-%version.jar
ln -s %_javadir/%name-%version.jar %buildroot/%_javadir/%name.jar

mkdir -p %buildroot/%_javadocdir/%name
cp -r ./docs/api/* %buildroot/%_javadocdir/%name

%files
%_javadir/*
%doc LICENSE.txt README.html RELEASE-NOTES.txt docs/*

%files javadoc
%_javadocdir/*

%changelog
* Sun Sep 20 2009 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt3
- jpackage-utils build req replaced by rpm-build-java (closes: #21516)

* Sun Oct 26 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt2
- Added jva-devel-default

* Tue Apr 29 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt1
- Initial RPM
