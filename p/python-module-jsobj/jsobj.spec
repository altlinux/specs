%define oname jsobj

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.4
Release: alt1.git20150120.1.1.1
Summary: Jsobj provides JavaScript-Style Objects in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jsobj/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gkovacs/jsobj.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%description
jsobj provides JavaScript-Style Objects in Python. It is based on
jsobject, but returns None if you try accessing non-existent keys
instead of throwing an exception.

%package -n python3-module-%oname
Summary: Jsobj provides JavaScript-Style Objects in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
jsobj provides JavaScript-Style Objects in Python. It is based on
jsobject, but returns None if you try accessing non-existent keys
instead of throwing an exception.

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
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1.git20150120.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.4-alt1.git20150120.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1.git20150120.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.git20150120
- Initial build for Sisyphus

