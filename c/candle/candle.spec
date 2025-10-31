%define _unpackaged_files_terminate_build 1

Name: candle
Release: alt2
Version: 10.10.4

Summary: %name application with G-Code visualizer written in Qt
Group: Engineering
License: GPL-3.0-only
Url: https://github.com/Denvi/Candle
VCS: https://github.com/Denvi/Candle

# Source-url: https://github.com/Denvi/Candle/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name.desktop

Patch0: alt-fix-app-resource-paths.patch
Patch1: alt-prepare-cmakefile.patch
Patch2: alt-fix-camera-plugin-segmfault.patch
Patch3: alt-fix-openGL-context-restore-error.patch

BuildRequires: cmake
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-serialport-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-websockets-devel

%description
A simple and reliable program for controlling a CNC machine on GRBL
firmware, sending commands and G-codes. 

Supported functions:
* Controlling GRBL-based cnc-machine via console commands, buttons
on form, numpad.
* Monitoring cnc-machine state.
* Loading, editing, saving and sending of G-code files to cnc-machine.
* Visualizing G-code files.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

sed -i 's;^\(Categories=\)\(.*\)$;\1Graphics\;\2;' deploy/linux%_desktopdir/%name.desktop
%__cp -a deploy/linux/usr %buildroot/
find %buildroot{%_datadir,%_libdir}/%name -type f -name '*.ts' -exec rm -f {} \;

%files
%doc readme.md
%dir %_libdir/%name
%dir %_defaultdocdir/%name
%doc %_defaultdocdir/%name/LICENSE
%doc %_defaultdocdir/%name/help
%_bindir/%name
%_libdir/*.so
%_libdir/%name/*
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.ico

%changelog
* Fri Oct 31 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 10.10.4-alt2
- update the application's category list

* Thu Oct 30 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 10.10.4-alt1
- new version

* Wed Dec 25 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.2-alt4
- change the display of the translation file search application

* Mon Dec 02 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.2-alt3
- use xcb when starting the app
- fix the display of icons with a dark theme (closes: 50419)

* Tue Jul 16 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.2-alt2
- fix display of available translation (closes: 50420)
- set the name of the app window to a capital letter
- add an app to the start menu
- update the patch that fixes the app build

* Mon Apr 01 2024 Dmitrii A. Fomchenkov <sirius@altlinux.org> 1.2-alt1
- first build for sisyphus (closes: 46743)
