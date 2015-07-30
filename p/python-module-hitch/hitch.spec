%define oname hitch

%def_with python3

Name: python-module-%oname
Version: 0.4.5
Release: alt1.git20150730
Summary: Loosely coupled testing framework
License: AGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/hitch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hitchtest/hitch.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-click
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-click
%endif

%py_provides %oname
%py_requires click

%description
Hitch is a loosely-coupled, isolated by design testing framework built
upon python's unittest that lets you write simple, easy to read and easy
to debug tests for *any* software (not just web apps and not just python
apps).

%if_with python3
%package -n python3-module-%oname
Summary: Loosely coupled testing framework
Group: Development/Python3
%py3_provides %oname
%py3_requires click

%description -n python3-module-%oname
Hitch is a loosely-coupled, isolated by design testing framework built
upon python's unittest that lets you write simple, easy to read and easy
to debug tests for *any* software (not just web apps and not just python
apps).
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Hitch is a loosely-coupled, isolated by design testing framework built
upon python's unittest that lets you write simple, easy to read and easy
to debug tests for *any* software (not just web apps and not just python
apps).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Hitch is a loosely-coupled, isolated by design testing framework built
upon python's unittest that lets you write simple, easy to read and easy
to debug tests for *any* software (not just web apps and not just python
apps).

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd
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
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.git20150730
- Initial build for Sisyphus

