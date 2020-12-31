Name: npth
Version: 1.6.0.20.g7e45b50
Release: alt3
Summary: The New GNU Portable Threads library

Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://www.gnupg.org/

Source: npth-%version.tar
Patch1: 0001-ALT-version-is-not-beta.patch

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%set_verify_elf_method strict

%description
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth. It has been designed as a replacement of
GNU Pth for non-ancient operating systems. In contrast to GNU Pth is is
based on the system's standard threads implementation. Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

%package -n libnpth
Group: System/Libraries
Summary: %summary

%description -n libnpth
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth. It has been designed as a replacement of
GNU Pth for non-ancient operating systems. In contrast to GNU Pth is is
based on the system's standard threads implementation. Thus nPth allows
the use of libraries which are not compatible to GNU Pth.

%package -n libnpth-devel
Group: Development/C
Summary: Development files for npth
Requires: lib%name = %version-%release

%description -n libnpth-devel
This package contains libraries and header files for
developing applications that use npth.

%prep
%setup -n npth-%version
%autopatch -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

# Manual page is re-used and changed pth-config.1 from libpth-devel package
install -D -pm0644 .rpm/npth-config.1 %buildroot%_man1dir/npth-config.1

%check
make check

%files -n libnpth
%_libdir/libnpth.so.*

%files -n libnpth-devel
%doc AUTHORS NEWS README
%_bindir/npth-config
%_libdir/libnpth.so
%_includedir/npth.h
%_man1dir/npth-config.1*
%_aclocaldir/npth.m4
%_pkgconfigdir/*.pc

%changelog
* Thu Dec 31 2020 Alexey Gladkov <legion@altlinux.ru> 1.6.0.20.g7e45b50-alt3
- Removed the suffix from the version completely.

* Wed Dec 30 2020 Alexey Gladkov <legion@altlinux.ru> 1.6.0.20.g7e45b50-alt2
- Marked version as not beta.

* Sun Dec 27 2020 Alexey Gladkov <legion@altlinux.ru> 1.6.0.20.g7e45b50-alt1
- New version (1.6) and git snapshot.
- Update License tag.

* Sun Feb 04 2018 Fr. Br. George <george@altlinux.ru> 1.5-alt2
- Remove unused buildreq

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_2
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_6
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_5
- initial fc import

