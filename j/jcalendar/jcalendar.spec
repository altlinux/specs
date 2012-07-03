
Name: jcalendar
Version: 1.3.2
Release: alt3

License: LGPL
Group: Development/Java
Summary: Graphic component to peek date in Java applications

BuildRequires: rpm-build-java ant jgoodies-forms jgoodies-looks unzip

BuildRequires: java-devel-default
BuildArch: noarch

Url: http://www.toedter.com/en/jcalendar/index.html
Packager: Michael Pozhidaev <msp@altlinux.ru>

Source: http://www.toedter.com/download/jcalendar-1.3.2.zip

Patch0: jcalendar-1.3.2-alt-build.diff

%description
JCalendar is a Java date chooser bean for graphically picking a date.
JCalendar is composed of several other Java beans, a JDayChooser, a
JMonthChooser and a JYearChooser. All these beans have a locale
property, provide several icons (Color 16x16, Color 32x32, Mono 16x16
and Mono 32x32) and their own locale property editor. So they can
easily be used in GUI builders. Also part of the package is a
JDateChooser, a bean composed of an IDateEditor (for direct date
editing) and a button for opening a JCalendar for selecting the date.

%package javadoc
Summary: API documentation for %name
Group: Development/Java
Requires: java-common
%description javadoc
Auto-generated API documentation for the %name.jar.

%prep
%setup -q
%patch -p1
rm -rf ./doc/api
rm -rf ./lib/%name-%version.jar ./looks-2.0.1.jar
ln -s %_javadir/jgoodies-looks.jar ./lib/looks.jar

%build
cd src
ant javadocs
mv ../doc/api ../doc/api_
ant jar
cd ..
mv doc/api_ doc/api

%install
mkdir -p %buildroot/%_javadir
install -m 644 ./lib/%name-%version.jar %buildroot/%_javadir/%name-%version.jar
ln -s %_javadir/%name-%version.jar %buildroot/%_javadir/%name.jar

mkdir -p %buildroot/%_javadocdir/%name
cp -r ./doc/api/* %buildroot/%_javadocdir/%name

%files
%_javadir/*
%doc doc/demo.html doc/images doc/index.html doc/license.html doc/style.css jcalendar-license.txt readme.txt

%files javadoc
%_javadocdir/*

%changelog
* Sat Sep 19 2009 Michael Pozhidaev <msp@altlinux.ru> 1.3.2-alt3
- jpackage-utils build req replaced by rpm-build-java (closes: #21514)

* Sun Oct 26 2008 Michael Pozhidaev <msp@altlinux.ru> 1.3.2-alt2
- Added java-devel-default

* Tue Apr 29 2008 Michael Pozhidaev <msp@altlinux.ru> 1.3.2-alt1
- Initial RPM
