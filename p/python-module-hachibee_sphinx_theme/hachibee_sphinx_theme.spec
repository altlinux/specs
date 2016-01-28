%define oname hachibee_sphinx_theme

%def_with python3

Name: python-module-%oname
Version: 0.2.5
Release: alt1.1
Summary: A simple sphinx theme
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/hachibee-sphinx-theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3 time

%description
Sphinx hachibee theme.

%if_with python3
%package -n python3-module-%oname
Summary: A simple sphinx theme
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Sphinx hachibee theme.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1.1
- NMU: Use buildreq for BR.

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus

