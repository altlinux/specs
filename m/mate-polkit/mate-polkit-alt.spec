# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize libgtk+2-gir-devel libpolkit-gir-devel pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary: 	PolicyKit integration for the MATE desktop
Name: 		mate-polkit
Version: 	1.4.0
Release: 	alt1_1.1
License: 	LGPLv2+
URL: 		http://mate-desktop.org
Group: 		File tools
Source0: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires: gtk2-devel
BuildRequires: glib2-devel >= 2.25.11
BuildRequires: libpolkit-devel >= 0.97-1
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: mate-common
BuildRequires: libcairo-gobject-devel

Provides: polkit-mate-1 = 1.1.0
Provides: libpolkit-gtk-mate-1 = 1.1.0

Provides: polkit-mate-authentication-agent-1

Requires: polkit >= 0.97

%description
mate-polkit provides an authentication agent for PolicyKit
that matches the look and feel of the MATE desktop.

%package devel
Summary: Development files for mate-polkit
Group: Development/C
Requires: mate-polkit = %{version}-%{release}
Requires: mate-polkit-docs = %{version}-%{release}
Provides: mate-polkit-devel = 1.1.0
Provides: mate-polkit-demo = 1.1.0

%description devel
Development files for mate-polkit.

%package docs
Summary: Development documentation for mate-polkit
Group: Development/C

%description docs
Development documentation for mate-polkit.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static \
	--enable-examples \
	--enable-introspection \
	--enable-gtk-doc

make

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang mate-polkit

%files -f mate-polkit.lang
%doc COPYING AUTHORS README
%{_sysconfdir}/xdg/autostart/*
%{_libexecdir}/*
# wildcard _libexecdir/*
%exclude %_prefix/lib/debug
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gir-1.0/*.gir

%files docs
%{_datadir}/gtk-doc


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Fri Aug 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

