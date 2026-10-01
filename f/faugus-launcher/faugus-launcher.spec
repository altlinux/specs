%define _unpackaged_files_terminate_build 1

Name: faugus-launcher
Version: 2.4.2
Release: alt1

Summary: A simple and lightweight app for running Windows games using UMU-Launcher

License: MIT
Group: Games/Other
Url: https://github.com/Faugus/faugus-launcher

# Source-url: https://github.com/Faugus/faugus-launcher/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-python3

BuildRequires: gtk-update-icon-cache

# find-requires scans Python imports (including function-local imports), but
# cannot infer GI typelibs selected by gi.require_version() or commands launched
# from Python (gamemoderun, mangohud, xdg-open, icoextract); keep these in sync.
Requires: gamemode
Requires: mangohud
Requires: python3(dbus)
Requires: python3(psutil)
Requires: python3(PIL)
Requires: typelib(Gtk) = 4.0
Requires: typelib(Adw)
Requires: typelib(Manette)
Requires: xdg-utils
Requires: /usr/bin/icoextract

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %name

%files -f %name.lang
%doc %_datadir/licenses/faugus-launcher/LICENSE
%_bindir/faugus-launcher
%_desktopdir/io.github.Faugus.faugus-launcher.desktop
%_desktopdir/io.github.Faugus.faugus-launcher.shortcut.desktop
%python3_sitelibdir/faugus/
%_datadir/faugus-launcher/
%_iconsdir/hicolor/scalable/actions/*.svg
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/metainfo/io.github.Faugus.faugus-launcher.metainfo.xml

%changelog
* Wed Sep 30 2026 Boris Yumankulov <boria138@altlinux.org> 2.4.2-alt1
- new version 2.4.2

* Mon Jul 06 2026 Boris Yumankulov <boria138@altlinux.org> 1.22.7-alt1
- new version 1.22.7

* Wed Apr 29 2026 Boris Yumankulov <boria138@altlinux.org> 1.18.8-alt1
- new version 1.18.8

* Sat Apr 11 2026 Boris Yumankulov <boria138@altlinux.org> 1.17.5-alt1
- new version 1.17.5

* Sat Mar 28 2026 Boris Yumankulov <boria138@altlinux.org> 1.17.2-alt1
- new version 1.17.2

* Mon Mar 23 2026 Boris Yumankulov <boria138@altlinux.org> 1.16.6-alt1
- new version 1.16.6

* Fri Mar 20 2026 Boris Yumankulov <boria138@altlinux.org> 1.16.5-alt1
- new version 1.16.5 (ALT bug: 58294)

* Wed Feb 18 2026 Boris Yumankulov <boria138@altlinux.org> 1.14.3-alt1
- new version 1.14.3

* Wed Feb 11 2026 Boris Yumankulov <boria138@altlinux.org> 1.14.2-alt1
- new version 1.14.2

* Mon Feb 02 2026 Boris Yumankulov <boria138@altlinux.org> 1.13.11-alt1
- initial build for ALT Sisyphus
