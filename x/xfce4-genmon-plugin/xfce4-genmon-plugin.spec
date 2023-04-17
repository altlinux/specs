Name: xfce4-genmon-plugin
Version: 4.2.0
Release: alt1

Summary: Generic monitor plugin for the Xfce panel
License: LGPLv2.1+
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>
Url: https://docs.xfce.org/panel-plugins/xfce4-genmon-plugin

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-genmon-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfconf-devel

Requires: xfce4-panel >= 4.12

%define _unpackaged_files_terminate_build 1

%description
The GenMon plugin cyclically spawns the indicated script/program,
captures its output and displays it as a string into the panel.

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

chmod +x scripts/migrate_to_xfconf.sh

%files -f %name.lang
%doc README AUTHORS NEWS
%doc scripts/
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Apr 17 2023 Mikhail Efremov <sem@altlinux.org> 4.2.0-alt1
- Packaged example scripts.
- Packaged NEWS file.
- Updated to 4.2.0.

* Sun Jan 24 2021 Mikhail Efremov <sem@altlinux.org> 4.1.1-alt1
- Updated to 4.1.1.

* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 4.1.0-alt1
- Updated to 4.1.0.

* Sun Sep 13 2020 Mikhail Efremov <sem@altlinux.org> 4.0.2-alt2.gc4f051b
- Fixed BR.
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.
- Upstream git snapshot.

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.0.2-alt1
- Updated to 4.0.2.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Drop obsoleted patch.
- Updated to 4.0.1.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 3.4-alt2
- Rebuild with libxfce4util-4.12.
- Fix Xfce name (XFCE -> Xfce).

* Mon May 14 2012 Mikhail Efremov <sem@altlinux.org> 3.4-alt1
- Fix translations.
- Updated to 3.4.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 3.3.1-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 3.3.1-alt2
- Rebuild with xfce4-panel-4.9.

* Fri Jan 06 2012 Mikhail Efremov <sem@altlinux.org> 3.3.1-alt1
- Updated to 3.3.1.

* Fri Dec 30 2011 Mikhail Efremov <sem@altlinux.org> 3.3.0-alt2
- Fix timer initialization.

* Tue May 03 2011 Mikhail Efremov <sem@altlinux.org> 3.3.0-alt1
- Updated Russian translation from upstream git.
- Drop upstreamed patches.
- Updated to 3.3.0.

* Sat Feb 05 2011 Mikhail Efremov <sem@altlinux.org> 3.2-alt2
- Add patches from Debian:
    + fix processes ending up as zombies when run from genmon.
    + close unused pipes to prevent freezing the UI.
    + explict link against libxfcegui4, fix build with xfce4-panel 4.7.
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Drop watch file.

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 3.2-alt1
- new version

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 3.1-alt1
- new version
- add watch file

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 3.0-alt1
- First build for Sisyphus.

