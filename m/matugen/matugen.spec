%global _unpackaged_files_terminate_build 1

Name: matugen
Version: 4.0.0
Release: alt1
Summary: A material you color generation tool
License: GPL-2.0
Group: Other
Url: https://crates.io/crates/matugen
VCS: https://github.com/InioX/matugen

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
A material you color generation tool with templates.

%prep
%setup -a 1
echo >> .cargo/config.toml
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name
%doc LICENSE

%changelog
* Wed Mar 11 2026 Vladislav Eliseev <general@altlinux.org> 4.0.0-alt1
- Updated to version 4.0.0.

* Thu Dec 11 2025 Vladislav Eliseev <general@altlinux.org> 3.1.0-alt1
- Updated to version 3.1.0.

* Sat Nov 08 2025 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.0-alt1
- Updated to version 3.0.0.

* Thu Jul 24 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.1-alt1
- Initial build for ALT.
