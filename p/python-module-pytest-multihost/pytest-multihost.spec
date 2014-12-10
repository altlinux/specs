%define oname pytest-multihost

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1.git20141209
Summary: Utility for writing multi-host tests for pytest
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-multihost
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://git.fedorahosted.org/git/python-pytest-multihost.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-yaml python-module-paramiko
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-yaml python3-module-paramiko
%endif

%py_provides pytest_multihost
%py_requires yaml paramiko

%description
A pytest plugin for multi-host testing.

%package -n python3-module-%oname
Summary: Utility for writing multi-host tests for pytest
Group: Development/Python3
%py3_provides pytest_multihost
%py3_requires yaml paramiko

%description -n python3-module-%oname
A pytest plugin for multi-host testing.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141209
- Version 0.4

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20141126
- Initial build for Sisyphus

