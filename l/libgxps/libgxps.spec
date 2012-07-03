%define ver_major 0.2
%define api_ver 0.1
%def_enable introspection
%def_enable man
%def_disable test

Name: libgxps
Version: %ver_major.2
Release: alt1

Summary: GObject based library for handling and rendering XPS documents
Group: System/Libraries
License: LGPLv2+
Url: http://live.gnome.org/libgxps

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: gtk-doc
BuildRequires: libgio-devel libcairo-devel libcairo-gobject-devel libfreetype-devel
BuildRequires: libarchive-devel libjpeg-devel libtiff-devel libpng-devel liblcms2-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_test:BuildRequires: libgtk+3-devel}
%{?_enable_man:BuildRequires: xsltproc}

%description
%name is a GObject based library for handling and rendering XPS
documents.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%package utils
Summary: Utilities to manipulate XPS files
Group: Graphics
Requires: %name = %version-%release

%description utils
This package contains utilities to manipulate XPS files from %name
package.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	%{?_enable_introspection:--enable-introspection=yes} \
	%{subst_enable man} \
	%{subst_enable test}

%make_build

%install
make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc AUTHORS NEWS README TODO

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%if_enabled introspection
%files gir
%_typelibdir/GXPS-%api_ver.typelib

%files gir-devel
%_girdir/GXPS-%api_ver.gir
%endif

%files utils
%_bindir/xpstojpeg
%_bindir/xpstopdf
%_bindir/xpstopng
%_bindir/xpstops
%_bindir/xpstosvg
%{?_enable_man:%_man1dir/*}

%files devel-doc
%_datadir/gtk-doc/html/%name

%changelog
* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Sat Jan 21 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt2
- used %%autoreconf to fix RPATH problem

* Sat Nov 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

