%define oname django-generate

%def_with python3

Name: python-module-%oname
Version: 0.0.6
Release: alt1.git20120918.1
Summary: Django slightly smarter than fixtures content generation app
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-generate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-generate.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
django-generate adds a management command called generate which allows
you to create objects from a dynamically created JSON description of
said objects. It's primary focus is to generate test content for use
during project development and testing. Objects are only created once
via Django's get_or_create method. Inheritance base model objects are
created where needed. File fields can also be populated from arbitrary
resources. In this way django-generate simplifies generating complex
objects when compared to Django's built in fixtures feature.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
django-generate adds a management command called generate which allows
you to create objects from a dynamically created JSON description of
said objects. It's primary focus is to generate test content for use
during project development and testing. Objects are only created once
via Django's get_or_create method. Inheritance base model objects are
created where needed. File fields can also be populated from arbitrary
resources. In this way django-generate simplifies generating complex
objects when compared to Django's built in fixtures feature.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Django slightly smarter than fixtures content generation app
Group: Development/Python3

%description -n python3-module-%oname
django-generate adds a management command called generate which allows
you to create objects from a dynamically created JSON description of
said objects. It's primary focus is to generate test content for use
during project development and testing. Objects are only created once
via Django's get_or_create method. Inheritance base model objects are
created where needed. File fields can also be populated from arbitrary
resources. In this way django-generate simplifies generating complex
objects when compared to Django's built in fixtures feature.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
django-generate adds a management command called generate which allows
you to create objects from a dynamically created JSON description of
said objects. It's primary focus is to generate test content for use
during project development and testing. Objects are only created once
via Django's get_or_create method. Inheritance base model objects are
created where needed. File fields can also be populated from arbitrary
resources. In this way django-generate simplifies generating complex
objects when compared to Django's built in fixtures feature.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.6-alt1.git20120918.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20120918
- Initial build for Sisyphus

