# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize libgio-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(pygtk-2.0) python-devel
# END SourceDeps(oneline)
BuildRequires: libgtk+2-gir-devel
%define _libexecdir %_prefix/libexec
%global desktop_file_utils_version 0.9

Name:           mate-character-map
Version:        1.5.0
Release:        alt2_1
Summary:        Unicode character picker and font browser

Group:          File tools
License:        GPLv3+ and GFDL and MIT
				# GPL for the source code, GFDL for the docs, MIT for Unicode data
URL:           	https://github.com/mate-desktop/mate-character-map
#https://github.com/mate-desktop/mate-character-map/archive/master.tar.gz
Source:         https://github.com/mate-desktop/mate-character-map/archive/%{name}-master.tar.gz

BuildRequires: 	mate-doc-utils >= 1.0.0
BuildRequires: 	gobject-introspection-devel
BuildRequires: 	scrollkeeper
BuildRequires: 	mate-common
BuildRequires:  gtk2-devel
BuildRequires:  libcairo-gobject-devel

Requires(post): desktop-file-utils >= %{desktop_file_utils_version}
Requires(postun): desktop-file-utils >= %{desktop_file_utils_version}
Source44: import.info
Provides: mate-charmap = %version
Obsoletes: mate-charmap <= 1.5.0-alt1_0
Conflicts: mate-charmap <= 1.5.0-alt1_0



%description
This program allows you to browse through all the available Unicode
characters and categories for the installed fonts, and to examine their
detailed properties. It is an easy way to find the character you might
only know by its Unicode name or code point.

%package devel
Summary: Libraries and headers for libmcharmap
Group: Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The mcharmap-devel package contains header files and other resources
needed to use the mcharmap library.

%prep
%setup -q -n mate-character-map-master
#sed -i -e 's,Categories=MATE;GTK;Utility;,Categories=GTK;Utility;,g' mucharmap.desktop.in.in mucharmap.desktop.in.in
#sed -i -e '/GTK;Utility;/ a\OnlyShowIn=MATE;' mucharmap.desktop.in.in

NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static \
	--with-gtk=2.0 \
	--disable-scrollkeeper \
	--enable-introspection

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT RUN_QUERY_IMMODULES_TEST=false

rm $RPM_BUILD_ROOT/%{_libdir}/*.la

%find_lang --with-gnome mucharmap


%files -f mucharmap.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/mucharmap
%{_bindir}/mate-character-map
%{_libdir}/libmucharmap.so.*
%{_datadir}/applications/mucharmap.desktop
%{_libdir}/girepository-1.0
%{_datadir}/mate/help/mucharmap/
#%{_datadir}/omf/mucharmap/
%{_datadir}/glib-2.0/schemas/org.mate.mucharmap.enums.xml
%{_datadir}/glib-2.0/schemas/org.mate.mucharmap.gschema.xml

%files devel
%{_includedir}/mucharmap-2.0/
%{_libdir}/libmucharmap.so
%{_libdir}/pkgconfig/mucharmap-2.pc
%{_datadir}/gir-1.0/*


%changelog
* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_1
- renamed to mate-character-map

* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- new release

