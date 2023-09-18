%def_disable snapshot

%def_disable installed_tests
%def_enable docs
%def_enable check

%define _name spelling
%define ver_major 0.2
%define api_ver 1

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: A spellcheck library for GTK 4
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/chergert/libspelling

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/chergert/libspelling.git
Source: %name-%version.tar
%endif

%define gtk_ver 4.6
%define enchant_ver 2.2.12

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-vala
BuildRequires: meson vala-tools
BuildRequires: libgtk4-devel >= %gtk_ver pkgconfig(gtksourceview-5) >= 5.6
BuildRequires: libenchant2-devel >= %enchant_ver libicu-devel
BuildRequires: gobject-introspection-devel libgtk4-gir-devel gir(GtkSource) = 5
%{?_enable_docs:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: xvfb-run /usr/bin/gjs hunspell-en}

%description
This library is heavily based upon GNOME Text Editor and GNOME Builder's
spellcheck implementation.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR
Requires: libenchant2-devel >= %enchant_ver

%description devel
Development files for %name, spell-checking library for GTK4
applications.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for Spelling library.

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for Spelling library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for Spelling library.

%package tests
Summary: Tests for Spelling library
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Spelling library.


%prep
%setup -n %name-%version

%build
%meson \
    %{?_disable_docs:-Ddocs=false} \
    %{?_enable_installed_tests:--enable-installed-tests}
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %name-%api_ver

%check
xvfb-run %__meson_test

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc NEWS README*

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.*

%files gir
%_typelibdir/Spelling-%api_ver.typelib

%files gir-devel
%_girdir/Spelling-%api_ver.gir

%if_enabled docs
%files devel-doc
%_datadir/doc/%name-%api_ver/
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%name-%api_ver/
%_datadir/installed-tests/%name-%api_ver/
%endif


%changelog
* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

