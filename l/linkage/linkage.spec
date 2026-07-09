%define _unpackaged_files_terminate_build 1

Name: linkage
Version: 0.3.3
Release: alt1

Summary: Desktop typing tutor, written in Rust
License: MIT
Group: Education
Url: https://github.com/linkage-rs/linkage
Vcs: https://github.com/linkage-rs/linkage.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Desktop typing tutor, written in Rust.

%prep
%setup -a1
%rust_prep

%build
export RUSTFLAGS="-Copt-level=3"
%rust_build

%install
%rust_install linkage

%check
%rust_test

%files
%doc LICENSE README.md
%_bindir/linkage

%changelog
* Tue Jul 07 2026 Mikhail Nogin <joycap@altlinux.org> 0.3.3-alt1
- Initial built for Sisyphus.
