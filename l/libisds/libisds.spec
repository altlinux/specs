# BEGIN SourceDeps(oneline):
BuildRequires: libssl-devel
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libisds
Version:        0.10.7
Release:        alt1_2
Summary:        Library for accessing the Czech Data Boxes
License:        LGPLv3
URL:            http://xpisar.wz.cz/%{name}/
Source0:        %{url}dist/%{name}-%{version}.tar.xz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-common
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
Requires:       pkg-config

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure \
    --disable-openssl-backend \
    --disable-static \
    --enable-test \
    --with-libcurl \
    --enable-curlreauthorizationbug
%make_build

%check
make check %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete
%find_lang %{name}
mv doc specification
# Remove multilib unsafe files
rm -rf client/.deps client/Makefile{,.in}

%files -f %{name}.lang
%doc COPYING
%doc README AUTHORS NEWS TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/isds.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%doc client specification

%changelog
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

