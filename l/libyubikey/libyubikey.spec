Group: Development/Other
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libyubikey
Version:        1.13
Release:        alt1_12
Summary:        C library for decrypting and parsing Yubikey One-time passwords

License:        BSD
URL:            http://opensource.yubico.com/yubico-c
Source0:        http://opensource.yubico.com/yubico-c/releases/%{name}-%{version}.tar.gz
BuildRequires:  gcc
Source44: import.info

%description
This package holds a low-level C software development kit for the Yubico
authentication device, the Yubikey.

%package devel
Group: Development/Other
Summary:        Development files for libyubikey
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the header file needed to develop applications that use
libyubikey.

%prep
%setup -q

%build
%configure --disable-static --disable-silent-rules
# --disable-rpath doesn't work for the configure script
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%check
export LD_LIBRARY_PATH=${RPM_BUILD_DIR}/%{name}-%{version}/.libs
make check

%install
%makeinstall_std INSTALL="install -p"



%files
%doc AUTHORS NEWS ChangeLog README
%doc --no-dereference COPYING
%{_bindir}/modhex
%{_bindir}/ykparse
%{_bindir}/ykgenerate
%{_libdir}/libyubikey.so.0
%{_libdir}/libyubikey.so.0.1.7
%{_mandir}/man1/ykgenerate.1*
%{_mandir}/man1/ykparse.1*
%{_mandir}/man1/modhex.1*

%files devel
%{_includedir}/yubikey.h
%{_libdir}/libyubikey.so

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_12
- update to new release by fcimport

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_11
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_8
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_2
- update to new release by fcimport

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_2
- update to new release by fcimport

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_3
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_1
- initial import by fcimport

