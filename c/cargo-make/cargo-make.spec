Name: cargo-make
Version:  0.36.5
Release:  alt1

Summary:  Rust task runner and build tool.
License:  Apache-2.0
Group:    Development/Tools
Url:      https://github.com/sagiegurari/cargo-make

Packager: Alexander Burmatov <thatman@altlinux.org>

Source:   %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
%ifarch ppc64le
BuildRequires: libssl-devel
%endif
BuildRequires: /proc

%description
%summary

%prep
%setup
%patch -p1

%build
%ifarch ppc64le
%rust_build --no-default-features --features=tls-native
%else
%rust_build
%endif

%install
%rust_install

%files
%_bindir/*
%doc *.md

%changelog
* Tue Feb 21 2023 Alexander Burmatov <thatman@altlinux.org> 0.36.5-alt1
- Initial build for Sisyphus
