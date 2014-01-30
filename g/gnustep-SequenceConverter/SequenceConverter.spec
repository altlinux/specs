%set_verify_elf_method unresolved=strict

Name: gnustep-SequenceConverter
Version: 1.6.0
Release: alt2
Summary: Biological sequence file format conversion applet for GNUstep
License: Free
Group: Graphical desktop/GNUstep
Url: http://bioinformatics.org/biococoa/wiki/pmwiki.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
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
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%_bindir/*
%_libdir/GNUstep

%changelog
* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus

