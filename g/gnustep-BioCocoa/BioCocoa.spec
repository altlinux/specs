%set_verify_elf_method unresolved=strict

Name: gnustep-BioCocoa
Version: 2.2.2
Release: alt1
Summary: Open source OpenStep (GNUstep/Cocoa) framework for bioinformatics
License: BSD
Group: Graphical desktop/GNUstep
Url: http://bioinformatics.org/biococoa/wiki/pmwiki.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %EVR

%description
BioCocoa is an open source OpenStep (GNUstep/Cocoa) framework for
bioinformatics written in Objective-C. We intend to provide OpenStep
programmers with a full suite of tools for handling and manipulating
biological sequences. OpenStep is a great framework for rapid
application development and it is therefore often used to create
innovative bioscientific apps. To speed up development even more,
BioCocoa wants to offer reusable OpenStep classes that are specific for
molecular biology and biofinformatics. At this time, BioCocoa includes:

* A set of model objects to represent biological sequences that are both
  easy to use, yet very powerful and lightweight.
* I/O classes to import and export sequences to and from a variety of
  commonly used formats including BEAST, Clustal, EMBL, Fasta, GCG-MSF,
  GDE, Hennig86, NCBI, NEXUS, NONA, PDB, Phylip, PIR, Plain/Raw,
  Swiss-Prot and TNT.
* Tools to manipulate and obtain information about sequences.
* Efficient caching so that large sequences maintained in files can be
  analyzed without loading them all into memory.
* Parsing classes for other biological data such as microarray gene
  expression, biomedical ontologies and metabolic models.
* An NSTextView based class to display sequences.
* BioCocoa can be used to create applications Apple Mac OSX using Cocoa,
  and on Linux and Windows using GNUstep.

%package -n lib%name
Summary: Shared libraries of BioCocoa
Group: System/Libraries

%description -n lib%name
BioCocoa is an open source OpenStep (GNUstep/Cocoa) framework for
bioinformatics written in Objective-C. We intend to provide OpenStep
programmers with a full suite of tools for handling and manipulating
biological sequences. OpenStep is a great framework for rapid
application development and it is therefore often used to create
innovative bioscientific apps. To speed up development even more,
BioCocoa wants to offer reusable OpenStep classes that are specific for
molecular biology and biofinformatics.

This package contains shared libraries of BioCocoa.

%package -n lib%name-devel
Summary: Development files of BioCocoa
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
BioCocoa is an open source OpenStep (GNUstep/Cocoa) framework for
bioinformatics written in Objective-C. We intend to provide OpenStep
programmers with a full suite of tools for handling and manipulating
biological sequences. OpenStep is a great framework for rapid
application development and it is therefore often used to create
innovative bioscientific apps. To speed up development even more,
BioCocoa wants to offer reusable OpenStep classes that are specific for
molecular biology and biofinformatics.

This package contains development files of BioCocoa.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd %buildroot%_libdir
for j in BioCocoa; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/Current/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$i
			rm GNUstep/Frameworks/$j.framework/Versions/Current/$j
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$j
		done
	done
done
popd

%files
%doc ChangeLog *.txt
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/BioCocoa.framework/Versions/2/Headers
%exclude %_libdir/GNUstep/Frameworks/BioCocoa.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/BioCocoa.framework/Versions/2/Headers
%_libdir/GNUstep/Frameworks/BioCocoa.framework/Headers

%changelog
* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus

