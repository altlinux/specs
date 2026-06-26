%define _unpackaged_files_terminate_build 1
%define app_id me.fouquet.Stencil

Name: stencil
Version: 1.2.0
Release: alt1

Summary: A batch file renaming utility for GNOME.
License: GPL-3.0-or-later
Group: File tools
Url: https://codeberg.org/fouquet/Stencil
Vcs: https://codeberg.org/fouquet/Stencil

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libadwaita-1) >= 1.8

%description
Stencil lets you build a rename queue from stackable operations and preview
every result live before renaming anything. Queues can be saved as presets,
exported and imported as JSON, and any rename can be undone.

%prep
%setup -a1
mkdir -pv .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/stencil
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_iconsdir/hicolor/scalable/apps/%app_id.svg

%changelog
* Fri Jun 26 2026 Pavel Mitrofanov <cobalt@altlinux.org> 1.2.0-alt1
- Initial commit.
