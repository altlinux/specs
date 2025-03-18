%define pypi_name django-cors-headers

%def_with check

Name:    python3-module-%pypi_name
Version: 4.7.0
Release: alt1

Summary: Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS)
License: MIT
Group:   Development/Python3
URL:     https://github.com/adamchainz/django-cors-headers

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses.
This allows in-browser requests to your Django application from other origins.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/corsheaders/
%python3_sitelibdir_noarch/*.dist-info/

%check
%pyproject_run_pytest

%changelog
* Fri Mar 14 2025 Alexander Burmatov <thatman@altlinux.org> 4.7.0-alt1
- Update version to 4.7.0.

* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 4.6.0-alt1
- Update version to 4.6.0.

* Tue Dec 12 2023 Alexander Burmatov <thatman@altlinux.org> 4.3.1-alt1
- Update version to 4.3.1.

* Tue Sep 26 2023 Alexander Burmatov <thatman@altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus.
