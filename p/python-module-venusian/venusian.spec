%define oname venusian

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.a6
Summary: A library for deferring decorator actions
License: BSD-derived
Group: Development/Python
Url: http://pypi.python.org/pypi/venusian
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator
is executed at import time, you can defer the action usually taken by
the decorator until a separate "scan" phase.

%if_with python3
%package -n python3-module-%oname
Summary: A library for deferring decorator actions (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator
is executed at import time, you can defer the action usually taken by
the decorator until a separate "scan" phase.

%package -n python3-module-%oname-tests
Summary: Tests for Venusian (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%add_python3_req_skip doesnt

%description -n python3-module-%oname-tests
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator
is executed at import time, you can defer the action usually taken by
the decorator until a separate "scan" phase.

This package contains tests for Venusian.
%endif

%package tests
Summary: Tests for Venusian
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip doesnt

%description tests
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator
is executed at import time, you can defer the action usually taken by
the decorator until a separate "scan" phase.

This package contains tests for Venusian.

%package pickles
Summary: Pickles for Venusian
Group: Development/Python

%description pickles
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator
is executed at import time, you can defer the action usually taken by
the decorator until a separate "scan" phase.

This package contains pickles for Venusian.

%package docs
Summary: Documentation for Venusian
Group: Development/Documentation

%description docs
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator
is executed at import time, you can defer the action usually taken by
the decorator until a separate "scan" phase.

This package contains documentation for Venusian.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

pushd docs
ln -s %_datadir/pylons_sphinx_theme _themes
%make pickle
%make html
popd

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/%oname/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a6
- Version 1.0a6
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a2
- Version 1.0a2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

