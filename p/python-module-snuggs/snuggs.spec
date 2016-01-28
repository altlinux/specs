%define oname snuggs

%def_with python3

Name: python-module-%oname
Version: 1.3.1
Release: alt1.git20150403.1
Summary: Snuggs are s-expressions for Numpy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/snuggs
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mapbox/snuggs.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-click python-module-numpy
#BuildPreReq: python-module-pyparsing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-click python3-module-numpy
#BuildPreReq: python3-module-pyparsing
%endif

%py_provides %oname
%py_requires click numpy pyparsing

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-numpy python-module-pluggy python-module-py python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-numpy python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-numpy-testing python-module-pyparsing python-module-setuptools-tests python3-module-numpy-testing python3-module-pyparsing python3-module-setuptools-tests rpm-build-python3 time

%description
Snuggs are s-expressions for Numpy.

%if_with python3
%package -n python3-module-%oname
Summary: Snuggs are s-expressions for Numpy
Group: Development/Python3
%py3_provides %oname
%py3_requires click numpy pyparsing

%description -n python3-module-%oname
Snuggs are s-expressions for Numpy.
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
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1.git20150403.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20150403
- Initial build for Sisyphus

