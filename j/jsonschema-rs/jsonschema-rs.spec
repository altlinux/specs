%define _unpackaged_files_terminate_build 1

%define pypi_name jsonschema-rs
%define mod_name jsonschema_rs

Name: %pypi_name
Version: 0.46.10
Release: alt1

Summary: A high-performance JSON Schema validator
License: MIT
Group: Development/Other
Url: https://docs.rs/jsonschema/latest/jsonschema/
Vcs: https://github.com/Stranger6667/jsonschema.git

Source: %name-%version.tar
Source1: vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-rust
BuildRequires(pre): rpm-build-pyproject
BuildRequires: rust-cargo
BuildRequires: maturin

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%description
Jsonschema-rs is a high-performance JSON Schema validator implemented in Rust.

%package -n python3-module-jsonschema-rs
Summary: Python bindings for jsonschema-rs
Group: Development/Python

%description -n python3-module-jsonschema-rs
High-performance JSON Schema validator for Python, implemented in Rust.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml

%build
export RUSTFLAGS="${RUSTFLAGS} -g"
export CARGO_PROFILE_RELEASE_STRIP='none'
%rust_build -p jsonschema-cli
pushd crates/jsonschema-py
%pyproject_build
popd

%install
install -Dm755 target/release/jsonschema-cli %buildroot%_bindir/jsonschema
pushd crates/jsonschema-py
%pyproject_install
popd

%files
%_bindir/jsonschema
%doc README.md

%files -n python3-module-jsonschema-rs
%doc crates/jsonschema-py/README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 06 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.46.10-alt1
- New version (0.46.10).

* Wed Jun 03 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.46.5-alt1
- New version (0.46.5).

* Wed Apr 08 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.45.1-alt1
- New version (0.45.1).

* Tue Mar 10 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.45.0-alt1
- New version (0.45.0).

* Mon Mar 02 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.44.0-alt1
- New version (0.44.0).

* Tue Feb 17 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 0.42.1-alt1
- Initial build for ALT.
