Name: valentina
Version: 0.3.0
Release: alt1

Summary: Pattern Making Application
License: GPLv3+
Group: Graphics

Url: https://github.com/dismine/Valentina
Source: %name-%version.tar

BuildRequires: gcc-c++ ccache
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: qt5-tools-devel >= 5.2.0

Requires: poppler-utils

# Disables debug packages and stripping of binaries:
%brp_strip_none %_bindir/* %_libdir/*

%description
Valentina is a cross-platform patternmaking program which allows designers
to create and model patterns of clothing. This software allows pattern
creation, using either standard sizing tables or an individual's set of
measurements. It blends new technologies with traditional methods to create
a unique pattern making tool.

%prep
%setup

%build
qmake-qt5 PREFIX=%buildroot%prefix Valentina.pro -r
%make_build

%install
export NO_DEBUGINFO_STRIP_DEBUG=true
%makeinstall_std
install -pDm644 dist/debian/%name.1 %buildroot%_man1dir/%name.1

%files
%doc README.txt LICENSE_GPL.txt
%_man1dir/%name.1*
%_bindir/valentina
%_libdir/libvpropertyexplorer.so
%_libdir/libvpropertyexplorer.so.*
%_libdir/libqmuparser.so
%_libdir/libqmuparser.so.*
%_datadir/applications/%name.desktop
%_datadir/pixmaps/*
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_datadir/%name/translations/*.qm
%dir %_datadir/%name/tables
%dir %_datadir/%name/tables/standard
%_datadir/%name/tables/standard/*.vst

%changelog
* Sat Mar 28 2015 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- built for ALT Linux (based on upstream spec)

* Mon Dec 22 2014 Roman Telezhinskyi
 - Initial build

