Name: cc65
Version: 2.19
Release: alt1
Summary: A free C compiler for 6502 based systems
Group: Development/Tools
# For license clarification see:
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=714058#30
License: zlib
Url: https://cc65.github.io
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc
BuildRequires: make

Requires: %name-common = %version-%release

#Recommends:     %name-doc = %version-%release
#Recommends:     %name-utils%{?_isa} = %version-%release

%description
cc65 is a complete cross development package for 65(C)02 systems,
including a powerful macro assembler, a C compiler, linker,
librarian and several other tools.

cc65 has C and runtime library support for many of the old 6502
machines, including

- the following Commodore machines:
  - VIC20
  - C16/C116 and Plus/4
  - C64
  - C128
  - CBM 510 (aka P500)
  - the 600/700 family
  - newer PET machines (not 2001).
- the Apple ]\[+ and successors.
- the Atari 8 bit machines.
- the Atari 2600 console.
- the Atari 5200 console.
- GEOS for the C64, C128 and Apple //e.
- the Bit Corporation Gamate console.
- the NEC PC-Engine (aka TurboGrafx-16) console.
- the Nintendo Entertainment System (NES) console.
- the Watara Supervision console.
- the VTech Creativision console.
- the Oric Atmos.
- the Oric Telestrat.
- the Lynx console.
- the Ohio Scientific Challenger 1P.

%package devel
Summary: Development files for %name
BuildArch: noarch
Group: Development/Tools
Requires: %name = %version-%release
Provides: %name-common = %version-%release

%description devel
This package contains the development files needed to
compile and link applications for the 65(C)02 CPU with
the %name cross compiler toolchain.

# %package doc
# Summary: Documentation files for %name
# BuildArch: noarch
# Group: Development/Documentation
# BuildRequires: linuxdoc-tools
# BuildRequires: texinfo
# 
# %description doc
# This package contains the documentation files for %name.

%package utils
Summary: Additional utilities for %name
BuildRequires: zlib-devel
Group: Development/Tools
%description utils
This package contains the additional utilities for %name.

They are not needed for compiling applications with %name,
but might be handy for some additional tasks.

Since these utility programs have some heavier dependencies,
and also can be used without the need of installing %name,
they have been split into this package.

%prep
%setup

%build

# Main binaries
%make_build 

# Additional binaries
mkdir -p util_bin
gcc util/atari/ataricvt.c \
  -o util_bin/ataricvt65    
gcc util/gamate/gamate-fixcart.c \
  -o util_bin/gamate-fixcart65  
gcc util/zlib/deflater.c \
  -o util_bin/deflater65 -lz

# Documentation
# make doc  

%install

# Main binaries
mkdir -p %buildroot%prefix
%makeinstall_std PREFIX=%_prefix

# Additional binaries
install -p -m 0755 util/ca65html %buildroot%_bindir
install -p -m 0755 util_bin/* %buildroot%_bindir

# Documentation


%files
%doc LICENSE README.md
%_bindir/ar65
%_bindir/ca65
%_bindir/cc65
%_bindir/chrcvt65
%_bindir/cl65
%_bindir/co65
%_bindir/da65
%_bindir/grc65
%_bindir/ld65
%_bindir/od65
%_bindir/sim65
%_bindir/sp65

%files devel
%doc LICENSE README.md
%_datadir/%name

%files utils
%doc LICENSE README.md
%_bindir/ataricvt65
%_bindir/ca65html
%_bindir/deflater65
%_bindir/gamate-fixcart65

# %files doc
# %doc LICENSE README.md
# %doc %_docdir/%name

%changelog
* Sat Jan 09 2021 Artyom Bystrov <arbars@altlinux.org> 2.19-alt1
- initial build for ALT Sisyphus
