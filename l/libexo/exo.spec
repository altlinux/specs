%define _name exo

Name: lib%_name
Version: 0.10.7
Release: alt2

Summary: Extension library to Xfce
Summary (ru_RU.UTF-8): Библиотека расширений Xfce
License: %lgpl2plus, %gpl2plus
Group: System/Libraries
Url: http://www.xfce.org
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/exo
Source: %_name-%version.tar
Patch: %_name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4  xfce4-dev-tools > 4.9 libxfce4util-devel libxfce4ui-devel
BuildPreReq: libICE-devel glib2-devel >= 2.27 libgtk+2-devel
BuildRequires: gtk-doc intltool perl-URI time

Requires: xfce4-common
Requires: libgtk+2-common

# There is no longer python bindings for exo.
Conflicts: python-module-exo < 0.7.0

%define _unpackaged_files_terminate_build 1

%description
Libexo is an extension library to Xfce, developed by os-cillation.
While Xfce comes with a quite few libraries that are targeted at desktop
development, libexo is targeted at application development.

%description -l ru_RU.UTF-8
Libexo - библиотека расширений Xfce предназначенная для использования в
приложениях разрабатываемых под Xfce.

%package devel
Summary: Development files for %name
Group: Development/C
PreReq: %name = %version-%release  libxfce4util-devel > 4.5

%description devel
This package contains development files required for packaging
%name-based software.

%package devel-doc
Summary: Documentation files for %name
Group: Development/Documentation
PreReq: %name-devel = %version-%release
BuildArch: noarch

%description devel-doc
This package contains documentation files required for packaging
%name-based software.

%prep
%setup -n %_name-%version
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag libexo_version_tag configure.ac.in

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-gtk-doc \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %_name-1

%check
make check

%files -f %_name-1.lang
%doc AUTHORS NEWS TODO README
%_bindir/*
%exclude %_bindir/exo-csource
%_libdir/*.so.*
%_libdir/xfce4/*
%_datadir/xfce4/*
%config(noreplace) %_sysconfdir/xdg/xfce4/helpers.rc
%_man1dir/*
%exclude %_man1dir/exo-csource.1.*
%_desktopdir/*
%_iconsdir/hicolor/*/*/*
%_pixmapsdir/%_name-*/

# Due to conflict with altlinux-freedesktop-menu-icon-theme-default
%exclude %_iconsdir/hicolor/48x48/categories/applications-internet.png
%exclude %_iconsdir/hicolor/48x48/categories/applications-other.png

%exclude %_datadir/xfce4/helpers/debian-*.desktop

%files devel
%_bindir/exo-csource
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man1dir/exo-csource.1.*

%files devel-doc
%_datadir/gtk-doc/html/%{_name}*

%changelog
* Sat Apr 28 2018 Mikhail Efremov <sem@altlinux.org> 0.10.7-alt2
- Added helper New Moon Web browser (by Anton Midyukov)
    (closes: #34637).

* Mon Sep 14 2015 Mikhail Efremov <sem@altlinux.org> 0.10.7-alt1
- Updated to 0.10.7.

* Tue May 26 2015 Mikhail Efremov <sem@altlinux.org> 0.10.6-alt1
- Updated to 0.10.6.

* Tue Mar 17 2015 Mikhail Efremov <sem@altlinux.org> 0.10.4-alt1
- Updated to 0.10.4.

* Thu Mar 05 2015 Mikhail Efremov <sem@altlinux.org> 0.10.3-alt1
- Don't package menu categories icons.
- Updated to 0.10.3.

* Mon Jan 12 2015 Mikhail Efremov <sem@altlinux.org> 0.10.2-alt3.git20150112
- Fix Xfce name (XFce,XFCE -> Xfce).
- Upstream git snapshot.

* Fri Dec 28 2012 Mikhail Efremov <sem@altlinux.org> 0.10.2-alt2
- Bring back changes for xfce4-terminal.

* Thu Dec 27 2012 Mikhail Efremov <sem@altlinux.org> 0.10.2-alt1
- Temporally revert commits for xfce4-terminal.
- Updated to 0.10.2.

* Mon Dec 10 2012 Mikhail Efremov <sem@altlinux.org> 0.10.1-alt1
- Updated to 0.10.1.

* Mon Dec 03 2012 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1
- Updated to 0.10.0.
- Don't package Debian-specific helpers.
- Require xfce4-common.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1
- Updated to 0.7.3.

* Mon Apr 09 2012 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- Updated to 0.7.2.

* Mon Feb 13 2012 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Updated to 0.7.1.

* Fri Dec 30 2011 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Drop python module subpackage.
- Drop obsileted patches.
- Updated to 0.7.0.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt3.1
- Rebuild with Python-2.7

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt3
- Drop obsoleted fix-russian-translation.patch.
- Updated Russian translation.

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt2
- Rename and update fix-russian-translation.patch.
- Updated Russian translation (by Artem Zolochevskiy).

* Fri Jun 24 2011 Mikhail Efremov <sem@altlinux.org> 0.6.2-alt1
- Updated alt-translation.patch.
- Updated to 0.6.2.

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt3
- Own %%_pixmapsdir/exo-1 dir.
- Enable tests.
- Fix tests.
- Package libexo-devel-doc as noarch.

* Fri Feb 11 2011 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt2
- Fix build with glib >= 2.27.

* Thu Jan 20 2011 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Rename package: exo -> libexo.
- Fix build python module on x86_64 (based on patch from FC).
- Fix license.
- Spec cleanup.
- Update and enable alt-translation.patch.
- Drop exo-0.3.2-alt-noatime.patch (obsolete).
- Drop exo-0.3.2-alt-eject.patch (obsolete).
- Drop alt-exo-iocharset.patch (obsolete).
- Updated to 0.6.0.

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.101-alt2.1
- rebuild for set:provides by request of mithraen

* Tue Jan 05 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.3.101-alt2
- Fix build with gtkdocize.

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.101-alt1.1
- Rebuilt with python 2.6

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.3.101-alt1
- Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.3.100-alt1
- Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.3.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.3.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 0.3.91-alt1
- Xfce 4.6 beta1

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.3.4-alt2.1
- Rebuilt with python-2.5.

* Wed Dec 12 2007 Alex V. Myltsev <avm@altlinux.ru> 0.3.4-alt2
- restore lost changes (now as patches)
- pull Russian translation from SVN
- create version script for libexo (new symbol added)

* Mon Dec 10 2007 Eugene Ostapets <eostapets@altlinux.org> 0.3.4-alt1
- Xfce 4.4.2 release

* Wed Nov 21 2007 Alex V. Myltsev <avm@altlinux.ru> 0.3.2-alt6
- Russian translation fixes

* Mon Oct 29 2007 Alex V. Myltsev <avm@altlinux.ru> 0.3.2-alt5
- use 'noatime' if allowed by HAL
- enable mount notifications through libnotify

* Wed Sep 12 2007 Alex V. Myltsev <avm@altlinux.ru> 0.3.2-alt4
- fix #12702: pushing eject on the disc drive should now work.

* Tue Jun 19 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2-alt3
- try fix 11176

* Sun Jun 17 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2-alt2
- fix 12005

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2-alt1
- add requires for hal

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.3.1.12-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  0.3.1.10rc1-alt2
- Fix buildreq and cleanup spec

* Sat Sep 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.3.1.10rc1-alt1
- Xfce 4.4rc1

* Wed Oct 12 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3.0-alt2
- fix macro

* Sun Mar 20 2005 Andrey Astafiev <andrei@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Sat Dec 25 2004 Andrey Astafiev <andrei@altlinux.ru> 0.2.0-alt1
- First version of RPM package for Sisyphus.
