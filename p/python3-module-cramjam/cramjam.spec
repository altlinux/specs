%define optflags_lto %nil
%define pypi_name cramjam

%def_with check

Name: python3-module-%pypi_name
Version: 2.11.0
Release: alt1

Summary: A collection of compression algorithms
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/cramjam
VCS: https://github.com/milesgranger/cramjam
Source0: %name-%version.tar
Source1: crates.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-maturin
# XXX: Since v2.8.4 isal and blosc2 subprojects could not be linked with
# system provided libs.
# use-system-isal-shared and use-system-blosc2-shared config opts did not
# produced any result
BuildRequires: gcc-c++ glibc-devel-static cmake nasm
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(python3)
BuildRequires: /proc
BuildRequires: rust-cargo
# BuildRequires: cargo-vendor-filterer
%{?!_without_check:%{?!_disable_check:
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-pytest
}}

%description
Your go-to for easy access to a plethora of compression algorithms,
all neatly bundled in one simple installation.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
# enable system libraries where supported
export ZSTD_SYS_USE_PKG_CONFIG=1
export PKG_CONFIG_PATH=%_pkgconfigdir
%pyproject_build

%install
%pyproject_install

%check
# XXX: Switched off test_variants cause it fails on different cases
# https://github.com/milesgranger/cramjam/issues/190
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest --ignore benchmarks -v \
-k 'not test_variants'

%files
%doc README.* LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Fri Aug 29 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.11.0-alt1
- 2.10.0 -> 2.11.0

* Tue Apr 15 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.10.0-alt1
- 2.9.0 -> 2.10.0

* Mon Dec 23 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.9.0-alt2
- fix FTBFS: disable broken tests

* Tue Dec 10 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.9.0-alt1
- 2.8.3 -> 2.9.0

* Thu May 16 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.8.3-alt1
- Initial build for Sisyphus
