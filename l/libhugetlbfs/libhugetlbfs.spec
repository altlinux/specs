%add_optflags %optflags_shared
Name: libhugetlbfs
Version: 2.13
Release: alt1_1
Summary: A library which provides easy access to huge pages of memory

Group: System/Libraries
License: LGPLv2+
URL: http://libhugetlbfs.sourceforge.net/
Source0: http://downloads.sourceforge.net/libhugetlbfs/%{name}-%{version}.tar.gz
Patch0: libhugetlbfs-2.13-s390x-build.patch
BuildRequires: glibc-devel
BuildRequires: glibc-devel-static
Conflicts: kernel < 2.6.16
Obsoletes: libhugetlbfs-test <= 1.1

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
Requires:	libhugetlbfs = %{version}-%{release}
%description devel
Contains header files for building with libhugetlbfs.

%package utils
Summary:	Userspace utilities for configuring the hugepage environment
Group:		File tools
Requires:	libhugetlbfs = %{version}-%{release}
%description utils
This packages contains a number of utilities that will help administrate the
use of huge pages on your system.  hugeedit modifies binaries to set default
segment remapping behavior. hugectl sets environment variables for using huge
pages and then execs the target program. hugeadm gives easy access to huge page
pool size control. pagesize lists page sizes available on the machine.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .s390x-build

%build
# Parallel builds are not reliable
make BUILDTYPE=NATIVEONLY

%install
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LDSCRIPTDIR=%{ldscriptdir} BUILDTYPE=NATIVEONLY
make install-helper PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LDSCRIPTDIR=%{ldscriptdir} BUILDTYPE=NATIVEONLY
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/hugepages.conf

# remove statically built libraries:
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
# remove unused sbin directory
rm -fr $RPM_BUILD_ROOT/%{_sbindir}/

%files
%{_libdir}/libhugetlbfs.so*
%{_datadir}/%{name}/
%{_mandir}/man7/libhugetlbfs.7.*
%ghost %config(noreplace) %{_sysconfdir}/security/limits.d/hugepages.conf
%exclude %{_libdir}/libhugetlbfs_privutils.so
%doc README HOWTO LGPL-2.1 NEWS

%files devel
%{_includedir}/hugetlbfs.h
%{_mandir}/man3/getpagesizes.3.*
%{_mandir}/man3/free_huge_pages.3.*
%{_mandir}/man3/get_huge_pages.3.*
%{_mandir}/man3/gethugepagesizes.3.*
%{_mandir}/man3/free_hugepage_region.3.*
%{_mandir}/man3/get_hugepage_region.3.*

%files utils
%{_bindir}/hugeedit
%{_bindir}/hugeadm
%{_bindir}/hugectl
%{_bindir}/pagesize
%{_bindir}/huge_page_setup_helper.py
%exclude %{_bindir}/cpupcstat
%exclude %{_bindir}/oprofile_map_events.pl
%exclude %{_bindir}/oprofile_start.sh
%{_mandir}/man8/hugeedit.8.*
%{_mandir}/man8/hugectl.8.*
%{_mandir}/man8/hugeadm.8.*
%{_mandir}/man1/pagesize.1.*
%exclude %{_mandir}/man8/cpupcstat.8.gz
%exclude /usr/lib/perl5/TLBC

%changelog
* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.12-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.12-alt2_2
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_2
- initial import by fcimport

