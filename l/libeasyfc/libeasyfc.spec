# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize pkgconfig(freetype2)
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libeasyfc
Version:	0.14.0
Release:	alt1_13
Summary:	Easy configuration generator interface for fontconfig

License:	LGPL-3.0-or-later
URL:		http://tagoh.bitbucket.org/libeasyfc/
Source0:	https://bitbucket.org/tagoh/libeasyfc/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-freetype.patch
Patch1:		%{name}-fix-config.patch

BuildRequires:	glib2-devel libgio libgio-devel gobject-introspection-devel libxml2-devel fontconfig-devel >= 2.12.93 libharfbuzz-devel libharfbuzz-gir-devel libharfbuzz-utils
BuildRequires:	gettext gettext-tools
Requires:	fontconfig >= 2.12.93
Source44: import.info

%description
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

%package	gobject
Group: System/Libraries
Summary:	GObject interface for libeasyfc
Requires:	%{name} = %{version}-%{release}

%description	gobject
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains an interface for GObject.

%package	devel
Group: Development/Other
Summary:	Development files for libeasyfc
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
Requires:	libgio

%description	devel
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains the development files to make any
applications with libeasyfc.

%package	gobject-devel
Group: Development/Other
Summary:	Development files for libeasyfc-gobject
Requires:	%{name}-gobject = %{version}-%{release}
Requires:	pkgconfig
Requires:	libgio

%description	gobject-devel
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains the development files to make any
applications with libeasyfc-gobject.

%prep
%setup -q
%patch0 -p1
%patch1 -p1



%build
%configure --disable-static
%make_build V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la




%files
%doc README AUTHORS ChangeLog
%doc --no-dereference COPYING
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
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.14.0-alt1_13
- update to new release by fcimport

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_6
- update to new release by fcimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_3
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.13.1-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.13.1-alt1_2
- update to new release by fcimport

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

