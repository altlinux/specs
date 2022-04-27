%define pypi_name semantic_version

%def_without bootstrap
%def_with check

Name: python3-module-%pypi_name
Version: 2.9.0
Release: alt1

Summary: A library implementing the 'SemVer' scheme.

Group: Development/Python3
License: BSD-2-Clause
URL:  https://github.com/rbarrois/python-semanticversion

Source: %name-%version.tar

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3

%if_with check
Buildrequires: python3-module-django
Buildrequires: python3-module-django-dbbackend-sqlite3
%endif

%description
This small python library provides a few tools to handle `SemVer`_ in Python.
It follows strictly the 2.0.0 version of the SemVer scheme.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if_with bootstrap
rm -f %buildroot%python3_sitelibdir/%pypi_name/django_fields.py
%endif

# Delete tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%check
%__python3 setup.py test

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Build new version.
- Build with check.

* Fri Feb 04 2022 Grigory Ustinov <grenka@altlinux.org> 2.8.5-alt6
- Change all back.

* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 2.8.5-alt5
- Bootstrap for python3.10.

* Thu Jul 15 2021 Grigory Ustinov <grenka@altlinux.org> 2.8.5-alt4
- Drop python2 support.

* Thu Feb 18 2021 Grigory Ustinov <grenka@altlinux.org> 2.8.5-alt3
- Change all back.

* Wed Feb 10 2021 Grigory Ustinov <grenka@altlinux.org> 2.8.5-alt2
- Bootstrap for python3.9.

* Mon Feb 8 2021 Vladimir Didenko <cow@altlinux.org> 2.8.5-alt1
- new version

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- Initial build
