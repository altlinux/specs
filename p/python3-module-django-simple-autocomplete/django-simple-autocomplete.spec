%define modname simple_autocomplete
%define oname django-simple-autocomplete

Name: python3-module-%oname
Version: 1.11
Release: alt1

Summary: Django app adding painless autocomplete to admin
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-simple-autocomplete/
BuildArch: noarch

# https://github.com/praekelt/django-simple-autocomplete.git
Source: %name-%version.tar
Patch0: fix-module-import-error.patch

BuildRequires(pre): rpm-build-python3


%description
App enabling the use of jQuery UI autocomplete widget for
ModelChoiceFields with minimal configuration required.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
App enabling the use of jQuery UI autocomplete widget for
ModelChoiceFields with minimal configuration required.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

sed -i 's|core.urlresolvers|urls|' $(find ./ -name '*.py')

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%modname/tests/

%files tests
%python3_sitelibdir/%modname/tests/


%changelog
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.11-alt1
- Version updated to 1.11
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt1.git20140226.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.git20140226.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140226
- Initial build for Sisyphus

