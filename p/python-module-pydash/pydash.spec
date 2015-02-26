%define oname pydash

%def_with python3

Name: python-module-%oname
Version: 3.0.1
Release: alt1.git20150225
Summary: The kitchen sink of Python utility libraries for doing "stuff" in a functional way
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pydash/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dgilland/pydash.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tox python-module-pytest-cov
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinx_rtd_theme
BuildPreReq: python-module-sphinxcontrib-napoleon
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tox python3-module-pytest-cov
%endif

%py_provides %oname

%description
The kitchen sink of Python utility libraries for doing "stuff" in a
functional way. Based on the Lo-Dash Javascript library.

%package -n python3-module-%oname
Summary: The kitchen sink of Python utility libraries for doing "stuff" in a functional way
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The kitchen sink of Python utility libraries for doing "stuff" in a
functional way. Based on the Lo-Dash Javascript library.

%package pickles
Summary: Pickles for %oname
Group: Development/Python
Requires: %name = %EVR

%description pickles
The kitchen sink of Python utility libraries for doing "stuff" in a
functional way. Based on the Lo-Dash Javascript library.

This package contains pickles for %oname.

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

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
%make pytest
%if_with python3
pushd ../python3
sed -i 's|py.test|py.test-%_python3_version|' makefile
%make pytest
popd
%endif

%files
%doc *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.git20150225
- Initial build for Sisyphus

