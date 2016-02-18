%define oname pyrelic

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt1.git20150520.1
Summary: Python API Wrapper for NewRelic API
License: MIT / GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pyrelic
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/andrewgross/pyrelic.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-six python-module-requests
#BuildPreReq: python-module-mock python-module-sure
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-httpretty
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-six python3-module-requests
#BuildPreReq: python3-module-mock python3-module-sure
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-httpretty
%endif

%py_provides %oname
%py_requires six requests

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-cryptography python-module-enum34 python-module-funcsigs python-module-mock python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pyasn1 python-module-pytest python-module-setuptools python-module-six python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ndg-httpsclient python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-urllib3
BuildRequires: python-module-coverage python-module-httpretty python-module-nose python-module-requests python-module-setuptools-tests python-module-sure python3-module-coverage python3-module-html5lib python3-module-mimeparse python3-module-nose python3-module-pbr python3-module-requests python3-module-setuptools-tests python3-module-unittest2 rpm-build-python3 time

%description
A New Relic client library written in Python.

%if_with python3
%package -n python3-module-%oname
Summary: Python API Wrapper for NewRelic API
Group: Development/Python3
%py3_provides %oname
%py3_requires six requests

%description -n python3-module-%oname
A New Relic client library written in Python.
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
#make run_test suite=unit
%make run_test suite=fixtures
%if_with python3
pushd ../python3
python3 setup.py test -v
#make run_test suite=unit NOSETESTS=nosetests3
%make run_test suite=fixtures NOSETESTS=nosetests3
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20150520.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20150520
- Initial build for Sisyphus

