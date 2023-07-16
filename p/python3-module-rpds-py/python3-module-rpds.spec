%define pypi_name rpds

%def_with check

Name: python3-module-%pypi_name-py
Version: 0.8.10
Release: alt1

Summary: Python bindings to the Rust rpds crate for persistent data structures
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/rpds-py
VCS: https://github.com/crate-py/rpds
Source0: %pypi_name-%version.tar
Source1: crates.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-maturin
BuildRequires: /proc
BuildRequires: rust-cargo
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hypothesis
%endif

%description
%summary.

%prep
%setup -n %pypi_name-%version
mkdir -p .cargo
cat >> .cargo/config <<EOF
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

tar xf %SOURCE1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.* LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/rpds_py-%version.dist-info

%changelog
* Thu Jul 13 2023 Anton Vyatkin <toni@altlinux.org> 0.8.10-alt1
- Initial build for Sisyphus
