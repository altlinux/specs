%define oname solar_theme

%def_with python3

Name: python-module-%oname
Version: 1.3.2
Release: alt1.git20140312
Summary: Theme for Python Sphinx
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/solar-theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/biotechcoder/solar-theme.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-sphinx-devel
%endif

%py_provides %oname
%py_requires sphinx

%description
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.

%if_with python3
%package -n python3-module-%oname
Summary: Theme for Python Sphinx
Group: Development/Python3
%py3_provides %oname
%py3_requires sphinx

%description -n python3-module-%oname
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Solar is an attempt to create a theme for the Python Sphinx
documentation generator based on the Solarized color scheme.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make docs
%make -C docs pickle

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git20140312
- Initial build for Sisyphus

