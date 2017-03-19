#%%set_verify_elf_method unresolved=relaxed
%define _localstatedir %_var
%define ver_major 0.7
%def_disable static
%def_disable gtk_doc
%define api_ver %ver_major

Name: libinfinity
Version: %ver_major.1
Release: alt1

Summary: A library to build collaborative text editors
Group: System/Libraries
License: LGPLv2.1+
Url: http://gobby.0x539.de/trac/wiki/Infinote/Libinfinity

Source: http://releases.0x539.de/%name/%name-%version.tar.gz

BuildRequires: gtk-doc libgio-devel libgnutls-devel libgsasl-devel
BuildRequires: libavahi-devel libpam-devel libxml2-devel libgtk+3-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
# for infinoted
BuildRequires: libdaemon-devel gnupg

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

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library.

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name library.

%package gtk
Summary: A library to build collaborative text editors (GTK+3 widgets)
Group: System/Libraries
Requires: %name = %version-%release

%description gtk
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains Gtk widgets for use in libinfinity-based and
Gtk-based applications.

%package gtk-devel
Summary: Libraries and headers for %name (GTK+3 widgets)
Group: Development/C
Requires: %name-gtk = %version-%release
Requires: %name-devel = %version-%release

%description gtk-devel
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains the headers of libinfinity (GTK+3 widgets) and all
files needed to link applications dependening on this library.

%package gtk-gir
Summary: GObject introspection data for the libinfgtk and inftextgtk libraries
Group: System/Libraries
Requires: %name-gtk = %version-%release
Requires: %name-gir = %version-%release

%description gtk-gir
GObject introspection data for the libinfgtk and inftextgtk libraries.

%package gtk-gir-devel
Summary: GObject introspection devel data for the libinfgtk and inftextgtk libraries
Group: Development/Other
BuildArch: noarch
Requires: %name-gtk-gir = %version-%release
Requires: %name-gtk-devel = %version-%release

%description gtk-gir-devel
GObject introspection devel data for the libinfgtk and inftextgtk libraries.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains development documentation for %name.

%package gtk-devel-doc
Summary: Development documentation for %name (GTK+3 widgets)
Group: Development/C
Conflicts: %name-gtk < %version
BuildArch: noarch

%description gtk-devel-doc
libinfinity is library to build collaborative text editors. Changes to
the text buffers are synced to all other clients over a central server.
Even though a central server is involved, the local user sees his
changes applied instantly and the merging is done on the individual
clients.

This package contains development documentation for %name (GTK+3 widgets).


%prep
%setup

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--with-gtk3=yes \
	%{?_enable_gtk_doc:--enable-gtk-doc}
%make_build

%install
%makeinstall_std

%find_lang --output=%name.lang %name-%api_ver

%files -n infinoted
%_bindir/*
%_man1dir/infinoted*
%dir %_libdir/infinoted-%api_ver
%dir %_libdir/infinoted-%api_ver/plugins
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-autosave.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-certificate-auth.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-dbus.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-directory-sync.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-document-stream.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-linekeeper.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-logging.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-note-chat.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-note-text.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-record.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-traffic-logging.so
%_libdir/infinoted-%api_ver/plugins/libinfinoted-plugin-transformation-protection.so

%exclude %_libdir/infinoted-%api_ver/plugins/*.la

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%_libdir/libinftext-%api_ver.so.*
%_libdir/libinfinoted-plugin-manager-%api_ver.so.*
%doc AUTHORS NEWS README*

%files devel
%_includedir/%name-%api_ver/
%_includedir/libinftext-%api_ver/
%_includedir/libinfinoted-plugin-manager-%api_ver/
%_libdir/%name-%api_ver.so
%_libdir/libinftext-%api_ver.so
%_libdir/libinfinoted-plugin-manager-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_pkgconfigdir/libinftext-%api_ver.pc
%_pkgconfigdir/libinfinoted-plugin-manager-%api_ver.pc

%files gir
%_typelibdir/InfGnutls-3.0.typelib
%_typelibdir/InfGsasl-1.0.typelib
%_typelibdir/InfText-0.7.typelib
%_typelibdir/Infinity-0.7.typelib
%_typelibdir/Infinityc-0.7.typelib
%_typelibdir/Infinityd-0.7.typelib
%_typelibdir/Infinoted-0.7.typelib

%files gir-devel
%_girdir/InfGnutls-3.0.gir
%_girdir/InfGsasl-1.0.gir
%_girdir/InfText-0.7.gir
%_girdir/Infinity-0.7.gir
%_girdir/Infinityc-0.7.gir
%_girdir/Infinityd-0.7.gir
%_girdir/Infinoted-0.7.gir

%files gtk
%_libdir/libinfgtk-%api_ver.so.*
%_libdir/libinftextgtk-%api_ver.so.*
%_iconsdir/hicolor/*/*/*

%files gtk-gir
%_typelibdir/InfGtk-0.7.typelib
%_typelibdir/InfTextGtk-0.7.typelib

%files gtk-gir-devel
%_girdir/InfGtk-0.7.gir
%_girdir/InfTextGtk-0.7.gir

%files gtk-devel
%_includedir/libinfgtk-%api_ver/
%_includedir/libinftextgtk-%api_ver/
%_libdir/libinfgtk-%api_ver.so
%_libdir/libinftextgtk-%api_ver.so
%_pkgconfigdir/libinfgtk-%api_ver.pc
%_pkgconfigdir/libinftextgtk-%api_ver.pc

%files devel-doc
%_datadir/gtk-doc/html/%name-%api_ver/
%_datadir/gtk-doc/html/libinftext-%api_ver/
%_datadir/gtk-doc/html/libinfinoted-plugin-manager-%api_ver/

%files gtk-devel-doc
%_datadir/gtk-doc/html/libinfgtk-%api_ver/
%_datadir/gtk-doc/html/libinftextgtk-%api_ver/


%changelog
* Sun Mar 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.7-alt2
- rebuilt against libgnutls.so.30

* Tue Oct 20 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.7-alt1
- 0.6.7

* Sat May 23 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.6-alt1
- 0.6.6

* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.4-alt1
- 0.6.4

* Thu Jun 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Thu Jun 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- 0.5.1

* Thu Jun 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

