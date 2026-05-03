%global _unpackaged_files_terminate_build 1

Name: matugen
Version: 4.1.0
Release: alt1
Summary: A cross-platform material you and base16 color generation tool
License: GPL-2.0
Group: Other
Url: https://crates.io/crates/matugen
VCS: https://github.com/InioX/matugen

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
A cross-platform material you and base16 color generation tool.
Features:
- Templating engine built with Chumsky (designed for colors)
- Generate / Export Material You and base16 color palettes
- Keyword Filters
- Custom Keywords / Colors
- Palette Customization

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
* Sun May 03 2026 Alexander Makeenkov <amakeenk@altlinux.org> 4.1.0-alt1
- Updated to version 4.1.0.

* Wed Mar 11 2026 Vladislav Eliseev <general@altlinux.org> 4.0.0-alt1
- Updated to version 4.0.0.

* Thu Dec 11 2025 Vladislav Eliseev <general@altlinux.org> 3.1.0-alt1
- Updated to version 3.1.0.

* Sat Nov 08 2025 Alexander Makeenkov <amakeenk@altlinux.org> 3.0.0-alt1
- Updated to version 3.0.0.

* Thu Jul 24 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.1-alt1
- Initial build for ALT.
