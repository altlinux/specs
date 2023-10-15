%define oname psycopg2cffi

%def_disable check

Name: python3-module-%oname
Version: 2.9.0
Release: alt2
Summary: An implementation of the psycopg2 module using cffi
License: LGPLv3+
Group: Development/Python3
Url: https://pypi.python.org/pypi/psycopg2cffi/

# https://github.com/chtd/psycopg2cffi.git
Source: %name-%version.tar

Patch: remove-distutils-for-python-3.12.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: postgresql-devel libpq-devel
BuildRequires: python3-module-six python3-module-cffi

%py3_provides %oname
%py3_requires six cffi

%description
An implementation of the psycopg2 module using cffi. The module is
currently compatible with Psycopg 2.5.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
An implementation of the psycopg2 module using cffi. The module is
currently compatible with Psycopg 2.5.

This package contains tests for %oname.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

python3 setup.py test ||:
install -d %buildroot%python3_sitelibdir/%oname/_impl/__pycache__
install -m644 %oname/_impl/__pycache__/*.so \
	%buildroot%python3_sitelibdir/%oname/_impl/__pycache__/

%check
python3 setup.py test

%files
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Sun Oct 15 2023 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt2
- Dropped dependency on distutils.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Automatically updated to 2.9.0.
- Transfer to python3.

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 2.8.1-alt1
- Build new version for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.6-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.7.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.6-alt1
- Updated to upstream version 2.7.6.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.2-alt1.git20150808.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.2-alt1.git20150808
- Version 2.7.2

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1.git20150208
- Initial build for Sisyphus

