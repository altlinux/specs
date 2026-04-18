%global _unpackaged_files_terminate_build 1
%define pypi_name fastar
%define module_name fastar

%def_with check

Name: python3-module-fastar
Version: 0.11.0
Release: alt1

Summary: High-level bindings for the Rust tar crate
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastar/
Vcs: https://github.com/DoctorJohn/fastar
AutoReq: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: cargo-vendor-config.py
Source3: crates.tar
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
BuildRequires: python3-dev
BuildRequires: libzstd-devel
BuildRequires: /proc
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-typing-extensions
%add_pyproject_deps_check_filter prek
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The fastar library wraps the Rust tar, flate2, and zstd crates,
providing a high-performance way to work with compressed and
uncompressed tar archives in Python.

%prep
%setup -a3
%SOURCE2 --root "%buildroot%prefix"
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
export ZSTD_SYS_USE_PKG_CONFIG=1
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
* Sun Apr 19 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.11.0-alt1
- Initial build for ALT Sisyphus.
