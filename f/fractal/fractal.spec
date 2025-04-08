Name: fractal
Version: 10.1
Release: alt1
Summary: Matrix messaging app for GNOME written in Rust
License: GPLv3
Group: Networking/Instant messaging
Url: https://gitlab.gnome.org/GNOME/fractal/
Source: https://gitlab.gnome.org/World/fractal/-/archive/10.1/fractal-10.1.tar.gz
Source1: vendor.tar
ExcludeArch: i586 armh

BuildRequires(pre): rpm-build-ninja rpm-build-rust
# Automatically added by buildreq on Mon Oct 30 2023 (-bi)
# optimized out: alt-os-release ca-trust clang17.0 clang17.0-devel clang17.0-support debugedit desktop-file-utils elfutils fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gst-plugins-bad1.0 gst-plugins1.0-devel gstreamer1.0-devel gtk4-update-icon-cache libX11-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libclang-cpp17 libctf-nobfd0 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgraphene-devel libgst-plugins1.0 libgtk4-devel libharfbuzz-devel libjson-glib libp11-kit libpango-devel libsasl2-3 libwayland-client libwayland-client-devel libwayland-egl llvm-common llvm17.0-libs ninja-build pipewire-libs pkg-config python3 python3-base python3-dev python3-module-setuptools rpm-build-file rpm-build-python3 rust sh5 shared-mime-info xml-utils xz
BuildRequires: clang gst-plugins-bad1.0-devel grass-sass libadwaita-devel libappstream-glib libgtk+3-devel libgtksourceview5-devel liblcms2-devel libseccomp-devel libshumate-devel libsqlite3-devel libssl-devel libwebp-devel meson pipewire-libs-devel rust-cargo

BuildRequires: /proc
BuildRequires: cmake xdg-desktop-portal-devel clang-devel

Requires: glycin-loaders gst-plugin-gtk4

%description
Its interface is optimized for collaboration in large groups, such as free
software projects, and will fit all screens, big or small.

Highlights:

* Find rooms to discuss your favorite topics, or talk privately to people,
  securely thanks to end-to-end encryption
* Send rich formatted messages, files, or your current location
* Reply to specific messages, react with emoji, edit or remove messages
* View images, and play audio and video directly in the conversation
* See who has read messages, and who is typing
* Log into multiple accounts at once (with Single-Sign On support)

%prep
%setup
tar xf %SOURCE1

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
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
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml

%changelog
* Sat Mar 15 2025 Ildar Mulyukov <ildar@altlinux.ru> 10.1-alt1
- new version

* Sat May 25 2024 Ildar Mulyukov <ildar@altlinux.ru> 7-alt1
- new version

* Thu Nov 16 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 5.beta2-alt2
- NMU: fixed FTBFS on LoongArch

* Mon Oct 30 2023 Ildar Mulyukov <ildar@altlinux.ru> 5.beta2-alt1
- new version

* Wed Feb 02 2022 Ildar Mulyukov <ildar@altlinux.ru> 4.4.1b1-alt1
- Initial build for Sisyphus
