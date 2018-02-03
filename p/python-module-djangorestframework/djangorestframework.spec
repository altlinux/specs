%define oname djangorestframework
%add_python3_req_skip django.utils.six.moves.http_client
%add_python3_req_skip django.utils.six.moves.urllib

%def_disable check
%def_with python3

Name: python-module-%oname
Version: 3.5.3
Release: alt1.1
Summary: Web APIs for Django, made easy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/djangorestframework/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tomchristie/django-rest-framework.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-defusedxml python-module-docutils python-module-flake8 python-module-html5lib python-module-httplib2 python-module-mkdocs python-module-pytest-cov python-module-pytest-django python-module-setuptools python-module-tornado python-module-livereload

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-django-tests python-module-pytest-django
#BuildPreReq: python-module-pytest-cov python-module-flake8
#BuildPreReq: python-module-markdown python-module-yaml
#BuildPreReq: python-module-defusedxml python-module-django-guardian
#BuildPreReq: python-module-django-filter python-module-django-oauth-plus
#BuildPreReq: python-module-oauth2 python-module-django-oauth2-provider
#BuildPreReq: python-module-django-dbbackend-sqlite3 python-module-mkdocs
#BuildPreReq: python-module-argh
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-django-tests python3-module-pytest-django
#BuildPreReq: python3-module-pytest-cov python3-module-flake8
#BuildPreReq: python3-module-markdown python3-module-yaml
#BuildPreReq: python3-module-defusedxml python3-module-django-guardian
#BuildPreReq: python3-module-django-filter python3-module-django-oauth-plus
#BuildPreReq: python3-module-oauth2 python3-module-django-oauth2-provider
#BuildPreReq: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-defusedxml python3-module-flake8 python3-module-html5lib python3-module-httplib2 python3-module-markdown python3-module-pytest-cov python3-module-pytest-django python3-module-setuptools python3-module-sphinx python3-module-tornado python3-module-livereload
%endif


%py_provides rest_framework

%description
Django REST framework is a powerful and flexible toolkit for building
Web APIs.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires django.test

%description tests
Django REST framework is a powerful and flexible toolkit for building
Web APIs.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Django REST framework is a powerful and flexible toolkit for building
Web APIs.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Web APIs for Django, made easy
Group: Development/Python3
%py3_provides rest_framework

%description -n python3-module-%oname
Django REST framework is a powerful and flexible toolkit for building
Web APIs.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires django.test

%description -n python3-module-%oname-tests
Django REST framework is a powerful and flexible toolkit for building
Web APIs.

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

mkdocs build

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python runtests.py
#if_with python3
%if 0
pushd ../python3
python3 runtests.py
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%files docs
%doc site/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.5.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 3.5.3-alt1
- Version 3.6.3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.4-alt2.git20150128.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 3.0.4-alt2.git20150128
- Rebuild with "def_disable check"
- Cleanup buildreqs

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.4-alt1.git20150128
- Version 3.0.4

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.git20141108
- Initial build for Sisyphus

