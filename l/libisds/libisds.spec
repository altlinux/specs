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
Version:        0.11.2
Release:        alt1_5
Summary:        Library for accessing the Czech Data Boxes
# COPYING:      LGPL-3.0 text
# README:       LGPL-3.0-or-later
# src/gettext.h:            GPL-3.0-or-later
## Not delivered in any binary package
# aclocal.m4:   GPL-2.0-or-later WITH Libtool-exception AND FSFULLR
# client/Makefile.in:       FSFULLR
# config.guess: GPL-3.0-or-later WITH Libtool-exception
# config.rpath: FSFULLR
# config.sub:   GPL-3.0-or-later WITH Libtool-exception
# configure:    GPL-2.0-or-later WITH Libtool-exception AND FSFUL
# depcomp:      GPL-2.0-or-later WITH Libtool-exception
# doc/Makefile.in:  FSFULLR
# install-sh:       X11 AND LicenseRef-Fedora-Public-Domain
# ltmain.sh:        GPL-2.0-or-later WITH Libtool-exception AND
#                   GPL-3.0-or-later AND GPL-3.0-or-later WITH Libtool-exception
# m4/gettext.m4:    FSFULLR
# m4/gpgme.m4:      FSFULLR
# m4/iconv.m4:      FSFULLR
# m4/intlmacosx.m4: FSFULLR
# m4/libgcrypt.m4:  FSFULLR
# m4/lib-ld.m4:     FSFULLR
# m4/lib-link.m4:   FSFULLR
# m4/lib-prefix.m4: FSFULLR
# m4/libtool.m4:    GPL-2.0-or-later WITH Libtool-exception AND FSFUL
# m4/ltoptions.m4:  FSFULLR
# m4/ltsugar.m4:    FSFULLR
# m4/lt~obsolete.m4:    FSFULLR
# m4/ltversion.m4:  FSFULLR
# m4/nls.m4:        FSFULLR
# m4/po.m4:         FSFULLR
# m4/progtest.m4:   FSFULLR
# Makefile.in:      FSFULLR
# missing:          GPL-2.0-or-later WITH Libtool-exception
# po/Makefile.in.in:    (Something similar to FSFUL)
# src/Makefile.in:          FSFULLR
# test/Makefile.in:         FSFULLR
# test/offline/Makefile.in: FSFULLR
# test/online/Makefile.in:  FSFULLR
# test/simline/Makefile.in: FSFULLR
# test-driver:      GPL-2.0-or-later WITH Libtool-exception
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
URL:            http://xpisar.wz.cz/%{name}/
Source0:        http://xpisar.wz.cz/%{name}/dist/%{name}-%{version}.tar.xz
Source1:        http://xpisar.wz.cz/%{name}/dist/%{name}-%{version}.tar.xz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
# Adapt tests to changes in curl-7.83, in upstream after 0.11.2,
# <https://github.com/curl/curl/issues/8844>
Patch0:         libisds-0.11.2-tests-Do-not-send-multi-line-HTTP-headers-by-server.patch
# Do not use deprecated CURLOPT_PROGRESSFUNCTION option,
# in upstream after 0.11.2
Patch1:         libisds-0.11.2-Use-CURLOPT_XFERINFOFUNCTION-curl-option-if-availabl.patch
# Fix a use-after-free in an example code, in upstream after 0.11.2
Patch2:         libisds-0.11.2-client-sendxmldoc-Fix-a-use-after-free-on-two-places.patch
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
License:        LGPL-3.0-or-later
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
find %{buildroot} -name '*.la' -delete
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
%{_mandir}/man3/isds.h.*
%{_mandir}/man3/libisds.*
%doc client

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 0.11.2-alt1_5
- update to new release by fcimport

* Sat May 21 2022 Igor Vlasenko <viy@altlinux.org> 0.11.2-alt1_2
- new version

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

