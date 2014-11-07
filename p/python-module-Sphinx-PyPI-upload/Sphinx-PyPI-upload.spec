%define oname Sphinx-PyPI-upload

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.hg20120424
Summary: setuptools command for uploading Sphinx documentation to PyPI
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Sphinx-PyPI-upload/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-sphinx
%endif

%py_provides sphinx_pypi_upload

%description
This package contains a setuptools command for uploading Sphinx
documentation to the Python Package Index (PyPI) at the dedicated URL
packages.python.org.

%package -n python3-module-%oname
Summary: setuptools command for uploading Sphinx documentation to PyPI
Group: Development/Python3
%py3_provides sphinx_pypi_upload

%description -n python3-module-%oname
This package contains a setuptools command for uploading Sphinx
documentation to the Python Package Index (PyPI) at the dedicated URL
packages.python.org.

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
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.hg20120424
- Initial build for Sisyphus

