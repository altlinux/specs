%def_enable snapshot

%define _name graphene
%define ver_major 1.5
%define api_ver 1.0

%def_disable static
%def_enable gtk_doc
%def_enable introspection
%def_enable tests
%def_disable gcc_vector
%ifarch i586 %arm
%def_disable sse2
%endif
%ifnarch %arm
%def_disable neon
%endif

Name: lib%_name
Version: %ver_major.2
Release: alt1

Summary: Graphene is a library of data types commonly used to implement 2D-in-3D or full 3D canvases
License: BSD-like
Group: System/Libraries
Url: https://ebassi.github.io/%_name

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
# VCS: https://github.com/ebassi/graphene.git
Source: %_name-%version.tar
%endif

BuildRequires: /proc
BuildRequires: gobject-introspection-devel gtk-doc

%description
%summary
Graphene only contains math data types, like vectors and matrices; it
does not deal with windowing system calls, event handling, drawing,
or a full scene graph.

%package devel
Summary: Development libraries and header files for Graphene
Group: Development/C
Requires: %name = %version-%release

%description devel
This package package includes the libraries and header files
for the Graphene library.

%package devel-doc
Summary: Development documentation for Graphene
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
%summary
This package contains development documentation for Graphene library.

%package gir
Summary: GObject introspection data for the Graphene library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Graphene library.

%package gir-devel
Summary: GObject introspection devel data for the Graphene library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Graphene library.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
    %{subst_enable static} \
    %{subst_enable introspection} \
    %{subst_enable sse2} \
    %{?_disable_gcc_vector:--disable-gcc-vector} \
    %{?_disable_neon:--disable-arm-neon} \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    %{?_disable_tests:--disable-tests}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/%name-%api_ver.so.*
#%doc ChangeLog

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%_name-%api_ver/
%_libdir/*.so
%_pkgconfigdir/%_name-%api_ver.pc
%_pkgconfigdir/%_name-gobject-%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/Graphene-%api_ver.typelib

%files gir-devel
%_girdir/Graphene-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Mon Nov 28 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- updated to 1.5.2-7-g280d7b5

* Tue May 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus

