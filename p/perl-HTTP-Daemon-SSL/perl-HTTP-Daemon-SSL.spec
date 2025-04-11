Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(HTTP/Status.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 57

Name:           perl-HTTP-Daemon-SSL
Version:        1.04
Release:        alt4_%autorelease
Summary:        Simple http server class with SSL support
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Daemon-SSL
Source0:        https://cpan.metacpan.org/modules/by-module/HTTP/HTTP-Daemon-SSL-%{version}.tar.gz
# Adapt tests to IO::Socket::SSL 1.80, CPAN RT#81932
Patch0:         HTTP-Daemon-SSL-1.04-Adapt-tests-to-IO-Socket-SSL-1.80.patch
# Do not test weak keys with OpenSSL 1.0.1, bug #1058728, CPAN RT#88998
Patch1:         HTTP-Daemon-SSL-1.04-Generate-keys-and-certificates-at-test-time.patch

BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTTP/Daemon.pm)
BuildRequires:  perl(IO/Socket/SSL.pm)
BuildRequires:  perl(IO/Socket/SSL/Utils.pm)

Requires:       perl(HTTP/Daemon.pm) >= 1
Requires:       perl(IO/Socket/SSL.pm) >= 0.930
Source44: import.info

%description
Instances of the HTTP::Daemon::SSL class are HTTP/1.1 servers that listen
on a socket for incoming requests. The HTTP::Daemon::SSL is a sub-class of
IO::Socket::SSL, so you can perform socket operations directly on it too.

%prep
%setup -q -n HTTP-Daemon-SSL-%{version}
%patch0  -p1
%patch1  -p1

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc BUGS Changes README
%{perl_vendor_privlib}/*

%changelog
* Fri Apr 11 2025 Igor Vlasenko <viy@altlinux.org> 1.04-alt4_57
- to Sisyphus as Tapper-Reports-Web dep

* Thu Apr 10 2025 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_57
- update to new release by fcimport

* Sat Mar 23 2024 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_45
- update to new release by fcimport

* Thu Aug 31 2023 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_43
- update to new release by fcimport

* Wed Feb 22 2023 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_42
- update to new release by fcimport

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_39
- update to new release by fcimport

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_38
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_37
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_36
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_35
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_34
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 1.04-alt3_33
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_33
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_32
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_31
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_30
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_29
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_28
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_27
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_26
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_25
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_24
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_23
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_22
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_21
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_19
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_18
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_15
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_12
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_9
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_8
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_8
- fc import

