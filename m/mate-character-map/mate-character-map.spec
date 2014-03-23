# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize libgio-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(pygtk-2.0) python-devel libgtk+2-gir-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%global _internal_version  2464a6c

Name:           mate-character-map
Version:        1.6.1
Release:        alt1_0.1.git2464a6c
Summary:        Unicode character picker and font browser

Group:          File tools
License:        GPLv2+ and LGPLv3+
URL:            http://pub.mate-desktop.org

# To generate tarball
# wget http://git.mate-desktop.org/%%{name}/snapshot/%%{name}-{_internal_version}.tar.xz -O %%{name}-%%{version}.git%%{_internal_version}.tar.xz
Source0: http://raveit65.fedorapeople.org/Mate/git-upstream/%{name}-%{version}.git%{_internal_version}.tar.xz

#Source:         http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz

BuildRequires:  mate-doc-utils >= 1.0.0
BuildRequires:  gobject-introspection-devel
BuildRequires:  mate-common
BuildRequires:  gtk2-devel
BuildRequires:  libcairo-gobject-devel
BuildRequires:  desktop-file-utils
Source44: import.info


%description
This program allows you to browse through all the available Unicode
characters and categories for the installed fonts, and to examine their
detailed properties. It is an easy way to find the character you might
only know by its Unicode name or code point.

%package devel
Summary: Libraries and headers for mate-character-map
Group: Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The mate-character-map package contains header files and other resources
needed to use the mate-character-map library.

%prep
#%setup -q
%setup -q -n %{name}-%{_internal_version}


%build
ln -s /usr/share/mate-doc-utils/mate-doc-utils.make .
NOCONFIGURE=1 ./autogen.sh

%configure \
    --disable-static \
    --with-gtk=2.0 \
    --disable-scrollkeeper \
    --enable-introspection

# remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT RUN_QUERY_IMMODULES_TEST=false

rm $RPM_BUILD_ROOT/%{_libdir}/*.la

%find_lang mucharmap

desktop-file-validate ${RPM_BUILD_ROOT}/%{_datadir}/applications/mucharmap.desktop


%files -f mucharmap.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/mucharmap
%{_bindir}/mate-character-map
%{_libdir}/libmucharmap.so.*
%{_datadir}/applications/mucharmap.desktop
%{_libdir}/girepository-1.0/*
%{_datadir}/omf/mucharmap/
%{_datadir}/mate/help/mucharmap/
%{_datadir}/glib-2.0/schemas/org.mate.mucharmap.enums.xml
%{_datadir}/glib-2.0/schemas/org.mate.mucharmap.gschema.xml

%files devel
%{_includedir}/mucharmap-2.0/
%{_libdir}/libmucharmap.so
%{_libdir}/pkgconfig/mucharmap-2.pc
%{_datadir}/gir-1.0/*


%changelog
* Sun Mar 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_0.1.git2464a6c
- new fc release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_1
- renamed to mate-character-map

* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1
- new release

