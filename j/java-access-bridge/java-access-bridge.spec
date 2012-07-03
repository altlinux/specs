Name: java-access-bridge
Version: 1.24.0
Release: alt2_jvm6
BuildArch: noarch
Summary: This package connects accessibility support in Java Swing to AT-SPI
Url: http://live.gnome.org/
License: %gpl2plus

Group: Accessibility
Packager: Michael Pozhidaev <msp@altlinux.ru>

# Automatically added by buildreq on Sat Oct 25 2008
BuildRequires: libat-spi xprop

BuildRequires(pre): rpm-build-java rpm-build-licenses
BuildRequires: jpackage-utils
BuildRequires: java-devel-sun >= 1.6.0
BuildRequires: libbonobo-devel libat-spi-devel

Source: http://ftp.gnome.org/pub/GNOME/sources/java-access-bridge/1.24/%name-%version.tar.gz

%description
This package contains the Java Access Bridge for GNOME, 
which connects the built-in accessibility support in
Java Swing apps to the GNOME Accessibility framework,
specifically the Assistive Technology Service Provider
Interface (AT-SPI).

%prep
%setup -q

%build
%configure --with-java-home=%_jvmdir/java-1.6.0-sun
%make_build

%install
%__install -d %buildroot%{_javadir}-ext
%__install -pD gnome-java-bridge.jar %buildroot%{_javadir}-ext/gnome-java-bridge.jar
%__install -pD bridge/accessibility.properties %buildroot%{_javadir}-ext/accessibility.properties

rln()
{
	local target=$1 && shift
	local source=$1 && shift
	target=`relative "$target" "$source"`
	ln -snf "$target" "%buildroot$source"
}
mkdir -p %buildroot%_javadir-1.6.0
#add_jvm_extension gnome-java-bridge gnome-java-bridge 1.6.0
rln %_javadir-ext/gnome-java-bridge.jar %_javadir-1.6.0/gnome-java-bridge.jar

%files
%doc AUTHORS INSTALL ChangeLog COPYING NEWS README 
%doc bridge/accessibility.properties
%{_javadir}-ext/gnome-java-bridge.jar
%{_javadir}-ext/accessibility.properties
%{_javadir}-1.*/gnome-java-bridge.jar

%changelog
* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 1.24.0-alt2_jvm6
- restored lost gnome-java-bridge.jar (due to misprint)

* Mon Dec 01 2008 Igor Vlasenko <viy@altlinux.ru> 1.24.0-alt1_jvm6
- added BuildRequires: rpm-build-java
- packaged to java-ext dir
- new version that corresponds to gnome 2.24

* Sat Oct 25 2008 Michael Pozhidaev <msp@altlinux.ru> 1.22.2-alt1
- Initial RPM

