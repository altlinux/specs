%define _unpackaged_files_terminate_build 1

Name: opari2
License: BSD
Group: Development/Tools
Summary: OPARI2 is a source-to-source instrumentation tool for OpenMP and hybrid codes
Version: 2.0.5
Release: alt1
Url: http://www.vi-hps.org/projects/score-p/

Source: %name-%version.tar

BuildRequires: gcc-c++ uncrustify doxygen gcc-fortran
BuildRequires: texlive-base-bin graphviz 

%description
OPARI2 is a source-to-source instrumentation tool for OpenMP and hybrid
codes.

%package devel
Summary: Development files of OPARI2
Group: Development/C++
Requires: %name = %EVR

%description devel
OPARI2 is a source-to-source instrumentation tool for OpenMP and hybrid
codes.

This package contains development files of OPARI2.

%package docs
Summary: Documentation for OPARI2
Group: Documentation
BuildArch: noarch

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

ln -s %_libexecdir/pomp2-parse-init-regions.awk %buildroot%_bindir/

%files
%doc AUTHORS ChangeLog COPYING README
%_bindir/*
%exclude %_bindir/%name-config
%_libexecdir/*.awk

%files devel
%_bindir/%name-config
%_includedir/*
%_datadir/%name

%files docs
%_docdir/%name

%changelog
* Fri Jul 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.5-alt1
- Updated to upstream version 2.0.5.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1.qa1
- NMU: applied repocop patch

* Thu Sep 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt1
- Updated to upstream version 2.0.2.

* Wed May 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Tue Sep 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

