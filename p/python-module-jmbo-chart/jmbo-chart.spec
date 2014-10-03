%define oname jmbo-chart

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20121204
Summary: Jmbo chart app
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jmbo-chart/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/jmbo-chart.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Jmbo chart app.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-django-setuptest

%description tests
Jmbo chart app.

This package contains tests for %oname.


%package -n python3-module-%oname
Summary: Jmbo chart app
Group: Development/Python3

%description -n python3-module-%oname
Jmbo chart app.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
Requires: python3-module-django-setuptest

%description -n python3-module-%oname-tests
Jmbo chart app.

This package contains tests for %oname.

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

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20121204
- Initial build for Sisyphus

