Name: python3-module-maturin
Version: 0.14.10
Release: alt1

Summary: Rust within Python
License: MIT
Group: Development/Python
Url: https://maturin.rs/

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_rust)
BuildRequires: python3(wheel)
BuildRequires: python3(tomli)
BuildRequires: pkgconfig(bzip2)

Requires: python3(tomli)
Provides: maturin = %version-%release
Obsoletes: maturin

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings
as well as rust binaries as python packages.

%prep
%setup
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 vendor
%else
tar xf %SOURCE1
%endif

%build
export CARGO_HOME=${PWD}/cargo
%pyproject_build

%install
%pyproject_install
chmod +x %buildroot%_bindir/maturin

%files
%_bindir/maturin
%python3_sitelibdir/maturin
%python3_sitelibdir/maturin-%version.dist-info

%changelog
* Wed Jan 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.10-alt1
- 0.14.10 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.7-alt1
- 0.13.7 released

* Wed Aug 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.20-alt1
- 0.12.20 released

* Wed Jul 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.18-alt1
- 0.12.18 released
