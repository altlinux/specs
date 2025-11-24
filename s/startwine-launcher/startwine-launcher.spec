AutoProv: no

%define nameUP StartWine
%define nameVR _v412
%define nameDN startwine

Name: startwine-launcher
Version: 412
Release: alt1

Summary: Installer StartWine-Launcher for Windows games

License: GPL-3.0
Group: Games/Other
Url: https://github.com/RusNor/StartWine-Launcher
Vcs: https://github.com/RusNor/StartWine-Launcher

Requires: zenity sysctl-conf-userns yad wget fuse curl

Source: %name-%version.tar

ExclusiveArch: x86_64

Provides: startwine = %EVR

%description
%summary

%prep
%setup

cat > %_builddir/%name-%version/%nameUP.desktop <<_EOF_
[Desktop Entry]
Name=StartWine
Name[ru]=StartWine
Comment=Software for launchers Microsoft Windows programs
Comment[ru]=Средство для запуска программ Microsoft Windows
Categories=Game;
Type=Application
Exec=startwine %F
Icon=StartWine
StartupNotify=true
Terminal=false
_EOF_

%build
%install
install -Dm755 %nameUP%nameVR %buildroot%_bindir/%nameDN
install -Dm644 %nameUP.desktop %buildroot%_desktopdir/%nameUP.desktop
install -Dm644 %nameUP.svg %buildroot%_iconsdir/hicolor/scalable/apps/%nameUP.svg


%files
%_bindir/%nameDN
%_desktopdir/%nameUP.desktop
%_iconsdir/hicolor/scalable/apps/%nameUP.svg

%changelog
* Mon Nov 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 412-alt1
- 411 -> 412:
  + Updated list of Wine versions.
  + Updated list of dxvk and vkd3d versions.
  + Fixed helper functions in sw_runlib.
  + Fixed EA Launcher autoinstall.
  + Added older versions of Wine staging and Proton Ge, maybe someone will need it.
  + Other improvements and fixes.

* Wed Sep 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 411-alt1
- 410 -> 411:
  + Updated default prefix backup.
  + Updated prefix configurations.
  + Updated list of Wine versions.
  + Updated list of dxvk and vkd3d versions.
  + Updated libs in utils.
  + Fixed DLSS option.
  + Fixed games autoinstall.
  + Removed OpenGL mode message.
  + Removed VULKAN mode message.
  + Added output colors in terminal.
  + wine explorer now opens in of current prefix.

* Sun Apr 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 410-alt1
- 4.0.9 -> 410

* Mon Mar 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.0.9-alt1
- 4.0.9

* Tue Dec 03 2024 Aleksandr Shamaraev <shad@altlinux.org> 4.0.8-alt2
- Added provides: startwine.

* Sat Nov 30 2024 Aleksandr Shamaraev <shad@altlinux.org> 4.0.8-alt1
- Update to version 4.0.8

* Wed Nov 27 2024 Aleksandr Shamaraev <shad@altlinux.org> 4.0.7-alt1
- Initial build for Sisyphus.
