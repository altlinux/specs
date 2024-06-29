%define version_vte 0.76.3
%define version_vte_api 2.91

Name: ptyxis
Version: 46.3
Release: alt1

Summary: Ptyxis is a terminal for GNOME with first-class support for containers
License: GPL-3.0
Group: Terminals

Url: https://gitlab.gnome.org/chergert/ptyxis

Requires: libvte-ptyxis = %EVR

# Source-url: https://gitlab.gnome.org/chergert/ptyxis/-/archive/%version/%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://gitlab.gnome.org/GNOME/vte/-/archive/%version_vte/%version_vte.tar.gz
Source1: vte-%name.tar

ExcludeArch: i586

Patch: vte-0.76.3-alt-bundle-patched-vte.patch
Patch1: vte-0.76.3-alt-drop-unused-dependency.patch

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-systemd

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libportal-gtk4)
BuildRequires: pkgconfig(json-glib-1.0)

# Vte dependency
%define gtk4_ver 4.14
%define glib_ver 2.72.0
%define pango_ver 1.22
%define gir_ver 0.10.2
%define tls_ver 3.2.7
%define pcre_ver 10.21

BuildRequires: gcc-c++ gperf
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk4_ver
BuildRequires: libpango-devel >= %pango_ver
BuildRequires: gobject-introspection-devel >= %gir_ver
BuildRequires: pkgconfig(gnutls) >= %tls_ver
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(libpcre2-8) >= %pcre_ver
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(systemd)
BuildRequires: gobject-introspection-devel >= %gir_ver
BuildRequires: libgtk4-gir-devel
BuildRequires: vala-tools libvala-devel

%description
%summary

%package -n libvte-ptyxis
Summary: Patched for ptyxis terminal emulator widget library for use with GTK+3
Group: System/Libraries

%description -n libvte-ptyxis
%summary

%prep
%setup -a1

# Upstream used own patched vte
%__subst '/dependency('\''vte-2.91-gtk4'\'', version: vte_req)/c\subproject('\''vte'\'').get_variable('\''libvte_gtk4_dep'\''),' src/meson.build

pushd subprojects/vte
%patch -p1
patch -p1 -i ../../build-aux/0001-add-notification-and-shell-precmd-preexec.patch
patch -p1 -i ../../build-aux/0001-a11y-implement-GtkAccessibleText.patch
%patch1 -p1
popd

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome  %name
%find_lang vte-ptyxis-%version_vte_api --output=vte-ptyxis.lang

# Drop unused vte files
rm -vr %buildroot%_includedir
rm -vr %buildroot%_libexecdir/vte-urlencode-cwd
rm -vr %buildroot/etc/profile.d
rm -vr %buildroot%_libexecdir/systemd/
rm -vr %buildroot%_pkgconfigdir
rm -vr %buildroot%_datadir/vala
rm -vr %buildroot%_libdir/girepository-1.0
rm -vr %buildroot%_datadir/gir-1.0
rm -vr %buildroot%_libdir/libvte-ptyxis-%version_vte_api-gtk4.so

%files -f %name.lang
%doc COPYING
%doc README.md
%_bindir/%name
%_libexecdir/%name-agent
%_desktopdir/org.gnome.Ptyxis.desktop
%_datadir/dbus-1/services/org.gnome.Ptyxis.service
%_datadir/glib-2.0/schemas/org.gnome.Ptyxis.gschema.xml
%_iconsdir/hicolor/scalable/apps/org.gnome.Ptyxis*.svg
%_iconsdir/hicolor/symbolic/apps/org.gnome.Ptyxis*.svg
%_datadir/metainfo/org.gnome.Ptyxis.metainfo.xml

%files -n libvte-ptyxis -f vte-ptyxis.lang
%_libdir/libvte-ptyxis-%version_vte_api-gtk4.so.*

%changelog
* Thu Jun 20 2024 Boris Yumankulov <boria138@altlinux.org> 46.3-alt1
- new version 46.3
- add libvte-ptyxis subpackage

* Sun Jun 09 2024 Boris Yumankulov <boria138@altlinux.org> 46.2-alt1
- initial build for ALT Sisyphus

