Name: xfce4-cpugraph-plugin
Version: 1.2.10
Release: alt3

Summary: CPU monitor for the Xfce panel
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-cpugraph-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-cpugraph-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel >= 4.16.0 libxfce4ui-gtk3-devel >= 4.16.0 libxfce4util-devel >= 4.17.2
BuildRequires: libxfconf-devel >= 4.12.0
BuildRequires: gcc-c++
BuildRequires: intltool

Requires: xfce4-panel >= 4.17

%define _unpackaged_files_terminate_build 1

%description
A CPU monitor plugin for the Xfce panel. It offers multiple display
modes (LED, gradient, fire, etc...) to show the current CPU load of
the system. The colors and the size of the plugin are customizable.

%prep
%setup
%patch -p1

%build
%ifarch %e2k
# explicit one required for std::string_view as of lcc 1.26.21
%add_optflags -std=c++17
%endif
%xfce4reconf
%configure \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_datadir/icons/hicolor/*/*/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Thu Oct 03 2024 Mikhail Efremov <sem@altlinux.org> 1.2.10-alt3
- Fixed build: added intltool to BR.

* Mon Dec 11 2023 Michael Shigorin <mike@altlinux.org> 1.2.10-alt2
- E2K: fix build with lcc 1.26.21 (ilyakurdyukov@)

* Mon Dec 04 2023 Mikhail Efremov <sem@altlinux.org> 1.2.10-alt1
- Updated to 1.2.10.

* Wed Jul 26 2023 Mikhail Efremov <sem@altlinux.org> 1.2.8-alt1
- Fixed build on e2k.
- Updated to 1.2.8.

* Thu Nov 03 2022 Mikhail Efremov <sem@altlinux.org> 1.2.7-alt1
- Updated and fixed BR.
- Dropped obsoleted patch.
- Updated to 1.2.7.

* Wed Feb 02 2022 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt1
- Updated to 1.2.6.

* Mon Jan 31 2022 Mikhail Efremov <sem@altlinux.org> 1.2.5-alt2
- Fixed translations.

* Mon Oct 11 2021 Mikhail Efremov <sem@altlinux.org> 1.2.5-alt1
- Updated to 1.2.5.

* Mon Oct 04 2021 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1
- Updated to 1.2.4.

* Wed Feb 24 2021 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt1
- Updated to 1.2.3.

* Mon Feb 15 2021 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Mon Feb 01 2021 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1.

* Mon Dec 28 2020 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Mon Sep 14 2020 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt2.g80e56c8
- Fixed BR.
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.
- Upstream git snapshot.

* Wed Jul 03 2019 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Mon Jun 24 2019 Mikhail Efremov <sem@altlinux.org> 1.0.91-alt1
- Updated to 1.0.91.

* Wed May 29 2019 Mikhail Efremov <sem@altlinux.org> 1.0.90-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 1.0.90.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt2
- Rebuild with libxfce4util-4.12.
- Fix Xfce name (XFCE -> Xfce).

* Wed Jul 04 2012 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1
- Updated to 1.0.5.

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1
- Updated to 1.0.4.

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1
- Updated to 1.0.3.

* Fri May 04 2012 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt2
- Don't package *.la files.

* Mon Apr 30 2012 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt2
- Rebuild with xfce4-panel-4.9.

* Sat Feb 05 2011 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.gz -> tar.
- Drop watch file.
- Updated to 1.0.1.

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- return from orphaned
- new version 0.4.0
- add watch file

* Mon Dec 18 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.3.0-alt1
- new version

* Sat Jan 01 2005 Andrey Astafiev <andrei@altlinux.ru> 0.2.2-alt2
- Rebuilt with new xfce4-panel.

* Sat Aug 14 2004 Andrey Astafiev <andrei@altlinux.ru> 0.2.2-alt1
- First version of RPM package for Sisyphus.
