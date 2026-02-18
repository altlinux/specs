%define xdg_name ru.linux_gaming.PortProtonQt
%define _unpackaged_files_terminate_build 1

Name: portprotonqt
Version: 0.1.11
Release: alt1

Summary: A modern GUI for PortProton project

License: GPL-3.0
Group: Games/Other
Url: https://git.linux-gaming.ru/Boria138/PortProtonQt

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-python3
BuildRequires: libvulkan-devel

Requires: qt6-svg udev pciutils mesa-info

ExclusiveArch: x86_64

%description
%summary

%prep
%setup

%build
%meson -Dpython_purelibdir=%python3_sitelibdir -Dudev_rulesdir=%_udevrulesdir
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc LICENSE
%_bindir/portprotonqt
%_bindir/vk_gpu_info
%_desktopdir/%xdg_name.desktop
%_datadir/metainfo/%xdg_name.metainfo.xml
%_datadir/bash-completion/completions/portprotonqt
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_udevrulesdir/60-portprotonqt.rules
%python3_sitelibdir/%name/

%changelog
* Wed Feb 18 2026 Boris Yumankulov <boria138@altlinux.org> 0.1.11-alt1
- new version 0.1.11
- switch pyproject to meson
- add log dependency

* Wed Jan 14 2026 Boris Yumankulov <boria138@altlinux.org> 0.1.10-alt1
- new version 0.1.10

* Mon Dec 08 2025 Boris Yumankulov <boria138@altlinux.org> 0.1.9-alt1
- new version 0.1.9

* Sun Oct 19 2025 Boris Yumankulov <boria138@altlinux.org> 0.1.8-alt1
- new version 0.1.8

* Tue Sep 23 2025 Mikhail Tergoev <fidel@altlinux.org> 0.1.6-alt1
- Initial build for ALT Sisyphus
