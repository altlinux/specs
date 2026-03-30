%define _unpackaged_files_terminate_build 1
%define pypi_name tomli
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.4.1
Release: alt1.1
Summary: A lil' TOML parser
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tomli
Vcs: https://github.com/hukkin/tomli
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%description
Tomli is a Python library for parsing TOML. Version 2.4.0 and later are
compatible with TOML v1.1.0. Older versions are TOML v1.0.0 compatible.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Mar 28 2026 Grigory Ustinov <grenka@altlinux.org> 2.4.1-alt1.1
- Demodernized packaging.

* Thu Mar 26 2026 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1
- 2.4.0 -> 2.4.1.

* Tue Jan 13 2026 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0.

* Tue Oct 14 2025 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.2.1 -> 2.3.0.

* Thu Nov 28 2024 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- 2.1.0 -> 2.2.1.

* Tue Nov 12 2024 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.2 -> 2.1.0.

* Fri Oct 04 2024 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 2.0.1 -> 2.0.2.

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

