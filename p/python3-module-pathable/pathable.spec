%define _unpackaged_files_terminate_build 1
%define pypi_name pathable

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.3
Release: alt1

Summary: Object-oriented paths
License: Apache-2.0
Group: Development/Python3
# Source-git: https://github.com/p1c2u/pathable
Url: https://pypi.org/project/pathable

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(poetry-core)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
Object-oriented paths.

Key features:
- Traverse resources like paths
- Access resources on demand with separate accessor layer

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus.
