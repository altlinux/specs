%set_verify_elf_method unresolved=strict

Name: gnustep-SequenceConverter
Version: 1.6.0
Release: alt5.1
Summary: Biological sequence file format conversion applet for GNUstep
License: Free
Group: Graphical desktop/GNUstep
Url: http://bioinformatics.org/biococoa/wiki/pmwiki.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-BioCocoa
Requires: gnustep-back

%description
SequenceConverter is a GNUstep applet to convert between sequence file
formats. The BioCocoa framework provides developers with the opportunity
to add support for reading and writing BEAST, Clustal, EMBL, Fasta,
GCG-MSF, GDE, Hennig86, NCBI, NEXUS, NONA, PDB, Phylip, PIR, Plain/Raw,
Swiss-Prot and TNT files by writing only three lines of code. The
framework is written in Cocoa (Objective-C).

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	OBJCFLAGS="%optflags -DGNUSTEP" \
	USE_NONFRAGILE_ABI=no
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt5.1
- NMU: Rebuild with libgnutls30.

* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt5
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt4
- Built with clang

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt3
- Built with gcc

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus

