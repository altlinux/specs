Name: ashell
Version: 0.3.0
Release: alt1
License: MIT

Summary: A ready to go Wayland status bar for Hyprland

Group: Graphical desktop/Other

Url: https://github.com/MalpenZibo/ashell

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust clang-devel
BuildRequires: /proc

BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(dbus-1)

Requires: fonts-ttf-symbols-nerd

%description
%summary.

%prep
%setup -a1

mkdir -p .cargo
cat <<EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/MalpenZibo/hyprland-rs"]
git = "https://github.com/MalpenZibo/hyprland-rs"
replace-with = "vendored-sources"

[source."git+https://github.com/MalpenZibo/iced_sctk"]
git = "https://github.com/MalpenZibo/iced_sctk"
replace-with = "vendored-sources"

[source."git+https://github.com/Smithay/client-toolkit?rev=3bed072"]
git = "https://github.com/Smithay/client-toolkit"
rev = "3bed072"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/smithay-clipboard?tag=pop-dnd-4"]
git = "https://github.com/pop-os/smithay-clipboard"
tag = "pop-dnd-4"
replace-with = "vendored-sources"

[source."git+https://github.com/pop-os/window_clipboard.git?tag=pop-dnd-6"]
git = "https://github.com/pop-os/window_clipboard.git"
tag = "pop-dnd-6"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name

%changelog
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
