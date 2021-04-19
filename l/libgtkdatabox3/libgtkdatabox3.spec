%define __name gtkdatabox
%define api_ver 3
%define _name %__name%api_ver

%def_enable glade
%def_enable gtk_doc

Name: lib%_name
Version: 1.0.0
Release: alt1

Summary: GTK+3 widget for fast data display
License: LGPLv2+
Group: System/Libraries
Url: https://gtkdatabox3.sourceforge.io/

Source: https://downloads.sourceforge.net/project/%_name/%__name-%version.tar.gz

BuildRequires: libgtk+3-devel >= 3.4.0 gtk-doc
%{?_enable_glade:BuildRequires: libgladeui2.0-devel}

%description
GtkDatabox3 is a widget for the Gtk+3 library designed to display large
amounts of numerical data fast and easy. One or more data sets of
thousands of data points (X and Y coordinate) may be displayed and
updated in split seconds. The widget is therefore used in many scientific
and private projects that need to show quickly changing data "live".

%package devel
Summary: Development files for GtkDatabox3
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries, header files for developing
applications that use GtkDatabox3 library.

%package devel-doc
Summary: Development documentation for GtkDatabox3
Group: Development/Documentation
Conflicts: %name < %version

%description devel-doc
This package provides development documenation for GtkDatabox3 library.

%prep
%setup -n %__name-%version

%build
%autoreconf
%configure --disable-static \
    %{subst_enable glade} \
    %{?_enable_gtk_doc:--enable-gtk-doc}
%nil
%make_build

%install
%makeinstall_std

%files
%_libdir/lib%__name.so.*

%files devel
%_includedir/*
%_libdir/lib%__name.so
%{?_enable_glade:
%_libdir/glade/modules/*.so
%_datadir/glade/catalogs/*
%_iconsdir/hicolor/scalable/apps/*.svg
%exclude %_libdir/glade/modules/*.la}
%_pkgconfigdir/*

%{?_enable_gtk_doc:
%files devel-doc
%_datadir/gtk-doc/html/%__name-1/}

%changelog
* Fri Apr 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus

