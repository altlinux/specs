Name: appliance-devel-hardware
Summary: Virtual package that require hardware development packages
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: Development/Other

# IDE
Requires: kicad

# PCB
Requires: pcb
Requires: pcb-library
Requires: pcb-doc
Requires: pcb-examples

# gEDA
Requires: geda
Requires: geda-gattrib
Requires: geda-gnetlist
Requires: geda-gschem
Requires: geda-gsymcheck
Requires: geda-symbols
Requires: geda-utils
Requires: geda-xgsch2pcb
Requires: geda-docs
Requires: geda-examples

# Gerber file viewer
Requires: gerbv
Requires: gerbv-examples

# VHDL
Requires: freehdl
Requires: gtkwave

# AVR
Requires: avr-binutils
Requires: avr-gcc
Requires: avr-gcc-c++
Requires: avr-libc
Requires: avr-libc-doc
Requires: avrdude
Requires: avrdude-docs
Requires: kontrollerlab
Requires: ponyprog2000
Requires: uisp

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

