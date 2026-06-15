Name: python3-module-maturin
Version: 1.14.0
Release: alt1

Summary: Rust within Python
License: MIT
Group: Development/Python
Url: https://maturin.rs/

Source0: %name-%version.tar
Source1: crates.tar
Source2: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
BuildRequires: rust-cargo /proc
BuildRequires: pkgconfig(bzip2)
BuildRequires: python3(semantic_version)
%pyproject_builddeps_build
%pyproject_builddeps_metadata

Requires: rust-cargo /proc
Provides: maturin = %version-%release
Obsoletes: maturin

%description
Build and publish crates with pyo3, cffi and uniffi bindings
as well as rust binaries as python packages.

%prep
%setup -a1
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
%endif

%build
# zstd-sys three levels down doesn't like lto
%define optflags_lto %nil
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_build

%install
%pyproject_install

%files
%_bindir/maturin
%python3_sitelibdir/maturin
%python3_sitelibdir/maturin-%version.dist-info

%changelog
* Mon Jun 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.14.0-alt1
- 1.14.0 released

* Tue May 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.13.3-alt1
- 1.13.3 released

* Fri Apr 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.13.1-alt1
- 1.13.1 released

* Mon Mar 02 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.12.6-alt1
- 1.12.6 released

* Tue Feb 24 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.12.4-alt1
- 1.12.4 released

* Fri Feb 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.12.3-alt1
- 1.12.3 released

* Tue Feb 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.12.2-alt1
- 1.12.2 released

* Mon Feb 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.12.1-alt1
- 1.12.1 released

* Wed Jan 14 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.11.5-alt1
- 1.11.5 released

* Thu Nov 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.10.2-alt1
- 1.10.2 released

* Wed Nov 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.10.1-alt1
- 1.10.1 released

* Tue Nov 11 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.10.0-alt1
- 1.10.0 released

* Thu Oct 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.6-alt1
- 1.9.6 released

* Fri Aug 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.4-alt1
- 1.9.4 released

* Mon Jul 28 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.2-alt1
- 1.9.2 released

* Wed Jul 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.1-alt1
- 1.9.1 released

* Thu Jun 26 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.0-alt1
- 1.9.0 released

* Wed May 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.6-alt1
- 1.8.6 released

* Mon May 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.5-alt1
- 1.8.5 released

* Fri Mar 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.3-alt1
- 1.8.3 released

* Tue Feb 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.2-alt1
- 1.8.2 released

* Thu Jan 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.1-alt1
- 1.8.1 released

* Wed Dec 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.7-alt1
- 1.7.7 released

* Wed Nov 27 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.5-alt1
- 1.7.5 released

* Thu Sep 26 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.4-alt1
- 1.7.4 released

* Wed Sep 25 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.2-alt1
- 1.7.2 released

* Fri Aug 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.1-alt1
- 1.7.1 released

* Mon Jul 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.7.0-alt1
- 1.7.0 released

* Wed Jun 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.6.0-alt1
- 1.6.0 released

* Tue Apr 16 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.1-alt1
- 1.5.1 released

* Fri Mar 29 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.0-alt2
- added runtime dependency to rust-cargo

* Wed Mar 20 2024 Ivan A. Melnikov <iv@altlinux.org> 1.5.0-alt1.1
- NMU: fix FTBFS on loongarch64
  + backport upstream patch on vendored libc crate
    that adds more ioctl constants.

* Fri Mar 15 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0 released

* Mon Dec 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released

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
