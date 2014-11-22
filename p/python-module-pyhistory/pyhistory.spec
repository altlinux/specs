%define oname pyhistory

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.git20141017
Summary: Package to help maintaining HISTORY file for Python project
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyhistory/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/beregond/pyhistory.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wheel python-module-tox
BuildPreReq: python-module-invoke
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-wheel python3-module-tox
BuildPreReq: python3-module-invoke
%endif

%py_provides %oname

%description
This package is created to help maintaining history file in environment
of high concurrency (literally: each pull request on GitHub had
conflicts in HISTORY.rst file because it was updated before creating
PR). Take into account it may NOT fit into your environment and/or
workflow since it was cutted for specific case, but it's good if so. :)

%package -n python3-module-%oname
Summary: Package to help maintaining HISTORY file for Python project
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This package is created to help maintaining history file in environment
of high concurrency (literally: each pull request on GitHub had
conflicts in HISTORY.rst file because it was updated before creating
PR). Take into account it may NOT fit into your environment and/or
workflow since it was cutted for specific case, but it's good if so. :)

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package is created to help maintaining history file in environment
of high concurrency (literally: each pull request on GitHub had
conflicts in HISTORY.rst file because it was updated before creating
PR). Take into account it may NOT fit into your environment and/or
workflow since it was cutted for specific case, but it's good if so. :)

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package is created to help maintaining history file in environment
of high concurrency (literally: each pull request on GitHub had
conflicts in HISTORY.rst file because it was updated before creating
PR). Take into account it may NOT fit into your environment and/or
workflow since it was cutted for specific case, but it's good if so. :)

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec \
	sed -i 's|pyhi |pyhi.py3 |g' '{}' +
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
mv %oname %oname.py3
popd
%endif

%python_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=%buildroot%python_sitelibdir
python setup.py test
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
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
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20141017
- Initial build for Sisyphus

