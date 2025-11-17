%define _unpackaged_files_terminate_build 1
%define candle_prefix %_libdir/%name

Name: candle
Release: alt1
Version: 10.11.1

Summary: %name application with G-Code visualizer written in Qt
Group: Engineering
License: GPL-3.0-only
Url: https://github.com/Denvi/Candle
VCS: https://github.com/Denvi/Candle

# Source-url: https://github.com/Denvi/Candle/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name.desktop

Patch0: alt-fix-app-resource-paths.patch
Patch1: alt-dont-use-rpath.patch
Patch2: alt-start-with-system-locale.patch

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
%autopatch -p1

%build
%cmake \
    -DCMAKE_INSTALL_BINDIR=%candle_prefix \
    #
%cmake_build

%install
%cmake_install

%__mv %buildroot%candle_prefix/%name %buildroot%candle_prefix/%{name}-bin
%__mkdir %buildroot%_bindir
cat>%buildroot%_bindir/%name<<-EOF
#!/bin/sh

export QT_QPA_PLATFORM=xcb
%candle_prefix/%{name}-bin \${1:+"\$@"}
EOF
%__chmod +x %buildroot%_bindir/%name

sed -i 's;^\(Categories=\)\(.*\)$;\1Graphics\;\2;' deploy/linux%_desktopdir/%name.desktop
%__cp -a deploy/linux/usr %buildroot/
find %buildroot%_datadir/%name -type f -name '*.ts' -exec rm -f {} \;

%files
%doc readme.md
%dir %_libdir/%name
%dir %_defaultdocdir/%name
%doc %_defaultdocdir/%name/LICENSE
%doc %_defaultdocdir/%name/help
%_bindir/%name
%candle_prefix
%_libdir/*.so
%_libdir/%name/*
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.ico

%changelog
* Mon Nov 17 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 10.11.1-alt1
- use the current system locale upon application launch (closes: 56815)
- fix the visibility of the float button that docks the window back to the
  main window (closes: 56821)
- new verson

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
