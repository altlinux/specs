%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name tepl
%define ver_major 6.2
%define api_ver 6

%def_enable gtk_doc
%def_enable introspection
# display required
%def_disable check
%def_disable installed_tests

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: GTK+ Text Editor Framework
License: LGPL-3.0-or-later
Group: System/Libraries
Url:  https://wiki.gnome.org/Projects/Tepl

%if_disabled snapshot
Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/swilmet/tepl.git
Source: %_name-%version.tar
%endif

%define glib_ver 2.64
%define gtk_doc_ver 1.0
%define gtk_ver 3.22
%define gtksource_ver 4.0
%define amtk_ver 5.0

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-gir
BuildRequires: meson glib2-devel >= %glib_ver libgtk+3-devel >= %gtk_ver libgtksourceview4-devel >= %gtksource_ver
BuildRequires: libxml2-devel libuchardet-devel gtk-doc >= %gtk_doc_ver
BuildRequires: pkgconfig(amtk-5) >= %amtk_ver
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: vala-tools
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.6.7 libgtk+3-gir-devel libgtksourceview4-gir-devel libamtk-gir-devel}

%description
Tepl is a library that eases the development of GtkSourceView-based
text editors and IDEs. Tepl is the acronym for "Text editor product
line".

%package devel
Summary: Development environment for Tepl
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the necessary components to develop for Tepl,
GTK+ Text Editor Framework.

%package devel-doc
Summary: Development documentation for Tepl
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
Tepl is a library that eases the development of GtkSourceView-based
text editors and IDEs. Tepl is the acronym for "TK+ Text Editor
Framework"

This package contains development documentation for Tepl.

%package gir
Summary: GObject introspection data for the Tepl library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Tepl library

%package gir-devel
Summary: GObject introspection devel data for the Tepl library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Tepl library

%package tests
Summary: Tests for the Tepl library
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Tepl library.

%prep
%setup -n %_name-%version

%build
%meson \
	%{?_disable_gtk_doc:-Dgtk_doc=false} \
	%{?_disable_introspection:-Dgobject_introspection=false} \
	%{?_enable_installed_tests:-Dinstalled_tests=true}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %_name %{_name}-%api_ver

%check
%meson_test

%files -f %_name.lang
%_libdir/%name-%api_ver.so.*
%doc NEWS README*

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
#%_vapidir/*

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver/
%endif

%if_enabled introspection
%files gir
%_typelibdir/Tepl-%api_ver.typelib

%files gir-devel
%_girdir/Tepl-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 6.2.0-alt1
- 6.2.0

* Fri May 27 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.2-alt1
- 6.0.2

* Wed May 04 2022 Yuri N. Sedunov <aris@altlinux.org> 6.0.1-alt1
- 6.0.1

* Thu Apr 21 2022 Yuri N. Sedunov <aris@altlinux.org> 5.99.1-alt1
- 5.99.1

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 5.99.0-alt1
- 5.99.0 (tepl-5 -> tepl-6)

* Fri Nov 20 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.1-alt1
- 5.0.1

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.0-alt1
- 5.0.0

* Fri Sep 04 2020 Yuri N. Sedunov <aris@altlinux.org> 4.99.4-alt1
- 4.99.4

* Thu Mar 05 2020 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt1
- 4.4.0

* Mon Dec 02 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Mon Jul 16 2018 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0 (ALT #35073)

* Sun Apr 08 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Wed Feb 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.99.1-alt1
- 3.99.1

* Sat Sep 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sun Aug 20 2017 Yuri N. Sedunov <aris@altlinux.org> 2.99.4-alt1
- 2.99.4

* Tue Jul 18 2017 Yuri N. Sedunov <aris@altlinux.org> 2.99.2-alt1
- 2.99.2

* Wed Jul 05 2017 Yuri N. Sedunov <aris@altlinux.org> 2.99.1-alt1
- first build for Sisyphus



