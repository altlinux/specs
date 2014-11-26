%define oname pyramid_facebook

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1
Summary: Pyramid routes and helpers for Facebook canvas applications
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools python-module-d2to1
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-d2to1 python-tools-2to3
%endif

%description
Provides simple pyramid routes/views for facebook canvas application.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Provides simple pyramid routes/views for facebook canvas application.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Pyramid routes and helpers for Facebook canvas applications
Group: Development/Python3

%description -n python3-module-%oname
Provides simple pyramid routes/views for facebook canvas application.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Provides simple pyramid routes/views for facebook canvas application.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt1
- Initial build for Sisyphus

