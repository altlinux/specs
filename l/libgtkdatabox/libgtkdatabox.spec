%define origname gtkdatabox

Name: lib%origname
Version: 0.9.1.3
Release: alt2

Summary: GTK+ widget for fast data display
License: LGPLv2+
Group: System/Libraries

Url: http://www.eudoxos.net/gtk/gtkdatabox/
Source0: http://downloads.sourceforge.net/gtkdatabox/gtkdatabox-%version.tar.gz

# Automatically added by buildreq on Wed Jul 29 2009
BuildRequires: libglade-devel libgladeui-devel

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

# This was the fix from 0.9.1.1-alt2. But let upstream sort this out, for now
# we simply get rid of deprecation macros (see below).
#subst	's/GTK_WIDGET_REALIZED/gtk_widget_get_realized/;
#	s/GTK_WIDGET_STATE/gtk_widget_get_state/;
#	s/GTK_WIDGET_VISIBLE/gtk_widget_get_visible/;
#	s/GTK_WIDGET_DRAWABLE/gtk_widget_is_drawable/;' \
#	gtk/gtkdatabox_ruler.c gtk/gtkdatabox.c

subst 's/-DG.K_DISABLE_DEPRECATED//' gtk/Makefile.in examples/Makefile.in

%build
%configure --disable-static --disable-rpath --enable-libglade --enable-glade
# fix rpath libtool issues
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%_libdir/libglade/2.0/libdatabox.so
%_libdir/glade3/modules/*.so
%_datadir/glade3/catalogs/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_datadir/gtk-doc/html/gtkdatabox/

%changelog
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
