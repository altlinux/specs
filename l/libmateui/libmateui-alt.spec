# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gdk-pixbuf-csource /usr/bin/gtkdocize /usr/bin/mateconftool-2 libpopt-devel pkgconfig(gdk-pixbuf-2.0) pkgconfig(gio-2.0) pkgconfig(ice) pkgconfig(libglade-2.0) pkgconfig(pango) pkgconfig(x11)
# END SourceDeps(oneline)
BuildRequires: libmatekeyring-devel
%define _libexecdir %_prefix/libexec

Summary: 		MATE base GUI library
Name: 			libmateui
Version: 		1.4.0
Release: 		alt1_1.1
URL: 			http://pub.mate-desktop.org
Source0: 		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License: 		LGPLv2+
Group: 			System/Libraries

# https://bugzilla.gnome.org/show_bug.cgi?id=606437
Patch0: libgnomeui-2.23.4-disable-event-sounds.patch

BuildRequires: 	glib2-devel
BuildRequires: 	pango-devel
BuildRequires: 	gtk2-devel
BuildRequires: 	mate-conf-devel
BuildRequires: 	mate-vfs-devel
BuildRequires: 	libmatecanvas-devel
BuildRequires: 	libmatecomponent-devel
BuildRequires: 	libxml2-devel
BuildRequires: 	libmate-devel
BuildRequires: 	libart_lgpl-devel
BuildRequires: 	libglade2-devel
BuildRequires: 	mate-keyring-devel
BuildRequires: 	libSM-devel
BuildRequires: 	fontconfig-devel
BuildRequires: 	gettext
BuildRequires: 	automake autoconf libtool
BuildRequires: 	intltool
BuildRequires:  mate-common
BuildRequires:  libmatecomponentui-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  libssl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libavahi-glib-devel
BuildRequires:  libselinux-devel

%description
MATE is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgmateui package
includes GUI-related libraries that are needed to run MATE. (The
libmate package includes the library features that don\'t use the X
Window System.)

%package devel
Summary: Libraries and headers for libmate
Group: Development/C
Requires: libmateui = %{version}-%{release}

%description devel
You should install the libmateui-devel package if you would like to
compile MATE applications. You do not need to install
libmateui-devel if you just want to use the MATE desktop
environment.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%patch0 -p1 -b .disable-sound-events

libtoolize --force --copy
autoreconf

%build

%configure \
	--disable-static \
	--disable-gtk-doc \
	PKG_CONFIG_PATH=/usr/lib64/pkgconfig

#sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%find_lang libmateui

%files -f libmateui.lang
%doc COPYING.LIB NEWS ChangeLog
%{_libdir}/lib*.so.*
%{_datadir}/pixmaps/*
%{_libdir}/libglade/2.0/*.so

%files devel
%doc %{_datadir}/gtk-doc/html/libmateui
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

