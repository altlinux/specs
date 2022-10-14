%define _unpackaged_files_terminate_build 1
%define oname django-guardian
%def_with check

Name: python3-module-%oname
Version: 2.4.0
Release: alt1

Summary: Implementation of per object permissions for Django 1.2 or later

License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-guardian

# https://github.com/lukaszb/django-guardian
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-environ
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%py3_provides %oname

BuildArch: noarch

%description
django-guardian is implementation of per object permissions as
authorization backend which is supported since Django 1.2. It won't work
with older Django releases.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
django-guardian is implementation of per object permissions as
authorization backend which is supported since Django 1.2. It won't work
with older Django releases.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

install -d %buildroot%python3_sitelibdir/%oname

%check
py.test-3 -v

%files
%doc AUTHORS CHANGES *.rst
%python3_sitelibdir/guardian
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/guardian/test*
%exclude %python3_sitelibdir/guardian/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/guardian/test*
%python3_sitelibdir/guardian/*/test*

%changelog
* Fri Oct 14 2022 Grigory Ustinov <grenka@altlinux.org> 2.4.0-alt1
- Automatically updated to 2.4.0.
- Build with check.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt2
- Fixed BuildRequires.

* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1.0-alt1
- Version updated to 2.1
- build for python2 disabled

* Fri Dec 21 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.9-alt1
- update to 1.4.9

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.4-alt1.git20140714.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.4-alt1.git20140714.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1.git20140714.1
- NMU: Use buildreq for BR.

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.git20140714
- Initial build for Sisyphus

