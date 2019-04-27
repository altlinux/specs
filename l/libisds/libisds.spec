# BEGIN SourceDeps(oneline):
BuildRequires: libssl-devel
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libisds
Version:        0.10.8
Release:        alt1_4
Summary:        Library for accessing the Czech Data Boxes
License:        LGPLv3
URL:            http://xpisar.wz.cz/%{name}/
Source0:        %{url}dist/%{name}-%{version}.tar.xz
# 1/3 Adapt tests missing en_US.UTF-8 locale, in upstream after 0.10
Patch0:         libisds-0.10.8-test-Allow-skipping-tests.patch
# 2/3 Adapt tests missing en_US.UTF-8 locale, in upstream after 0.10
Patch1:         libisds-0.10-test-Skip-tests-in-offline-utf82locale-if-a-locale-i.patch
# 3/3 Adapt tests missing en_US.UTF-8 locale, in upstream after 0.10
Patch2:         libisds-0.10-test-Try-C.UTF-8-in-offline-utf82locale-test.patch
# Adapt tests to GnuTLS 3.6.4, bug #1651213, in upstream after 0.10
Patch3:         libisds-0.10-Test-Accept-IE_NETWORK-error-when-client-does-not-pr.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  libcurl-devel
BuildRequires:  gcrypt-utils libgcrypt-devel
BuildRequires:  gpgme libgpgme-devel
BuildRequires:  libexpat-devel >= 2.0.0
# Run-time:
BuildRequires:  gnupg2
# Tests:
BuildRequires:  libgnutls-devel libgnutlsxx-devel
Requires:       gnupg2
Source44: import.info

%description
This is a library for accessing ISDS (InformaA.nA. systA.m datovA.ch schrA.nek /
Data Box Information System) SOAPa..services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure \
    --disable-openssl-backend \
    --disable-static \
    --enable-test \
    --with-libcurl \
    --enable-curlreauthorizationbug
%{make_build}

%check
make check %{?_smp_mflags}

%install
%{makeinstall_std}
find $RPM_BUILD_ROOT -name '*.la' -delete
%find_lang %{name}
mv doc specification
# Remove multilib unsafe files
rm -rf client/.deps client/Makefile{,.in}

%files -f %{name}.lang
%doc --no-dereference COPYING
%doc README AUTHORS NEWS TODO
%{_libdir}/libisds.so.5
%{_libdir}/libisds.so.5.*

%files devel
%{_includedir}/isds.h
%{_libdir}/libisds.so
%{_libdir}/pkgconfig/%{name}.pc
%doc client specification

%changelog
* Sat Apr 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.8-alt1_4
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.8-alt1_1
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.7-alt1_4
- update to new release by fcimport

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.7-alt1_2
- new version

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.10.3-alt1_1
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.10.2-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- update to new release by fcimport

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_4
- update to new release by fcimport

* Tue Apr 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_2
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_1
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt3_3
- update to new release by fcimport

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- initial import by fcimport

