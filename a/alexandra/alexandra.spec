Name:		alexandra
Version:	1.2.3
Release:	alt2
Summary:	A small and user friendly opensource video library with great potential
License:	GPLv2
Group:		Video
Url:		http://alexandra-qt.sourceforge.net/
Source0:	%name-%version.tar.gz

# Automatically added by buildreq on Fri Aug 14 2015 (-bi)
# optimized out: elfutils libGL-devel libqt5-concurrent libqt5-core libqt5-gui libqt5-widgets libstdc++-devel libzen-devel python-base
BuildRequires: gcc4.7-c++ libmediainfo-devel qt5-base-devel

%set_gcc_version 4.7

%description
Alexandra Video Library - a simple and convenient program for the organization
and management of the home video library. You can completely customize the
catalog movies in a list, add a description and detailed information about the
movie in a lot of fields available, attach posters and much more. Directly from
the program, you can start playing the film, with the available choice of any
video player on your computer if you wish.

A small and user friendly opensource video library with great potential,
written in C++ using Qt5 framework.

%prep
%setup

%build
%qmake_qt5 src/%name.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Sun Aug 23 2015 Motsyo Gennadi <drool@altlinux.ru> 1.2.3-alt2
- fix build for Sisyphus (build with gcc4.7, tnx to Michael Shigorin)

* Mon Aug 17 2015 Motsyo Gennadi <drool@altlinux.ru> 1.2.3-alt0.M70T.1
- build for t7

* Fri Aug 14 2015 Motsyo Gennadi <drool@altlinux.ru> 1.2.3-alt1
- initial build for ALT Linux
