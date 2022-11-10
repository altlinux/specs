%def_disable snapshot

%define _name gtksourceview
%define ver_major 4.8
%define api_ver 4

%def_disable static
%def_disable gtk_doc
%def_enable introspection
%def_enable vala
%def_enable installed_tests
%def_enable gspell
%def_enable check
%ifarch %valgrind_arches
%def_enable valgrind
%endif

Name: lib%{_name}4
Version: %ver_major.4
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

%define gtk_ver 3.24.0
%define libxml2_ver 2.6.0
%define gspell_ver 1.8.0
%define fribidi_ver 0.19.7

BuildRequires(pre): meson rpm-build-gnome rpm-macros-valgrind

# From meson.build
BuildRequires: gcc-c++ gtk-doc itstool
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libxml2-devel >= %libxml2_ver
BuildRequires: libfribidi-devel >= %fribidi_ver
BuildRequires: perl-XML-Parser zlib-devel
%{?_enable_gspell:BuildRequires: libgspell-devel >= %gspell_ver}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools libvala-devel}
%{?_enable_check:BuildRequires: xvfb-run %{?_enable_valgrind:valgrind}
BuildRequires: fonts-ttf-roboto fonts-ttf-google-noto-sans-vf}

%description
GtkSourceView is a text widget that extends the standard gtk+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package contains shared GtkSourceView library.

%package devel
Summary: Files to compile applications that use GtkSourceView
Group: Development/C
Requires: %name = %version-%release

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
Requires: %name = %version-%release

%description gir
GObject introspection data for the GtkSourceView library

%package gir-devel
Summary: GObject introspection devel data for the GtkSourceView library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GtkSourceView library

%package tests
Summary: Tests for the GtkSourceView library
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed GtkSourceView library.

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -n %_name-%version

%build
%meson \
	%{?_enable_gtk_doc:-Dgtk-doc=true} \
	%{?_disable_introspection:-Dgir=false} \
	%{?_disable_vala:-Dvapi=false} \
	%{?_enable_installed_tests:-Dinstall_tests=true}
%nil
%meson_build

%install
%meson_install
%find_lang %_name-%api_ver

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
xvfb-run %meson_test

%files -f %_name-%api_ver.lang
%_libdir/lib%_name-%api_ver.so.*
%_datadir/%_name-%api_ver/
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

%if_enabled gtk_doc
%files devel-doc
%_gtk_docdir/*
%endif

%if_enabled introspection
%files gir
%_typelibdir/GtkSource-%api_ver.typelib

%files gir-devel
%_girdir/GtkSource-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 4.8.4-alt1
- 4.8.4

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 4.8.3-alt1
- 4.8.3

* Wed Mar 09 2022 Yuri N. Sedunov <aris@altlinux.org> 4.8.2-alt1.1
- fixed %%check

* Sat Sep 04 2021 Yuri N. Sedunov <aris@altlinux.org> 4.8.2-alt1
- 4.8.2

* Tue Aug 31 2021 Yuri N. Sedunov <aris@altlinux.org> 4.8.1-alt2
- updated to 4.8.1-32-g3c7ac24c

* Tue Mar 02 2021 Yuri N. Sedunov <aris@altlinux.org> 4.8.1-alt1
- 4.8.1

* Sun Sep 13 2020 Yuri N. Sedunov <aris@altlinux.org> 4.8.0-alt1
- 4.8.0

* Sat Jun 27 2020 Yuri N. Sedunov <aris@altlinux.org> 4.6.1-alt1
- 4.6.1

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 4.6.0-alt1
- 4.6.0

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt1
- 4.4.0

* Mon Jun 03 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1.1
- made valgrind tests optional

* Sat Mar 16 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.3-alt1
- 4.0.3

* Sun Jun 17 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt1
- 4.0.2

* Fri May 11 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt1
- 4.0.1

* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Sat Dec 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.99.7-alt1
- 3.99.7

* Tue Oct 17 2017 Yuri N. Sedunov <aris@altlinux.org> 3.99.6-alt1
- 3.99.6

* Wed Sep 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.99.5-alt1
- 3.99.5

* Sun Apr 23 2017 Yuri N. Sedunov <aris@altlinux.org> 3.99.4-alt1
- 3.99.4

* Wed Nov 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.99.2-alt1
- first build for Sisyphus




