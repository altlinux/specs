%ifarch i586
%def_without check
%else
%def_with check
%endif

Name: ouch
Version: 0.8.0
Release: alt1
Summary: Painless compression and decompression for your terminal
License: MIT
Group: Archiving/Compression
Url: https://crates.io/crates/ouch
VCS: https://github.com/ouch-org/ouch

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: clang-devel
BuildRequires: cmake
BuildRequires: gcc-c++

%if_with check
BuildRequires: git-core
%endif

%description
ouch stands for Obvious Unified Compression Helper and is a CLI tool
to help you compress and decompress files of several formats.

%prep
%setup -a 1
%rust_prep

%build
%ifarch i586
export BINDGEN_EXTRA_CLANG_ARGS="-D__CLANG_MAX_ALIGN_T_DEFINED -D_GCC_MAX_ALIGN_T"
%endif
%rust_build

%install
%rust_install

%check
%rust_test -- --test-threads=1

%files
%_bindir/%name
%doc README.md LICENSE

%changelog
* Fri Jun 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.0-alt1
- Updated to version 0.8.0.

* Sat Apr 25 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.1-alt1
- Updated to version 0.7.1.

* Wed Jul 16 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.1-alt1
- Updated to version 0.6.1.

* Wed Dec 20 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.1-alt1
- Updated to version 0.5.1.

* Mon Jan 30 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.1-alt1
- Updated to version 0.4.1

* Sat Dec 17 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.0-alt1
- Updated to version 0.4.0

* Thu Jun 02 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.1-alt1
- Initial build for ALT
