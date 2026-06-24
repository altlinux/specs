%global _unpackaged_files_terminate_build 1

Name: tuckr
Version: 0.13.1
Release: alt1
Summary: A super powered replacement for GNU Stow
License: GPL-3.0
Group: System/Configuration/Other
URL: https://raphgl.github.io/Tuckr
VCS: https://github.com/RaphGL/Tuckr

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Tuckr is a dotfile manager inspired by Stow and Git.
Tuckr aims to make dotfile management less painful.
It follows the same model as Stow, symlinking files onto $HOME.

%prep
%setup -a 1
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
* Wed Jun 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.13.1-alt1
- Initial build for ALT.
