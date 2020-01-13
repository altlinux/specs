%define oname txpostgres

Name: python3-module-%oname
Version: 1.7.0
Release: alt1

Summary: Twisted wrapper for asynchronous PostgreSQL connections
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/txpostgres/
BuildArch: noarch

# https://github.com/wulczer/txpostgres.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-psycopg2
BuildRequires: python3-module-pytest
BuildRequires: python3-module-twisted-core-test


%description
A Twisted wrapper for asynchronous PostgreSQL connections.

Based on the interface exposed from the native Postgres C library by the
Python psycopg2 driver.

Can be used as a drop-in replacement for Twisted's adbapi module when
working with PostgreSQL. The only part that does not provide 100%%
compatibility is connection pooling, although pooling provided by
txpostgres is very similar to the one Twisted adbapi offers.

%package tests
Summary: Tests for %oname
Group: Development/Python3

%description tests
A Twisted wrapper for asynchronous PostgreSQL connections.

Based on the interface exposed from the native Postgres C library by the
Python psycopg2 driver.

This package contains tests for %oname.

%prep
%setup

sed -i '/c.async/s/^/#/' test/test_txpostgres.py

%build
%python3_build_debug

%install
%python3_install

cp -fR test/ %buildroot%python3_sitelibdir/%oname

%check
py.test3

%files
%doc LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%oname/test/

%files tests
%python3_sitelibdir/%oname/test/


%changelog
* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.7.0-alt1
- Version updated to 1.7.0
- porting on python3

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.2.0.1-alt2.git20140624.1.1
- Added missing dep on Pytest.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0.1-alt2.git20140624.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0.1-alt2.git20140624
- Fixed build

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0.1-alt1.git20140624
- Initial build for Sisyphus

