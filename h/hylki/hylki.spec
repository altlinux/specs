%define _unpackaged_files_terminate_build 1
%define app_id co.hyprlab.Hylki
# Keep peak memory bounded for the large GTK4 application crate.
%define rust_lto "off"
%define rust_codegen_units 16
%define rust_debug "limited"

Name: hylki
Version: 1.47.1
Release: alt1

Summary: GNOME email client with IMAP, POP3 and JMAP support

License: AGPL-3.0-or-later
Group: Networking/Mail
Url: https://github.com/hyprlab/hylki

# rustc runs out of the 32-bit address space building the main crate
ExcludeArch: %ix86

# Source-url: https://github.com/hyprlab/hylki/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: gcc-c++ gettext-tools
BuildRequires: pkgconfig(gtk4) >= 4.14
BuildRequires: pkgconfig(libadwaita-1) >= 1.7
BuildRequires: pkgconfig(webkitgtk-6.0) >= 2.44
BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: glib2-devel
# The PDF footer test needs an actual Sans font for Pango/Cairo.
BuildRequires: fonts-ttf-dejavu

%description
Hylki is a GNOME email client built with Rust, GTK4 and libadwaita.
It supports multiple IMAP, POP3 and JMAP accounts, OAuth authentication,
full-text search, rich-text composition and OpenPGP integration.
Passwords and OAuth tokens are stored using the desktop Secret Service.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
%rust_build
for po in po/*.po; do
    lang=$(basename "$po" .po)
    mkdir -p "locale/$lang/LC_MESSAGES"
    msgfmt -o "locale/$lang/LC_MESSAGES/%name.mo" "$po"
done
msgfmt --desktop --template=data/%app_id.desktop -d po -o %app_id.desktop
msgfmt --xml --template=data/%app_id.metainfo.xml -d po -o %app_id.metainfo.xml

%install
%rust_install
install -Dm644 %app_id.desktop %buildroot%_desktopdir/%app_id.desktop
install -Dm644 %app_id.metainfo.xml %buildroot%_datadir/metainfo/%app_id.metainfo.xml
for size in 256x256 512x512; do
    install -Dm644 data/icons/hicolor/$size/apps/%app_id.png \
        %buildroot%_iconsdir/hicolor/$size/apps/%app_id.png
done
install -Dm644 data/icons/hicolor/scalable/apps/%app_id.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/%app_id.svg
install -Dm644 data/icons/hicolor/symbolic/apps/%app_id-symbolic.svg \
    %buildroot%_iconsdir/hicolor/symbolic/apps/%app_id-symbolic.svg
cp -a locale %buildroot%_datadir/
%find_lang %name

%check
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
export XDG_CONFIG_HOME="$PWD/test-home/config"
export XDG_DATA_HOME="$PWD/test-home/data"
export XDG_CACHE_HOME="$PWD/test-home/cache"
export XDG_STATE_HOME="$PWD/test-home/state"
mkdir -p "$XDG_CONFIG_HOME" "$XDG_DATA_HOME" "$XDG_CACHE_HOME" "$XDG_STATE_HOME"
%rust_test -- --test-threads=1

%files -f %name.lang
%doc README.md LICENSE
%_bindir/%name
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%{app_id}*

%changelog
* Sun Nov 08 2026 Vitaly Lipatov <lav@altlinux.ru> 1.47.1-alt1
- initial build for Sisyphus.

