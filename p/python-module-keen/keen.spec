%define oname keen

%def_with python3

Name: python-module-%oname
Version: 0.3.9
Release: alt1.git20150209.1
Summary: Python Client for Keen IO
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/keen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/keenlabs/KeenClient-Python.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-modules-json
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-requests python-module-pycrypto
#BuildPreReq: python-module-Padding python-module-nose
#BuildPreReq: python-module-urllib3 python-module-mock
#BuildPreReq: python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-requests python3-module-pycrypto
#BuildPreReq: python3-module-Padding python3-module-nose
#BuildPreReq: python3-module-urllib3 python3-module-mock
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pluggy python-module-py python-module-pyasn1 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ndg-httpsclient python3-module-ntlm python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-setuptools xz
BuildRequires: python-module-Padding python-module-chardet python-module-ndg-httpsclient python-module-nose python-module-ntlm python-module-pbr python-module-pycrypto python-module-pytest python-module-unittest2 python3-module-Padding python3-module-chardet python3-module-html5lib python3-module-nose python3-module-pbr python3-module-pycrypto python3-module-pytest python3-module-unittest2 python3-module-urllib3 rpm-build-python3 time

%description
This is the official Python Client for the Keen IO API. The Keen IO API
lets developers build analytics features directly into their apps.

%package -n python3-module-%oname
Summary: Python Client for Keen IO
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is the official Python Client for the Keen IO API. The Keen IO API
lets developers build analytics features directly into their apps.

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
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.9-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1.git20150209
- Version 0.3.9

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20141125
- Initial build for Sisyphus

