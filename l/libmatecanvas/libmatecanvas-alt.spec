# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/gtkdocize pkgconfig(gail-3.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(libglade-2.0) pkgconfig(pango) pkgconfig(pangoft2)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define gettext_package libmatecanvas-2.0

Summary:        MateCanvas widget
Name:           libmatecanvas
Version:        1.4.0
Release:        alt1_1.1
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
License:        LGPLv2+
Group:          System/Libraries
BuildRequires:  gtk2-devel
BuildRequires:  libart_lgpl-devel
BuildRequires:  libglade2-devel
BuildRequires:  libgail-devel
BuildRequires:  libtool gettext
BuildRequires:  intltool
BuildRequires:  mate-common
BuildRequires:  gtk-doc
Patch33: libmatecanvas-1.4.0-alt-link.patch

%description
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%package devel
Summary: Libraries and headers for libgnomecanvas
Group: Development/C
Requires: libmatecanvas = %{version}-%{release}
# for /usr/share/gtk-doc/html
Requires: gtk-doc

%description devel
The canvas widget allows you to create custom displays using stock items
such as circles, lines, text, and so on. It was originally a port of the
Tk canvas widget but has evolved quite a bit over time.

%prep
%setup -q
%patch33 -p1
NOCONFIGURE=1 ./autogen.sh

%build
# runs on make anyway, let's use the ./autogen.sh hammer for now.
%configure \
	--enable-glade \
	--disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} 

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%find_lang libmatecanvas

%files -f libmatecanvas.lang
%doc COPYING.LIB AUTHORS NEWS README
%{_libdir}/lib*.so.*
%{_libdir}/libglade/2.0/libgladematecanvas.so

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/libmatecanvas/*

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

