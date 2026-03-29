%define _unpackaged_files_terminate_build 1
%define pypi_name model-bakery
%define mod_name model_bakery

%def_with check

Name: python3-module-%pypi_name
Version: 1.23.3
Release: alt1.1
Summary: Smart object creation facility for Django
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/model-bakery
Vcs: https://github.com/model-bakers/model_bakery
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-uv-build

%if_with check
BuildRequires: python3-module-black
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pillow
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-ruff
BuildRequires: python3-module-ty

BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
Model Bakery offers you a smart way to create fixtures for testing in Django.
With a simple and powerful API you can create many objects with a single line of
code.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.23.3-alt1.1
- Demodernized packaging.

* Thu Mar 12 2026 Stanislav Levin <slev@altlinux.org> 1.23.3-alt1
- 1.20.5 -> 1.23.3.

* Mon Jun 09 2025 Stanislav Levin <slev@altlinux.org> 1.20.5-alt1
- 1.20.4 -> 1.20.5.

* Thu Feb 27 2025 Stanislav Levin <slev@altlinux.org> 1.20.4-alt1
- 1.20.3 -> 1.20.4.

* Wed Feb 12 2025 Stanislav Levin <slev@altlinux.org> 1.20.3-alt1
- 1.20.1 -> 1.20.3.

* Fri Jan 10 2025 Stanislav Levin <slev@altlinux.org> 1.20.1-alt1
- 1.20.0 -> 1.20.1.

* Thu Oct 10 2024 Stanislav Levin <slev@altlinux.org> 1.20.0-alt1
- 1.18.2 -> 1.20.0.

* Mon Jul 01 2024 Stanislav Levin <slev@altlinux.org> 1.18.2-alt1
- 1.18.1 -> 1.18.2.

* Mon Jun 03 2024 Stanislav Levin <slev@altlinux.org> 1.18.1-alt1
- 1.18.0 -> 1.18.1.

* Mon Apr 22 2024 Stanislav Levin <slev@altlinux.org> 1.18.0-alt1
- 1.14.0 -> 1.18.0.

* Fri Aug 18 2023 Stanislav Levin <slev@altlinux.org> 1.14.0-alt1
- 1.13.0 -> 1.14.0.

* Thu Aug 17 2023 Stanislav Levin <slev@altlinux.org> 1.13.0-alt1
- Initial build for Sisyphus.
