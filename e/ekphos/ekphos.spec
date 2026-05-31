%global _unpackaged_files_terminate_build 1

Name: ekphos
Version: 0.25.0
Release: alt1
Summary: Markdown research tool inspired by Obsidian
License: MIT
Group: File tools
Url: https://crates.io/crates/ekphos
VCS: https://github.com/hanebox/ekphos

ExcludeArch: %ix86

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
An open source, lightweight, fast, terminal-based
markdown research tool built with Rust.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install
mkdir -p %buildroot%_datadir/%name
cp -r themes %buildroot%_datadir/%name

%check
%rust_test

%files
%_bindir/%name
%_datadir/%name
%doc LICENSE

%changelog
* Sun May 31 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.25.0-alt1
- Updated to version 0.25.0.

* Sat Apr 18 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.20.10-alt1
- Initial build for ALT.
