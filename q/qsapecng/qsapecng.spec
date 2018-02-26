%define origname QSapecNG

Name: qsapecng
Version: 1.2.2
Release: alt1
Summary: QSapecNG is a Qt-based program for symbolic analysis of linear analog circuits
License: GPLv3
Group: Development/C++
Source: %origname-%version-source.tar
URL: http://qsapecng.sourceforge.net/
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

BuildRequires: cmake gcc-c++
BuildRequires: libqt4-devel libqwt-devel boost-devel-headers

%description
QSapecNG - Qt-based Symbolic Analysis Program for Electric Circuits
(New Generation). It is an open source, multi-platform project, continuously
enhanced by students and researchers of Department of Electronics and
Telecommunications of the University of Florence. In fact, it consists of two
independent parts: the SapecNG framework engine and the application gui QSapecNG.
It comes as continuation of SapWin for Windows, in order to give to the project
a full compatibility on other platforms. Through SapecNG/QSapecNG users can draw,
solve and analyze analog circuits as well as manage them.


%prep
%setup -n %origname-%version-source

%build
%cmake_insource
%make_build VERBOSE=1

%install
%makeinstall_std

%files
%doc README LICENSE AUTHOR TODO
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon May 09 2011 Evgeny Sinelnikov <sin@altlinux.ru> 1.2.2-alt1
- Initial release for Sisyphus

