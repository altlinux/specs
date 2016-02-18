%define oname pinocchio

%def_with python3

Name: python-module-%oname
Version: 0.4.2
Release: alt1.git20141201.1
Summary: pinocchio plugins for the nose testing framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pinocchio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mkwiatkowski/pinocchio.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose python-module-colorama
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-module-colorama
%endif

%py_provides %oname
%py_requires nose colorama

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-nose python-module-setuptools-tests python3-module-nose python3-module-setuptools-tests rpm-build-python3

%description
Extra plugins for the nose testing framework. Provides tools for
flexibly assigning decorator tags to tests, choosing tests based on
their runtime, doing moderately sophisticated code coverage analysis of
your unit tests, and making your test descriptions look like
specifications.

%package -n python3-module-%oname
Summary: pinocchio plugins for the nose testing framework
Group: Development/Python3
%py3_provides %oname
%py3_requires nose colorama

%description -n python3-module-%oname
Extra plugins for the nose testing framework. Provides tools for
flexibly assigning decorator tags to tests, choosing tests based on
their runtime, doing moderately sophisticated code coverage analysis of
your unit tests, and making your test descriptions look like
specifications.

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
%doc IDEAS *.rst doc/* examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc IDEAS *.rst doc/* examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20141201.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20141201
- Initial build for Sisyphus

