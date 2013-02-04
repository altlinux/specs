# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize libgio-devel pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(pygtk-2.0) python-devel
# END SourceDeps(oneline)
BuildRequires: libgtk+2-gir-devel
%define _libexecdir %_prefix/libexec
%define glib2_version 2.3.0
%define desktop_file_utils_version 0.9

Name:           mate-charmap
Version:        1.5.0
Release:        alt1_0
Summary:        Unicode character picker and font browser

Group:          File tools
License:        GPLv3+ and GFDL and MIT
				# GPL for the source code, GFDL for the docs, MIT for Unicode data
URL:           	https://github.com/gfunkmonk2
Source:         mate-character-map-%{version}.tar.xz

BuildRequires: 	mate-doc-utils >= 1.0.0
BuildRequires: 	glib2-devel >= %{glib2_version}
BuildRequires: 	gobject-introspection-devel
#BuildRequires: 	mate-conf-devel
BuildRequires: 	desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: 	scrollkeeper
BuildRequires: 	gettext
BuildRequires: 	intltool
BuildRequires: 	mate-common
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel
BuildRequires:  libcairo-gobject-devel

Provides: mate-character-map = %{version}-%{release}

%description
This program allows you to browse through all the available Unicode
characters and categories for the installed fonts, and to examine their
detailed properties. It is an easy way to find the character you might
only know by its Unicode name or code point.

%package devel
Summary: Libraries and headers for libmucharmap
Group: Development/C
Requires: mate-charmap = %{version}-%{release}
Provides: mate-character-map-devel = %{version}-%{release}

%description devel
The mucharmap-devel package contains header files and other resources
needed to use the mucharmap library.

%prep
%setup -q -n mate-character-map-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static \
	--with-gtk=2.0 \
	--disable-scrollkeeper \
	--enable-introspection

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT RUN_QUERY_IMMODULES_TEST=false

%find_lang --with-gnome --all-name  mucharmap

%files -f mucharmap.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/mucharmap
%{_bindir}/mate-character-map
%{_libdir}/libmucharmap.so.*
%{_datadir}/applications/mucharmap.desktop
%{_libdir}/girepository-1.0/*
%{_datadir}/mate/help/mucharmap/*
%{_datadir}/glib-2.0/schemas/*
#%{_datadir}/omf/mucharmap/*

%files devel
%{_includedir}/mucharmap-2.0
%{_libdir}/libmucharmap.so
%{_libdir}/pkgconfig/mucharmap-2.pc
%{_datadir}/gir-1.0


%changelog
* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- new release

