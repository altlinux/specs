Name: xfce4-session
Version: 4.10.0
Release: alt1

Summary: Session manager for XFce desktop environment
Summary (ru): Менеджер сессий для окружения рабочего стола Xfce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://www.xfce.org/
Packager: XFCE Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/xfce4-session
Source: %name-%version.tar
Source1: xfce.wmsession

Patch: %name-%version-%release.patch

%def_enable gnome

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfconf-devel libxfce4ui-devel
# For gdk-pixbuf-csource and exo-csource (needed in maintainer mode)
BuildRequires: libgdk-pixbuf-devel libexo-devel
# GNOME compatibility
%{?_enable_gnome:BuildRequires: libgnome-keyring-devel}
BuildRequires: iceauth intltool libSM-devel libglade-devel libwnck-devel xorg-cf-files

Requires: wm-common-freedesktop
Requires: upower

Obsoletes: xfce-utils < %version

%description
%name is the session manager for the XFce desktop environment.

%description -l ru
Данный пакет содержит в себе менеджер сессий, используемый в окружении
рабочего стола Xfce.

%package -n libxfsm
Summary: Library for XFce session manager plugins
Group: Development/C
License: GPL

%description -n libxfsm
This package contains library for XFce session manager.

%package devel
Summary: Development files to build XFce session manager plugins
Group: Development/C
License: GPL
PreReq: libxfsm = %version-%release

%description devel
This package contains files to develop plugins for XFce session manager.

%package engines
Summary: Additional splash screen engines for XFce session manager
Group: Graphical desktop/XFce
License: GPL
PreReq: %name = %version-%release

%description engines
Additional splash screen engines for XFce session manager.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	%{?_enable_gnome:--enable-libgnome-keyring} \
	--enable-debug=no
%make_build

%install
%makeinstall_std
install -Dm0644 %SOURCE1 %buildroot%_x11sysconfdir/wmsession.d/10Xfce4
%find_lang %name

%files -f %name.lang
%doc README NEWS AUTHORS
%doc doc/FAQ doc/README.Kiosk
%_x11sysconfdir/wmsession.d/*
%config(noreplace) %_sysconfdir/xdg/xfce4/*
%config(noreplace) %_sysconfdir/xdg/autostart/*.desktop
%_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml
%_bindir/*
%dir %_libdir/xfce4/session
%dir %_libdir/xfce4/session/splash-engines
%_libdir/xfce4/session/splash-engines/libmice.so
%exclude %_libdir/xfce4/session/splash-engines/*.la
%_libdir/xfce4/session/xfsm-*
%_desktopdir/*
%_iconsdir/hicolor/*/*/*
%_mandir/man?/*
%_datadir/xsessions/*.desktop

%files -n libxfsm
%_libdir/lib*.so.*

%files devel
%_includedir/xfce4/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%files engines
%_datadir/themes/Default/balou
%_libdir/xfce4/session/splash-engines/*.so
%exclude %_libdir/xfce4/session/splash-engines/libmice.so
%_libdir/xfce4/session/balou*

%changelog
* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 24 2012 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- Stop ssh-agent started from /etc/X11/profile.d/ssh-agent.sh.
- Fix gpg-agent shutdown.
- Replace mkdirhier with mkdir (closes: #27265).
- Updated from upstream git (e5f6df86fe):
    + Translations.
    + Skip gpg/ssh-agent if GNOME compat is enabled and gnome-keyring
      found.
    + Remove remaining code to shutdown gconf.
- Updated to 4.9.2.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Fri Apr 13 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Rewritten patch: Restore XKB settings after suspend/hibernate.
- Obsolete xfce-utils.
- Add xfce.wmsession from xfce-utils.
- Drop old patches.
- Updated to 4.9.0.

* Mon Feb 13 2012 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt1
- Updated to 4.8.3.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt5
- Rebuild with xfce4-panel-4.9.

* Tue Dec 20 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt4
- Updated Debian's force-xfsettingsd-start.patch.

* Thu Dec 01 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt3
- Restore XKB settings after suspend/hibernate.

* Thu Oct 13 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt2
- Added patches from Debian.
- Lock screen on suspend/hibernate in favor power manager's settings.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt1
- Drop obsoleted patches.
- Updated to 4.8.2.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt5
- Only perform hostname checks when TCP connections are enabled.
- Updated Russian documentation.
- Updated Russian translation.

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt4
- Updated Russian translation (by Artem Zolochevskiy).

* Wed Jul 20 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt3
- Fix documentation generation.

* Tue Jul 19 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt2
- Update Russian translation (by Artem Zolochevskiy).
- Patches from upstream:
    + Fix GDM_LANG usage to be compatible with GDM3.
    + Fix crash if save timeout for a client is triggered.

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Updated to 4.8.1.

* Mon Jan 24 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Spec cleanup, tar.bz2 -> tar.
- Fix shadows in 'simple' splash engine (patch from Ubuntu).
- Drop old Ubuntu's icons.
- Remove old patches.
- Fix license.
- Updated to 4.8.0.

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
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

* Mon Oct 15 2007 Igor Zubkov <icesik@altlinux.org> 4.4.1-alt1.1
- NMU
  + fix build with new intltool

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release
- add patches from Ubuntu 7.04
- add images from Ubuntu 7.04

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Wed Oct 25 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt2
- fix x86_64

* Wed Sep 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- new version 4.4rc1

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

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Mon Dec 22 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.2-alt1
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
