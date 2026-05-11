%define pypi_name djangorestframework-simplejwt
%define mod_name rest_framework_simplejwt

%def_with check

Name:    python3-module-%pypi_name
Version: 5.5.1
Release: alt2

Summary: A JSON Web Token authentication plugin for the Django REST Framework
License: MIT
Group:   Development/Python3
URL:     https://github.com/jazzband/djangorestframework-simplejwt

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-jose
BuildRequires: python3-module-jwt
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-cryptography
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch: simplejwt-5.5.1-fix-ec-keys.patch

%description
%summary.

%prep
%setup -n %pypi_name-%version
%patch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install
%find_lang %name

%check
%pyproject_run_pytest

%files -f %name.lang
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 11 2026 Anton Vyatkin <toni@altlinux.org> 5.5.1-alt2
- Fix FTBFS.

* Thu Oct 16 2025 Alexander Burmatov <thatman@altlinux.org> 5.5.1-alt1
- New 5.5.1 version.

* Mon Aug 05 2024 Alexander Burmatov <thatman@altlinux.org> 5.3.1-alt2
- Fix tests.

* Tue Jan 09 2024 Alexander Burmatov <thatman@altlinux.org> 5.3.1-alt1
- New 5.3.1 version.

* Mon Oct 23 2023 Alexander Burmatov <thatman@altlinux.org> 5.3.0-alt1
- Initial build for Sisyphus.
