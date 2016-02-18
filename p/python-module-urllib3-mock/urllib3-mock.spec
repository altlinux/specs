%define oname urllib3-mock

%def_with python3

Name: python-module-%oname
Version: 0.3.3
Release: alt1.git20150417.1
Summary: A utility library for mocking out the `urllib3` Python library
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/urllib3-mock
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/florentx/urllib3-mock.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-mock python-module-pytest-cov
#BuildPreReq: python-module-flake8 python-module-requests
#BuildPreReq: python-module-urllib3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-mock python3-module-pytest-cov
#BuildPreReq: python3-module-flake8 python3-module-requests
#BuildPreReq: python3-module-urllib3
%endif

%py_provides urllib3_mock
%py_requires urllib3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-enum34 python-module-funcsigs python-module-mccabe python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-setuptools python-module-six python-module-unittest2 python-module-urllib3 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-pep8 python3 python3-base python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mccabe python3-module-ndg-httpsclient python3-module-ntlm python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-urllib3 python3-pyflakes python3-tools-pep8 xz
BuildRequires: python-module-flake8 python-module-mock python-module-pytest-cov python-module-requests python-module-setuptools-tests python3-module-flake8 python3-module-html5lib python3-module-pbr python3-module-pytest-cov python3-module-requests python3-module-setuptools-tests python3-module-unittest2 rpm-build-python3 time

%description
A utility library for mocking out the urllib3 Python library.

%if_with python3
%package -n python3-module-%oname
Summary: A utility library for mocking out the `urllib3` Python library
Group: Development/Python3
%py3_provides urllib3_mock
%py3_requires urllib3

%description -n python3-module-%oname
A utility library for mocking out the urllib3 Python library.
%endif

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
python setup.py test -v
py.test -vv . --cov urllib3_mock --cov-report term-missing
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv . --cov urllib3_mock \
	--cov-report term-missing
popd
%endif

%files
%doc CHANGES *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1.git20150417.1
- NMU: Use buildreq for BR.

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20150417
- Initial build for Sisyphus

