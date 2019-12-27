Group: Development/C
%add_optflags %optflags_shared
%define fedora 30
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# -*- rpm-spec -*-

%global with_gir 0

%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%global with_gir 1
%endif

Summary: A GObject library for interacting with oVirt REST API
Name: libgovirt
Version: 0.3.6
Release: alt1_1
License: LGPLv2+
Source0: http://ftp.gnome.org/pub/GNOME/sources/libgovirt/0.3/%{name}-%{version}.tar.xz
URL: https://gitlab.gnome.org/GNOME/libgovirt
BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: intltool
BuildRequires: librest-devel librest-gir-devel
%if %{with_gir}
BuildRequires: gobject-introspection-devel
%endif
#needed for make check
BuildRequires: glib-networking
BuildRequires: dconf libdconf
Source44: import.info

%description
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package devel
Group: Development/C
Summary: Libraries, includes, etc. to compile with the libgovirt library
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: libgio

%description devel
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

Libraries, includes, etc. to compile with the libgovirt library

%prep
%setup -q

%build
%if %{with_gir}
%global gir_arg --enable-introspection=yes
%else
%global gir_arg --enable-introspection=no
%endif

%configure %{gir_arg}
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la
%find_lang %{name} --with-gnome

%check
make check



%files -f %{name}.lang
%doc AUTHORS COPYING MAINTAINERS README
%{_libdir}/%{name}.so.2*
%if %{with_gir}
%{_libdir}/girepository-1.0/GoVirt-1.0.typelib
%endif

%files devel
%{_libdir}/%{name}.so
%dir %{_includedir}/govirt-1.0/
%dir %{_includedir}/govirt-1.0/govirt/
%{_includedir}/govirt-1.0/govirt/*.h
%{_libdir}/pkgconfig/govirt-1.0.pc
%if %{with_gir}
%{_datadir}/gir-1.0/GoVirt-1.0.gir
%endif

%changelog
* Fri Dec 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.6-alt1_1
- update to new release by fcimport

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_8
- fixed build

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_7
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_2
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.4-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_2
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_4
- update to new release by fcimport

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_2
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_1
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1_2
- initial fc import

