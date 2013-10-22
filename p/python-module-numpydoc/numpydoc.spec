%define oname numpydoc

%def_without python3

Name: python-module-%oname
Version: 0.5
Release: alt1.dev.git20131021
Epoch: 1

Summary: Numpy's Sphinx extensions
License: BSD
Group: Development/Python
Url: http://numpy.scipy.org/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

# https://github.com/numpy/numpydoc.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Numpy's documentation uses several custom extensions to Sphinx.  These
are shipped in this ``numpydoc`` package, in case you want to make use
of them in third-party projects.

%if_with python3
%package -n python3-module-%oname
Summary: Numpy's Sphinx extensions
Group: Development/Python3

%description -n python3-module-%oname
Numpy's documentation uses several custom extensions to Sphinx.  These
are shipped in this ``numpydoc`` package, in case you want to make use
of them in third-party projects.

%package -n python3-module-%oname-tests
Summary: Tests for numpydoc
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-numpydoc = %EVR

%description -n python3-module-%oname-tests
Numpy's documentation uses several custom extensions to Sphinx.  These
are shipped in this ``numpydoc`` package, in case you want to make use
of them in third-party projects.

This package contains tests for numpydoc.
%endif

%package tests
Summary: Tests for numpydoc
Group: Development/Python
BuildArch: noarch
Requires: python-module-numpydoc = %EVR

%description tests
Numpy's documentation uses several custom extensions to Sphinx.  These
are shipped in this ``numpydoc`` package, in case you want to make use
of them in third-party projects.

This package contains tests for numpydoc.

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
popd
%endif

%build

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%python_build_debug

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Wed Oct 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.5-alt1.dev.git20131021
- Initial build for Sisyphus

