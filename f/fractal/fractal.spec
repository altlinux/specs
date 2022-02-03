Name: fractal
Version: 4.4.1b1
Release: alt1
Summary: Matrix messaging app for GNOME written in Rust
License: GPL3
Group: Other
Url: https://gitlab.gnome.org/GNOME/fractal/
Source: %name-%version.tar
Source1: vendor.tar
Source2: liblmdb.pc
ExcludeArch: i586 armh

BuildRequires(pre): rpm-build-ninja rpm-build-rust
# optimized out: at-spi2-atk ca-trust cmake-modules fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gst-plugins-bad1.0 gst-plugins1.0-devel gstreamer1.0-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libenchant2-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgst-plugins1.0 libgtk+3-devel libharfbuzz-devel libjson-glib libpango-devel libsasl2-3 libstdc++-devel libwayland-client libwayland-cursor libwayland-egl llvm12.0-libs ninja-build pkg-config python3 python3-base rust sh4 shared-mime-info xml-utils xz
BuildRequires: cmake desktop-file-utils gcc-c++ gst-plugins-bad1.0-devel libappstream-glib libgspell-devel libgtksourceview4-devel libhandy1-devel libssl-devel meson

BuildRequires: /proc
BuildRequires: libdbus-devel libges-devel liblmdb-devel libolm-devel

%description
Its interface is optimized for collaboration in large groups, such as free
software projects.

* Come to talk to us on Matrix: <https://matrix.to/#/#fractal:gnome.org>
* Main repository: <https://gitlab.gnome.org/GNOME/fractal/>

%prep
%setup
tar xf %SOURCE1
subst 's/dead_code,//' fractal-gtk/src/main.rs
mkdir -p .cargo
cat >> .cargo/config <<EOF
[target.x86_64-unknown-linux-gnu.fractal-gtk]
rustc-link-lib = ["lmdb","olm"]

[source.crates-io]
replace-with = "vendored-sources"

[source."https://github.com/danigm/gettext-rs"]
git = "https://github.com/danigm/gettext-rs"
branch = "no-gettext"
replace-with = "vendored-sources"

[source."https://github.com/matrix-org/matrix-rust-sdk.git"]
git = "https://github.com/matrix-org/matrix-rust-sdk.git"
rev = "ebcb2024d14614b8c984c5b95de5df04eec7933b"
replace-with = "vendored-sources"

[source."https://github.com/ruma/ruma"]
git = "https://github.com/ruma/ruma"
rev = "e2728a70812412aade9322f6ad832731978a4240"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
export NPROCS=4
export OLM_LINK_VARIANT=dylib
export PKG_CONFIG_PATH=`dirname %SOURCE2`
%meson \

%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%rust_test

%files -f %name.lang
%doc *.md
%_bindir/*
%_desktopdir/*.desktop
%_datadir/%name
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml

%changelog
* Wed Feb 02 2022 Ildar Mulyukov <ildar@altlinux.ru> 4.4.1b1-alt1
- Initial build for Sisyphus
