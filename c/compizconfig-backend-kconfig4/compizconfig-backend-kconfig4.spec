Name: compizconfig-backend-kconfig4
Version: 0.8.8
Release: alt2
Summary: KConfig Settings library for plugins - OpenCompositing Project
License: GPL
Group: Graphical desktop/KDE
Url: http://www.compiz-fusion.org/

PreReq: libcompizconfig >= %version

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXext-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel
BuildRequires: libXtst-devel libXv-devel libXxf86misc-devel libcompizconfig-devel libstartup-notification-devel libxkbfile-devel
BuildRequires: libxslt-devel xorg-xf86vidmodeproto-devel

%description
The OpenCompositing Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
through plugins and themes contributed by the community giving a
rich desktop experience.

%prep
%setup -q
%patch -p1

%build
%K4build

%install
%K4install

%files
%dir %_libdir/compizconfig
%dir %_libdir/compizconfig/backends
%_libdir/compizconfig/backends/*.so

%changelog
* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt2
- restore compiz in Sisyphus

* Thu Apr 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Wed Oct 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

