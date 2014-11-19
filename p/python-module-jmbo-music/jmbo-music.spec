%define oname jmbo-music

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.8
Release: alt1.git20141119
Summary: Jmbo music app
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jmbo-music/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/jmbo-music.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pylast python-module-lxml
BuildPreReq: python-module-jmbo-gallery python-module-jmbo-foundry
BuildPreReq: python-module-jmbo-twitter python-module-jmbo-downloads
BuildPreReq: python-module-memcached python-module-gunicorn
BuildPreReq: python-module-jmbo-friends python-module-jmbo-analytics
BuildPreReq: python-module-django-compressor python-module-jmbo-poll
BuildPreReq: python-module-django-simple-autocomplete
BuildPreReq: python-module-django-debug-toolbar
BuildPreReq: python-module-jmbo-contact python-module-jmbo-competition
BuildPreReq: python-module-jmbo-banner python-module-jmbo-show
BuildPreReq: python-module-django-registration
BuildPreReq: python-module-django-object-tools
BuildPreReq: python-module-django-gizmo python-module-django-tests
BuildPreReq: python-module-django-richcomments
BuildPreReq: python-module-django-recaptcha
BuildPreReq: python-module-jmbo-chart python-module-jmbo-calendar
BuildPreReq: python-module-django-export
BuildPreReq: python-module-django-googlesearch
BuildPreReq: python-module-django-section
BuildPreReq: python-module-django-analytics
BuildPreReq: python-module-django-dfp
BuildPreReq: python-module-django-setuptest python-module-coverage
BuildPreReq: python-module-mimeparse python-tools-pep8
BuildPreReq: python-module-django-dbbackend-psycopg2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pylast python3-module-lxml
BuildPreReq: python3-module-jmbo-gallery python3-module-jmbo-foundry
BuildPreReq: python3-module-jmbo-twitter python3-module-jmbo-downloads
BuildPreReq: python3-module-memcached python3-module-gunicorn
BuildPreReq: python3-module-jmbo-friends python3-module-jmbo-analytics
BuildPreReq: python3-module-django-compressor python3-module-jmbo-poll
BuildPreReq: python3-module-django-simple-autocomplete
BuildPreReq: python3-module-django-debug-toolbar
BuildPreReq: python3-module-jmbo-contact python3-module-jmbo-competition
BuildPreReq: python3-module-jmbo-banner python3-module-jmbo-show
BuildPreReq: python3-module-django-registration
BuildPreReq: python3-module-django-object-tools
BuildPreReq: python3-module-django-gizmo python3-module-django-tests
BuildPreReq: python3-module-django-richcomments
BuildPreReq: python3-module-django-recaptcha
BuildPreReq: python3-module-jmbo-chart python3-module-jmbo-calendar
BuildPreReq: python3-module-django-export
BuildPreReq: python3-module-django-googlesearch
BuildPreReq: python3-module-django-section
BuildPreReq: python3-module-django-analytics
BuildPreReq: python3-module-django-setuptest
BuildPreReq: python3-module-mimeparse python3-tools-pep8
BuildPreReq: python3-module-django-dfp python3-module-coverage
BuildPreReq: python3-module-django-dbbackend-psycopg2
BuildPreReq: python-tools-2to3
%endif

%description
Jmbo music app.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-django-setuptest

%description tests
Jmbo music app.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Jmbo music app
Group: Development/Python3

%description -n python3-module-%oname
Jmbo music app.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
Requires: python3-module-django-setuptest

%description -n python3-module-%oname-tests
Jmbo music app.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1.git20141119
- Version 0.2.8

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1.git20140714
- Initial build for Sisyphus

