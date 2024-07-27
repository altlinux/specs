%define pypi_name drf-yasg

%def_without check

Name: python3-module-%pypi_name
Version: 1.21.7
Release: alt1

Summary: Automated generation of real Swagger/OpenAPI 2.0 schemas DRF code
License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/axnsan12/drf-yasg

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-django
BuildRequires: python3-module-pytz
BuildRequires: python3-module-inflection
BuildRequires: python3-module-uritemplate
%endif

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%python3_sitelibdir/drf_yasg
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 22 2024 Anton Vyatkin <toni@altlinux.org> 1.21.7-alt1
- Initial build for Sisyphus.
