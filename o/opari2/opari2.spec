Name: opari2
License: BSD
Group: Development/Tools
Summary: OPARI2 is a source-to-source instrumentation tool for OpenMP and hybrid codes
Version: 1.1.1
Release: alt1
Url: http://www.vi-hps.org/projects/score-p/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.vi-hps.org/upload/packages/opari2/opari2-1.1.1.tar.gz

BuildPreReq: gcc-c++ uncrustify doxygen gcc-fortran
BuildPreReq: texlive-base-bin graphviz 

%description
OPARI2 is a source-to-source instrumentation tool for OpenMP and hybrid
codes.

%package devel
Summary: Development files of OPARI2
Group: Development/C++

%description devel
OPARI2 is a source-to-source instrumentation tool for OpenMP and hybrid
codes.

This package contains development files of OPARI2.

%package docs
Summary: Documentation for OPARI2
Group: Documentation

%description docs
OPARI2 is a source-to-source instrumentation tool for OpenMP and hybrid
codes.

This package contains documentation for OPARI2.

%prep
%setup

%build
#autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING README
%_bindir/*
%exclude %_bindir/%name-config

%files devel
%_bindir/%name-config
%_includedir/*
%_datadir/%name

%files docs
%_docdir/%name

%changelog
* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Tue Sep 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

