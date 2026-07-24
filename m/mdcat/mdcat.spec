%global _unpackaged_files_terminate_build 1
%def_with check

Name: mdcat
Version: 2.13.0
Release: alt1
Summary: cat for markdown
License: MPL-2.0
Group: Text tools
URL: https://crates.io/crates/mdcat
VCS: https://github.com/BIRSAx2/mdcat

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(openssl)

%description
Fancy cat for Markdown.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name

%changelog
* Fri Jul 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 2.13.0-alt1
- Initial build for ALT.
