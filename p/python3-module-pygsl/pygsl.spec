%define oname pygsl

Name: python3-module-%oname
Version: 2.3.0
Release: alt2.1

Summary: Python interface for GNU Scientific Library (GSL)
License: GPLv2
Group: Development/Python3
Url: http://pygsl.sourceforge.net/

Source: %oname-%version.tar.gz
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libgsl-devel libnumpy-py3-devel
BuildRequires: python3-module-numpy swig

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/gsl_dist

%description
This project provides a python interface for the GNU scientific library
(GSL).

%package devel
Summary: Development files of Python interface for GSL
Group: Development/Python3
BuildArch: noarch
Requires: %name = %version-%release

%description devel
This project provides a python interface for the GNU scientific library
(GSL).

This package contains development files of Python interface for GSL.

%package testing
Summary: Tests for Python interface for GSL
Group: Development/Python3
Requires: %name = %version-%release

%description testing
This project provides a python interface for the GNU scientific library
(GSL).

This package contains tests for Python interface for GSL.

%package docs
Summary: Documentation for Python interface for GSL
Group: Development/Documentation
BuildArch: noarch

%description docs
This project provides a python interface for the GNU scientific library
(GSL).

This package contains documentation for Python interface for GSL.

%package examples
Summary: Examples for Python interface for GSL
Group: Development/Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description examples
This project provides a python interface for the GNU scientific library
(GSL).

This package contains examples for Python interface for GSL.

%prep
%setup
%patch0 -p2

rm -f swig_src/*

%build
%__python3 setup.py config
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc CREDITS ChangeLog README TODO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/testing

%files devel
%_includedir/*/*

%files testing
%python3_sitelibdir/%oname/testing

%files docs
%doc doc/*.html

%files examples
%doc examples/*


%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.3.0-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt2
- Fixed build with numpy.

* Tue Mar 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.3.0-alt1
- Version updated to 2.3.0
- porting to python3.

* Tue Aug 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.0-alt1
- Updated to upstream version 2.2.0.

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt3
- Rebuilt with gsl90 instead of gsl

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt2.1
- Rebuild with Python-2.7

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt2
- Rebuilt for debuginfo

* Tue Dec 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1
- Initial build for Sisyphus

