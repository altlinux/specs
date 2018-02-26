Name: sifdec
Version: 2.0.0
Release: alt1.svn20090528.1
Summary: Decoder for translating SIF into Fortran 77 and data files
License: LGPL v2.1 or later
Group: File tools
Url: http://cuter.rl.ac.uk/cuter-www/sifdec/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://magi-trac-svn.mathappl.polymtl.ca/SVN/cuter/sifdec/branches/SifDec2
Source: %name-%version.tar.gz

Requires: %name-data = %version
BuildPreReq: gcc-fortran

%description
SifDec is a decoder. It tranlates test problems, written in so-called
Standard Input Format (SIF), into well-defined Fortran 77 and data
files. Once translated, these files may be manipulated to provide tools
suitable for testing optimization packages.

The SIF is a superset of the MPS modelling language. SifDec can
therefore decode any Linear Program coded in MPS format.

SifDec used to be part of, and has been extensively used with, the CUTE
testing environment and is now a vital component of the CUTEr testing
environment, which includes ready-to-use interfaces to existing
packages, such as MINOS, SNOPT, filterSQP, KNITRO, but could also serve
different purposes.

Novel features include the ability to decode parameterized test
problems, and to prepare the decoded problem for packages using
automatic differentiation techniques.

%package data
Summary: Data files for SifDec
Group: File tools
BuildArch: noarch

%description data
SifDec is a decoder. It tranlates test problems, written in so-called
Standard Input Format (SIF), into well-defined Fortran 77 and data
files. Once translated, these files may be manipulated to provide tools
suitable for testing optimization packages.

This package contains data files for SifDec.

%package doc
Summary: Documentation for SifDec
Group: Documentation
BuildArch: noarch

%description doc
SifDec is a decoder. It tranlates test problems, written in so-called
Standard Input Format (SIF), into well-defined Fortran 77 and data
files. Once translated, these files may be manipulated to provide tools
suitable for testing optimization packages.

This package contains documentation for SifDec.

%prep
%setup

%build
pushd custom
./install_mysifdec -double -debug
popd

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name/sif
install -d %buildroot%_man1dir
install -d %buildroot%_docdir/%name

pushd custom
rm -f bin/*akefile bin/README bin/*.o
install -m755 bin/* double/bin/%name %buildroot%_bindir
popd

install -p -m644 common/sif/* %buildroot%_datadir/%name/sif
install -p -m644 common/man/man1/* %buildroot%_man1dir
install -p -m644 common/doc/*.pdf %buildroot%_docdir/%name

%files
%doc COPYING-GLPL LICENSE TROUBLESHOOTING WHATSNEW
%_bindir/*
%_man1dir/*

%files data
%_datadir/%name

%files doc
%_docdir/%name

%changelog
* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20090528.1
- Rebuilt for debuginfo

* Tue Sep 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20090528
- Initial build for Sisyphus

