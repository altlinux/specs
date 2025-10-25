Name: hyprland-per-window-layout
Version: 2.17
Release: alt1
Summary: Hyprland per window layout
License: MIT
Group: Graphical desktop/Other
Url: https://aur.archlinux.org/packages/hyprland-per-window-layout

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Per window keyboard layout (language) for Hyprland wayland compositor.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name
%doc LICENSE

%changelog
* Sat Oct 25 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.17-alt1
- Updated to version 2.17.

* Thu Aug 14 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.15-alt1
- Updated to version 2.15.

* Wed Jul 16 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.14-alt1
- Updated to version 2.14.

* Mon Jul 07 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.13-alt1
- Initial build for ALT.
