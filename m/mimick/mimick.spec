%global _unpackaged_files_terminate_build 1
%global namespace dev.nicx.mimick
%def_with check

Name: mimick
Version: 9.9.0
Release: alt1
Summary: Immich Desktop Client for Linux
License: GPL-3.0-or-later
Group: Graphics
URL: https://mimick.nicx.dev
VCS: https://github.com/nicx17/mimick

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libheif)
BuildRequires: pkgconfig(pango)

%if_with check
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
%endif

%description
Mimick is an unofficial Immich desktop client for Linux.
It provides a GTK4/libadwaita interface for automatic background
sync of local photo and video folders to a self-hosted Immich server,
and an optional library browser for viewing, searching, and managing
assets directly from the desktop.

%prep
%setup -a1
%rust_prep

%build
%ifarch i586
export CARGO_PROFILE_RELEASE_LTO=false
%endif
%rust_build

%install
%rust_install
install -Dm644 setup/%namespace.desktop \
    %buildroot%_desktopdir/%namespace.desktop
install -Dm644 setup/metainfo/%namespace.metainfo.xml \
    %buildroot%_datadir/metainfo/%namespace.metainfo.xml
install -Dm644 src/assets/scalable/apps/%namespace.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/%namespace.svg

%check
# `tempfile` inherits TMPDIR.  The default RPM build temp directory can return
# invalid descriptors for NamedTempFile, so keep test fixtures inside the
# build tree instead.
mkdir -p .tmp
export TMPDIR="$PWD/.tmp"
%rust_test
desktop-file-validate %buildroot%_desktopdir/%namespace.desktop
appstream-util validate-relax --nonet \
    %buildroot%_datadir/metainfo/%namespace.metainfo.xml

%files
%_bindir/%name
%_desktopdir/%namespace.desktop
%_datadir/metainfo/%namespace.metainfo.xml
%_iconsdir/hicolor/scalable/apps/%namespace.svg
%doc LICENSE THIRD_PARTY_LICENSES.txt THIRD_PARTY_LICENSES_SUMMARY.txt

%changelog
* Mon Aug 17 2026 Alexander Makeenkov <amakeenk@altlinux.org> 9.9.0-alt1
- Initial build for ALT.
