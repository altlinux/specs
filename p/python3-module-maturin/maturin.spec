Name: python3-module-maturin
Version: 1.3.1
Release: alt1

Summary: Rust within Python
License: MIT
Group: Development/Python
Url: https://maturin.rs/

Source0: %name-%version.tar
Source1: crates.tar
Source2: pyproject_deps.json

BuildRequires(pre): rpm-build-pyproject
BuildRequires: rust-cargo /proc
BuildRequires: pkgconfig(bzip2)
%pyproject_builddeps_build

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
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install
chmod +x %buildroot%_bindir/maturin

%files
%_bindir/maturin
%python3_sitelibdir/maturin
%python3_sitelibdir/maturin-%version.dist-info

%changelog
* Thu Nov 09 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- 1.3.1 released

* Fri Oct 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Fri Sep 15 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- 1.2.3 released

* Thu Jun 15 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- 1.1.0 released

* Wed May 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Fri Apr 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.17-alt1
- 0.14.17 released

* Wed Jan 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.10-alt1
- 0.14.10 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13.7-alt1
- 0.13.7 released

* Wed Aug 03 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.20-alt1
- 0.12.20 released

* Wed Jul 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.18-alt1
- 0.12.18 released
