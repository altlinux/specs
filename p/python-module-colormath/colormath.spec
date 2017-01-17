%define _unpackaged_files_terminate_build 1
%define oname colormath

%def_with python3

Name: python-module-%oname
Version: 2.1.1
Release: alt1
Summary: Python module that abstracts common color math operations
License: GPLv3
Group: Development/Python
Url: http://pypi.python.org/pypi/colormath
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gtaylor/python-colormath.git
Source0: https://pypi.python.org/packages/f5/f0/1358c821de66e5f3fc107b8a1afbea100a3bbaa0f7024f990b5d1911a055/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
This module implements a large number of different color operations such
as color space conversions, Delta E, and density to spectral.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 module that abstracts common color math operations
Group: Development/Python3

%description -n python3-module-%oname
This module implements a large number of different color operations such
as color space conversions, Delta E, and density to spectral.
%endif

%prep
%setup -q -n %{oname}-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug
%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt PKG-INFO README.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt examples PKG-INFO README.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.git20140701.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.git20140701
- Version 2.0.2

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20130430
- New snapshot

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.8-alt2.git20121128.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20121128
- New snapshot

* Sat May 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20110928
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.git20110928
- Initial build for Sisyphus

