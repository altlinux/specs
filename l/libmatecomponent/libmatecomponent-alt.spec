# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/gtkdocize /usr/bin/perl libpopt-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define libxml2_version 2.4.21
%define mate_corba_version 1.1.0

Summary: 		libmate component system
Name: 			libmatecomponent
Version: 		1.4.0
Release: 		alt1_1.1
URL: 			http://mate-desktop.org
Source0: 		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License: 		GPLv2+ and LGPLv2+
Group: 			System/Libraries
BuildRequires: 	libxml2-devel >= %{libxml2_version}
BuildRequires: 	mate-corba-devel >= %{mate_corba_version}
BuildRequires: 	intltool >= 0.14-1
BuildRequires: 	automake autoconf libtool
BuildRequires: 	gtk-doc
BuildRequires: 	flex bison zlib-devel popt-devel
BuildRequires: 	libdbus-glib-devel
BuildRequires: 	gettext
BuildRequires:  mate-common
Provides: 		libmatecomponent-activation = %{version}-%{release}

Patch0: libbonobo-multishlib.patch

%description
libmatecomponent is a component system based on CORBA, used by the MATE desktop.

%package devel
Summary: 	Libraries and headers for libmatecomponent
Group: 		Development/C
Requires:  	libmatecomponent = %{version}-%{release}
Provides: 	libmatecomponent-activation-devel = %{version}-%{release}

%description devel
libmatecomponent is a component system based on CORBA, used by the MATE desktop.

This package contains header files used to compile programs that
use libmatecomponent.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .multishlib
NOCONFIGURE=1 ./autogen.sh 

%build
%configure \
	--disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

## kill other stuff
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/matecomponent/monikers/*.la
rm $RPM_BUILD_ROOT%{_libdir}/matecorba-2.0/*.la

for serverfile in $RPM_BUILD_ROOT%{_libdir}/matecomponent/servers/*.server; do
    sed -i -e 's|location *= *"/usr/lib\(64\)*/|location="/usr/$LIB/|' $serverfile
done

# noarch packages install to /usr/lib/matecomponent/servers
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/matecomponent/servers

%find_lang libmatecomponent

%files -f libmatecomponent.lang

%doc AUTHORS COPYING NEWS README doc/NAMESPACE

%{_libdir}/lib*.so.*
%{_libdir}/matecomponent
%{_libdir}/matecorba-2.0/*.so*
%{_bindir}/*
%{_libexecdir}/*
# wildcard _libexecdir/*
%exclude %_prefix/lib/debug
%{_sbindir}/*
%dir %{_prefix}/lib/matecomponent/servers
%dir %{_prefix}/lib/matecomponent
%dir %{_sysconfdir}/matecomponent-activation
%config %{_sysconfdir}/matecomponent-activation/*
%{_datadir}/man/man*/*
%{_libdir}/matecomponent-2.0/samples/matecomponent-echo-2

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/idl/*
%{_datadir}/gtk-doc/html/libmatecomponent
%{_datadir}/gtk-doc/html/matecomponent-activation/*

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

