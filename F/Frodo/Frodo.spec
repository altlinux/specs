# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install swig
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 4.1b
%define pkgversion %(echo %version|sed s/\\\\\./\\_/)

Summary: Commodore 64 emulator
Name: Frodo
Version: 4.1b
Release: alt3
License: Distributable
Group: Emulators
URL: http://frodo.cebix.net/
Source0: http://frodo.cebix.net/downloads/%{name}V%{pkgversion}.Src.tar.gz
Source1: Frodo.png
Source2: Frodo.desktop
Source3: FrodoPC.desktop
Source4: FrodoSC.desktop
Patch0: Frodo-4.1b-paths.patch
Patch1: Frodo-4.1b-opt.patch
Patch2: Frodo-4.1b-alpha.patch
Patch3: Frodo-4.1b-SAM.patch
Patch4: Frodo-4.1b-gcc6.patch
BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: libSDL-devel >= 1.2.0
BuildRequires: libXt-devel 
BuildRequires: desktop-file-utils
Requires: icon-theme-hicolor
Source44: import.info

%package gui
Summary: Preferences editor for Frodo
Group: Emulators
Requires: %{name}
Requires: libtk tk

%description
Frodo V4.1 is a free, portable C64 emulator for BeOS, Unix, MacOS,
AmigaOS, RiscOS and WinNT/95 systems.

This emulator focuses on the exact reproduction of special graphical
effects possible on the C64, and has therefore relatively high system
requirements. It should only be run on systems with at least a
PowerPC/Pentium/68060. Frodo is capable of running most games and
demos correctly, even those with FLI, FLD, DYCP, open borders,
multiplexed sprites, timing dependent decoders, fast loaders etc. 6510
emulation: All undocumented opcodes, 100 percent correct decimal mode,
instruction/cycle exact emulation. VIC emulation: Line-/cycle-based
emulation, all display modes, sprites with collisions/priorities, DMA
cycles, open borders, all $d011/$d016 effects. SID emulation:
Real-time digital emulation (16 bit, 44.1kHz), including filters (only
under BeOS, Linux, HP-UX, MacOS and AmigaOS). 1541 emulation: Drive
simulation in directories, .d64/x64 or .t64/LYNX files, or
processor-level 1541 emulation that works with about 95 percent of all
fast loaders and even some copy protection schemes. Other peripherals:
Keyboard and joystick (real joysticks (only under BeOS, Linux and
AmigaOS) or keyboard emulation). The full source code in C++ is
available. Frodo is freeware.

%description gui
An enhanced Tcl/Tk preferences GUI for Frodo written by Gerard Decatrel

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1

%build
cd Src
autoconf
%configure
%make_build all FRODOHOME="\\\"%{_datadir}/Frodo/\\\""

%install
install -d 755 %{buildroot}%{_bindir}
install -d 755 %{buildroot}%{_datadir}/Frodo/{64prgs,64imgs}
install -m 755 Src/Frodo Src/FrodoPC Src/FrodoSC %{buildroot}%{_bindir}
install -m 755 TkGui.tcl %{buildroot}%{_datadir}/Frodo
install -m 644 "Frodo Logo" "1541 ROM" "Basic ROM" "Char ROM" "Kernal ROM" \
  %{buildroot}%{_datadir}/Frodo
install -m 644 64prgs/* %{buildroot}%{_datadir}/Frodo/64prgs

#install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/

#install desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor dribble        \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}
desktop-file-install --vendor dribble        \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE3}
desktop-file-install --vendor dribble        \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE4}

%files
%{_bindir}/Frodo
%{_bindir}/FrodoPC
%{_bindir}/FrodoSC
%{_datadir}/Frodo
%{_datadir}/applications/dribble-%{name}.desktop
%{_datadir}/applications/dribble-%{name}PC.desktop
%{_datadir}/applications/dribble-%{name}SC.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%doc CHANGES Docs/*
%exclude %{_datadir}/Frodo/TkGui.tcl

%files gui
%{_datadir}/Frodo/TkGui.tcl

%changelog
* Sat Sep 25 2021 Ilya Mashkin <oddity@altlinux.ru> 4.1b-alt3
- Build for Sisyphus

* Mon Sep 20 2021 Igor Vlasenko <viy@altlinux.org> 4.1b-alt2_22
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 4.1b-alt2_21
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 4.1b-alt2_20
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 4.1b-alt1_20
- update to new release by fcimport

* Thu Feb 27 2020 Igor Vlasenko <viy@altlinux.ru> 4.1b-alt1_19
- update to new release by fcimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 4.1b-alt1_18
- new version

