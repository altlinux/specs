%def_disable snapshot
%define _name gtksourceview
%define ver_major 5.14
%define api_ver 5

%def_disable static
%def_disable doc
%def_enable introspection
%def_enable vala
%def_enable installed_tests

%ifarch armh
%def_disable check
%else
%def_enable check
%endif

%ifarch %valgrind_arches
%def_enable valgrind
%endif

Name: lib%{_name}%api_ver
Version: %ver_major.1
Release: alt1

Summary: GtkSourceView text widget library
License: LGPLv2+
Group: System/Libraries
Url: https://wiki.gnome.org/Projects/GtkSourceView

%if_disabled snapshot
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define glib_ver 2.72
%define gtk_ver 4.6
%define pcre2_ver 10.21
%define libxml2_ver 2.6.0
%define fribidi_ver 0.19.7

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-gir rpm-macros-valgrind
BuildRequires: meson gcc-c++ itstool
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk4-devel >= %gtk_ver
BuildRequires: libpcre2-devel >= %pcre2_ver
BuildRequires: libxml2-devel >= %libxml2_ver
BuildRequires: libfribidi-devel >= %fribidi_ver
BuildRequires: perl-XML-Parser zlib-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk4-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools libvala-devel}
%{?_enable_doc:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: dbus xvfb-run %{?_enable_valgrind:valgrind}
BuildRequires: fonts-ttf-roboto}

%description
GtkSourceView is a text widget that extends the standard gtk+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package contains shared GtkSourceView library.

%package devel
Summary: Files to compile applications that use GtkSourceView
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the files required to develop applications against
the GtkSourceView library.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
GtkSourceView is a text widget that extends the standard gtk+ 3.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package provides development documentation for %_name.

%package gir
Summary: GObject introspection data for the GtkSourceView library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the GtkSourceView library

%package gir-devel
Summary: GObject introspection devel data for the GtkSourceView library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the GtkSourceView library

%package tests
Summary: Tests for the GtkSourceView library
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed GtkSourceView library.

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -n %_name-%version

%build
%meson \
    %{?_enable_doc:-Ddocumentation=true} \
    %{?_disable_introspection:-Dgir=false} \
    %{?_disable_vala:-Dvapi=false} \
    %{?_enable_installed_tests:-Dinstall-tests=true}
%nil
%meson_build

%install
%meson_install
%find_lang %_name-%api_ver

%check
export GTK_A11Y=none
dbus-run-session xvfb-run %__meson_test

%files -f %_name-%api_ver.lang
%_libdir/lib%_name-%api_ver.so.*
%_datadir/%_name-%api_ver/
%_iconsdir/hicolor/scalable/actions/*.svg
%doc AUTHORS NEWS README*

%files devel
%_includedir/%_name-%api_ver/
%_libdir/lib%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%if_enabled vala
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi
%endif
%doc HACKING

%if_enabled doc
%files devel-doc
%_datadir/doc/%_name-%api_ver/
%endif

%if_enabled introspection
%files gir
%_typelibdir/GtkSource-%api_ver.typelib

%files gir-devel
%_girdir/GtkSource-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_bindir/%_name%api_ver-widget
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Sat Oct 05 2024 Yuri N. Sedunov <aris@altlinux.org> 5.14.1-alt1
- 5.14.1

* Sat Sep 14 2024 Yuri N. Sedunov <aris@altlinux.org> 5.14.0-alt1
- 5.14.0

* Fri May 31 2024 Yuri N. Sedunov <aris@altlinux.org> 5.12.1-alt1
- 5.12.1

* Sat Mar 16 2024 Yuri N. Sedunov <aris@altlinux.org> 5.12.0-alt1
- 5.12.0

* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 5.10.0-alt1
- 5.10.0

* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 5.8.0-alt1
- 5.8.0

* Wed Jan 11 2023 Yuri N. Sedunov <aris@altlinux.org> 5.6.2-alt1
- 5.6.2

* Thu Sep 22 2022 Yuri N. Sedunov <aris@altlinux.org> 5.6.1-alt1
- 5.6.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 5.6.0-alt1
- 5.6.0

* Sun Jun 12 2022 Yuri N. Sedunov <aris@altlinux.org> 5.4.2-alt1
- 5.4.2

* Thu Apr 21 2022 Yuri N. Sedunov <aris@altlinux.org> 5.4.1-alt1
- 5.4.1

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 5.4.0-alt1
- 5.4.0

* Fri Mar 11 2022 Yuri N. Sedunov <aris@altlinux.org> 5.2.0-alt1.1
- fixed %%check

* Sat Sep 04 2021 Yuri N. Sedunov <aris@altlinux.org> 5.2.0-alt1
- 5.2.0

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 5.0.0-alt1
- 5.0.0

* Fri Feb 12 2021 Yuri N. Sedunov <aris@altlinux.org> 4.99.0-alt1
- first build for Sisyphus




