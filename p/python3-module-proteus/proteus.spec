%define oname proteus

%def_with bootstrap
%def_without check

Name: python3-module-%oname
Version: 5.2.1
Release: alt1

Summary: Library to access Tryton server as a client
License: LGPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/proteus/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest python3-module-trytond-tests
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
py.test3 -vv
%endif

%files
%doc CHANGELOG COPYRIGHT LICENSE README.rst doc/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 5.2.1-alt1
- Version updated to 5.2.1
- disable python2, enable python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt1
- Updated to upstream release 4.4.0.

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

