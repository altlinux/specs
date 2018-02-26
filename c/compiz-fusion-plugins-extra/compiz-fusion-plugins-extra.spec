Name: compiz-fusion-plugins-extra
Version: 0.8.8
Release: alt2
Summary: Collection of plugins from OpenCompositing for Compiz
License: GPL
Group: System/X11
Url: http://www.compiz-fusion.org/

PreReq: COMPIZ_CORE_ABIVERSION = %compiz_core_abi_version

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): rpm-build-compiz
BuildRequires: compiz-devel >= %version compiz-bcop compiz-fusion-plugins-main-devel >= %version
BuildRequires: GConf gcc-c++ intltool libGConf-devel libGLU-devel libXext-devel libnotify-devel

%description
The OpenCompositing Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

rm -f %buildroot%_libdir/compiz/*.la

%find_lang --output=%name.lang compiz-plugins-extra

%files -f %name.lang
%_includedir/compiz/compiz-animationaddon.h
%_pkgconfigdir/compiz-animationaddon*
%_libdir/compiz/*.so
%_datadir/compiz/*

%changelog
* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt2
- restore compiz in Sisyphus

* Thu Apr 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Mon Nov 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt2
- updated build dependencies

* Fri Apr 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Sat Dec 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt2
- rebuild

* Wed Oct 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Sat Aug 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt2
- rebuild for new compiz ABI

* Tue Mar 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Sat Feb 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt3
- rebuild with compiz-0.8.0

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt2
- updated build dependencies

* Tue Sep 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Wed Sep 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.7-alt1
- 0.7.7

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Fri Feb 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.99-alt2
- git snapshot 2008-02-08 (ee32874db55edd53c3a6184e6de28e5c0b8225a6)

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.99-alt1
- 0.6.99

* Sun Oct 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Oct 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt2
- fixed requires

* Wed Aug 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- initial release

