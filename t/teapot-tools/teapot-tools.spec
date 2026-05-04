%define _unpackaged_files_terminate_build 1

Name: teapot-tools
Version: 0.4.3
Release: alt1

Summary: gclient reimplementation in Rust
License: Apache-2.0
Group: Development/Tools

URL: https://github.com/selfisekai/teapot_tools
VCS: https://github.com/selfisekai/teapot_tools
Source0: %name-%version.tar
Source1: %name-vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: python3
BuildRequires: rust-cargo
BuildRequires: protobuf-compiler
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(python3)

%description
reimplementation of gclient from depot_tools and cipd from luci-go in Rust (or
as some may call it, Python with extra steps).

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
install -D target/release/download_from_google_storage \
  %buildroot%_bindir/download_from_google_storage
install -D target/release/gclient \
  %buildroot%_bindir/gclient

%files
%_bindir/download_from_google_storage
%_bindir/gclient
%doc README.md

%changelog
* Tue Dec 09 2025 David Sultaniiazov <x1z53@altlinux.org> 0.4.3-alt1
- Initial build.
