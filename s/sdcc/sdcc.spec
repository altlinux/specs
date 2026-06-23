Name: sdcc
Version: 4.6.0
Release: alt1
Epoch: 1

Summary: Small Device C Compiler
License: GPLv2
Group: Development/C
Url: http://sdcc.sourceforge.net

Source: %name-%version.tar

BuildRequires: rpm-build-python3
BuildRequires: flex gcc-c++ boost-devel >= 1:1.85.0-alt3 gputils >= 1.5.2
BuildRequires: zlib-devel

Provides: sdcc-common = %EVR sdcc-doc = %EVR
Obsoletes: sdcc-common sdcc-doc

%description
SDCC is a free open source, retargettable, optimizing ANSI C compiler
suite that targets a growing list of processors including the Intel
MCS51 based microprocessors (8031, 8032, 8051, 8052, etc.), Maxim
(formerly Dallas) DS80C390 variants, Freescale (formerly Motorola)
HC08 based (hc08, s08) and Zilog Z80 based MCUs (z80, z180, gbz80,
Rabbit 2000/3000, Rabbit 3000A). Work is in progress on supporting
the Microchip PIC16 and PIC18 targets. It can be retargeted for other
microprocessors.

%package common
License: GPLv2 LGPLv2
Group:   Development/C
Summary: Libraries and Header Files for the SDCC C compiler

%description common
SDCC is a free open source, retargettable, optimizing ANSI C compiler
suite that targets a growing list of processors including the Intel
MCS51 based microprocessors (8031, 8032, 8051, 8052, etc.), Maxim
(formerly Dallas) DS80C390 variants, Freescale (formerly Motorola)
HC08 based (hc08, s08) and Zilog Z80 based MCUs (z80, z180, gbz80,
Rabbit 2000/3000, Rabbit 3000A). Work is in progress on supporting
the Microchip PIC16 and PIC18 targets. It can be retargeted for other
microprocessors.

%package doc
Group:     Development/C
Summary:   Documentation for the SDCC C compiler
BuildArch: noarch

%description doc
SDCC is a free open source, retargettable, optimizing ANSI C compiler
suite that targets a growing list of processors including the Intel
MCS51 based microprocessors (8031, 8032, 8051, 8052, etc.), Maxim
(formerly Dallas) DS80C390 variants, Freescale (formerly Motorola)
HC08 based (hc08, s08) and Zilog Z80 based MCUs (z80, z180, gbz80,
Rabbit 2000/3000, Rabbit 3000A). Work is in progress on supporting
the Microchip PIC16 and PIC18 targets. It can be retargeted for other
microprocessors.

%global _configure_detect_runstatedir %nil

%prep
%setup
find support -type f |xargs grep -l 'env python' |\
	xargs sed -ri '/^#!\/usr\/bin\/env python$/ s,env python,python3,'

%build
export CC=gcc CXX=g++
%configure \
	--docdir=%_docdir/%name-%version \
	--enable-werror=no \
	%nil

%make_build sdcc-sdbinutils
%make_build

%install
%makeinstall_std STRIP=:
# clashes with binutils
rm -vf %buildroot%_bindir/c++filt
rm -vf %buildroot%_includedir/*
rm -vf %buildroot%_infodir/*
rm -rvf %buildroot%_datadir/locale
# not used anywhere
rm -vf %buildroot%_libdir/*.a
# bindir copy
rm -rvf %buildroot%_prefix/%_target_alias
# ain't no such thing
rm -vf %buildroot%_man1dir/serialview*

%brp_strip_none %_datadir/sdcc/*

%files 
%_bindir/*
%_datadir/%name
%_libexecdir/sdcc
%_man1dir/ucsim.1*
%_docdir/%name-%version

%changelog
* Tue Jun 23 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1:4.6.0-alt1
- 4.6.0 released

* Wed Apr 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1:4.5.0-alt2
- fixed build with gcc15

* Wed Jan 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1:4.5.0-alt1
- 4.5.0 released

* Thu Oct 31 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1:4.4.0-alt4
- pin gcc13 for build

* Thu Jun 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1:4.4.0-alt3
- rebuilt after boost #281 fixed

* Thu May 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1:4.4.0-alt2
- fixed build with boost 1.85

* Wed Jan 31 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:4.4.0-alt1
- 4.4.0

* Tue Jul 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:4.3.0-alt1
- 4.3.0

* Wed Apr 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:4.2.0-alt1
- 4.2.0

* Tue Nov 30 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:4.1.0-alt1
- 4.1.0

* Thu Jun 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.9.0-alt2
- Updated build dependencies.

* Mon Oct 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.9.0-alt1
- Updated to upstream version 3.9.0 (Closes: #37328).

* Tue Sep 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.6.0-alt1
- Updated to upstream version 3.6.0.

* Thu Mar 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8378-alt1.1
- Removed -Werror flag

* Sat Jan 12 2013 Yury A. Romanov <damned@altlinux.ru> 8378-alt1
- Switched to 8378

* Tue Nov 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5119-alt1.qa3
- Fixed build with make 3.82

* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5119-alt1.qa2
- Fixed build with glibc 2.11.3

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 5119-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for sdcc
  * postclean-05-filetriggers for spec file

* Fri Mar 28 2008 Yury A. Romanov <damned@altlinux.ru> 5119-alt1
- 5119

* Thu Jan 03 2008 Yury A. Romanov <damned@altlinux.ru> 4988-alt1
- Initial build

