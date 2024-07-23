%def_disable snapshot
%def_enable installed_tests
%{?_enable_snapshot:%def_enable gtk_doc}
%def_enable check

%define _name gspell
%define namespace Gspell
%define ver_major 1.12
%define api_ver 1

Name: lib%_name
Version: %ver_major.2
Release: alt1.1

Summary: A spell-checking library for GTK+3 applications
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://wiki.gnome.org/Projects/gspell

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define gtk_ver 3.20.0
%define enchant_ver 2.2.12

BuildRequires(pre): rpm-build-gir rpm-build-vala %{?_enable_check:rpm-macros-valgrind}
BuildRequires: autoconf-archive
BuildRequires: libgtk+3-devel >= %gtk_ver libenchant2-devel >= %enchant_ver libicu-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel vala-tools gtk-doc
%if_enabled check
BuildRequires: xvfb-run hunspell-en
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif
%endif

%description
gspell library provides a flexible API to add spell checking to a GTK+
applications.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR
Requires: libenchant2-devel >= %enchant_ver

%description devel
Development files for %_name, spell-checking library for GTK+
applications.

%package gir
Summary: GObject introspection data for the Gspell
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the Gspell library.

%package gir-devel
Summary: GObject introspection devel data for the Gspell
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the Gspell library.

%package devel-doc
Summary: Development documentation for Gspell
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for Gspell library.

%package tests
Summary: Tests for Gspell library
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Gspell library.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    %{?_enable_installed_tests:--enable-installed-tests}

%install
%makeinstall_std
%find_lang --output=%name.lang %_name-%api_ver

%check
xvfb-run %make -k check VERBOSE=1

%files -f %name.lang
%_bindir/%_name-app1
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.*

%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/%_name-*/

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Tue Jul 23 2024 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1.1
- iv@: use rpm-macros-valgrind to detect valgrind presence

* Sat Jul 29 2023 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Sun Apr 30 2023 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1
- enabled %%check

* Tue Sep 27 2022 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Tue Apr 19 2022 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Wed Mar 09 2022 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt2
- 1.9.1-23-ge93d99e (new russian translation)

* Sat Mar 13 2021 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- updated to 1.9.1-5-g7f16cd2

* Fri Sep 04 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

* Sat Jan 25 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Sat Jun 16 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Thu Feb 15 2018 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1-1-g916fca8 with enchant2

* Sun Oct 29 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Sun Sep 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Aug 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Sun Apr 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sat Mar 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Feb 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Fri Dec 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Sun Nov 06 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sat Jul 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Fri Jun 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Apr 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Mar 13 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Fri Feb 12 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- first build for sisyphus

