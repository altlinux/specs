%define cargo_prep %nil
%define cargo_build %rust_build
%define cargo_install %rust_install

%define appid io.github.lgse.Strata

Name: strata
Version: 1.0.0
Release: alt1

Summary: A fast, keyboard-first GTK4 file manager

License: MIT
Group: File tools
Url: https://github.com/lgse/strata

ExcludeArch: %ix86

# Source-url: https://github.com/lgse/strata/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: pkgconfig(gtk4) pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(poppler-glib) pkgconfig(fontconfig)
BuildRequires: pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0) pkgconfig(cairo)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: /usr/bin/glib-compile-resources
BuildRequires: desktop-file-utils
# tests (ffmpeg media fixtures, sans-serif rendering)
BuildRequires: ffmpeg /usr/bin/ffprobe ffmpegthumbnailer fonts-ttf-dejavu bubblewrap

# every preview and thumbnail renderer runs under bubblewrap (started by name)
Requires: /usr/bin/bwrap
# video previews spawn ffmpeg and ffprobe by name
Requires: /usr/bin/ffmpeg /usr/bin/ffprobe
# remote locations (SMB, SFTP) through GIO
Requires: gvfs

%description
Strata is a keyboard-first file manager for GTK4 desktops with Wayland
as the primary display stack. It combines Miller-column navigation with
Icons and List views, instant fuzzy filename search, previews of text,
Markdown, images, PDF, audio and video (rendered in a bubblewrap sandbox),
GIO/GVfs remote locations and custom context menu actions.

Optional helpers: RAW previews use ImageMagick or libraw, AppImage icons
need squashfs-tools, video thumbnails use ffmpegthumbnailer.

This build does not include the non-free UnRAR code (no RAR extraction)
and does not install the org.freedesktop.FileManager1 D-Bus service
template as an active system service.

%prep
%setup -a1
%cargo_prep
install -vD %SOURCE2 .cargo/config.toml

%build
# upstream full LTO with one codegen unit needs >12 GB RAM for the final rustc
export CARGO_PROFILE_RELEASE_LTO=off
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=16
# the default "rar" feature embeds RARLAB's non-free UnRAR code
%cargo_build --no-default-features

%install
%cargo_install
install -Dm0644 data/%appid.desktop %buildroot%_desktopdir/%appid.desktop
install -Dm0644 data/icons/scalable/apps/%appid.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/%appid.svg
# inactive template, users may opt in per user (see README)
install -Dm0644 data/%appid.FileManager1.service \
    %buildroot%_datadir/%name/%appid.FileManager1.service
# tell the in-app updater that the binary is owned by the package manager
install -Dm0644 /dev/stdin %buildroot%_datadir/%name/install-source.toml <<'MARKER'
manager = "apt-get"
package = "strata"
channel = "stable"
update_command = "apt-get update && apt-get install strata"
MARKER

%check
desktop-file-validate %buildroot%_desktopdir/%appid.desktop
# skipped: tests of the user-owned executable path/portal setup, trash and
# file operations that need a real home/trash; one media test that panics
# without a GTK display (no skip guard upstream)
env -u DISPLAY -u WAYLAND_DISPLAY GDK_BACKEND=x11 \
%rust_test --no-default-features -- \
    --skip portal_setup:: --skip services::file_providers:: \
    --skip adapters::local_operations:: --skip adapters::local_jobs:: \
    --skip adapters::trash_restore:: --skip adapters::local_files:: \
    --skip ui::media::tests::reopening_resumes_where_the_preview_closed

%files
%doc README.md LICENSE THIRD_PARTY_LICENSES.md
%_bindir/%name
%_desktopdir/%appid.desktop
%_iconsdir/hicolor/scalable/apps/%appid.svg
%_datadir/%name/

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for Sisyphus
