%def_with check

Name:     cargo-release
Version:  0.24.5
Release:  alt1

Summary:  Helper for publishing new crate versions
License:  Apache-2.0 and MIT
Group:    Development/Tools
Url:      https://github.com/crate-ci/cargo-release

Packager: Alexander Burmatov <thatman@altlinux.org>

Source:   %name-%version.tar
Patch:    %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: libssl-devel
%if_with check
BuildRequires: git
%endif

%description
Cargo subcommand 'release': everything about releasing a rust crate

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
%doc LICENSE-APACHE LICENSE-MIT README.md docs/*

%changelog
* Tue Mar 07 2023 Alexander Burmatov <thatman@altlinux.org> 0.24.5-alt1
- Initial build for Sisyphus
