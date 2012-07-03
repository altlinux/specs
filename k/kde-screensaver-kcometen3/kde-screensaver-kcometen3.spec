%define srcname kcometen3
Name: kde-screensaver-%srcname
Version: 1.1
Release: alt1.4

Summary: An OpenGL screensaver for KDE3
Summary(ru_RU.UTF8): Скринсейвер для KDE3, использующий OpenGL
License: GPL
Group: Graphical desktop/KDE
Url: http://user.cs.tu-berlin.de/~pmueller/
Source0: http://user.cs.tu-berlin.de/~pmueller/%{srcname}-%{version}.tar.gz
Packager: Motsyo Gennadi <drool@altlinux.ru>

Requires: kdebase-wm kdelibs >= %{get_version kdelibs}

BuildRequires(pre): kdelibs

# Automatically added by buildreq on Tue Apr 19 2011 (-bi)
# optimized out: elfutils fontconfig kdelibs libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXext-devel libXrender-devel libXt-devel libacl-devel libart_lgpl-devel libattr-devel libidn-devel libpng-devel libqt3-devel libqt3-settings libstdc++-devel libtqt-devel libutempter-devel xorg-xproto-devel zlib-devel
BuildRequires: gcc-c++ imake kdelibs-devel xorg-cf-files

%description
An OpenGL screensaver for KDE

%description -l ru_RU.UTF8
Скринсейвер для KDE3, использующий OpenGL

%prep
%setup -q -n %srcname-%version

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure --disable-rpath
%make_build

%install
%K3install

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_K3bindir/*
%_K3datadir/applnk/*/*/*.desktop
%_K3datadir/apps/%srcname

%changelog
* Tue Apr 19 2011 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1.4
- fix build

* Tue Mar 08 2011 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1.3
- move to alternate place

* Fri Nov 12 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1.2
- fix build (libGLU-devel)

* Sat Nov 21 2009 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1.1
- added russian description and summary (fixed #22163). Thanks to Phantom.
- cleanup spec

* Mon Jun 18 2007 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1
- build for Sisyphus

* Thu Jun 14 2007 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt0.M40.1
- initial build for ALT Linux (M40)
