%define _unpackaged_files_terminate_build 1
%define pypi_name ruff

Name: python3-module-%pypi_name
Version: 0.0.285
Release: alt1

Summary: An extremely fast Python linter, written in Rust
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/ruff/
Vcs: https://github.com/astral-sh/ruff

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml
Source3: %pyproject_deps_config_name
Patch0: python3-module-ruff-0.0.285-alt-fix-jemalloc-linking.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: libjemalloc-devel

%description
%summary.

%prep
%setup -a1
%autopatch -p1
cat %SOURCE2 >> .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%ifarch aarch64
# aarch64 needs this flag to avoid the following building errors:
#    - undefined reference to `__aarch64_swp1_acq'
#    - undefined reference to `__aarch64_cas1_acq_rel'
export CFLAGS="$CFLAGS -mno-outline-atomics"
%endif
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md BREAKING_CHANGES.md
%attr(755,root,root) %_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 22 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.285-alt1
- Built for ALT Sisyphus.

