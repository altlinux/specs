%define pypi_name drf-yaml

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.1
Release: alt2

Summary: YAML support for Django REST Framework
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/drf-yaml
VCS: https://github.com/Qu4tro/drf-yaml

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch: rename_from_debian.patch
Patch1: django-5.0-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-django
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-toml
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
%summary.

%prep
%setup -n %pypi_name-%version
%autopatch -p1

# we replace rest_framwork_yaml with drf_yaml, look patch for details
mkdir rest_framework_yaml
cp -r drf_yaml/* rest_framework_yaml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.*
%python3_sitelibdir/rest_framework_yaml
%python3_sitelibdir/rest_framework_yaml-%version.dist-info

%changelog
* Wed Jul 31 2024 Anton Vyatkin <toni@altlinux.org> 3.0.1-alt2
- Fixed FTBFS.

* Mon Jul 22 2024 Anton Vyatkin <toni@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus
