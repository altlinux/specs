# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gdk-pixbuf-csource /usr/bin/gtkdocize /usr/bin/pkg-config gobject-introspection-devel libXres-devel libgdk-pixbuf-gir-devel libgtk+2-gir-devel pkgconfig(glib-2.0) pkgconfig(gobject-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           libmatewnck
Version:        1.5.0
Release:        alt1_1
Summary:        MATE Desktop Window Navigator Construction Kit libraries

Group:          System/Libraries
License:        LGPLv2+ and GPLv2+
URL:            http://www.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xres)
BuildRequires:  mate-common
BuildRequires:  pkgconfig(libstartup-notification-1.0)
Source44: import.info

%description
Window navigator construction Kit for MATE Desktop

%package devel
Group: Development/C
Summary:  Development libraries and headers for libmatewnck
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for libmatewnck

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_libdir}/girepository-1.0/Matewnck-1.0.typelib
%{_libdir}/libmatewnck.so.*
%{_datadir}/gtk-doc/html/libmatewnck/
%{_bindir}/matewnck-urgency-monitor
%{_bindir}/matewnckprop

%files devel
%{_libdir}/libmatewnck.so
%{_libdir}/pkgconfig/libmatewnck.pc
%{_includedir}/libmatewnck/
%{_datadir}/gir-1.0/Matewnck-1.0.gir

%changelog
* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_5.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_5
- new version

