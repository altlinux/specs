%define _unpackaged_files_terminate_build 1

Name: winehelper
Version: 0.10.0
Release: alt1

Summary: Program for easy installation of Windows applications.

License: LGPLv2+
Group: Emulators
Url: https://git.linux-gaming.ru/CastroFidel/winehelper

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

Requires: wine winetricks
Requires: p7zip zenity wmctrl
Requires: glibc-core libstdc++6 glibc-pthread glibc-nss libunwind libunixODBC2 libgnutls30
Requires: libnm libnss libnss-mdns libnsl1 libfreetype libcups libfontconfig1 ca-certificates
Requires: ocl-icd libGL libEGL libvulkan1 xorg-dri-swrast xorg-dri-intel xorg-dri-radeon

%add_findreq_skiplist %_datadir/%name/autoinstall/*
%add_findreq_skiplist %_datadir/%name/manualinstall/*
%add_findreq_skiplist %_datadir/%name/testinstall/*
%add_findreq_skiplist %_datadir/%name/database/*

ExclusiveArch: x86_64

%description
Program for easy installation of Windows applications with the possibility
of automatic prefix tuning.

%package qt
Group: Emulators
Summary: Graphical interface for WineHelper
Requires: %name = %EVR
%description qt
%summary

%prep
%setup

%build
%install
# base files:
install -Dm755 %name %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/%name/{autoinstall,manualinstall,testinstall,database,image}
install -m755 dependencies.sh %buildroot%_datadir/%name/
install -m644 sha256sum.list %buildroot%_datadir/%name/
install -m644 manualinstall/* %buildroot%_datadir/%name/manualinstall/
install -m644 autoinstall/*  %buildroot%_datadir/%name/autoinstall/
install -m644 testinstall/*  %buildroot%_datadir/%name/testinstall/
install -m644 database/* %buildroot%_datadir/%name/database/
install -m644 image/*.png %buildroot%_datadir/%name/image/

install -Dm644 auto_completion/bash_completion/%name %buildroot%_sysconfdir/bash_completion.d/%name
install -Dm644 auto_completion/zsh_completion/_%name %buildroot%_datadir/zsh/Completion/Linux/_%name

# GUI files:
install -Dm644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm644 image/gui/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -Dm644 image/gui/%name-symbolic.svg %buildroot%_iconsdir/hicolor/symbolic/apps/%name-symbolic.svg
install -m755 %{name}_gui.py %buildroot%_datadir/%name/%{name}_gui.py

%files
%doc LICENSE LICENSE_AGREEMENT CHANGELOG COPYING THIRD-PARTY GENERAL README.md
%_bindir/%name
%_datadir/%name/
%exclude %_datadir/%name/%{name}_gui.py
%_sysconfdir/bash_completion.d/%name
%_datadir/zsh/Completion/Linux/_%name

%files qt
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/symbolic/apps/%name-symbolic.svg
%_datadir/%name/%{name}_gui.py

%changelog
* Wed Mar 18 2026 Mikhail Tergoev <fidel@altlinux.org> 0.10.0-alt1
- updated to version 0.10.0
- updated installation scripts: emias, ctm-service (ALT bug: 58046)
- added installation scripts: apropos-z, olimp
- added wine-cx support (fork crossover)
- GUI: fixes and improvements

* Fri Feb 13 2026 Mikhail Tergoev <fidel@altlinux.org> 0.9.0-alt1
- updated to version 0.9.0
- added wine-wow64 support
- added wine-cpcsp_proxy support for wine-wow64
- added an option to skip 32-bit dependency checking if wine-wow64 is used
- added installation scripts: dialux 4, ksamu, emias
- updated the ved-control installation script
- tax programs have been migrated to 64-bit prefixes and wine-wow64
- t-flex programs have been migrated to use wine-wow64
- arm-kt programs have been migrated to use wine-wow64
- improved base prefix creation
- improved creation and unpacking of prefix backups
- system winetricks is used
- GUI: main functions fixed/improved
- GUI: icon display fixed for shortcuts (desktop files)
- GUI: added the ability to launch the "Wine Control Panel"
- GUI: moved file association, ESYNC, FSYNC, DXVK, and VK3D to "Advanced Settings"
- GUI: removed unused Wine versions
- GUI: added a filter to limit Wine version usage based on prefix

* Fri Oct 24 2025 Mikhail Tergoev <fidel@altlinux.org> 0.8.0-alt1
- updated to version 0.8.0
- added autodetection of .reg and .dll files to add them to the prefix registry
- added links to certificate pages to the "Help" tab
- other minor improvements and optimizations to scripts and the graphical interface

* Mon Oct 20 2025 Mikhail Tergoev <fidel@altlinux.org> 0.7.0-alt1
- updated to version 0.7.0
- GUI: added a button to open a directory with backups and logs
- GUI: added a button to open a directory with a prefix
- GUI: added a button to block buttons for an installed application if it is already running
- GUI: added a display of the installation process for third-party components using winetricks
- GUI: added the ability to display and install test scripts (disabled by default)
- added installation scripts for t-flex version 18
- added a list of test software installation scripts to the CLI
- added the ability to associate files for transfer to applications launched in WineHelper

* Wed Oct 01 2025 Mikhail Tergoev <fidel@altlinux.org> 0.6.0-alt1
- updated to version 0.6.0
- fixed typos (ALT bug: 55538)
- added Qt5 graphics mode
- added tray icon for Qt5 graphics mode
- updated installation scripts for t-flex-*
- updated installation script for scadoffice
- added manual installation of NetTest (demo version)
- added ARM-KT installation scripts
- winehelper killall - kills only processes running in WinwHelper
- other minor script improvements and optimizations

* Mon Jul 14 2025 Mikhail Tergoev <fidel@altlinux.org> 0.5.0-alt1
- 0.5.0
- removed requires: cups-pdf (ALT bug: 55212)
- removed check requires libOSMesa from scripts (ALT bug: 55211)

* Fri Jul 04 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.9-alt1
- 0.4.9

* Tue Jul 01 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.7-alt1
- 0.4.7
- updated scripts and prefix for ved-* and ctm-* (ALT bug: 54921 54922)

* Thu Jun 26 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.6-alt1
- 0.4.6

* Thu Jun 19 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.5-alt1
- 0.4.5

* Wed Jun 18 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.3-alt1
- 0.4.3
- removed requires: fonts-ttf-ms (ALT bug: 54833)

* Fri May 30 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.0-alt1
- 0.4.0

* Tue May 27 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.9-alt1
- 0.3.9

* Mon May 26 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.8-alt1
- 0.3.8
- removed command: update-menus (ALT bug: 54274)

* Tue May 06 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.7-alt2
- added new manualinstall path

* Tue May 06 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.7-alt1
- updated to version 0.3.7
- updated check: noexec only for /home (ALT bug: 54095)

* Wed Mar 12 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.2-alt1
- initial build for ALT Sisyphus
