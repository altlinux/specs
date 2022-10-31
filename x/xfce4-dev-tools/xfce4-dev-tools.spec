Name: xfce4-dev-tools
Version: 4.17.1
Release: alt1

Summary: Development tools for Xfce
Summary (ru): Инструменты для разработчика Xfce
License: GPLv2+
Url: https://docs.xfce.org/xfce/xfce4-dev-tools/start
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>
Vcs: https://gitlab.xfce.org/xfce/xfce4-dev-tools.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: glib2-devel
BuildRequires: xsltproc docbook-style-xsl

Requires: intltool >= 0.50.0
Requires: xfce4-common

%define _unpackaged_files_terminate_build 1

%description
Development tools for Xfce

%description -l ru
Данный пакет содержит в себе инструменты необходимые для разработчика
окружения рабочего стола Xfce.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--enable-maintainer-mode
%make_build

%install
%makeinstall_std

%find_lang %name

%check
make check

%files -f %name.lang
%doc AUTHORS HACKING README.md NEWS
%_bindir/*
%_datadir/aclocal/*
%_man1dir/*

%changelog
* Mon Oct 31 2022 Mikhail Efremov <sem@altlinux.org> 4.17.1-alt1
- Updated to 4.17.1.

* Wed May 04 2022 Mikhail Efremov <sem@altlinux.org> 4.17.0-alt3
- Updated Url tag.
- Don't use egrep.

* Mon Oct 04 2021 Mikhail Efremov <sem@altlinux.org> 4.17.0-alt2
- Don't pull git.
- Don't pull docker (closes: #41043).

* Tue Jul 27 2021 Mikhail Efremov <sem@altlinux.org> 4.17.0-alt1
- Dropped exo-csource symlink.
- Updated to 4.17.0.

* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 4.16.0-alt1
- Updated to 4.16.0.

* Tue Nov 03 2020 Mikhail Efremov <sem@altlinux.org> 4.15.1-alt1
- Updated to 4.15.1.

* Sun Sep 13 2020 Mikhail Efremov <sem@altlinux.org> 4.15.0-alt2
- Added exo-csource symlink.

* Tue Sep 01 2020 Mikhail Efremov <sem@altlinux.org> 4.15.0-alt1
- Add Vcs tag.
- Don't use rpm-build-licenses.
- Updated to 4.15.0.

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt1
- Updated to 4.14.0.

* Fri Jun 28 2019 Mikhail Efremov <sem@altlinux.org> 4.13.0-alt1
- Updated url.
- Updated to 4.13.0.

* Wed Jun 13 2018 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt2
- Use _unpackaged_files_terminate_build.
- Remove autom4te.cache before running automake.

* Thu Mar 05 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Wed Feb 18 2015 Mikhail Efremov <sem@altlinux.org> 4.11.1-alt1
- Updated to 4.11.1.

* Mon Feb 24 2014 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Updated to 4.11.0.

* Mon Feb 17 2014 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt2.git20130429
- Fix Xfce name (XFce,XFCE -> Xfce).
- Upstream git snapshot (master branch).

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- Updated to 4.9.2.

* Wed Apr 11 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Thu Nov 17 2011 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Patches from upstream:
  + Update build.
  + Remove spec file and rpm build.
  + Add support for LT_PREREQ (Xfce bug #6920).
- Updated to 4.9.0.

* Fri Oct 14 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt3
- Fix work with intltool-0.50.

* Mon Jan 31 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt2
- Drop rpm-build-xfce4 requires.
- Fix License.
- Fix Url.

* Mon Jan 17 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Updated to 4.8.0.

* Mon Jan 11 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.7.2-alt1
- New version.

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
- Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Mon Oct 20 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta 1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.0.1-alt1
- Xfce 4.4.2 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Tue Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- initial build
