%add_optflags %optflags_shared
Name:      libmkv
Version:   0.6.5.1
Release:   alt2_9
Summary:   An alternative to the official libmatroska library

Group:     System/Libraries
License:   GPLv2+
URL:       https://github.com/saintdev/libmkv
# https://github.com/saintdev/libmkv/tarball/0.6.5.1
Source0:   %{name}-%{version}.tar.gz

# From HandBrake sources
Patch0:    A01-hbmv-pgs.patch


BuildRequires: autoconf, automake, libtool
Source44: import.info

%description
This library is meant to be an alternative to the official libmatroska library.
It is written in plain C, and is intended to be very portable.

%prep
%setup -q -n saintdev-libmkv-d2906c0

%patch0 -p1 -b .hbmv_pgm

%build
# bug in autotools requires missing m4 directory
mkdir m4
autoreconf --verbose --force --install
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%{_libdir}/libmkv.so.*
%doc AUTHORS COPYING README

%package devel
Summary:   An alternative to the official libmatroska library - devel files
Group:     Development/C
Requires:  %{name} = %{version}

%description devel
This library is meant to be an alternative to the official libmatroska library.
It is writen in plain C, and is intended to be very portable.  These are the
development files.

%files devel
%{_includedir}/libmkv.h
%{_libdir}/libmkv.so

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt2_8
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt2_6
- update to new release by fcimport

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt2_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt2_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt2_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt2_2
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt2_1
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.5.1-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.4.1-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.4.1-alt1_1
- initial import by fcimport

