%define _unpackaged_files_terminate_build 1
%define oname pytest-multihost

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.1
Summary: Utility for writing multi-host tests for pytest
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-multihost
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://git.fedorahosted.org/git/python-pytest-multihost.git
Source0: https://pypi.python.org/packages/6b/ad/d71a4e8cbcd0d5dfcca90562e17dddb0d1a137d9f35baa048fa7f08d6208/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-modules-json
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-yaml python-module-paramiko
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-yaml python3-module-paramiko
%endif

%py_provides pytest_multihost
%py_requires yaml paramiko

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-ecdsa python-module-pycrypto python-module-setuptools python-module-yaml python3-module-ecdsa python3-module-pycrypto python3-module-setuptools python3-module-yaml rpm-build-python3
BuildRequires: python-module-pytest
BuildRequires: python3-module-pytest

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
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20141209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.git20141209.1
- NMU: Use buildreq for BR.

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141209
- Version 0.4

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20141126
- Initial build for Sisyphus

