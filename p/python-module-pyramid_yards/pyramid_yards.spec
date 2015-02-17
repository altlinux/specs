%define oname pyramid_yards

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4
Release: alt1.git20150214
Summary: Pyramid Request Parameter Validation
License: BSD-derived
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_yards/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mardiros/pyramid_yards.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid python-module-colander
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid python3-module-colander
%endif

%py_provides %oname
%py_requires pyramid colander

%description
A lib that add a "yards" attribute to the pyramid request, containing
every validated parameter using colander schemas.

This lib has been inspired by the cornice validated property, but the
implementation differ.

%package -n python3-module-%oname
Summary: Pyramid Request Parameter Validation
Group: Development/Python3
%py3_provides %oname
%py3_requires pyramid colander

%description -n python3-module-%oname
A lib that add a "yards" attribute to the pyramid request, containing
every validated parameter using colander schemas.

This lib has been inspired by the cornice validated property, but the
implementation differ.

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
%doc *.rst COPYRIGHT LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst COPYRIGHT LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150214
- Initial build for Sisyphus

