%define _unpackaged_files_terminate_build 1
%define abiversion 1

Name: resvg
Version: 0.45.1
Release: alt1

Summary: An SVG rendering library writen in rust
License: Apache-2.0 or MIT
Group: Development/Other
Url: https://crates.io/crates/resvg
Vcs: https://github.com/linebender/resvg.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust

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

%description -n libresvg-devel
%summary.

%package -n qt-resvg-devel
Summary: An idiomatic Qt API for resvg
Group: Development/C
BuildArch: noarch

Requires: libresvg-devel

%description -n qt-resvg-devel
%summary.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%rust_build --all-features -p usvg -p resvg -p resvg-capi

%install
%rust_install resvg usvg

# Install C library.
install -Dm 755 target/release/libresvg.so "%buildroot%_libdir/libresvg.so.%abiversion"
ln -sr %buildroot%_libdir/libresvg.so.%abiversion %buildroot%_libdir/libresvg.so
# Install API.
install -Dm 755 crates/c-api/resvg.h %buildroot%_includedir/resvg.h
install -Dm 755 crates/c-api/ResvgQt.h %buildroot%_includedir/ResvgQt.h

%check
%rust_test --all --all-features

%files
%doc crates/resvg/LICENSE-*
%doc README.md docs/
%_bindir/resvg

%files -n usvg
%doc crates/usvg/LICENSE-*
%doc crates/usvg/docs/
%doc crates/usvg/README.md
%_bindir/usvg

%files -n libresvg%abiversion
%doc crates/c-api/LICENSE-*
%_libdir/libresvg.so.%abiversion

%files -n libresvg-devel
%doc crates/c-api/LICENSE-*
%doc crates/c-api/README.md
%_libdir/libresvg.so
%_includedir/resvg.h

%files -n qt-resvg-devel
%doc crates/c-api/LICENSE-*
%doc crates/c-api/README.md
%_includedir/ResvgQt.h

%changelog
* Tue Jul 29 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.45.1-alt1
- Initial build.
