%define _unpackaged_files_terminate_build 1
%define pypi_name tomlkit

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.6
Release: alt1

Summary: Style preserving TOML library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tomlkit
VCS: https://github.com/sdispater/tomlkit.git

Source: %name-%version.tar
Source1: toml-test.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(poetry-core)

%if_with check
BuildRequires: python3(yaml)
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
TOML Kit is a 1.0.0-compliant TOML library. It includes a parser that preserves
all comments, indentations, whitespace and internal element ordering, and makes
them accessible and editable via an intuitive API. You can also create new TOML
documents from scratch using the provided helpers.

%prep
%setup -a1
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/tomlkit/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 0.11.6-alt1
- 0.11.5 -> 0.11.6.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.11.5-alt1
- 0.11.4 -> 0.11.5.

* Sat Aug 13 2022 Stanislav Levin <slev@altlinux.org> 0.11.4-alt1
- 0.10.1 -> 0.11.4.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.10.0 -> 0.10.1.

* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.9.2 -> 0.10.0.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1
- 0.9.1 -> 0.9.2.

* Mon Feb 07 2022 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1
- 0.9.0 -> 0.9.1.

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
