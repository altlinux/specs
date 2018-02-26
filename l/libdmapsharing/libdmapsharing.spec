# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/pkg-config /usr/bin/vala-gen-introspect /usr/bin/vapigen libavahi-devel pkgconfig(avahi-client) pkgconfig(check) pkgconfig(gee-1.0) pkgconfig(glib-2.0) pkgconfig(gnome-vfs-2.0) pkgconfig(gnome-vfs-module-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name: libdmapsharing
Version: 2.9.14
Release: alt2_1
License: LGPLv2+
Source: http://www.flyn.org/projects/libdmapsharing/%{name}-%{version}.tar.gz
URL: http://www.flyn.org/projects/libdmapsharing/
Summary: A DMAP client and server library
Group: Development/C
BuildRequires: libglib2-devel libsoup-devel >= 2.32
BuildRequires: libavahi-glib-devel libgdk-pixbuf-devel gst-plugins-devel >= 0.10.23.2
Source44: import.info

%description 
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%files 
%{_libdir}/libdmapsharing-3.0.so.*
%doc AUTHORS COPYING ChangeLog NEWS README


%package devel
Summary: Files needed to develop applications using libdmapsharing
Group: Development/C
Requires: libdmapsharing = %{version}-%{release}

%description devel
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.  This package provides the libraries, include files, and
other resources needed for developing applications using libdmapsharing.

%files devel
%{_libdir}/pkgconfig/libdmapsharing-3.0.pc
%{_includedir}/libdmapsharing-3.0/
%{_libdir}/libdmapsharing-3.0.so
%{_datadir}/gtk-doc/html/libdmapsharing-3.0

%prep

%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libdmapsharing-3.0.la

%changelog
* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.9.14-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.9.14-alt1_1
- initial import by fcimport

