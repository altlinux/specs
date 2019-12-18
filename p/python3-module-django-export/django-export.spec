%define oname django-export

Name: python3-module-%oname
Version: 1.11.0
Release: alt1

Summary: Django app allowing for filtered exporting of model data
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-export/
BuildArch: noarch

# https://github.com/praekelt/django-export.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
Requires: python3-module-django-object-tools


%description
django-export allows you to export model objects in a wide range of
serialized formats (JSON, CSV, XML, YAML). Exports can be filtered and
ordered on any of the particular model's fields.

django-export utilizes django-object-tools to hook into Django's admin
interface and take care of user permissions.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
django-export allows you to export model objects in a wide range of
serialized formats (JSON, CSV, XML, YAML). Exports can be filtered and
ordered on any of the particular model's fields.

django-export utilizes django-object-tools to hook into Django's admin
interface and take care of user permissions.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

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
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.11.0-alt1
- Version updated to 1.11.0
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.4-alt1.git20110909.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.4-alt1.git20110909.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20110909
- Initial build for Sisyphus

