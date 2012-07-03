Name: ccsm
Version: 0.8.4
Release: alt3

Summary: CompizConfig Settings Manager
License: GPL
Group: System/X11
Url: http://www.compiz-fusion.org/

Requires: compiz >= %version compiz-fusion-plugins-main >= %version compiz-fusion-plugins-extra >= %version python-module-sexy
Provides: simple-%name = %version-%release
Conflicts: simple-%name < 0.8.2-alt2

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: rpm-build-python intltool python-devel python-modules-compiler python-module-compizconfig-devel >= %version

%description
Configure Compiz with CompizConfig

# does that mean #python_sitelibdir_noarch ?
#define python_sitelibdir %_prefix/lib/python%__python_version/site-packages

%prep
%setup -q
%patch -p1

subst "s,@prefix@,%_prefix," ccm/Constants.py.in

%build
%make
intltool-merge -d -u po %name.desktop.in %name.desktop

%install
%make PREFIX=%_prefix DESTDIR=%buildroot install

mkdir -p %buildroot%_altdir
cat > %buildroot%_altdir/%name <<__EOF__
%_bindir/simple-%name	%_bindir/%name	10
__EOF__

%find_lang %name

%files -f %name.lang
%_altdir/%name
%_bindir/%name
%python_sitelibdir_noarch/ccm
%python_sitelibdir_noarch/ccsm-%version-py%_python_version.egg-info
%_desktopdir/*.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.4-alt3
- restore compiz in Sisyphus

* Thu Mar 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt2
- icons cleanup

* Wed Oct 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Mon Sep 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt4
- translated desktop file

* Thu May 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt3
- provides simple-ccsm

* Mon Apr 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt2
- requires compiz-fusion-plugins-extra

* Tue Mar 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Sat Feb 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt2
- noach package

* Tue Sep 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Wed Sep 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.7-alt1
- 0.7.7

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Sun Apr 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Fri Feb 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.99-alt2
- git snapshot 2008-02-05 (b1652ec55abae0d9f28fa1683fb7c03fb927f9e4)

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.99-alt1
- 0.6.99

* Sun Oct 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Aug 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt3
- fixed DataDir in Constants.py
- fixed requires

* Thu Aug 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt2
- fixed build for x86_64

* Wed Aug 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- initial release

