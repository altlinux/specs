%define oname pytest-services

%def_with python3

Name: python-module-%oname
Version: 1.1.3
Release: alt1.git20150725.1.1
Summary: Services plugin for pytest testing framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-services/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pytest-dev/pytest-services.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: libmemcached-devel libmysqlclient-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-requests python-module-subprocess32
#BuildPreReq: python-module-tox python-module-mock
#BuildPreReq: python-module-mysqlclient python-module-pylibmc
#BuildPreReq: python-module-pytest-cov python-module-pytest-pep8
#BuildPreReq: python-module-psutil
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-requests
#BuildPreReq: python3-module-tox python3-module-mock
#BuildPreReq: python3-module-mysqlclient python3-module-pylibmc
#BuildPreReq: python3-module-pytest-cov python3-module-pytest-pep8
#BuildPreReq: python3-module-psutil
%endif

%py_provides pytest_services
%py_requires requests psutil subprocess32

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-enum34 python-module-execnet python-module-ndg-httpsclient python-module-ntlm python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-pytest-cache python-module-rlcompleter2 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-pep8 python3 python3-base python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-execnet python3-module-genshi python3-module-ndg-httpsclient python3-module-ntlm python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-pytest-cache python3-module-pytest-pep8 python3-module-setuptools python3-module-urllib3 xz
BuildRequires: python-module-mysqlclient python-module-pbr python-module-pylibmc python-module-pytest-cov python-module-pytest-pep8 python-module-subprocess32 python-module-tox python-module-unittest2 python3-module-html5lib python3-module-mysqlclient python3-module-pbr python3-module-pylibmc python3-module-pytest-cov python3-module-tox python3-module-unittest2 python3-tools-pep8 rpm-build-python3 time

%description
The plugin provides a set of fixtures and utility functions to start
service processes for your tests with pytest.

%package -n python3-module-%oname
Summary: Services plugin for pytest testing framework
Group: Development/Python3
%py3_provides pytest_services
%py3_requires requests psutil

%description -n python3-module-%oname
The plugin provides a set of fixtures and utility functions to start
service processes for your tests with pytest.

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
py.test -vv --fixtures tests
%if_with python3
pushd ../python3
py.test-%_python3_version -vv --fixtures tests
popd
%endif

%files
%doc *.rst docs/*.rst docs/api
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst docs/api
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt1.git20150725.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt1.git20150725.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20150725
- Version 1.1.3

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.git20150120
- Version 1.0.4

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20150120
- Initial build for Sisyphus

