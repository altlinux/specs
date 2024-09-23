%define _unpackaged_files_terminate_build 1
%define xdg_name org.gnome.Papers

Name: papers
Version: 47.0
Release: alt2

Summary: A document viewer for PDF and other document formats aimed at the GNOME desktop
License: GPL-2.0
Group: Office
Url: https://welcome.gnome.org/app/Papers/
VCS: https://gitlab.gnome.org/GNOME/Incubator/papers

Source0: %name-%version.tar
Source1: %name-%version-shell-rs-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: rust-cargo
BuildRequires: rustfmt
BuildRequires: clippy
BuildRequires: gi-docgen
BuildRequires: itstool
BuildRequires: appstream
BuildRequires: libgtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libgtk4-gir-devel
BuildRequires: libadwaita-gir-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: sysprof-devel
BuildRequires: libexempi-devel
BuildRequires: libdbus-devel
BuildRequires: libnautilus-devel
BuildRequires: libpoppler-glib-devel
BuildRequires: libdjvu-devel
BuildRequires: libtiff-devel
BuildRequires: libgxps-devel
BuildRequires: libspectre-devel
BuildRequires: libarchive-devel

%description
Papers is a document viewer capable of displaying multiple and single
page document formats like PDF and Postscript.

%package doc
Summary: Documentation files for Papers
Group: Documentation
Requires: %name = %EVR

%description doc
%{summary doc}

%package devel
Summary: Development files for Papers
Group: Development/GNOME and GTK+
Requires: %name = %EVR

%description devel
%{summary devel}

%package gir
Summary: GObject instrospection data for Papers
Group: System/Libraries
Requires: %name = %EVR

%description gir
%{summary gir}

%package gir-devel
Summary: GObject introspection devel data for Papers
Group: System/Libraries
Requires: %name-gir = %EVR

%description gir-devel
%{summary gir-devel}

%prep
%setup -a1
%autopatch -p1

%build
%meson
%meson_build -v

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%doc README.md
%_bindir/papers
%_bindir/papers-*
%_desktopdir/*.desktop
%_libdir/*.so.*
%_libdir/%name/
%_libdir/nautilus/extensions-4/libpapers-document-properties.so
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%xdg_name.svg
%_iconsdir/hicolor/*/apps/%xdg_name-symbolic.svg
%_datadir/thumbnailers/%name.thumbnailer
%_datadir/metainfo/%xdg_name.metainfo.xml
%_datadir/metainfo/%name-*.metainfo.xml
%_man1dir/*.1.*

%files doc
%_docdir/libppsdocument/
%_docdir/libppsview/

%files devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*.pc

%files gir
%_libdir/girepository-1.0/*.typelib

%files gir-devel
%_datadir/gir-1.0/*.gir

%changelog
* Mon Sep 23 2024 Anton Zhukharev <ancieg@altlinux.org> 47.0-alt2
- Fixed value of the group tag (closes 51526).

* Fri Sep 20 2024 Anton Zhukharev <ancieg@altlinux.org> 47.0-alt1
- Updated to 47.0.

* Tue Sep 17 2024 Anton Zhukharev <ancieg@altlinux.org> 46.2-alt1
- Built for ALT Sisyphus.

