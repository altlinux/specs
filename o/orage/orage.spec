Name: orage
Version: 4.12.1
Release: alt3

Summary: Time-managing application for the Xfce desktop environment
Summary (ru_RU.UTF-8): Календарь для окружения рабочего стола Xfce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://www.xfce.org/projects/orage/
Packager: Xfce Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4util-devel
BuildRequires: flex intltool libnotify-devel libical-devel libpopt-devel libdbus-glib-devel

Requires: xfce4-common

Obsoletes: xfcalendar < 4.8.3
Provides: xfcalendar = %version-%release

%define _unpackaged_files_terminate_build 1

%description
%name is the time-managing application for the Xfce desktop environment.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе календарь для окружения рабочего стола
Xfce.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-dbus \
	--enable-libical \
	--enable-libnotify \
	--enable-archive \
	--enable-libxfce4panel \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_bindir/*
%_desktopdir/*
%_datadir/orage/
%_liconsdir/*
%_iconsdir/hicolor/*/apps/*
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_man1dir/*
%_datadir/dbus-1/services/*.service

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Tue Jan 09 2018 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt3
- Updated translations from upstream.
- Fixed build with libical 3.x.

* Mon Jan 25 2016 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt2
- Rebuid with libical-2.0.0.

* Fri Apr 10 2015 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt1
- Updated to 4.12.1.

* Thu Apr 09 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Fix plugin module name.
- Updated to 4.12.0.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt3
- Rebuild with libxfce4util-4.12.

* Mon Dec 16 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt2
- Update translations from upstream git.
- Require xfce4-common.

* Mon Dec 09 2013 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 4.10.0.

* Wed Nov 20 2013 Mikhail Efremov <sem@altlinux.org> 4.8.4-alt2
- Rebuid with libical-1.0-alt2.

* Fri Feb 01 2013 Mikhail Efremov <sem@altlinux.org> 4.8.4-alt1
- Updated to 4.8.4.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt2
- Rebuild with xfce4-panel-4.9.

* Fri Jan 06 2012 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt1
- Rename package: xfcalendar -> orage.
- Updated to 4.8.3.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2.2-alt1
- Updated to 4.8.2.2.

* Fri Aug 19 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1.3-alt2
- Change globaltime utility menu category.
- Use for help xdg-open instead of firefox.

* Mon Jul 11 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1.3-alt1
- Updated to 4.8.1.3.

* Thu Mar 24 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt2
- Fix BR: added libdbus-glib-devel.
- Update translations from upstream git.

* Wed Mar 09 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Updated to 4.8.1.

* Thu Jan 27 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec update & cleanup.
- tar.bz2 -> tar
- Don't use internal libical.
- Remove old patches.
- Updated to 4.8.0.

* Sun Jan 24 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Fix build. Fixed problem with alarm.

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
- Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
- Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Mon Oct 15 2007 Igor Zubkov <icesik@altlinux.org> 4.4.1-alt1.1
- NMU
  + fix build with new intltool

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

* Tue Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
- 4.2.3

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

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 0.1.9-alt1
- 0.1.9

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 0.1-alt0.9
- First version of RPM package for Sisyphus.
- Spec derived from original version.
