%define oname clize

%def_with python3

Name: python-module-%oname
Version: 3.0
Release: alt1.a2.git20150111
Summary: Command-line argument parsing for Python, without the effort
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/clize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/epsy/clize.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sigtools python-module-six
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-sigtools python3-module-six
%endif

%py_provides %oname
%py_requires sigtools six

%description
Clize procedurally turns your functions into convenient command-line
interfaces.

%package -n python3-module-%oname
Summary: Command-line argument parsing for Python, without the effort
Group: Development/Python3
%py3_provides %oname
%py3_requires sigtools six

%description -n python3-module-%oname
Clize procedurally turns your functions into convenient command-line
interfaces.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Clize procedurally turns your functions into convenient command-line
interfaces.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Clize procedurally turns your functions into convenient command-line
interfaces.

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

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

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
%doc docs/_build/html examples

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.a2.git20150111
- Initial build for Sisyphus

