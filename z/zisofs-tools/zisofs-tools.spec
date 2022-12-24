Group: System/Base
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: Utilities for creating compressed CD-ROM filesystems
Name: zisofs-tools
Version: 1.0.8
Release: alt2_29
License: GPL+
URL: http://www.kernel.org/pub/linux/utils/fs/zisofs/
#Source: http://www.kernel.org/pub/linux/utils/fs/zisofs/zisofs-tools-%{version}.tar.bz2
Source: http://mirror.linux.org.au/linux/utils/fs/zisofs/zisofs-tools-%{version}.tar.bz2
Patch0: zisofs-tools-configure-c99.patch
BuildRequires:  gcc
BuildRequires: zlib-devel
Source44: import.info
Conflicts: mkzftree < 1.0.8
Obsoletes: mkzftree < 1.0.8
Provides: mkzftree = %version

%description
A utility which works in combination with an appropriately patched
version of mkisofs to allow the creation of compressed CD-ROM
filesystems.

%prep
%setup -q
%patch0 -p1


%build
%configure
%make_build

%install
make install INSTALLROOT="$RPM_BUILD_ROOT"

%files
%doc README zisofs.magic COPYING
%{_bindir}/mkzftree
%{_mandir}/man1/mkzftree.1*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.0.8-alt2_29
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_18
- update to new release by fcimport

* Wed Sep 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_15
- to Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_15
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_14
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_13
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_12
- update to new release by fcimport

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_11
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_10
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_9
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_8
- update to new release by fcimport

* Tue May 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_7
- first import

