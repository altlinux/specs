AutoProv: no

%define nameUP StartWine
%define nameVR _v408
%define nameDN startwine

Name: startwine-launcher
Version: 4.0.8
Release: alt2

Summary: Installer StartWine-Launcher for Windows games

License: GPL-3.0-or-later
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
* Tue Dec 03 2024 Aleksandr Shamaraev <shad@altlinux.org> 4.0.8-alt2
- Added provides: startwine.

* Sat Nov 30 2024 Aleksandr Shamaraev <shad@altlinux.org> 4.0.8-alt1
- Update to version 4.0.8

* Wed Nov 27 2024 Aleksandr Shamaraev <shad@altlinux.org> 4.0.7-alt1
- Initial build for Sisyphus.
