# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/xmlto pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define glib2_version 1.0
%define _libexecdir %_prefix/libexec
%define dbus_version		0.90
%define dbus_glib_version	0.70

Summary: 		Desktop notification library
Name: 			libmatenotify
Version: 		1.4.0
Release: 		alt1_1.1
URL: 			http://pub.mate-desktop.org
Source0: 		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License: 		LGPLv2+
Group: 			System/Libraries
BuildRequires: 	libtool
BuildRequires: 	glib2-devel >= %{glib2_version}
BuildRequires: 	libgdk-pixbuf-devel
BuildRequires: 	libdbus-devel >= %{dbus_version}
BuildRequires: 	libdbus-glib-devel >= %{dbus_glib_version}
#BuildRequires: 	gobject-introspection-devel
BuildRequires:  mate-common
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel


%description
libnotify is a library for sending desktop notifications to a notification
daemon, as defined in the freedesktop.org Desktop Notifications spec. These
notifications can be used to inform the user about an event or display some
form of information without getting in the user's way.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	libmatenotify = %{version}-%{release}

%description devel
This package contains libraries and header files needed for
development of programs using %{name}.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static \

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%files
%doc COPYING NEWS AUTHORS

%{_bindir}/mate-notify-send
%{_libdir}/libmatenotify.so.*
#%{_libdir}/girepository-1.0/mate/Notify-0.7.typelib

%files devel
%dir %{_includedir}/libmatenotify
%{_includedir}/libmatenotify/*
%{_libdir}/libmatenotify.so
%{_libdir}/pkgconfig/libmatenotify.pc
%dir %{_datadir}/gtk-doc/html/libmatenotify
%{_datadir}/gtk-doc/html/libmatenotify/*
#%{_datadir}/gir-1.0/mate/Notify-0.7.gir


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

