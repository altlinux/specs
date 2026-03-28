%define _unpackaged_files_terminate_build 1

Name: faugus-launcher
Version: 1.17.2
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

Requires: gamemode
Requires: convert
Requires: typelib(AyatanaAppIndicator3)
Requires: typelib(Gtk) = 3.0

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output=%name.lang faugus-proton-manager faugus-run %name

%files -f %name.lang
%doc %_datadir/licenses/faugus-launcher/LICENSE
%_bindir/faugus-launcher
%_bindir/faugus-run
%_bindir/faugus-proton-manager
%_bindir/faugus-shortcut
%_desktopdir/faugus-launcher.desktop
%_desktopdir/faugus-shortcut.desktop
%python3_sitelibdir/faugus/
%_datadir/faugus-launcher/
%_iconsdir/hicolor/256x256/apps/*.png
%_iconsdir/hicolor/256x256/apps/faugus-mono.svg
%_iconsdir/hicolor/scalable/actions/*.svg
%_datadir/metainfo/faugus-launcher.metainfo.xml

%changelog
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



