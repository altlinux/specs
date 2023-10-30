%define pypi_name djangorestframework-simplejwt
%define mod_name rest_framework_simplejwt

%def_with check

Name:    python3-module-%pypi_name
Version: 5.3.0
Release: alt1

Summary: A JSON Web Token authentication plugin for the Django REST Framework
License: MIT
Group:   Development/Python3
URL:     https://github.com/jazzband/djangorestframework-simplejwt

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-jose
BuildRequires: python3-module-jwt
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name

%check
%pyproject_run_pytest

%files -f %name.lang
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/djangorestframework_simplejwt-0.0.0.dist-info/

%changelog
* Mon Oct 23 2023 Alexander Burmatov <thatman@altlinux.org> 5.3.0-alt1
- Initial build for Sisyphus.
