%define oname praekelt_pyramid_celery

%def_with python3

Name: python-module-%oname
Version: 1.4.0
Release: alt1.git20140915
Summary: Pyramid configuration with celery integration
License: BSD
Group: Development/Python
Url: https://github.com/praekelt/pyramid_celery
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/pyramid_celery.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-celery
BuildPreReq: python-module-mock python-module-PasteDeploy
BuildPreReq: python-module-zope.deprecation python-module-repoze.lru
BuildPreReq: python-module-zope.component python-module-redis-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-celery
BuildPreReq: python3-module-mock python3-module-PasteDeploy
BuildPreReq: python3-module-zope.deprecation python3-module-repoze.lru
BuildPreReq: python3-module-zope.component python3-module-redis-py
%endif

%py_provides pyramid_celery

%description
Pyramid configuration with celery integration. Allows you to use pyramid
.ini files to configure celery and have your pyramid configuration
inside celery tasks.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Pyramid configuration with celery integration. Allows you to use pyramid
.ini files to configure celery and have your pyramid configuration
inside celery tasks.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Pyramid configuration with celery integration
Group: Development/Python3
%py3_provides pyramid_celery

%description -n python3-module-%oname
Pyramid configuration with celery integration. Allows you to use pyramid
.ini files to configure celery and have your pyramid configuration
inside celery tasks.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Pyramid configuration with celery integration. Allows you to use pyramid
.ini files to configure celery and have your pyramid configuration
inside celery tasks.

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

%check
rm -fR build
py.test
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc *.txt *.md examples
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
%doc *.txt *.md examples
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20140915
- Initial build for Sisyphus

