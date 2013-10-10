Name: emerald-themes
Version: 0.7.8
Release: alt1

Group: Graphical desktop/Other
Summary: Themes for Emerald, the window decorator for Compiz
Url: http://www.compiz-fusion.org/
License: GPL

Packager: Motsyo Gennadi <drool@altlinux.ru>

Source0: %name-%version.tar.bz2

Requires: emerald >= %version

BuildArch: noarch

%description
Emerald is themeable window decorator and compositing manager for Compiz.

This package contains themes for emerald.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_datadir/emerald

%changelog
* Thu Oct 10 2013 Motsyo Gennadi <drool@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Mon Sep 23 2013 Motsyo Gennadi <drool@altlinux.ru> 0.5.2-alt2
- build for Sisyphus

* Wed Oct 31 2012 Motsyo Gennadi <drool@altlinux.ru> 0.5.2-alt1.M60T.1
- build for t6

* Sat Feb 20 2010 Motsyo Gennadi <drool@altlinux.ru> 0.5.2-alt1.M51.1
- pickup from archive, build for M51

* Wed Oct 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Mon Mar 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Thu Mar 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- 0.2.0 release

* Sun Feb 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt0.0rc1
- 0.2.0-RC1

* Mon Feb 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt0.0pre1
- 0.2.0pre1

* Sat Dec 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Mon Dec 11 2006 Sergey V Turchin <zerg at altlinux dot org> 0.1.3-alt1
- new version

* Thu Nov 09 2006 Sergey V Turchin <zerg at altlinux dot org> 0.1.2-alt1
- new version

* Tue Nov 07 2006 Sergey V Turchin <zerg at altlinux dot org> 0.1.1-alt1
- intial specfile


