Name: dwm
Version: 6.0
Release: alt1

Summary: Dynamic window manager for X

License: MIT
Group: Graphical desktop/Other
Url: http://dwm.suckless.org/

Source: http://www.suckless.org/download/%name-%version.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source1: dwm.wmsession

Patch0: %name.config.patch

# Automatically added by buildreq on Wed Nov 29 2006
BuildRequires: libX11-devel libXinerama-devel

%description
dwm is a dynamic window manager for X. 
It manages windows in tiling and floating modes. 
Either mode can be applied dynamically, optimizing 
the environment for the application in use and the
task performed. It is the little brother of wmii.

%prep
%setup -q

patch -p2 -i %PATCH0

%build
%make_build

%install
%make_install install DESTDIR=%buildroot

install -pD -m 644 %SOURCE1 %buildroot%_sysconfdir/X11/wmsession.d/14%name


%files
%_bindir/*
%_man1dir/*
%doc README
%config %_sysconfdir/X11/wmsession.d/14%name

%changelog
* Mon Jan 02 2012 Ilya Mashkin <oddity@altlinux.ru> 6.0-alt1
- 6.0

* Sun Jul 10 2011 Ilya Mashkin <oddity@altlinux.ru> 5.9-alt1
- 5.9

* Fri Jul 23 2010 Ilya Mashkin <oddity@altlinux.ru> 5.8.2-alt1
- 5.8.2

* Sat Oct 17 2009 Ilya Mashkin <oddity@altlinux.ru> 5.7.2-alt1
- 5.7.2

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 5.6.1-alt1
- 5.6.1

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 5.5-alt1
- 5.5

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_wms for dwm

* Fri May 25 2007 Lunar Child <luch@altlinux.ru> 4.1-alt1
- new version 4.1 (with rpmrb script)

* Fri May 25 2007 Lunar Child <luch@altlinux.ru> 4.1.tar.gz-alt1
- new version 4.1.tar.gz (with rpmrb script)

* Fri May 25 2007 Lunar Child <luch@altlinux.ru> 4.1-alt1
- new version 4.1 (with rpmrb script)

* Fri May 11 2007 Lunar Child <luch@altlinux.ru> 4.0-alt1
- new version

* Thu Jan 04 2007 Lunar Child <luch@altlinux.ru> 2.8-alt1
- new version

* Wed Nov 29 2006 Lunar Child <luch@altlinux.ru> 2.3-alt1
- new version

* Thu Nov 09 2006 Lunar Child <luch@altlinux.ru> 2.1-alt1
- new version

* Tue Oct 24 2006 Lunar Child <luch@altlinux.ru> 2.0-alt1
- First build for ALT Linux Sisyphus
