%define _unpackaged_files_terminate_build 1
%define candle_prefix %_libdir/%name

Name: candle
Release: alt3
Version: 1.2

Summary: %name application with G-Code visualizer written in Qt
Group: Engineering
License: GPL-3.0-only
Url: https://github.com/Denvi/Candle
VCS: https://github.com/Denvi/Candle/archive/refs/tags/v1.2b.tar.gz

Source: %name-%version.tar
Source1: %name.desktop
# Fixes build errors
Patch0: alt-build-fixes.patch
Patch1: alt-fix-translation.patch
Patch2: alt-capitalize-title.patch
Patch3: alt-invert-icons-if-the-theme-is-dark.patch

ExcludeArch: armh

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-serialport-devel

%description
A simple and reliable program for controlling a CNC machine on GRBL firmware,
sending commands and G-codes. 

Supported functions:

  * Controlling GRBL-based cnc-machine via console commands, buttons on form,
  numpad.
  * Monitoring cnc-machine state.
  * Loading, editing, saving and sending of G-code files to cnc-machine.
  * Visualizing G-code files.

%prep
%setup
%autopatch -p2

%build
%qmake_qt5 -o Makefile src/candle.pro
%make_build

%install
mkdir -p %buildroot{%_bindir,%_pixmapsdir,%_desktopdir,%candle_prefix}
install -m755 %name %buildroot%candle_prefix/%{name}-bin
install -Dpm 0644 src/images/%{name}_256.png %buildroot%_iconsdir/hicolor/256x256/apps/%name.png
install -Dpm 0644 %SOURCE1 %buildroot%_desktopdir/

mkdir -p %buildroot%_datadir/%name/translations
install -m644 src/translations/*.qm %buildroot%_datadir/%name/translations

cat>%buildroot%_bindir/%name<<-EOF
#!/bin/sh

export QT_QPA_PLATFORM=xcb
%candle_prefix/%{name}-bin \${1:+"\$@"}
EOF
%__chmod +x %buildroot%_bindir/%name

%files
%doc readme.md
%_bindir/%name
%candle_prefix
%_datadir/%name/translations/*.qm
%_desktopdir/%name.desktop
%_iconsdir/hicolor/256x256/apps/%name.png

%changelog
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
