%define oname django-generate

Name: python3-module-%oname
Version: 0.0.6
Release: alt2

Summary: Django slightly smarter than fixtures content generation app
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-generate/
BuildArch: noarch

# https://github.com/praekelt/django-generate.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


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
Group: Development/Python3
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

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.6-alt2
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.6-alt1.git20120918.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.6-alt1.git20120918.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20120918
- Initial build for Sisyphus

