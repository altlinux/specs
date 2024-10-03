%def_disable libgtop

Name: xfce4-systemload-plugin
Version: 1.3.2
Release: alt2

Summary: System load plugin for the Xfce panel
Summary(ru_RU.UTF-8): Отображение использования ресурсов системы на панели Xfce
License: BSD-2-Clause
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-systemload-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-systemload-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4util-devel >= 4.17.2 libxfce4ui-gtk3-devel >= 4.16.0 libxfce4panel-gtk3-devel >= 4.16.0 libxfconf-devel >= 4.14.0
BuildRequires: gcc-c++
BuildRequires: libX11-devel libgtk+3-devel libstartup-notification libupower-devel
%{?_enable_libgtop:BuildRequires: libgtop-devel}
BuildRequires: intltool

Requires: xfce4-panel >= 4.17

%define _unpackaged_files_terminate_build 1

%description
%name is the system load plugin for the Xfce panel.

%description -l ru_RU.UTF-8
%name -- это модуль, отображающий уровень использования системных ресурсов
на панели графической среды Xfce.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-upower \
	%{subst_enable libgtop} \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md COPYING AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*.*


%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Thu Oct 03 2024 Mikhail Efremov <sem@altlinux.org> 1.3.2-alt2
- Fixed build: added intltool to BR.

* Thu Nov 03 2022 Mikhail Efremov <sem@altlinux.org> 1.3.2-alt1
- Fixed build on 32bit arches.
- Updated BR.
- Updated to 1.3.2.

* Wed Jan 12 2022 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt2
- Disabled libgtop support.

* Tue Mar 23 2021 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.

* Wed Mar 10 2021 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Mon Dec 21 2020 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1
- Updated to 1.2.4.

* Mon Sep 14 2020 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt3.gbfecbdd
- Fixed BR.
- Updated Vcs tag.
- Upstream git snapshot.

* Wed Mar 25 2020 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt2
- Update Url.
- Add Vcs tag.
- Fix license.

* Tue Aug 13 2019 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt1
- Updated to 1.2.3.

* Thu Nov 29 2018 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1
- Convert Russian summary/description to UTF-8.
- Fix license.
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 1.2.1.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt2
- Rebuild with libxfce4util-4.12.

* Fri Nov 21 2014 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt1
- Build with libupower support.
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 1.1.2.

* Wed Jun 05 2013 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt2
- Updated translations from upstream git.

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1
- Updated to 1.1.1.

* Fri May 04 2012 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt2
- Don't package *.la files.

* Fri Apr 20 2012 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Rebuild with xfce4-panel-4.9.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Remove xfce4-systemload-plugin-asneeded.patch.
- Spec updated, tar.bz2 -> tar.
- Updated to 1.0.0.

* Mon Oct 15 2007 Igor Zubkov <icesik@altlinux.org> 0.4.2-alt1.1
- NMU
  + fix build with new intltool

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.4.2-alt1
- new version

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4-alt1
- 0.4

* Tue Jan 18 2005 Andrey Astafiev <andrei@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Mon Dec 27 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.4-alt2
- Rebuilt with libxfcegui4.so.3

* Wed Nov 19 2003 Andrey Astafiev <andrei@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Mon Nov 03 2003 Andrey Astafiev <andrei@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Wed Oct 15 2003 Andrey Astafiev <andrei@altlinux.ru> 0.3.2-alt1
- Changed Group tag.

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 0.3.2-alt0.9
- First version of RPM package for Sisyphus.
