# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(FindBin.pm) perl(base.pm) perl(sigtrap.pm)
# END SourceDeps(oneline)
Name: libhugetlbfs
Version: 2.20
Release: alt1_2
Summary: A library which provides easy access to huge pages of memory

Group: System/Libraries
License: LGPLv2+
URL: https://github.com/libhugetlbfs/libhugetlbfs
Source0: https://www.mgebm.net/~emunson/%{name}-%{version}.tar.gz

BuildRequires: glibc-devel
BuildRequires: glibc-devel-static

%define ldscriptdir %{_datadir}/%{name}/ldscripts
Source44: import.info

%description
libhugetlbfs is a library which provides easy access to huge pages of memory.
It is a wrapper for the hugetlbfs file system. Applications can use huge pages
to fulfill malloc() requests without being recompiled by using LD_PRELOAD.
Alternatively, applications can be linked against libhugetlbfs without source
modifications to load BSS or BSS, data, and text segments into large pages.

%package devel
Summary:	Header files for libhugetlbfs
Group:		Development/C
Requires:	%{name} = %{version}
%description devel
Contains header files for building with libhugetlbfs.

%package utils
Summary:	Userspace utilities for configuring the hugepage environment
Group:		File tools
Requires:	%{name} = %{version}
%description utils
This packages contains a number of utilities that will help administrate the
use of huge pages on your system.  hugeedit modifies binaries to set default
segment remapping behavior. hugectl sets environment variables for using huge
pages and then execs the target program. hugeadm gives easy access to huge page
pool size control. pagesize lists page sizes available on the machine.

%prep
%setup -q -n %{name}-%{version}

%build
# Parallel builds are not reliable
CFLAGS="%{optflags}" make BUILDTYPE=NATIVEONLY

%install
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LDSCRIPTDIR=%{ldscriptdir} BUILDTYPE=NATIVEONLY
make install-helper PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LDSCRIPTDIR=%{ldscriptdir} BUILDTYPE=NATIVEONLY
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/hugepages.conf

# remove statically built libraries:
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
# remove unused sbin directory
rm -fr $RPM_BUILD_ROOT/%{_sbindir}/

# touching all ghosts; hack for rpm 4.0.4
for rpm_404_ghost in %{_sysconfdir}/security/limits.d/hugepages.conf
do
    mkdir -p %buildroot`dirname "$rpm_404_ghost"`
    touch %buildroot"$rpm_404_ghost"
done


%files
%{_libdir}/libhugetlbfs.so*
%{_datadir}/%{name}/
%{_mandir}/man7/libhugetlbfs.7*
%ghost %config(noreplace) %{_sysconfdir}/security/limits.d/hugepages.conf
%exclude %{_libdir}/libhugetlbfs_privutils.so
%doc README HOWTO LGPL-2.1 NEWS

%files devel
%{_includedir}/hugetlbfs.h
%{_mandir}/man3/getpagesizes.3*
%{_mandir}/man3/free_huge_pages.3*
%{_mandir}/man3/get_huge_pages.3*
%{_mandir}/man3/gethugepagesize.3*
%{_mandir}/man3/gethugepagesizes.3*
%{_mandir}/man3/free_hugepage_region.3*
%{_mandir}/man3/get_hugepage_region.3*
%{_mandir}/man3/hugetlbfs_find_path.3*
%{_mandir}/man3/hugetlbfs_find_path_for_size.3*
%{_mandir}/man3/hugetlbfs_test_path.3*
%{_mandir}/man3/hugetlbfs_unlinked_fd.3*
%{_mandir}/man3/hugetlbfs_unlinked_fd_for_size.3*

%files utils
%{_bindir}/hugeedit
%{_bindir}/hugeadm
%{_bindir}/hugectl
%{_bindir}/pagesize
%{_bindir}/huge_page_setup_helper.py
%exclude %{_bindir}/cpupcstat
%exclude %{_bindir}/oprofile_map_events.pl
%exclude %{_bindir}/oprofile_start.sh
%{_mandir}/man8/hugeedit.8*
%{_mandir}/man8/hugectl.8*
%{_mandir}/man8/hugeadm.8*
%{_mandir}/man1/pagesize.1*
%{_mandir}/man1/ld.hugetlbfs.1*
%exclude %{_mandir}/man8/cpupcstat.8*
%exclude %{_libdir}/perl5/TLBC

%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.20-alt1_2
- fixed build

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.19-alt1_1
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1_4
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1_3
- update to new release by fcimport

* Fri Jun 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1_2
- converted for ALT Linux by srpmconvert tools

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.17-alt1_1
- update to new release by fcimport

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 2.16-alt1_2
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 2.16-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1_2
- update to new release by fcimport

* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1_2
- update to new release by fcimport

* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.12-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.12-alt2_2
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_2
- initial import by fcimport

