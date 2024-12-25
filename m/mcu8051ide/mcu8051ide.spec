Name:    mcu8051ide
Version: 1.4.9
Release: alt1

Summary: IDE for MCS-51 based MCUs
License: GPLv2
Group:   Development/Tools
Url:     https://sourceforge.net/projects/mcu8051ide/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

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
%patch -p1

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
* Thu Dec 05 2024 Ulysses Apokin <ulysses@altlinux.org> 1.4.9-alt1
- Initial build for Sisyphus.
