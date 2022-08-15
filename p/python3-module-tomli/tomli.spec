%define _unpackaged_files_terminate_build 1
%define pypi_name tomli

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.1
Release: alt2

Summary: A lil' TOML parser
License: MIT
Group: Development/Python3
# Source-git: https://github.com/hukkin/tomli.git
Url: https://pypi.org/project/tomli

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

BuildArch: noarch

%description
Tomli is a Python library for parsing TOML. Tomli is fully compatible with TOML
v1.0.0.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -- -v

%files
%doc README.md
%python3_sitelibdir/tomli/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 11 2022 Stanislav Levin <slev@altlinux.org> 2.0.1-alt2
- Modernized packaging.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 2.0.0 -> 2.0.1.

* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.2.2 -> 2.0.0.

* Tue Nov 02 2021 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 1.2.1 -> 1.2.2.

* Wed Sep 29 2021 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.1.0 -> 1.2.1.

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- NMU: drop BR: python3-module-flit (publishing tool)

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.

