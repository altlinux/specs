# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#
# spec file for package libhugetlbfs
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define my_make_flags V=1 CFLAGS="%{optflags} -fPIC" LDFLAGS="-pie" BUILDTYPE=NATIVEONLY PREFIX=%{_prefix} LIBDIR32=%{_libdir} DESTDIR=%{buildroot}
Name:           libhugetlbfs
Version:        2.23.0.g6b126a4
Release:        alt1_3.4
Summary:        Helper library for the Huge Translation Lookaside Buffer Filesystem
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://github.com/libhugetlbfs/libhugetlbfs
Source0:        libhugetlbfs-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         libhugetlbfs.tests-malloc.patch
Patch1:         libhugetlbfs_ia64_fix_missing_test.patch
Patch2:         disable-rw-on-non-ldscripts.diff
Patch3:         zero_filesize_segment.patch
Patch4:         glibc-2.34-fix.patch
BuildRequires:  doxygen
BuildRequires:  glibc-devel glibc-devel-static
# bug437293
%ifarch ppc64
Obsoletes:      libhugetlbfs-64bit
%endif
Source44: import.info
Patch33: libhugetlbfs_loongarch64_basic_support.patch

%description
The libhugetlbfs package interacts with the Linux hugetlbfs to
make large pages available to applications in a transparent manner.

%package devel
Summary:        Development files for libhugetlbfs
Group:          Development/Other
Requires:       %{name} = %EVR

%description devel
Devel package, header and static library, of libhugetlbfs.

%package utils
Group: System/Base
Summary:	Userspace utilities for configuring the hugepage environment
Requires:	%{name} = %EVR

%description utils
This packages contains a number of utilities that will help administrate the
use of huge pages on your system.  hugeedit modifies binaries to set default
segment remapping behavior. hugectl sets environment variables for using huge
pages and then execs the target program. hugeadm gives easy access to huge page
pool size control. pagesize lists page sizes available on the machine.

%files utils
%{_bindir}/hugeedit
%{_bindir}/hugeadm
%{_bindir}/hugectl
%{_bindir}/pagesize
%{_mandir}/man8/hugeedit.8*
%{_mandir}/man8/hugectl.8*
%{_mandir}/man8/hugeadm.8*
%{_mandir}/man1/pagesize.1*
%{_mandir}/man1/ld.hugetlbfs.1*
%{_libdir}/libhugetlbfs_privutils.so


%package tests
Summary:        Tests for package libhugetlbfs
Group:          Development/Tools

%description tests
The testsuite for libhugetlbfs. Binaries can be found in
%{_libdir}/libhugetlbfs/tests.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch33 -p1


%build
echo %{version} > version
make %{my_make_flags}

%install
make %{my_make_flags} PMDIR="%{perl_vendor_privlib}/TLBC" \
	install install-tests
mkdir -p %{buildroot}%{_prefix}/include
cp -avL hugetlbfs.h %{buildroot}%{_prefix}/include
chmod 644 %{buildroot}%{_libdir}/*.a
if [ -f %{buildroot}%{_libdir}/libhugetlbfs/tests/obj64/dummy.ldscript ]; then
	chmod -f a-x %{buildroot}%{_libdir}/libhugetlbfs/tests/obj64/dummy.ldscript
fi
rm -r %{buildroot}%{_libdir}/libhugetlbfs/tests

mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/security/limits.d/hugepages.conf

# remove statically built libraries:
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a


%files
%doc LGPL-2.1 HOWTO README NEWS
%{_datadir}/libhugetlbfs
#%{_bindir}/*
#%{_mandir}/man[178]/*%{?ext_man}
#%{_libdir}/libhugetlbfs_privutils.so
%{_libdir}/libhugetlbfs.so
%{_mandir}/man7/libhugetlbfs.7*
%ghost %config(noreplace) %{_sysconfdir}/security/limits.d/hugepages.conf
%exclude %{_libdir}/libhugetlbfs_privutils.so

%files devel
%{_includedir}/hugetlbfs.h
#%{_libdir}/libhugetlbfs.a
%{_mandir}/man3/*%{?ext_man}

%files tests
%{_libdir}/libhugetlbfs/

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 2.23.0.g6b126a4-alt1_3.4
- merged basic support of LoongArch (lp64d ABI) architecture

* Mon Jul 17 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.23.0.g6b126a4-alt1_2.3
- Basic support of LoongArch (lp64d ABI) architecture

* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 2.23.0.g6b126a4-alt1_2.2
- new version

* Thu May 20 2021 Slava Aseev <ptrnine@altlinux.org> 2.20-alt2_9
- fixed build due to missing rpm-build-python

* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 2.20-alt2_8
- fixed build

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 2.20-alt1_8
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.20-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.20-alt1_3
- update to new release by fcimport

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

