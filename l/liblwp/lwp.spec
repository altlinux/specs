%add_optflags %optflags_shared
%define oldname lwp
Name:           liblwp
Version:        2.6
Release:        alt1_13
Summary:        C library for user-mode threading
Group:          System/Libraries
License:        LGPLv2
URL:            http://www.coda.cs.cmu.edu/
Source0:        ftp://ftp.coda.cs.cmu.edu/pub/lwp/src/%{oldname}-%{version}.tar.gz
Source1:        ftp://ftp.coda.cs.cmu.edu/pub/lwp/src/%{oldname}-%{version}.tar.gz.asc
Patch0:         lwp-2.6-no-longjmp_chk.patch
Patch1:		lwp-2.6-system-valgrind.h
BuildRequires:	valgrind-devel
Source44: import.info
Provides: lwp = %{version}-%{release}

%description
The LWP user-space threads library. The LWP threads library is used by the Coda
distributed file-system, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library).

%package        devel
Summary:        Development files for %{oldname}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}
Provides: lwp-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1 -b .nolongjmpchk
%patch1 -p1 -b .system-valgrind

# using system header
rm -rf src/valgrind.h

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
./src/testlwp 2

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{oldname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{oldname}.pc

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_12
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_8
- update to new release by fcimport

* Sat Apr 27 2013 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_7
- initial fc import

