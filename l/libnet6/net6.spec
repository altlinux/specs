# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(gnutls) pkgconfig(sigc++-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname net6
Name:           libnet6
Version:        1.3.14
Release:        alt1_12
Summary:        A TCP protocol abstraction for library C++

Group:          Development/C
License:        LGPLv2
URL:            http://releases.0x539.de/net6/
Source0:        http://releases.0x539.de/net6/%{oldname}-%{version}.tar.gz
Patch1:         net6-1.3.14-drop-deprecated-gnutls-call.patch

BuildRequires:  libsigc++2-devel, libgnutls-devel
Requires:       libgnutls
Source44: import.info
Provides: net6 = %{version}-%{release}

%description
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.


%package devel
Summary:        Development libraries for net6
Group:          Development/C
Requires:       %{name} = %{version}
Requires:       pkgconfig
Provides: net6-devel = %{version}-%{release}

%description devel
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.

This package contains the header files for the use of the net6 development
library.


%prep
%setup -n %{oldname}-%{version} -q
%patch1 -p1


%build
# Build in C++11 mode as glibmm headers use C++11 features. This can be dropped
# when GCC in Fedora switches to C++11 by default (with GCC 6, most likely).
export CXXFLAGS="%{optflags} -std=c++11"

%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %oldname


%files -f %{oldname}.lang
%doc README AUTHORS ChangeLog COPYING NEWS
%{_libdir}/*.so.*

%files devel
%{_includedir}/net6
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_12
- update to new release by fcimport

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_11
- new version

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_8
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_5
- update to new release by fcimport

* Sat Apr 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_4
- initial fc import

