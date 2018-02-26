Name: compiz-fusion-plugins-main
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
BuildRequires: compiz-devel >= %version compiz-bcop
BuildRequires: GConf gcc-c++ glib2-devel intltool libGLU-devel libGConf-devel libXext-devel libjpeg-devel libpango-devel

%description
The OpenCompositing Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity.

%package devel
Summary: Development file for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development file for %name

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

%find_lang --output=%name.lang compiz-plugins-main

%files -f %name.lang
%_libdir/compiz/*.so
%_datadir/compiz/*

%files devel
%_includedir/compiz
%_pkgconfigdir/*.pc

%changelog
* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt2
- restore compiz in Sisyphus

* Thu Apr 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Tue Nov 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt2
- updated build dependencies

* Fri Apr 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Fri Jan 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt3
- session plugin: used XDG_CONFIG_HOME

* Sat Dec 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt2
- rebuild

* Wed Oct 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Sat Aug 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt3
- rebuild for new compiz ABI

* Wed Mar 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt2
- updated l10n

* Tue Mar 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Sat Feb 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt5
- rebuild with compiz-0.8.0

* Tue Dec 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt4
- expo: don't allow movement of windows that are not supposed to be moved (SA33077)

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt3
- updated build dependencies

* Mon Oct 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt2
- applied post-0.7.8 upstream changes (3b020f98c3f95451cc9334092baad8febfb268c9)

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
- git snapshot 2008-02-08 (90fd5bff13dda7f37a5eb14234d5021cf07dfdd9)

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.99-alt1
- 0.6.99

* Sun Oct 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Oct 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt2
- fixed requires

* Wed Aug 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- initial release

