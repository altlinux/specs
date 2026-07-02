Name: tree-sitter
Version: 0.26.10
Release: alt1

Summary: Parser generator tool and an incremental parsing library
License: MIT
Group: Development/Tools

Url: https://github.com/tree-sitter/tree-sitter
Source: %name-%version.tar

BuildRequires: gcc make
%ifnarch %e2k
BuildRequires: rust-cargo
BuildRequires: clang22.1 clang22.1-support libclang22 libclang-cpp22 libstdc++-devel llvm-common
BuildRequires: /proc
%endif

%description
Tree-sitter is a parser generator tool and an incremental parsing library.
It can build a concrete syntax tree for a source file and efficiently update
the syntax tree as the source file is edited.

%package -n lib%name
Summary: Tree-sitter library
Group: Development/Other

%description -n lib%name
Tree-sitter library

%package -n lib%name-devel
Summary: Devel package for tree-sitter library
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for tree-sitter library

%package -n %name-cli
Summary: Tree-sitter CLI tool
Group: Development/Other

%description -n %name-cli
Tree-sitter CLI tool

%prep
%setup

%ifnarch %e2k
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%endif

%build
%make_build

%ifnarch %e2k
cargo build --offline --release
%endif

%install
export PREFIX=%_prefix
export DESTDIR=%buildroot
export INCLUDEDIR=%_includedir
export LIBDIR=%_libdir
export PCLIBDIR=%_pkgconfigdir
make install

%ifnarch %e2k
mkdir -p %buildroot%_bindir
install -m 0755 target/release/%name %buildroot%_bindir
%endif

# install directory for parser symlinks
install -d %{buildroot}%{_libdir}/%name

%files -n lib%name
%_libdir/*.so.0.*
%_libdir/%name
%exclude %_libdir/*.a

%files -n lib%name-devel
%_libdir/*.so
%_libdir/*.so.0
%_includedir/*
%_pkgconfigdir/%name.pc

%ifnarch %e2k
%files -n %name-cli
%_bindir/%name
%endif

%changelog
* Thu Jul 2 2026 Vladimir Didenko <cow@altlinux.ru> 0.26.10-alt1
- new version

* Mon May 25 2026 Vladimir Didenko <cow@altlinux.ru> 0.26.9-alt1
- new version

* Tue Apr 7 2026 Vladimir Didenko <cow@altlinux.ru> 0.26.8-alt1
- new version

* Mon Mar 30 2026 Vladimir Didenko <cow@altlinux.ru> 0.26.7-alt1
- new version

* Tue Oct 14 2025 Vladimir Didenko <cow@altlinux.ru> 0.25.10-alt1
- new version

* Wed Sep 10 2025 Vladimir Didenko <cow@altlinux.ru> 0.25.9-alt1
- new version

* Mon Jul 14 2025 Vladimir Didenko <cow@altlinux.ru> 0.25.8-alt1
- new version

* Fri Jun 6 2025 Vladimir Didenko <cow@altlinux.ru> 0.25.6-alt1
- new version

* Fri May 30 2025 Vladimir Didenko <cow@altlinux.ru> 0.25.5-alt1
- new version

* Tue May 20 2025 Vladimir Didenko <cow@altlinux.ru> 0.25.4-alt1
- new version

* Mon Mar 10 2025 Vladimir Didenko <cow@altlinux.ru> 0.25.3-alt1
- new version

* Wed Feb 19 2025 Vladimir Didenko <cow@altlinux.ru> 0.25.2-alt1
- new version

* Mon Feb 3 2025 Vladimir Didenko <cow@altlinux.ru> 0.25.1-alt1
- new version

* Tue Jan 14 2025 Vladimir Didenko <cow@altlinux.ru> 0.24.7-alt1
- new version

* Thu Jan 9 2025 Vladimir Didenko <cow@altlinux.ru> 0.24.6-alt1
- new version

* Tue Dec 17 2024 Vladimir Didenko <cow@altlinux.ru> 0.24.5-alt1
- new version

* Tue Nov 19 2024 Michael Shigorin <mike@altlinux.org> 0.24.4-alt3
- E2K: skip cli build for now (BR: rust-cargo)

* Thu Nov 14 2024 Vladimir Didenko <cow@altlinux.ru> 0.24.4-alt2
- fix neovim freeze (upstream issue: #3930)

* Tue Nov 12 2024 Vladimir Didenko <cow@altlinux.ru> 0.24.4-alt1
- new version

* Thu Oct 10 2024 Vladimir Didenko <cow@altlinux.ru> 0.24.3-alt1
- new version

* Mon Oct 7 2024 Vladimir Didenko <cow@altlinux.ru> 0.24.2-alt1
- new version

* Wed Oct 2 2024 Vladimir Didenko <cow@altlinux.ru> 0.23.2-alt1
- new version

* Wed Aug 28 2024 Vladimir Didenko <cow@altlinux.ru> 0.23.0-alt1
- new version

* Mon Aug 26 2024 Vladimir Didenko <cow@altlinux.ru> 0.22.6-alt2
- pack directory to store parser symlinks

* Wed May 8 2024 Vladimir Didenko <cow@altlinux.ru> 0.22.6-alt1
- new version

* Mon Apr 22 2024 Vladimir Didenko <cow@altlinux.ru> 0.22.5-alt1
- new version

* Thu Mar 21 2024 Vladimir Didenko <cow@altlinux.ru> 0.22.2-alt1
- new version

* Tue Mar 12 2024 Vladimir Didenko <cow@altlinux.ru> 0.22.1-alt1
- new version

* Mon Feb 26 2024 Vladimir Didenko <cow@altlinux.ru> 0.21.0-alt1
- new version

* Sat Jan 27 2024 Vladimir Didenko <cow@altlinux.ru> 0.20.9-alt1
- new version

* Thu Apr 6 2023 Vladimir Didenko <cow@altlinux.ru> 0.20.8-alt1
- new version

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.ru> 0.20.7-alt1
- new version

* Sat Mar 5 2022 Vladimir Didenko <cow@altlinux.ru> 0.20.6-alt1
- new version

* Mon Jan 31 2022 Vladimir Didenko <cow@altlinux.ru> 0.20.4-alt1
- new version

* Thu Dec 2 2021 Vladimir Didenko <cow@altlinux.ru> 0.20.1-alt1
- new version

* Tue Jul 6 2021 Vladimir Didenko <cow@altlinux.ru> 0.20.0-alt1.git0926fad1
- new version

* Wed Mar 17 2021 Vladimir Didenko <cow@altlinux.ru> 0.19.3-alt2
- build CLI tool

* Tue Mar 16 2021 Vladimir Didenko <cow@altlinux.ru> 0.19.3-alt1
- new version

* Tue Nov 24 2020 Vladimir Didenko <cow@altlinux.ru> 0.17.3-alt1
- initial build for Sisyphus
