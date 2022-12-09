Name: kooha
Version: 2.2.2
Release: alt1

Summary: Simple screen recorder with a minimal interface

License: GPL-3.0+
Group: Video
Url: https://github.com/SeaDve/Kooha

Source: %url/archive/%version/Kooha-%version.tar.gz
Source1: vendor.tar

BuildPreReq: rpm-macros-meson rpm-build-rust
BuildRequires: /proc
BuildRequires: meson glib2-devel libgio-devel libgtk4-devel libadwaita-devel gstreamer1.0-devel gst-plugins1.0-devel libpulseaudio-devel /usr/bin/appstream-util

%description
%summary.

%prep
%setup -n Kooha-%version
# Unpacked vendor/ into the source (used .gear/tags).
tar -xf %SOURCE1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

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
%find_lang %name

%files -f %name.lang
%doc COPYING README.md
%_bindir/%name
%_desktopdir/io.github.seadve.Kooha.desktop
%_datadir/glib-2.0/schemas/io.github.seadve.Kooha.gschema.xml
%_iconsdir/hicolor/scalable/apps/io.github.seadve.Kooha.svg
%_iconsdir/hicolor/symbolic/apps/io.github.seadve.Kooha-symbolic.svg
%dir %_datadir/%name/
%_datadir/%name/resources.gresource
%_datadir/metainfo/io.github.seadve.Kooha.metainfo.xml
%_datadir/locale/zh_Hans/LC_MESSAGES/%name.mo
%_datadir/locale/zh_Hant/LC_MESSAGES/%name.mo

%changelog
* Fri Dec 09 2022 Leontiy Volodin <lvol@altlinux.org> 2.2.2-alt1
- Initial build for ALT Sisyphus.
