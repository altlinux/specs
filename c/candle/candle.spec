%define _unpackaged_files_terminate_build 1

Name: candle
Release: alt1
Version: 1.2

Summary: %name application with G-Code visualizer written in Qt
Group: Engineering
License: GPL-3.0-only
Url: https://github.com/Denvi/Candle
VCS: https://github.com/Denvi/Candle/archive/refs/tags/v1.2b.tar.gz

Source: %name-%version.tar
# Fixes build errors
Patch0: alt-build-fixes.patch

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
mkdir -p %buildroot%_bindir
install -m755 %name %buildroot%_bindir

%files
%doc readme.md
%_bindir/%name

%changelog
* Mon Apr 01 2024 Dmitrii A. Fomchenkov <sirius@altlinux.org> 1.2-alt1
- first build for sisyphus (closes: 46743)
