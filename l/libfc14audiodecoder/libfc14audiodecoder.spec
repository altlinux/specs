# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name: libfc14audiodecoder
Version: 1.0.2
Release: alt2_4

Summary: C wrapper library for Future Composer audio decoding
Group: System/Libraries
License: GPLv2+
URL: http://xmms-fc.sourceforge.net
Source0: http://downloads.sourceforge.net/xmms-fc/%{name}-%{version}.tar.bz2
Source44: import.info

%description
This library provides a C API for a Future Composer audio decoder, which
has been used in several plug-ins for versatile audio players like XMMS,
BMP, Audacious and GStreamer.


%package devel
Summary: Files needed for developing with %{name}
Group: Development/C
Requires: libfc14audiodecoder = %{version}-%{release}

%description devel
This package contains the files that are needed when building
software that uses %{name}.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"


%files
%doc COPYING README
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/fc14audiodecoder.h


%changelog
* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_4
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2
- initial import by fcimport

