%define oname netkit

%def_with python3

Name: python-module-%oname
Version: 0.2.116
Release: alt1.git20141127.1.1.1
Summary: Useful kit for network programming
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/netkit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dantezhu/netkit.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

%description
Useful kit for network programming.

%package -n python3-module-%oname
Summary: Useful kit for network programming
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Useful kit for network programming.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
pushd python
%python_build_debug
popd

%if_with python3
pushd ../python3/python
%python3_build_debug
popd
%endif

%install
pushd python
%python_install
popd

%if_with python3
pushd ../python3/python
%python3_install
popd
%endif

%check
pushd python
python setup.py test
popd
%if_with python3
pushd ../python3/python
python3 setup.py test
popd
%endif

%files
%doc *.md tools/* python/examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md tools/* python/examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.116-alt1.git20141127.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.116-alt1.git20141127.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.116-alt1.git20141127.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.116-alt1.git20141127
- Version 0.2.116

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.115-alt1.git20141125
- Initial build for Sisyphus

