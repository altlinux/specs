%define _unpackaged_files_terminate_build 1
%define pypi_name tomli

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.2
Release: alt1
Summary: A lil' TOML parser
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tomli
Vcs: https://github.com/hukkin/tomli
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Tomli is a Python library for parsing TOML. Tomli is fully compatible with TOML
v1.0.0.

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
%pyproject_run_unittest -v

%files
%doc README.md
%python3_sitelibdir/tomli/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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

