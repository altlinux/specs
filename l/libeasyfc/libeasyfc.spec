# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize pkgconfig(fontconfig) pkgconfig(freetype2) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(harfbuzz) pkgconfig(libxml-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libeasyfc
Version:	0.13.1
Release:	alt1_1
Summary:	Easy configuration generator interface for fontconfig

Group:		System/Libraries
License:	LGPLv3+
URL:		http://tagoh.bitbucket.org/libeasyfc/
Source0:	https://bitbucket.org/tagoh/libeasyfc/downloads/%{name}-%{version}.tar.bz2

BuildRequires:	glib2-devel gobject-introspection-devel libxml2-devel fontconfig-devel >= 2.10.92 libharfbuzz-devel
BuildRequires:	gettext
Requires:	fontconfig >= 2.10.92
Source44: import.info

%description
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

%package	gobject
Summary:	GObject interface for libeasyfc
Group:		System/Libraries
Requires:	%{name}%{?_isa} = %{version}

%description	gobject
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains an interface for GObject.

%package	devel
Summary:	Development files for libeasyfc
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}
Requires:	pkgconfig

%description	devel
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains the development files to make any
applications with libeasyfc.

%package	gobject-devel
Summary:	Development files for libeasyfc-gobject
Group:		Development/C
Requires:	%{name}-gobject%{?_isa} = %{version}
Requires:	%{name}-devel%{?_isa} = %{version}
Requires:	pkgconfig

%description	gobject-devel
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains the development files to make any
applications with libeasyfc-gobject.

%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%doc README AUTHORS COPYING ChangeLog
%{_libdir}/libeasyfc.so.*

%files	gobject
%{_libdir}/libeasyfc-gobject.so.*
%{_libdir}/girepository-*/Easyfc-*.typelib

%files	devel
%{_includedir}/libeasyfc
%exclude %{_includedir}/libeasyfc/ezfc-gobject.h
%{_libdir}/libeasyfc.so
%{_libdir}/pkgconfig/libeasyfc.pc
%{_datadir}/gtk-doc/html/libeasyfc

%files	gobject-devel
%{_includedir}/libeasyfc/ezfc-gobject.h
%{_libdir}/libeasyfc-gobject.so
%{_libdir}/pkgconfig/libeasyfc-gobject.pc
%{_datadir}/gir-*/Easyfc-*.gir

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.13.1-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_6
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_1
- update to new release by fcimport

* Sat Apr 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.12.1-alt1_1
- fixed build

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_1
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_1
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_1
- spec cleanup thanks to ldv@

* Tue Dec 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_1
- update to new release by fcimport

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_1
- initial import by fcimport

