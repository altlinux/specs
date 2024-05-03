%define _unpackaged_files_terminate_build 1
%define optflags_lto %nil
%define pypi_name uv
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.39
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
export OPENSSL_NO_VENDOR=1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
# https://docs.rs/openssl/latest/openssl/
export OPENSSL_NO_VENDOR=1
export OPENSSL_LIB_DIR="%_libdir"
export OPENSSL_INCLUDE_DIR="%_includedir"
%pyproject_build

%install
%pyproject_install

%check
# smoke test
%pyproject_run -- uv --help

%files
%doc README.*
%_bindir/uv
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri May 03 2024 Stanislav Levin <slev@altlinux.org> 0.1.39-alt1
- 0.1.38 -> 0.1.39.

* Thu Apr 25 2024 Stanislav Levin <slev@altlinux.org> 0.1.38-alt1
- Initial build for Sisyphus.
