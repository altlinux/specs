%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define xdg_name org.gnome.Papers

Name: papers
Version: 50.2
Release: alt1

Summary: A document viewer for PDF and other document formats aimed at the GNOME desktop
License: GPL-2.0
Group: Office
Url: https://welcome.gnome.org/app/Papers/
Vcs: https://gitlab.gnome.org/GNOME/papers

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: gi-docgen
BuildRequires: itstool
BuildRequires: appstream
BuildRequires: blueprint-compiler
BuildRequires: gobject-introspection-devel
BuildRequires: libgtk4-gir-devel
BuildRequires: pkgconfig(ddjvuapi)
BuildRequires: pkgconfig(exempi-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libnautilus-extension-4)
BuildRequires: pkgconfig(libspelling-1)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(sysprof-capture-4)

%description
Papers is a document viewer capable of displaying multiple and single
page document formats like PDF and Postscript.

%package doc
Summary: Documentation files for Papers
Group: Documentation
BuildArch: noarch
Requires: %name = %EVR

%description doc
%summary.

%package devel
Summary: Development files for Papers
Group: Development/GNOME and GTK+
Requires: %name = %EVR

%description devel
%summary.

%package gir
Summary: GObject instrospection data for Papers
Group: System/Libraries
Requires: %name = %EVR

%description gir
%summary.

%package gir-devel
Summary: GObject introspection devel data for Papers
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR

%description gir-devel
%summary.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson -Dshell=true \
       -Dpreviewer=true \
       -Dthumbnailer=true \
       -Dnautilus=true \
       -Dcomics=enabled \
       -Ddjvu=enabled \
       -Dpdf=enabled \
       -Dtiff=enabled \
       -Dtests=false \
       -Ddocumentation=true \
       -Duser_doc=true \
       -Dintrospection=enabled \
       -Dsysprof=enabled \
       -Dkeyring=enabled \
       -Dgtk_unix_print=enabled \
       -Dspell_check=enabled
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
%_datadir/metainfo/%xdg_name.*.metainfo.xml
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
* Wed Jul 01 2026 Anton Zhukharev <ancieg@altlinux.org> 50.2-alt1
- Updated to 50.2.

* Tue Mar 17 2026 Anton Zhukharev <ancieg@altlinux.org> 50.0-alt1
- Updated to 50.0.

* Tue Feb 24 2026 Anton Zhukharev <ancieg@altlinux.org> 49.4-alt1
- Updated to 49.4.

* Mon Jan 12 2026 Anton Zhukharev <ancieg@altlinux.org> 49.3-alt1
- Updated to 49.3.

* Mon Dec 22 2025 Anton Zhukharev <ancieg@altlinux.org> 49.2-alt1
- Updated to 49.2.

* Wed Jul 23 2025 Anton Zhukharev <ancieg@altlinux.org> 48.5-alt1
- Updated to 48.5.

* Mon Jun 23 2025 Anton Zhukharev <ancieg@altlinux.org> 48.4-alt1
- Updated to 48.4.

* Mon May 26 2025 Anton Zhukharev <ancieg@altlinux.org> 48.3-alt1
- Updated to 48.3.

* Thu Apr 24 2025 Anton Zhukharev <ancieg@altlinux.org> 48.2-alt1
- Updated to 48.2.

* Thu Mar 20 2025 Anton Zhukharev <ancieg@altlinux.org> 48.0-alt1
- Updated to 48.0.

* Tue Mar 11 2025 Anton Zhukharev <ancieg@altlinux.org> 47.4-alt1
- Updated to 47.4.

* Mon Feb 03 2025 Anton Zhukharev <ancieg@altlinux.org> 47.3-alt1
- Updated to 47.3.

* Mon Sep 23 2024 Anton Zhukharev <ancieg@altlinux.org> 47.0-alt2
- Fixed value of the group tag (closes 51526).

* Fri Sep 20 2024 Anton Zhukharev <ancieg@altlinux.org> 47.0-alt1
- Updated to 47.0.

* Tue Sep 17 2024 Anton Zhukharev <ancieg@altlinux.org> 46.2-alt1
- Built for ALT Sisyphus.

