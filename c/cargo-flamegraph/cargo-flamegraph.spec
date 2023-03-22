Name:     cargo-flamegraph
Version:  0.6.2
Release:  alt1

Summary:  Easy flamegraphs for Rust projects and everything else
License:  Apache-2.0 and MIT
Group:    Development/Tools
Url:      https://github.com/flamegraph-rs/flamegraph

Packager: Alexander Burmatov <thatman@altlinux.org>

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust

%description
A Rust-powered flamegraph generator with additional support for Cargo projects!
It can be used to profile anything, not just Rust projects!
No perl or pipes required.

%prep
%setup
%patch -p1

%build
%rust_build

%install
%rust_install

%files
%_bindir/*
%doc LICENSE-APACHE LICENSE-MIT README.md example.svg example_cropped.png

%changelog
* Thu Mar 09 2023 Alexander Burmatov <thatman@altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus
