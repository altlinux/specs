%define oname blessings

%def_disable check

Name: python3-module-blessings
Version: 1.7
Release: alt1

Summary: A thin, practical wrapper around terminal capabilities in Python

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/blessings/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

#BuildRequires: /dev/pts
BuildRequires: python3-module-setuptools python3-tools
%if_with test
BuildRequires: python3-modules-curses python3-module-nose
%endif

%description
A thin, practical wrapper around terminal coloring, styling, and
positioning.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A thin, practical wrapper around terminal coloring, styling, and
positioning.

This package contains tests for %oname.


%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune
rm -rf %buildroot%python3_sitelibdir/blessings/tests.py

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- build python3 module separately, cleanup spec
- new version (1.7) with rpmgs script

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6-alt1.git20140520.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1.git20140520.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.git20140520
- Initial build for Sisyphus

