%define _unpackaged_files_terminate_build 1
%define soname 3

Name: dovi_tool
Version: 2.1.2
Release: alt1

Summary: Utilites for working with Dolby Vision
Group: Video
License: MIT
Url: https://github.com/quietvoid/dovi_tool

Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: dolby_vision-vendor.tar

BuildRequires: fontconfig-devel
BuildRequires: /proc rust rust-cargo rust-cargo-c rpm-macros-rust

%package -n libdovi%{soname}
Summary: Library to read & write Dolby Vision metadata
Group: System/Libraries

%package -n libdovi-devel
Summary: Development headers for libdovi
Group: Development/C

%description
dovi_tool is a CLI tool combining multiple utilities for working with Dolby
Vision.

%description -n libdovi%{soname}
Library to read & write Dolby Vision metadata.

%description -n libdovi-devel
Development headers for libdovi.

%prep
%setup -a1 -a2

for d in . dolby_vision; do
pushd "$d"
mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/plotters-rs/plotters"]
git = "https://github.com/plotters-rs/plotters"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
strip = "none"
lto= "thin"
debug = "full"
EOF
popd
done

%build
for d in . dolby_vision; do
pushd "$d"
%rust_build
popd
done

%install
install -Dm755 target/release/%name %buildroot%_bindir/%name
# libdovi
pushd dolby_vision
cargo cinstall --release --prefix=%buildroot%_prefix --libdir=%buildroot%_libdir
popd
rm -f %buildroot%_libdir/libdovi.a

%check
cargo test --bins --release

%files
%doc LICENSE README.md docs
%_bindir/*

%files -n libdovi%{soname}
%_libdir/libdovi.so.%{soname}*
%doc dolby_vision/LICENSE dolby_vision/README.md dolby_vision/CHANGELOG.md

%files -n libdovi-devel
%_includedir/*
%_pkgconfigdir/*.pc
%_libdir/libdovi.so

%changelog
* Mon Aug 05 2024 L.A. Kostis <lakostis@altlinux.ru> 2.1.2-alt1
- 2.1.2.

* Tue Jun 11 2024 L.A. Kostis <lakostis@altlinux.ru> 2.1.1-alt2
- build with debuginfo.

* Mon Jun 03 2024 L.A. Kostis <lakostis@altlinux.ru> 2.1.1-alt1
- 2.1.1.

* Thu Nov 09 2023 L.A. Kostis <lakostis@altlinux.ru> 2.1.0-alt1
- 2.1.0.
- Use rpm macros for rust (and fix debuginfo).

* Fri Jul 14 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.0.3-alt2
- Updated vendor dependencies to support LoongArch.

* Thu Mar 16 2023 L.A. Kostis <lakostis@altlinux.ru> 2.0.3-alt1
- Initial build for ALTLinux.

