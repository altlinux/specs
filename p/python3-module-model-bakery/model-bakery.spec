%define _unpackaged_files_terminate_build 1
%define pypi_name model-bakery
%define mod_name model_bakery

%def_with check

Name: python3-module-%pypi_name
Version: 1.18.2
Release: alt1
Summary: Smart object creation facility for Django
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/model-bakery
Vcs: https://github.com/model-bakers/model_bakery
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
Model Bakery offers you a smart way to create fixtures for testing in Django.
With a simple and powerful API you can create many objects with a single line of
code.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
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
