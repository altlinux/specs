%def_disable static
%def_disable gtk_doc
%define api_ver 0.5

Name: libinfinity
Version: 0.5.2
Release: alt1

Summary: A library to build collaborative text editors
Group: System/Libraries
License: LGPLv2.1+
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
Url: http://gobby.0x539.de/

Source: http://releases.0x539.de/%name/%name-%version.tar.gz

BuildRequires: gtk-doc libgio-devel libgnutls-devel libgsasl-devel
BuildRequires: libavahi-devel libpam-devel libxml2-devel libgtk+3-devel
# for infinoted
BuildRequires: libdaemon-devel

%description
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains the shared object files used at runtime by
libinfinity-based application.

%package -n infinoted
Summary: Simple stand-alone infinote server application
Group: System/Servers
Requires: %name = %version-%release

%description -n infinoted
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains the simple stand-alone infinote server application.

%package devel
Summary: Libraries and headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains the headers of libinfinity and all files needed
to link applications dependening on this library.

%package gtk3
Summary: A library to build collaborative text editors (GTK+3 widgets)
Group: System/Libraries
Requires: %name = %version-%release

%description gtk3
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains Gtk widgets for use in libinfinity-based and
Gtk-based applications.

%package gtk3-devel
Summary: Libraries and headers for %name (GTK+3 widgets)
Group: Development/C
Requires: %name-gtk3 = %version-%release

%description gtk3-devel
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains the headers of libinfinity (GTK+3 widgets) and all
files needed to link applications dependening on this library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains development documentation for %name.

%package gtk3-devel-doc
Summary: Development documentation for %name (GTK+3 widgets)
Group: Development/C
Conflicts: %name-gtk3 < %version
BuildArch: noarch

%description gtk3-devel-doc
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains development documentation for %name (GTK+3 widgets).


%prep
%setup -q

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--with-gtk3
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --output=%name.lang %name-%api_ver

%files -n infinoted
%_bindir/*
%_man1dir/infinoted*
%_libdir/infinoted-%api_ver/note-plugins/libinfd-note-plugin-text.so

%exclude %_libdir/infinoted-%api_ver/note-plugins/libinfd-note-plugin-text.la

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%_libdir/libinftext-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%name-%api_ver/
%_includedir/libinftext-%api_ver/
%_libdir/%name-%api_ver.so
%_libdir/libinftext-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_pkgconfigdir/libinftext-%api_ver.pc

%files gtk3
%_libdir/libinfgtk-%api_ver.so.*
%_libdir/libinftextgtk-%api_ver.so.*
%_iconsdir/hicolor/*/*/*

%files gtk3-devel
%_includedir/libinfgtk-%api_ver/
%_includedir/libinftextgtk-%api_ver/
%_libdir/libinfgtk-%api_ver.so
%_libdir/libinftextgtk-%api_ver.so
%_pkgconfigdir/libinfgtk-%api_ver.pc
%_pkgconfigdir/libinftextgtk-%api_ver.pc

%files devel-doc
%_datadir/gtk-doc/html/%name-%api_ver/
%_datadir/gtk-doc/html/libinftext-%api_ver/

%files gtk3-devel-doc
%_datadir/gtk-doc/html/libinfgtk-%api_ver/
%_datadir/gtk-doc/html/libinftextgtk-%api_ver/


%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Thu Jun 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

