Name: cargo-expand
Version:  1.0.40
Release:  alt1

Summary:  Subcommand to show result of macro expansion
License:  Apache-2.0 and MIT
Group:    Development/Tools
Url:      https://github.com/dtolnay/cargo-expand

Packager: Alexander Burmatov <thatman@altlinux.org>

Source:   %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: rust-cargo

%description
Allows you to inspect the code that macros expand to.

%prep
%setup
%patch -p1

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/*
%doc LICENSE-APACHE LICENSE-MIT README.md

%changelog
* Tue Mar 07 2023 Alexander Burmatov <thatman@altlinux.org> 1.0.40-alt1
- Initial build for Sisyphus
