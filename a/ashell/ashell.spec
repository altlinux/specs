Name: ashell
Version: 0.4.1
Release: alt1
License: MIT

Summary: A ready to go Wayland status bar for Hyprland

Group: Graphical desktop/Other

Url: https://github.com/MalpenZibo/ashell
Vcs: https://github.com/MalpenZibo/ashell.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust clang-devel
BuildRequires: /proc

BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libudev)

%description
%summary.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml
subst 's|"rfkill"|"%_sbindir/rfkill"|' src/services/bluetooth/mod.rs

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name

%changelog
* Sun Mar 16 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.4.1-alt1
- new version (0.4.1) with rpmgs script

* Wed Jan 22 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.4.0-alt1
- new version (0.4.0) with rpmgs script
- re-drop Requires: fonts-ttf-symbols-nerd
- The Cargo config is moved to a separate file.
- spec: add vcs

* Fri Dec 13 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.3.1-alt1
- new version 0.3.1 (with rpmrb script)

* Thu Nov 28 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.3.0-alt1
- new version (0.3.0) with rpmgs script

* Fri Nov 08 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- new version (0.2.0) with rpmgs script
- restore requires on fonts-ttf-symbols-nerd (upstream bug)

* Tue Nov 05 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.5-alt1
- new version (0.1.5) with rpmgs script
- drop requires on fonts-ttf-symbols-nerd

* Sun Oct 27 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.4-alt1
- Initial build
