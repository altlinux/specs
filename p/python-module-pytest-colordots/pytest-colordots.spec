%define oname pytest-colordots

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20141120.1
Summary: Colorizes the progress indicators
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-colordots
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/svenstaro/pytest-colordots.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-blessings
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-blessings
%endif

%py_provides pytest_colordots

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3

%description
Colorizes the progress indicators

This is an adoption of pytest-greendots which sadly does not have an
upstream repository.

%package -n python3-module-%oname
Summary: Colorizes the progress indicators
Group: Development/Python3
%py3_provides pytest_colordots

%description -n python3-module-%oname
Colorizes the progress indicators

This is an adoption of pytest-greendots which sadly does not have an
upstream repository.

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20141120.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141120
- Initial build for Sisyphus

