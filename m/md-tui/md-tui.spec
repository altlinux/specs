%global _unpackaged_files_terminate_build 1
%global bin_name mdt

Name: md-tui
Version: 0.10.1
Release: alt1
Summary: Markdown renderer in the terminal
License: AGPL-3.0
Group: File tools
Url: https://crates.io/crates/md-tui
VCS: https://github.com/henriklovhaug/md-tui

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
TUI application for viewing markdown files directly in your terminal.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install %bin_name

%files
%_bindir/%bin_name
%doc LICENSE

%changelog
* Fri Jun 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.10.1-alt1
- Updated to version 0.10.1.

* Sat May 09 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.10.0-alt1
- Updated to version 0.10.0.

* Thu Mar 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.5-alt1
- Updated to version 0.9.5.

* Sun Mar 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.4-alt1
- Updated to version 0.9.4.

* Sun Nov 30 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.1-alt1
- Initial build for ALT.

