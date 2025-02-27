Name:    mcu8051ide
Version: 1.4.9
Release: alt2

Summary: IDE for MCS-51 based MCUs
License: GPLv2
Group:   Development/Tools
Url:     https://sourceforge.net/projects/mcu8051ide/

Source: %name-%version.tar
Patch0: 0001-corrected-to-the-current-project-link.patch
Patch1: 0002-fixed-obsolete-CMakeList.txt.patch
Patch2: 0003-removed-m5-lib-from-mcu8051ide.patch

BuildRequires(pre): cmake rpm-build-xdg

Requires: tcl tk bwidget tcl-pkg-incrtcl4 tcl-tdom tcl-img tcllib tclx

BuildArch: noarch

%description
Graphical integrated development environment for 8051.
MCU 8051 IDE is an integrated development environment for microcontrollers
based on 8051. Supported programming languages are C and assembly. It has
its own assembler and it support two other external assemblers. For C
language it uses the SDCC compiler.

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%doc ChangeLog LICENSE README doc/handbook/%name.en.pdf
%_datadir/appdata/%name.appdata.xml
%_datadir/applications/%name.desktop
%_man1dir/%name.1.xz
%_xdgmimedir/packages/application-x-%name.xml
%_pixmapsdir/%name.png
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Wed Feb 26 2025 Ulysses Apokin <ulysses@altlinux.org> 1.4.9-alt2
- Fix segmentation fault (ALT #52967).

* Thu Dec 05 2024 Ulysses Apokin <ulysses@altlinux.org> 1.4.9-alt1
- Initial build for Sisyphus.
