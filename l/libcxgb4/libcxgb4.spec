# BEGIN SourceDeps(oneline):
BuildRequires: libsysfs-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:    libcxgb4
Version: 1.3.3
Release: alt1_5
Summary: Chelsio T4 iWARP HCA Userspace Driver
Group:   System/Libraries
License: GPLv2 or BSD
Url:     http://www.openfabrics.org/
Source:  http://www.openfabrics.org/downloads/cxgb4/%{name}-%{version}.tar.gz
Source1: libcxgb4-modprobe.conf

BuildRequires: libibverbs-devel >= 1.1.3, libtool
Obsoletes: %{name}-devel
ExcludeArch: s390 s390x
Provides: libibverbs-driver.%{_arch}
Source44: import.info

%description
Userspace hardware driver for use with the libibverbs InfiniBand/iWARP verbs
library.  This driver enables Chelsio T4 based iWARP capable Ethernet devices.

%package static
Summary: Static version of the libcxgb4 driver
Group: System/Libraries
Requires: %{name} = %{version}
%description static
Static version of libcxgb4 that may be linked directly to an application.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
install -p -m 644 -D %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/modprobe.d/libcxgb4.conf
# remove unpackaged files from the buildroot
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%{_libdir}/*.so*
%{_sysconfdir}/libibverbs.d/*.driver
%{_sysconfdir}/modprobe.d/libcxgb4.conf
%doc AUTHORS COPYING README

%files static
%{_libdir}/*.a

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_2
- update to new release by fcimport

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_1
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_3
- initial fc import

