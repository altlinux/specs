Name: sdcc
Version: 8378
Release: alt1
Group: Development/C
URL: http://sdcc.sourceforge.net
License: GPL
Summary: Small Device C Compiler
Source: %name-%version.tar
#Patch: sdcc-5119-alt-glibc-2.11.3.patch
#Patch1: sdcc-5119-alt-SDCCicode.patch
#Patch2: sdcc-5119-alt-make-3.82.patch
BuildPreReq: flex gcc-c++ boost-devel gputils
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
License: GPL, LGPL
Group:         Development/C
Summary:       Libraries and Header Files for the SDCC C compiler
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
License:       GPL
Group:         Development/C
Summary:       Documentation for the SDCC C compiler
BuildArch:	noarch
%description doc
SDCC is a free open source, retargettable, optimizing ANSI C compiler
suite that targets a growing list of processors including the Intel
MCS51 based microprocessors (8031, 8032, 8051, 8052, etc.), Maxim
(formerly Dallas) DS80C390 variants, Freescale (formerly Motorola)
HC08 based (hc08, s08) and Zilog Z80 based MCUs (z80, z180, gbz80,
Rabbit 2000/3000, Rabbit 3000A). Work is in progress on supporting
the Microchip PIC16 and PIC18 targets. It can be retargeted for other
microprocessors.

%prep
%setup -q -n %name-%version
#%patch -p2
#%patch1 -p2
#%patch2 -p2
%build
%configure --docdir=%_docdir/%name-%version
%make_build
%install
%make_install DESTDIR=%buildroot install
#rm -fr /usr/src/tmp/sdcc-buildroot/usr/share/sdcc/lib/src

%files 
%_bindir/*

%files common
%_datadir/%name/*

%files doc
%_docdir/%name-%version/*

# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/%name-%version 


%changelog
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

