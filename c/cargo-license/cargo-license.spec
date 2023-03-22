Name:     cargo-license
Version:  0.5.1
Release:  alt1

Summary:  Cargo subcommand to see license of dependencies
License:  MIT
Group:    Development/Tools
Url:      https://github.com/onur/cargo-license

Packager: Alexander Burmatov <thatman@altlinux.org>

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust

%description
Cargo subcommand to view lists of license dependencies.

%prep
%setup
%patch -p1

%build
%rust_build

%install
%rust_install

%files
%_bindir/*
%doc LICENSE README.md

%changelog
* Thu Mar 09 2023 Alexander Burmatov <thatman@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus
