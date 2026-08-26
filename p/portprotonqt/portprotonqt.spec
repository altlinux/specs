%define xdg_name ru.linux_gaming.PortProtonQt
%define _unpackaged_files_terminate_build 1

Name: portprotonqt
Version: 1.4.1
Release: alt1

Summary: Modern GUI for managing and launching games from PortProton and Steam

License: GPL-3.0
Group: Games/Other
Url: https://git.linux-gaming.ru/Linux-Gaming/PortProtonQt

Source: %name-%version.tar

BuildRequires(pre): meson rpm-build-python3
BuildRequires: libvulkan-devel libSDL3-devel

Requires: qt6-svg udev pciutils mesa-info qt6-imageformats python3(dbus_fast) libqt6-multimedia

ExclusiveArch: x86_64

# False positive from scripts
%filter_from_requires /gamemode-daemon/d
%filter_from_requires /plasma-workspace/d
%filter_from_requires /setxkbmap/d
%filter_from_requires /xfconf-utils/d
%filter_from_requires /qdbus/d
%filter_from_requires /xrandr/d
%filter_from_requires /xkbcomp/d

%description
%summary

%package os
Group: Games/Other
Summary: Meta package for portprotonqt-os for use system tabs
Requires: %name = %EVR
Requires: udisks2 bluez upower NetworkManager-daemon pulseaudio-utils
Requires: python3(qrcode)
%description os
%summary

%prep
%setup

%build
%meson -Dpython_purelibdir=%python3_sitelibdir -Dudev_rulesdir=%_udevrulesdir
%meson_build

%install
%meson_install

bash ./dev-scripts/generate-completions.sh
cd completions
install -Dm 0644 portprotonqt %buildroot%_datadir/bash-completion/completions/portprotonqt
install -Dm 0644 portprotonqt.fish %buildroot%_datadir/fish/vendor_completions.d/portprotonqt.fish
install -Dm 0644 _portprotonqt %buildroot%_datadir/zsh/site-functions/_portprotonqt
cd -

%find_lang %name

%files -f %name.lang
%doc LICENSE
%_bindir/portprotonqt
%_bindir/vk_gpu_info
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name.log.desktop
%_desktopdir/%xdg_name.silent.desktop
%_datadir/mime/packages/%xdg_name.xml
%_datadir/metainfo/%xdg_name.metainfo.xml
%_datadir/portproton/scripts/
%_datadir/portproton/conf/
%_datadir/bash-completion/completions/portprotonqt
%_datadir/fish/vendor_completions.d/portprotonqt.fish
%_datadir/zsh/site-functions/_portprotonqt
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_udevrulesdir/60-portprotonqt.rules
%python3_sitelibdir/%name/

%files os
%_datadir/polkit-1/rules.d/%xdg_name.rules
%_sysusersdir/portprotonqt.conf

%changelog
* Wed Aug 26 2026 Mikhail Tergoev <fidel@altlinux.org> 1.4.1-alt1
- new version 1.4.1

* Tue Aug 25 2026 Mikhail Tergoev <fidel@altlinux.org> 1.4.0-alt1
- new version 1.4.0
- portprotonqt-os package separated
- Fixes:
  + CVE-2026-59678: An Incorrect Authorization vulnerability in portprotonqt-os

* Mon Jul 13 2026 Mikhail Tergoev <fidel@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Wed Jun 10 2026 Mikhail Tergoev <fidel@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Tue May 26 2026 Mikhail Tergoev <fidel@altlinux.org> 1.1.0-alt1
- new version 1.1.0
- fix zh_CN locale

* Sat May 23 2026 Boris Yumankulov <boria138@altlinux.org> 1.0-alt1
- new version 1.0
- replace upstream
- bundle PortProton scripts (ALT bug: 58288 58286 58287)

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
