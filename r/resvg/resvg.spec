%define _unpackaged_files_terminate_build 1

%define abiversion 0.50

%define rust_opt_level 3
%define rust_codegen_units 1
%define rust_lto "fat"

Name: resvg
Version: %abiversion.0
Release: alt1

Summary: An SVG rendering library writen in rust
License: Apache-2.0 or MIT
Group: Development/Other
Url: https://crates.io/crates/resvg
Vcs: https://github.com/linebender/resvg.git

Source: %name-%version.tar
%{!?_enable_rust_vendoring:
Source1: vendor.tar
}

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo-c
%{?_enable_rust_vendoring:
BuildRequires: cargo-vendor-filterer
}

%description
It can be used as a Rust library, as a C library, and as a CLI
application to render static SVG files.

The core idea is to make a fast, small, portable SVG library with the
goal to support the whole SVG spec.

%package -n usvg
Summary: usvg (micro SVG) is an SVG simplification tool
Group: Development/Other

%description -n usvg
%summary.

%package -n libresvg%abiversion
Summary: C api for resvg library
Group: Development/C

%description -n libresvg%abiversion
%summary.

%package -n libresvg-devel
Summary: Header files and libraries required to use resvg C library
Group: Development/C
Requires: libresvg-devel = %EVR

%description -n libresvg-devel
%summary.

%package -n libresvg-devel-static
Summary: Resvg C static library
Group: Development/C

%description -n libresvg-devel-static
%summary.

%package -n qt-resvg-devel
Summary: An idiomatic Qt API for resvg
Group: Development/C
BuildArch: noarch

Requires: libresvg-devel

%description -n qt-resvg-devel
%summary.

%prep
%setup %{!?_enable_rust_vendoring:-a1}
%rust_prep

%build
%rust_build --all-features -p usvg -p resvg
%rust_cbuild --all-features -p resvg-capi

%install
%rust_install resvg usvg
%rust_cinstall -p resvg-capi

%check
%rust_test --all --all-features

%files
%doc crates/resvg/LICENSE-MIT
%doc README.md docs/
%_bindir/resvg

%files -n usvg
%doc crates/usvg/LICENSE-MIT
%doc crates/usvg/docs/
%doc crates/usvg/README.md
%_bindir/usvg

%files -n libresvg%abiversion
%doc crates/c-api/LICENSE-MIT
%_libdir/libresvg.so.%{abiversion}*

%files -n libresvg-devel
%doc crates/c-api/LICENSE-MIT
%doc crates/c-api/README.md
%_libdir/libresvg.so
%_includedir/resvg/resvg.h
%_pkgconfigdir/resvg.pc

%files -n libresvg-devel-static
%doc crates/c-api/LICENSE-MIT
%doc crates/c-api/README.md
%_libdir/libresvg.a

%files -n qt-resvg-devel
%doc crates/c-api/LICENSE-MIT
%doc crates/c-api/README.md
%_includedir/resvg/ResvgQt.h

%changelog
* Thu Nov 19 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.50.0-alt1
- New version (0.50.0).
- Downgrade major version.
- Change qt-resvg header path.
- Include pkgbuild into libresvg-devel.
- Package libresvg-devel-static.

* Tue Aug 04 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.48.1-alt1
- New version (0.48.1).

* Tue Feb 10 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.47.0-alt1
- New version (0.47.0).

* Fri Feb 06 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.46.0-alt1
- New version (0.46.0).
- Fix C library SONAME header generation.

* Tue Jul 29 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.45.1-alt1
- Initial build.
