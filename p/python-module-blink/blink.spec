%define oname blink

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.1
Summary: REST client interface
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/blink/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-modules-json python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-requests
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-cryptography python-module-enum34 python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-urllib3
BuildRequires: python-module-requests python-module-setuptools-tests python3-module-requests python3-module-setuptools-tests rpm-build-python3

%description
A REST interface from Python.

%package -n python3-module-%oname
Summary: REST client interface
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A REST interface from Python.

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus

