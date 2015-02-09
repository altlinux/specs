%define oname db

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.0
Release: alt1.git20150208
Summary: A db package that doesn't suck
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/db.py/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/yhat/db.py.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-prettytable python-module-pandas
BuildPreReq: python-module-pybars3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-prettytable python3-module-pandas
BuildPreReq: python3-module-pybars3
%endif

%py_provides %oname
%py_requires prettytable pandas pybars3

%description
db.py is an easier way to interact with your databases. It makes it
easier to explore tables, columns, views, etc. It puts the emphasis on
user interaction, information display, and providing easy to use helper
functions.

db.py uses `pandas` to manage data, so if you're already using pandas,
db.py should feel pretty natural. It's also fully compatible with the
IPython Notebook, so not only is db.py extremely functional, it's also
pretty.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
db.py is an easier way to interact with your databases. It makes it
easier to explore tables, columns, views, etc. It puts the emphasis on
user interaction, information display, and providing easy to use helper
functions.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A db package that doesn't suck
Group: Development/Python3
%py3_provides %oname
%py3_requires prettytable pandas pybars3

%description -n python3-module-%oname
db.py is an easier way to interact with your databases. It makes it
easier to explore tables, columns, views, etc. It puts the emphasis on
user interaction, information display, and providing easy to use helper
functions.

db.py uses `pandas` to manage data, so if you're already using pandas,
db.py should feel pretty natural. It's also fully compatible with the
IPython Notebook, so not only is db.py extremely functional, it's also
pretty.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
db.py is an easier way to interact with your databases. It makes it
easier to explore tables, columns, views, etc. It puts the emphasis on
user interaction, information display, and providing easy to use helper
functions.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
nosetests -v
%if_with python3
pushd ../python3
nosetests3 -v
popd
%endif

%files
%doc CHANGES.txt *.rst docs/* examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.txt *.rst docs/* examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20150208
- Initial build for Sisyphus

