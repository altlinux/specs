# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gdk-pixbuf-csource /usr/bin/gtkdocize /usr/bin/pkg-config libgdk-pixbuf-gir-devel libgtk+2-gir-devel pkgconfig(gtk+-2.0) pkgconfig(x11)
# END SourceDeps(oneline)
Summary: 		Window Navigator Construction Kit
Name: 			libmatewnck
Version: 		1.4.0
Release: 		alt1_5.1
URL: 			http://pub.mate-desktop.org
Source0: 		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License: 		LGPLv2+
Group: 			System/Libraries

Requires: 		libstartup-notification

BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libstartup-notification-devel
BuildRequires:  libXres-devel
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel
BuildRequires:  mate-common
BuildRequires:  gtk-doc
BuildRequires:  libcairo-gobject-devel
#only for bad mate-common from fedora
BuildRequires:  libtool
Source44: import.info


%description
libmatewnck (pronounced "libmatewink") is used to implement pagers, tasklists,
and other such things. It allows applications to monitor information
about open windows, workspaces, their names/icons, and so forth.

%package devel
Summary: Libraries and headers for libmatewnck
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static \
	--enable-gtk-doc \
	--enable-startup-notification

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README NEWS
%{_bindir}/matewnck-urgency-monitor
%{_bindir}/matewnckprop
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/Matewnck-1.0.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/libmatewnck/libmatewnck
%{_datadir}/gir-1.0/Matewnck-1.0.gir
%doc %{_datadir}/gtk-doc

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_5.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_5
- new version

