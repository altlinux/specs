Name: tree-sitter
Version: 0.22.5
Release: alt1

Summary: Parser generator tool and an incremental parsing library

Group: Development/Tools
License: MIT
Url: https://github.com/tree-sitter/tree-sitter

Source: %name-%version.tar

BuildRequires: gcc make
BuildRequires: rust-cargo
BuildRequires: /proc

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

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/bytecodealliance/wasmtime?rev=fa6fcd946b8f6d60c2d191a1b14b9399e261a76d"]
git = "https://github.com/bytecodealliance/wasmtime"
rev = "fa6fcd946b8f6d60c2d191a1b14b9399e261a76d"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "cli/vendor"
EOF

%build
%make_build

cargo build --offline --release

%install
export PREFIX=%_prefix
export DESTDIR=%buildroot
export INCLUDEDIR=%_includedir
export LIBDIR=%_libdir
export PCLIBDIR=%_pkgconfigdir
make install

mkdir -p %buildroot%_bindir
install -m 0755 target/release/%name %buildroot%_bindir

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/*.a

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/%name.pc

%files -n %name-cli
%_bindir/%name

%changelog
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
