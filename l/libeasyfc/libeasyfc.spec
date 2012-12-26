# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize pkgconfig(freetype2)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libeasyfc
Version:	0.10
Release:	alt1_1
Summary:	Easy configuration generator interface for fontconfig

Group:		System/Libraries
License:	LGPLv3+
URL:		http://tagoh.bitbucket.org/libeasyfc/
Source0:	https://bitbucket.org/tagoh/libeasyfc/downloads/%{name}-%{version}.tar.bz2

BuildRequires:	glib2-devel gobject-introspection-devel libxml2-devel fontconfig-devel >= 2.9.91
BuildRequires:	gettext
Requires:	fontconfig >= 2.9.91
Source44: import.info

%description
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

%package	gobject
Summary:	GObject interface for libeasyfc
Group:		System/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	gobject
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains an interface for GObject.

%package	devel
Summary:	Development files for libeasyfc
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains the development files to make any
applications with libeasyfc.

%package	gobject-devel
Summary:	Development files for libeasyfc-gobject
Group:		Development/C
Requires:	%{name}-gobject%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description	gobject-devel
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains the development files to make any
applications with libeasyfc-gobject.

%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


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

