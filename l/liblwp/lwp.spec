%add_optflags %optflags_shared
%define oldname lwp
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           liblwp
Version:        2.6
Release:        alt2_16
Summary:        C library for user-mode threading
Group:          System/Libraries
License:        LGPLv2
URL:            http://www.coda.cs.cmu.edu/
Packager:       Igor Vlasenko <viy@altlinux.ru>

Source0:        ftp://ftp.coda.cs.cmu.edu/pub/lwp/src/%{oldname}-%{version}.tar.gz
Source1:        ftp://ftp.coda.cs.cmu.edu/pub/lwp/src/%{oldname}-%{version}.tar.gz.asc
Source2:        fake_valgrind.h
Patch0:         lwp-2.6-no-longjmp_chk.patch
Patch1:		lwp-2.6-system-valgrind.h

BuildRequires:  rpm-macros-valgrind
%ifarch %valgrind_arches
BuildRequires:	valgrind-devel valgrind-tool-devel
%endif

Source44: import.info
Provides: lwp = %{version}-%{release}

%description
The LWP user-space threads library. The LWP threads library is used by the Coda
distributed file-system, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library).

%package        devel
Summary:        Development files for %{oldname}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Provides: lwp-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1 -b .nolongjmpchk
%ifarch %valgrind_arches
%patch1 -p1 -b .system-valgrind
# using system header
rm -rf src/valgrind.h
%else
cp -f "%SOURCE2" src/valgrind.h
%endif

%build
%configure --disable-static
%make_build

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
* Thu Sep 12 2024 Ivan A. Melnikov <iv@altlinux.org> 2.6-alt2_16
- NMU: build w/o valgrind on architectures it does not support

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_16
- update to new release by fcimport

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

