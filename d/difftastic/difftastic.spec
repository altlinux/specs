%define _unpackaged_files_terminate_build 1
%global bin_name difft

Name: difftastic
Version: 0.69.0
Release: alt1

Summary: A structural diff that understands syntax
License: MIT
Group: File tools
URL: https://difftastic.wilfred.me.uk
Vcs: https://github.com/Wilfred/difftastic

Source: %name-%version.tar
Source1: vendor.tar
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: gcc-c++

%description
Difftastic is a structural diff tool that compares files based on their syntax.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install %bin_name

%check
%rust_test

%files
%doc LICENSE
%doc README.md
%_bindir/%bin_name

%changelog
* Fri May 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.69.0-alt1
- Updated to version 0.69.0.

* Wed Apr 15 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.68.0-alt1
- Updated to version 0.68.0.

* Wed Nov 26 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.67.0-alt1
- Updated to version 0.67.0.

* Tue Jul 17 2023 Michael Chernigin <chernigin@altlinux.org> 0.47.0-alt1
- Update to b6895d42 from upstream, branch master
- Initial build for ALT Linux

