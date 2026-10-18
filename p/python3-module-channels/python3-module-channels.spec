%define pypi_name channels

%def_with check

Name: python3-module-%pypi_name
Version: 4.3.2
Release: alt0.1

Summary: Developer-friendly asynchrony for Django
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/channels
VCS: https://github.com/django/channels

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-daphne
BuildRequires: python3-module-async-timeout
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

# upstream installs its tests as a top-level package
rm -rv %buildroot%python3_sitelibdir/tests

%check
# selenium tests need a browser
%pyproject_run_pytest -v --ignore=tests/sample_project/tests/test_selenium.py

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Oct 18 2026 Vitaly Lipatov <lav@altlinux.ru> 4.3.2-alt0.1
- NMU: new version 4.3.2.
- Dropped test-fix patch (applied upstream).
- Skip selenium tests in %%check (need a browser).
- Do not package top-level tests module.

* Fri Aug 01 2025 Anton Vyatkin <toni@altlinux.org> 4.2.2-alt1
- New version 4.2.2.

* Tue Nov 19 2024 Anton Vyatkin <toni@altlinux.org> 4.2.0-alt1
- New version 4.2.0.

* Mon Jul 22 2024 Anton Vyatkin <toni@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus
