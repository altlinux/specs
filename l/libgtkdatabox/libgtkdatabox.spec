%define origname gtkdatabox
%def_disable libglade

Name: lib%origname
Version: 0.9.2.0
Release: alt1

Summary: GTK+ widget for fast data display
License: LGPLv2+
Group: System/Libraries

Url: http://www.eudoxos.net/gtk/gtkdatabox/
Source: http://downloads.sourceforge.net/gtkdatabox/gtkdatabox-%version.tar.gz

BuildRequires: libgladeui-devel gtk-doc
%{?_enable_libglade:BuildRequires: libglade-devel}

%description
GtkDatabox is a widget for the GTK+ library designed to display large amounts of
numerical data fast and easy.

%package devel
Summary: Development files for gtkdatabox
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries, header files, and documentation for
developing applications that use %name.

%prep
%setup -n %origname-%version

%build
gtkdocize --copy
%autoreconf
%configure --disable-static \
	--enable-gtk-doc \
	--enable-glade \
	%{subst_enable libglade}
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%{?_enable_libglade:%_libdir/libglade/2.0/libdatabox.so}
%_libdir/glade3/modules/*.so
%_datadir/glade3/catalogs/*

%exclude %_libdir/glade3/modules/*.la

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
#%_datadir/gtk-doc/html/gtkdatabox/

%changelog
* Tue Dec 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.9.2.0-alt1
- 0.9.2.0
- built against libgladeui-1.so.11
- disabled glade-2.0 support

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 0.9.1.3-alt2
- Fix RPATH issue.

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 0.9.1.3-alt1
- 0.9.1.3

* Tue Oct 19 2010 Victor Forsiuk <force@altlinux.org> 0.9.1.1-alt3
- Remove GDK_DISABLE_DEPRECATED and GTK_DISABLE_DEPRECATED to allow
  build with recent libgtk+ (2.22).

* Tue Jul 13 2010 Victor Forsiuk <force@altlinux.org> 0.9.1.1-alt2
- Fix FTBFS (replace deprecated GTK macro with related functions).

* Wed Jul 29 2009 Victor Forsyuk <force@altlinux.org> 0.9.1.1-alt1
- Initial build.
