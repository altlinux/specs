# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/gtkdocize /usr/bin/mateconftool-2 libpopt-devel pkgconfig(audiofile) pkgconfig(esound) pkgconfig(gail) pkgconfig(gail-3.0) pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libglade-2.0) pkgconfig(pango) pkgconfig(pangoft2)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary:		MateCanvas widget
Name:			libmatecanvas
Version:		1.4.0
Release:		alt1_7
URL:			http://mate-desktop.org
Source0:		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License:		LGPLv2+
Group:			System/Libraries

BuildRequires:	gtk2-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libglade2-devel
BuildRequires:	mate-common
Source44: import.info
Patch33: libmatecanvas-1.4.0-alt-link.patch


%description
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%package devel
Summary:	Libraries and headers for libmatecanvas
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The libmatecanvas-devel package contains libraries and header files for
developing applications that use libmatecanvas.


%prep
%setup -q
%patch33 -p1
NOCONFIGURE=1 ./autogen.sh


%build
%configure \
	--enable-glade \
	--disable-static

make %{?_smp_mflags} 


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

find $RPM_BUILD_ROOT -name '*.la' -exec rm -fv {} ';'

%find_lang %{name}


%files -f %{name}.lang
%doc COPYING.LIB AUTHORS NEWS README
%{_libdir}/libmatecanvas-2.so.0*
%{_libdir}/libglade/2.0/libgladematecanvas.so

%files devel
%{_libdir}/libmatecanvas-2.so
%{_libdir}/pkgconfig/libmatecanvas-2.0.pc
%{_includedir}/libmatecanvas-2.0/
%{_datadir}/gtk-doc


%changelog
* Sun Nov 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_7
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

