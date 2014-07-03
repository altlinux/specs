# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname net6
Name:           libnet6
Version:        1.3.14
Release:        alt1_6
Summary:        A TCP protocol abstraction for library C++

Group:          Development/C
License:        LGPLv2
URL:            http://releases.0x539.de/net6/
Source0:        http://releases.0x539.de/net6/%{oldname}-%{version}.tar.gz

BuildRequires:  libsigc++2-devel libgnutls-devel
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
Requires:       %{name} = %{version}-%{release}
Provides: net6-devel = %{version}-%{release}

%description devel
net6 is a library which eases the development of network-based applications
as it provides a TCP protocol abstraction for C++. It is portable to both
the Windows and Unix-like platforms.

This package contains the header files for the use of the net6 development
library.


%prep
%setup -n %{oldname}-%{version} -q


%build
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
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_5
- update to new release by fcimport

* Sat Apr 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1_4
- initial fc import

