%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject-fmt-rust
%define mod_name pyproject_fmt_rust

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.6
Release: alt1
Summary: Format pyproject.toml files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyproject-fmt-rust
Vcs: https://github.com/tox-dev/pyproject-fmt-rust
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: vendor_rust.tar
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%summary.

%prep
%setup -a2
%autopatch -p1
mkdir -p .cargo
cat < vendor_cargoconf.toml >> .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 01 2024 Stanislav Levin <slev@altlinux.org> 1.1.6-alt1
- 1.1.5 -> 1.1.6.

* Wed Jul 03 2024 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- Initial build for Sisyphus.
