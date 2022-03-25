%define _unpackaged_files_terminate_build 1
%define oname proteus

%def_without bootstrap
%def_with check

Name: python3-module-%oname
Version: 6.2.2
Release: alt1

Summary: Library to access Tryton server as a client
License: GPL-3
Group: Development/Python3
Url: https://pypi.org/project/proteus/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-trytond-tests
%endif

%if_without bootstrap
Requires: python3-module-trytond python3-module-trytond_party
%endif

%py_provides %oname

%description
A library to access Tryton's models like a client.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%if_with bootstrap
%add_python3_req_skip trytond.tests.test_tryton
%endif

%description tests
A library to access Tryton's models like a client.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if_with check
%check
export PYTHONPATH=$PWD
py.test3 -vra
%endif

%files
%doc CHANGELOG COPYRIGHT LICENSE README.rst doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Mar 25 2022 Danil Shein <dshein@altlinux.org> 6.2.2-alt1
- Version updated to 6.2.2
- fix FTBS

* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.4.1-alt1
- Version updated to 5.4.1.

* Tue Oct 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.1-alt2
- enable bootstrap requires, enable tests

* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.1-alt1
- Version updated to 5.2.1
- disable python2, enable python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt1
- Updated to upstream release 4.4.0.

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

