%define _unpackaged_files_terminate_build 1
%define pypi_name rignore
%define module_name rignore
%def_with check

Name: python3-module-rignore
Version: 0.7.6
Release: alt1

Summary: Python bindings for the Rust ignore crate
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rignore/
Vcs: https://github.com/patrick91/rignore
AutoReq: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: cargo-vendor-config.py
Source3: cargo-config.toml.in
Source4: crates.tar
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
BuildRequires: python3-dev
%pyproject_builddeps_build
%if_with check
BuildRequires: git
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
rignore provides Python bindings for the Rust ignore crate,
enabling high-performance .gitignore-style file matching from
Python.

%prep
%setup -a4
%SOURCE2 --in %SOURCE3 --out .cargo/config.toml --root "%buildroot%prefix"
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jun 26 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.7.6-alt1
- Initial build for ALT Sisyphus.
