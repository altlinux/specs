%define _unpackaged_files_terminate_build 1
%define pypi_name zizmor
%def_with check
# -flto=auto in default optflags produces slim GCC LTO objects that
# rustc's final link cannot consume (undefined references to ts_* and
# aws_lc_* symbols from cc-built static libraries).
%define optflags_lto %nil
# Link against the system jemalloc instead of building it from source
# (avoids an offline autotools build and a linker mismatch between
# prefixed vendored symbols and the unprefixed system library).
%define setup_cargo_env() \
export CARGO_HOME="${PWD}/cargo" \
export JEMALLOC_OVERRIDE="%_libdir/libjemalloc.so" \
export CARGO_FEATURE_UNPREFIXED_MALLOC_ON_SUPPORTED_PLATFORMS=1 \
%nil

Name: %pypi_name
Version: 1.30.0
Release: alt1

Summary: Static analysis for GitHub Actions
License: MIT
Group: Development/Tools
Url: https://pypi.org/project/zizmor/
Vcs: https://github.com/zizmorcore/zizmor

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: cargo-vendor-config.py
Source3: cargo-config.toml.in
Source4: crates.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
BuildRequires: rust-cargo
BuildRequires: python3-dev
BuildRequires: /proc
BuildRequires: libjemalloc-devel
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
zizmor is a static analysis tool for GitHub Actions CI/CD workflows.
It can find security issues in typical GitHub Actions CI/CD setups,
and also has robust support for detecting the newly-disclosed
"impossible" TOCTOU privilege-escalation vulnerabilities.

%package -n python3-module-%pypi_name
Summary: Metadata for the zizmor PyPI distribution
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%pypi_name
PyPI distribution metadata for zizmor, so that Python tooling can
see it as an installed distribution. This subpackage contains only
the metadata; the tool itself is in the zizmor package.

%prep
%setup -a4
%autopatch -p1
%SOURCE2 --in %SOURCE3 --out .cargo/config.toml --root "%buildroot%prefix"
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup bench
%endif

%build
%setup_cargo_env
%pyproject_build

%install
%pyproject_install

%check
%setup_cargo_env
cargo test %_smp_mflags --release --no-fail-fast -p zizmor
%pyproject_run_pytest bench/test_bench_basic.py

%files
%doc README.md LICENSE
%_bindir/%name

%files -n python3-module-%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.30.0-alt1
- Initial build for ALT Sisyphus.
