%define pypi_name drf-spectacular

%def_with check

Name:    python3-module-%pypi_name
Version: 0.26.5
Release: alt1

Summary: Sane and flexible OpenAPI 3 schema generation for Django REST framework
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/tfranzel/drf-spectacular

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-uritemplate
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-inflection
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-djangorestframework-simplejwt
BuildRequires: python3-module-django-filter
BuildRequires: python3-module-django-oauth-toolkit
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

%check
# Remove tests with broken imports
rm -fr tests/contrib
python3 runtests.py --fast

%files
%doc *.rst
%python3_sitelibdir/drf_spectacular/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Sep 28 2023 Alexander Burmatov <thatman@altlinux.org> 0.26.5-alt1
- Initial build for Sisyphus.
