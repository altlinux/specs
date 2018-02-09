%define oname vcrpy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.2.0
Release: alt1.git20150108.1.1.1
Summary: Automatically mock your HTTP interactions to simplify and speed up testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/vcrpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kevin1024/vcrpy.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-yaml python-module-mock
#BuildPreReq: python-module-six python-module-contextlib2
#BuildPreReq: python-module-wrapt python-module-pytest-localserver
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-yaml python3-module-mock
#BuildPreReq: python3-module-six python3-module-contextlib2
#BuildPreReq: python3-module-wrapt python3-module-pytest-localserver
%endif

%py_provides vcr

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools
BuildRequires: python-module-contextlib2 python-module-pbr python-module-pytest-localserver python-module-setuptools python-module-unittest2 python-module-wrapt python-module-yaml python3-module-contextlib2 python3-module-html5lib python3-module-pbr python3-module-pytest-localserver python3-module-setuptools python3-module-unittest2 python3-module-wrapt python3-module-yaml rpm-build-python3

%description
Automatically mock your HTTP interactions to simplify and speed up
testing.

%package -n python3-module-%oname
Summary: Automatically mock your HTTP interactions to simplify and speed up testing
Group: Development/Python3
%py3_provides vcr
%py3_requires requests.packages
%add_python3_req_skip requests.packages.urllib3.connectionpool

%description -n python3-module-%oname
Automatically mock your HTTP interactions to simplify and speed up
testing.

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1.git20150108.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20150108.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20150108.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150108
- Version 1.2.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141103
- Initial build for Sisyphus

