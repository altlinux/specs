Name: xfwm4
Version: 4.10.0
Release: alt1

Summary: Window manager for XFce
Summary (ru_RU.UTF8): Менеджер окон для окружения рабочего стола Xfce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://www.xfce.org/
Packager: XFCE Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/xfwm4
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4ui-devel libxfconf-devel
# For exo-csource (needed in maintainer mode)
BuildPreReq: libexo-devel

BuildRequires: gnome-doc-utils xml-utils xsltproc
BuildRequires: intltool libSM-devel libXcomposite-devel libXdamage-devel libXext-devel libXrandr-devel libglade-devel
BuildRequires: libstartup-notification-devel libwnck-devel xorg-cf-files
BuildRequires: gtk-doc

%description
%name is a window manager compatable with GNOME, GNOME2, KDE2, KDE3 and
XFce.

%description -l ru_RU.UTF8
Данный пакет содержит в себе менеджер окон для окружения рабочего стола
Xfce. Совместим с окружениями рабочего стола GNOME и KDE.

%prep
%setup

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-startup-notification \
	--enable-randr \
	--enable-render \
	--enable-xsync \
	--enable-compositor \
	--enable-debug=no

%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README TODO AUTHORS
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_liconsdir/*
%_iconsdir/hicolor/scalable/apps/*
%_iconsdir/hicolor/*/actions/*
%_datadir/themes/*
%_libdir/xfce4/*

%changelog
* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Wed Apr 11 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Drop obsoleted patch.
- Updated to 4.9.0.

* Tue Dec 20 2011 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt1
- Updated to 4.8.3.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt1
- Drop obsoleted patches.
- Updated to 4.8.2.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt5
- Updated Russian documentation.
- Updated Russian translation.

* Fri Aug 19 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt4
- Add Russian documentation (by Artem Zolochevskiy).

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt3
- Updated Russian translation (by Artem Zolochevskiy).

* Fri Jul 08 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt2
- Fix documentation building.

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Updated to 4.8.1.

* Tue Jan 25 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Spec cleanup, tar.bz2 -> tar.
- Drop 01_keysym_svn_backport.patch (obsolete).
- Updated to 4.8.0.

* Thu Sep 03 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt4
- Russian translation updated

* Mon May 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Fix build with new toolchain. Added autoconf and audomake version requiremens. 

* Wed May 13 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Russian translation updated

* Sun Apr 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Mon Nov 12 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt2
- fix work with gtk 2.12, tnx avm@
- bug 13388

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Fri Nov 10 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt2
- strict library version build requires

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  4.3.99.1-alt2
- Fix buildreq and cleanup spec

* Sat Sep 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- 4.4rc1

* Fri Nov 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3.2-alt1
- 4.2.3.2

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.99.3-alt1
- 4.1.99.3

* Mon Nov 01 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.91-alt1
- 4.1.91

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3.1-alt1
- 4.0.3.1

* Tue Dec 23 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Tue Nov 18 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Sep 26 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- 3.99.2

* Mon Jul 14 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.1-alt0.9
- 3.99.1

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 3.90.0-alt0.9
- First version of RPM package for Sisyphus.
- Spec derived from original version.
