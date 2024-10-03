Name: xfce4-fsguard-plugin
Version: 1.1.3
Release: alt2

Summary: Plugin checks the chosen mountpoint for free disk space
License: BSD-2-Clause
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>

Url: https://docs.xfce.org/panel-plugins/xfce4-fsguard-plugin
Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-fsguard-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel >= 4.12 libxfce4ui-gtk3-devel libxfce4util-devel
BuildRequires: intltool

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
A little Xfce plugin, which checks the free space on the chosen
mountpoint frequently. It displays 4 different icons and a message box,
depending on the free space. The amount of free disk space is visible in
a tooltip. If you left-click on its icon, it opens the mountpoint
directory in the file manager.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/*/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Thu Oct 03 2024 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt2
- Fixed build: added intltool to BR.

* Thu Apr 20 2023 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt1
- Updated to 1.1.3.

* Mon Dec 28 2020 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt1
- Cleanup BR.
- Added Vcs tag.
- Updated Url tag.
- Fixed License tag.
- Updated to 1.1.2.

* Wed Aug 14 2019 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1
- Updated to 1.1.1.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 1.1.0.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 1.0.2.

* Wed Jun 05 2013 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt2
- Updated translations from upstream git.
- Don't package *.la files.

* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Updated to 1.0.1.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Rebuild with xfce4-panel-4.9.

* Sat Feb 05 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Fix desktop file path.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.
- Updated to 1.0.0.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.2-alt1
- new version

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.1-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- new version
- return from orphaned
- add watch file

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.3.0-alt1
- First build for Sisyphus.

