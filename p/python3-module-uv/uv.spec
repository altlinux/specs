%define _unpackaged_files_terminate_build 1
%define optflags_lto %nil
%define pypi_name uv
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.26
Release: alt1
Summary: An extremely fast Python package installer and resolver
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/uv
Vcs: https://github.com/astral-sh/uv
Source: %name-%version.tar
Source1: vendor_rust.tar
Source2: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: /usr/bin/cmake
BuildRequires: libssl-devel
%if_with check
%pyproject_builddeps_metadata
%endif

%description
An extremely fast Python package installer and resolver, written in Rust.
Designed as a drop-in replacement for common pip and pip-tools workflows.

%prep
%setup -a1
%autopatch -p1
cat < vendor_cargoconf.toml >> .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# smoke test
%pyproject_run -- uv --help

%files
%doc README.*
%_bindir/uv
%_bindir/uvx
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jul 18 2024 Stanislav Levin <slev@altlinux.org> 0.2.26-alt1
- 0.2.25 -> 0.2.26.

* Tue Jul 16 2024 Stanislav Levin <slev@altlinux.org> 0.2.25-alt1
- 0.2.24 -> 0.2.25.

* Fri Jul 12 2024 Stanislav Levin <slev@altlinux.org> 0.2.24-alt1
- 0.2.23 -> 0.2.24.

* Tue Jul 09 2024 Stanislav Levin <slev@altlinux.org> 0.2.23-alt1
- 0.2.22 -> 0.2.23.

* Mon Jul 08 2024 Stanislav Levin <slev@altlinux.org> 0.2.22-alt1
- 0.2.21 -> 0.2.22.

* Wed Jul 03 2024 Stanislav Levin <slev@altlinux.org> 0.2.21-alt1
- 0.2.18 -> 0.2.21.

* Mon Jul 01 2024 Stanislav Levin <slev@altlinux.org> 0.2.18-alt1
- 0.2.17 -> 0.2.18.

* Thu Jun 27 2024 Stanislav Levin <slev@altlinux.org> 0.2.17-alt1
- 0.2.15 -> 0.2.17.

* Tue Jun 25 2024 Stanislav Levin <slev@altlinux.org> 0.2.15-alt1
- 0.2.13 -> 0.2.15.

* Thu Jun 20 2024 Stanislav Levin <slev@altlinux.org> 0.2.13-alt1
- 0.2.12 -> 0.2.13.

* Tue Jun 18 2024 Stanislav Levin <slev@altlinux.org> 0.2.12-alt1
- 0.2.11 -> 0.2.12.

* Thu Jun 13 2024 Stanislav Levin <slev@altlinux.org> 0.2.11-alt1
- 0.2.10 -> 0.2.11.

* Tue Jun 11 2024 Stanislav Levin <slev@altlinux.org> 0.2.10-alt1
- 0.2.9 -> 0.2.10.

* Fri Jun 07 2024 Stanislav Levin <slev@altlinux.org> 0.2.9-alt1
- 0.2.8 -> 0.2.9.

* Thu Jun 06 2024 Stanislav Levin <slev@altlinux.org> 0.2.8-alt1
- 0.2.6 -> 0.2.8.

* Tue Jun 04 2024 Stanislav Levin <slev@altlinux.org> 0.2.6-alt1
- 0.2.5 -> 0.2.6.

* Wed May 29 2024 Stanislav Levin <slev@altlinux.org> 0.2.5-alt1
- 0.2.4 -> 0.2.5.

* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1
- 0.2.2 -> 0.2.4.

* Fri May 24 2024 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1
- 0.1.45 -> 0.2.2.

* Tue May 21 2024 Stanislav Levin <slev@altlinux.org> 0.1.45-alt1
- 0.1.44 -> 0.1.45.

* Wed May 15 2024 Stanislav Levin <slev@altlinux.org> 0.1.44-alt1
- 0.1.43 -> 0.1.44.

* Tue May 14 2024 Stanislav Levin <slev@altlinux.org> 0.1.43-alt1
- 0.1.42 -> 0.1.43.

* Mon May 13 2024 Stanislav Levin <slev@altlinux.org> 0.1.42-alt1
- 0.1.41 -> 0.1.42.

* Wed May 08 2024 Stanislav Levin <slev@altlinux.org> 0.1.41-alt1
- 0.1.39 -> 0.1.41.

* Fri May 03 2024 Stanislav Levin <slev@altlinux.org> 0.1.39-alt1
- 0.1.38 -> 0.1.39.

* Thu Apr 25 2024 Stanislav Levin <slev@altlinux.org> 0.1.38-alt1
- Initial build for Sisyphus.
