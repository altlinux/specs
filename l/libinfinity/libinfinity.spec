# BEGIN SourceDeps(oneline):
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel pkgconfig(avahi-client) pkgconfig(gio-2.0) pkgconfig(libdaemon)
# END SourceDeps(oneline)
BuildRequires: chrpath
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define rel 2
%define libversion 0.7

Name:           libinfinity
Version:        0.7.1
Release:        alt1_2
Summary:        Library implementing the infinote protocol
Group:          System/Libraries
License:        LGPLv2+
URL:            http://gobby.0x539.de/trac/wiki/Infinote/Libinfinity
Source0:        http://releases.0x539.de/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libgsasl)
BuildRequires:  gtk-doc
BuildRequires:  libpam0-devel
Source44: import.info


%description
libinfinity is an implementation of the Infinote protocol written in
GObject-based C. 


#--------------------------------------------------------------------

%package -n     infinoted
Summary:        Server for the infinote protocol
Group:          System/Servers

%description -n infinoted
Server daemon for the infinote protocol.

%files -n infinoted -f %{name}-%{libversion}.lang
%{_bindir}/infinoted-%{libversion}
%{_libdir}/infinoted-%{libversion}/plugins/*
%{_mandir}/man1/infinoted-*
%{_datadir}/icons/hicolor/*/apps/infinote.*

#--------------------------------------------------------------------

%define libinfinity_major 0
%define libinfinity libinfinity%{libversion}_%{libinfinity_major}

%package -n %{libinfinity}
Summary: Library providing gtk bindings for %{name}
Group:   System/Libraries

%description   -n %{libinfinity}
This package provides the gtk bindings for %{name}

%files -n %{libinfinity}
%{_libdir}/libinfinity-%{libversion}.so.%{libinfinity_major}
%{_libdir}/libinfinity-%{libversion}.so.%{libinfinity_major}.*

#--------------------------------------------------------------------

%define libinftext_major 0
%define libinftext libinftext%{libversion}_%{libinftext_major}

%package -n %{libinftext}
Summary: Library providing gtk bindings for %{name}
Group:   System/Libraries

%description   -n %{libinftext}
This package provides the gtk bindings for %{name}

%files -n %{libinftext}
%{_libdir}/libinftext-%{libversion}.so.%{libinftext_major}
%{_libdir}/libinftext-%{libversion}.so.%{libinftext_major}.*


#--------------------------------------------------------------------

%define libinfgtk_major 0
%define libinfgtk libinftgtk%{libversion}_%{libinfgtk_major}

%package -n %{libinfgtk}
Summary: Library providing gtk bindings for %{name}
Group:   System/Libraries

%description  -n %{libinfgtk}
This package provides the gtk bindings for %{name}

%files -n %{libinfgtk}
%{_libdir}/libinfgtk-%{libversion}.so.%{libinfgtk_major}
%{_libdir}/libinfgtk-%{libversion}.so.%{libinfgtk_major}.*

#--------------------------------------------------------------------

%define libinftextgtk_major 0
%define libinftextgtk libinftextgtk%{libversion}_%{libinftextgtk_major}

%package -n %{libinftextgtk}
Summary: Library providing gtk bindings for %{name}
Group:   System/Libraries

%description   -n %{libinftextgtk}
This package provides the gtk bindings for %{name}

%files -n %{libinftextgtk}
%{_libdir}/libinftextgtk-%{libversion}.so.%{libinftextgtk_major}
%{_libdir}/libinftextgtk-%{libversion}.so.%{libinftextgtk_major}.*

#--------------------------------------------------------------------

%define libinfinoted_plugin_manager_major 0
%define libinfinoted_plugin_manager libinfinoted-plugin-manager%{libversion}_%{libinfinoted_plugin_manager_major}

%package -n %{libinfinoted_plugin_manager}
Summary: A small library that is shared by infinoted and infinoted plugins
Group:   System/Libraries

%description -n %{libinfinoted_plugin_manager}
This is a small library that is shared by infinoted and infinoted plugins.
It provides a way for plugins to access the state of the server.

%files -n %{libinfinoted_plugin_manager}
%{_libdir}/libinfinoted-plugin-manager-%{libversion}.so.%{libinfinoted_plugin_manager_major}
%{_libdir}/libinfinoted-plugin-manager-%{libversion}.so.%{libinfinoted_plugin_manager_major}.*

#--------------------------------------------------------------------

%define libinfinity_devel libinfinity-devel

%package -n %{libinfinity_devel}
Summary: Devel files for %libinfinity
Group: Development/C
Requires: %{libinfinity} = %{version}-%{release}

%description -n %{libinfinity_devel}
This package provides the devel files for libinfinity

%files -n %{libinfinity_devel}
%{_includedir}/libinfinity-%{libversion}/
%{_libdir}/libinfinity-%{libversion}.so
%{_libdir}/pkgconfig/libinfinity-%{libversion}.pc
%{_datadir}/gtk-doc/html/libinfinity-%{libversion}/

#--------------------------------------------------------------------

%define libinftext_devel libinftext-devel

%package -n %{libinftext_devel}
Summary: Devel files for %libinftext
Group: Development/C
Requires: %{libinftext} = %{version}-%{release}

%description -n %{libinftext_devel}
This package provides the devel files for libinftext

%files -n %{libinftext_devel}
%{_includedir}/libinftext-%{libversion}/
%{_libdir}/libinftext-%{libversion}.so
%{_libdir}/pkgconfig/libinftext-%{libversion}.pc
%{_datadir}/gtk-doc/html/libinftext-%{libversion}/

#--------------------------------------------------------------------

%define libinfgtk_devel libinftgtk-devel

%package -n %{libinfgtk_devel}
Summary: Devel files for %libinfgtk
Group: Development/GNOME and GTK+
Requires: %{libinfgtk} = %{version}-%{release}

%description -n %{libinfgtk_devel}
This package provides the devel files for libinfgtk

%files -n %{libinfgtk_devel}
%{_includedir}/libinfgtk-%{libversion}/
%{_libdir}/libinfgtk-%{libversion}.so
%{_libdir}/pkgconfig/libinfgtk-%{libversion}.pc
%{_datadir}/gtk-doc/html/libinfgtk-%{libversion}/

#--------------------------------------------------------------------

%define libinftextgtk_devel libinftextgtk-devel

%package -n %{libinftextgtk_devel}
Summary: Devel files for %libinftextgtk
Group: Development/GNOME and GTK+
Requires: %{libinftextgtk} = %{version}-%{release}

%description -n %{libinftextgtk_devel}
This package provides the devel files for libinftextgtk

%files -n %{libinftextgtk_devel}
%{_includedir}/libinftextgtk-%{libversion}/
%{_libdir}/libinftextgtk-%{libversion}.so
%{_libdir}/pkgconfig/libinftextgtk-%{libversion}.pc
%{_datadir}/gtk-doc/html/libinftextgtk-%{libversion}/

#--------------------------------------------------------------------

%define libinfinoted_plugin_manager_devel libinfinoted-plugin-manager-devel

%package -n %{libinfinoted_plugin_manager_devel}
Summary: Devel files for %{libinfinoted_plugin_manager}
Group: Development/C
Requires: %{libinfinoted_plugin_manager} = %{version}-%{release}

%description -n %{libinfinoted_plugin_manager_devel}
This package provides the devel files for libinfinoted-plugin-manager.

%files -n %{libinfinoted_plugin_manager_devel}
%{_includedir}/libinfinoted-plugin-manager-%{libversion}/
%{_libdir}/libinfinoted-plugin-manager-%{libversion}.so
%{_libdir}/pkgconfig/libinfinoted-plugin-manager-%{libversion}.pc
%{_datadir}/gtk-doc/html/libinfinoted-plugin-manager-%{libversion}/

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure --with-gtk3
%make 

%install
%makeinstall 
rm -f %{buildroot}%{_iconsdir}/*/icon-theme.cache
%find_lang %{name}-%{libversion}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done



%changelog
* Wed Dec 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_2
- raised from the dead as mga import

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

