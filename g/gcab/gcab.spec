%define ver_major 0.7
%define api_ver 1.0

Name: gcab
Version: %ver_major
Release: alt1

Summary: M$ Cabinet archive tool
Group: File tools
License: LGPLv2+
Url: http://ftp.gnome.org/pub/gnome/sources/gcab

Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

Requires: lib%name = %version-%release

BuildRequires: intltool gtk-doc vala-tools glib2-devel
BuildRequires: gobject-introspection-devel zlib-devel

%description
gcab is a tool to manipulate Cabinet archive.

%package -n lib%name
Summary: Library to manipulate Cabinet archives
Group: System/Libraries

%description -n lib%name
libgcab is a library to manipulate Cabinet archive using GIO/GObject.

%package -n lib%name-devel
Summary: Development files for gcab library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
libgcab is a library to manipulate Cabinet archive.

Libraries, includes, needed to develop applications with the gcab library.

%package -n lib%name-devel-doc
Summary: Development documentation for gcab library
Group: Development/Documentation
Conflicts: lib%name < %version
BuildArch: noarch

%description -n lib%name-devel-doc
libgcab is a library to manipulate Cabinet archive using GIO/GObject.

This package contains development documentation for gcab library.

%package -n lib%name-gir
Summary: GObject introspection data for the gcab library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the gcab library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the gcab library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the gcab library


%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--enable-gtk-doc \
	--enable-fast-install
%make_build VERSION=%version

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_man1dir/%name.1*
%doc NEWS

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name-devel
%_includedir/lib%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%_pkgconfigdir/lib%name-%api_ver.pc
%_vapidir/lib%name-%api_ver.vapi

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name/

%files -n lib%name-gir
%_typelibdir/GCab-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/GCab-%api_ver.gir

%changelog
* Wed Mar 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- 0.7

* Tue Mar 17 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Sat Mar 14 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt0.1
- 0.6 snapshot

* Mon Mar 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Sun Feb 24 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- first build for Sisyphus

