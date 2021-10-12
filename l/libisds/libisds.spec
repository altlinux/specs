# BEGIN SourceDeps(oneline):
BuildRequires: libssl-devel
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Build manual pages
%bcond_without libisds_enables_man
# Support network operations
%bcond_without libisds_enables_net
# Use OpenSSL instead of libgcrypt and gpgme
%bcond_with libisds_enables_openssl
# Perform tests
%bcond_without libisds_enables_test

Name:           libisds
Version:        0.11.1
Release:        alt1_4
Summary:        Library for accessing the Czech Data Boxes
# COPYING:      LGPLv3 text
# README:       LGPLv3+
# src/gettext.h:            GPLv3+
## Not delivered in any binary package
# aclocal.m4:   GPLv2+ with exceptions and FSFULLR
# client/Makefile.in:       FSFULLR
# config.guess: GPLv3+ with exceptions
# config.rpath: FSFULLR
# config.sub:   GPLv3+ with exceptions
# configure:    GPLv2+ with exceptions and FSFUL
# depcomp:      GPLv2+ with exceptions  
# doc/Makefile.in:  FSFULLR
# install-sh:       MIT and Public Domain
# ltmain.sh:        GPLv2+ with exceptions and GPLv3+ and GPLv3+ with exceptions
# m4/gettext.m4:    FSFULLR
# m4/gpgme.m4:      FSFULLR
# m4/iconv.m4:      FSFULLR
# m4/intlmacosx.m4: FSFULLR
# m4/libgcrypt.m4:  FSFULLR
# m4/lib-ld.m4:     FSFULLR
# m4/lib-link.m4:   FSFULLR
# m4/lib-prefix.m4: FSFULLR
# m4/libtool.m4:    GPLv2+ with exceptions and FSFUL
# m4/ltoptions.m4:  FSFULLR
# m4/ltsugar.m4:    FSFULLR
# m4/lt~obsolete.m4:    FSFULLR
# m4/ltversion.m4:  FSFULLR
# m4/nls.m4:        FSFULLR
# m4/po.m4:         FSFULLR
# m4/progtest.m4:   FSFULLR
# Makefile.in:      FSFULLR
# missing:          GPLv2+ with exceptions
# po/Makefile.in.in:    (Something similar to FSFUL)
# src/Makefile.in:          FSFULLR
# test/Makefile.in:         FSFULLR
# test/offline/Makefile.in: FSFULLR
# test/online/Makefile.in:  FSFULLR
# test/simline/Makefile.in: FSFULLR
# test-driver:      GPLv2+ with exceptions
License:        LGPLv3+ and GPLv3+
URL:            http://xpisar.wz.cz/%{name}/
Source0:        %{url}dist/%{name}-%{version}.tar.xz
Source1:        %{url}dist/%{name}-%{version}.tar.xz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-4B528393E6A3B0DFB2EF3A6412C9C5C767C6FAA2.gpg
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
%if %{with libisds_enables_man}
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt xsltproc
%endif
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-tools libasprintf-devel
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  libxml2-devel
%if %{with libisds_enables_net}
BuildRequires:  libcurl-devel
%endif
%if %{with libisds_enables_openssl}
BuildRequires:  openssl
%else
BuildRequires:  gpgme libgpgme-devel
BuildRequires:  libgcrypt-devel
%endif
BuildRequires:  libexpat-devel >= 2.0.0
# Run-time:
%if !%{with libisds_enables_openssl}
BuildRequires:  gnupg2
%endif
# Tests:
%if %{with libisds_enables_test}
BuildRequires:  glibc-gconv-modules
BuildRequires:  libgnutls-devel libgnutlsxx-devel
%endif
%if !%{with libisds_enables_openssl}
Requires:       gnupg2
%endif
Source44: import.info

%description
This is a library for accessing ISDS (InformaA.nA. systA.m datovA.ch schrA.nek /
Data Box Information System) SOAPa..services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%package        devel
Group: Development/C
Summary:        Development files for %{name}
License:        LGPLv3+
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
autoreconf -fi

%build
%configure \
%if %{with libisds_enables_man}
    --enable-doc \
%else
    --disable-doc \
%endif
    --disable-online-test \
%if %{with libisds_enables_openssl}
    --enable-openssl-backend \
%else
    --disable-openssl-backend \
%endif
    --disable-static \
%if %{with libisds_enables_test}
    --enable-test \
%else
    --disable-test \
%endif
%if %{with libisds_enables_net}
    --with-libcurl \
%else
    --without-libcurl \
%endif
    --enable-curlreauthorizationbug
%{make_build}

%check
make check %{?_smp_mflags}

%install
%{makeinstall_std}
find $RPM_BUILD_ROOT -name '*.la' -delete
%find_lang %{name}
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
%{_mandir}/man3/*
%doc client

%changelog
* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 0.11.1-alt1_4
- fc update

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1_1
- update to new release by fcimport

* Sun Mar 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_3
- new version

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

