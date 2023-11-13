Name: fractal
Version: 5.beta2
Release: alt1
Summary: Matrix messaging app for GNOME written in Rust
License: GPL3
Group: Networking/Instant messaging
Url: https://gitlab.gnome.org/GNOME/fractal/
Source: %name-%version.tar
Source1: vendor.tar
ExcludeArch: i586 armh

BuildRequires(pre): rpm-build-ninja rpm-build-rust
# Automatically added by buildreq on Mon Oct 30 2023 (-bi)
# optimized out: alt-os-release ca-trust clang17.0 clang17.0-devel clang17.0-support debugedit desktop-file-utils elfutils fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gst-plugins-bad1.0 gst-plugins1.0-devel gstreamer1.0-devel gtk4-update-icon-cache libX11-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libclang-cpp17 libctf-nobfd0 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgraphene-devel libgst-plugins1.0 libgtk4-devel libharfbuzz-devel libjson-glib libp11-kit libpango-devel libsasl2-3 libwayland-client libwayland-client-devel libwayland-egl llvm-common llvm17.0-libs ninja-build pipewire-libs pkg-config python3 python3-base python3-dev python3-module-setuptools rpm-build-file rpm-build-python3 rust sh5 shared-mime-info xml-utils xz
BuildRequires: clang gst-plugins-bad1.0-devel libadwaita-devel libappstream-glib libgtk+3-devel libgtksourceview5-devel libshumate-devel libsqlite3-devel libssl-devel meson pipewire-libs-devel rust-cargo

BuildRequires: /proc
BuildRequires: cmake xdg-desktop-portal-devel clang-devel

%description
Its interface is optimized for collaboration in large groups, such as free
software projects.

* Come to talk to us on Matrix: <https://matrix.to/#/#fractal:gnome.org>
* Main repository: <https://gitlab.gnome.org/GNOME/fractal/>

%prep
%setup
tar xf %SOURCE1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/dalek-cryptography/curve25519-dalek/?rev=e44d4b5903106dde0e5b28a2580061de7dfe8a9f"]
git = "https://github.com/dalek-cryptography/curve25519-dalek/"
rev = "e44d4b5903106dde0e5b28a2580061de7dfe8a9f"
replace-with = "vendored-sources"

[source."git+https://github.com/matrix-org/matrix-rust-sdk.git?rev=4643bae28445e058080896a280083b32fd403146"]
git = "https://github.com/matrix-org/matrix-rust-sdk.git"
rev = "4643bae28445e058080896a280083b32fd403146"
replace-with = "vendored-sources"

[source."git+https://github.com/matrix-org/vodozemac/?rev=e3b658526f6f1dd0a9065c1c96346b796712c425"]
git = "https://github.com/matrix-org/vodozemac/"
rev = "e3b658526f6f1dd0a9065c1c96346b796712c425"
replace-with = "vendored-sources"

[source."git+https://github.com/ruma/ruma.git?rev=f1772ae5bc1d849655498f51b0fec7b0ef10e339"]
git = "https://github.com/ruma/ruma.git"
rev = "f1772ae5bc1d849655498f51b0fec7b0ef10e339"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
%meson \

#%%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
# rebuild is too long
#%%rust_test

%files -f %name.lang
%doc *.md
%_bindir/*
%_desktopdir/*.desktop
%_datadir/%name
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml

%changelog
* Mon Oct 30 2023 Ildar Mulyukov <ildar@altlinux.ru> 5.beta2-alt1
- new version

* Wed Feb 02 2022 Ildar Mulyukov <ildar@altlinux.ru> 4.4.1b1-alt1
- Initial build for Sisyphus
