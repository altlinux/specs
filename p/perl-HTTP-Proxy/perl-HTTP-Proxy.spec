Name:           perl-HTTP-Proxy
Version:        0.304
Release:        alt3
Summary:        A pure Perl HTTP proxy
Group:          Development/Other
License:        GPL-1.0-or-later or Artistic-1.0
URL:            https://metacpan.org/release/HTTP-Proxy
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/HTTP-Proxy-%{version}.tar.gz
# Add support for IPv6, bug #1422948, CPAN RT#120275
Patch1:     HTTP-Proxy-0.304-Support-IPv6.patch
# debugging 23connect
Patch2:		HTTP-Proxy-0.303-23connect-logging-debug.patch
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Module/Build.pm), perl(Module/Build/Tiny.pm)
BuildRequires:  perl(Test/Pod.pm), perl(Test/Pod/Coverage.pm), perl(HTML/Parser.pm)
BuildRequires:  perl(HTTP/Daemon.pm), perl(LWP/UserAgent.pm), perl(Crypt/SSLeay.pm)
BuildRequires:  perl(File/Spec.pm), perl(Pod/Coverage/TrustPod.pm), perl(Test/CPAN/Meta.pm)
BuildRequires:  perl(Carp.pm), perl(Exporter.pm), perl(ExtUtils/MakeMaker.pm), perl(Fcntl.pm)
BuildRequires:  perl(File/Spec.pm), perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/Find.pm), perl(File/Path.pm), perl(File/Temp.pm), perl(HTTP/Daemon.pm), perl(HTTP/Date.pm)
BuildRequires:  perl(HTTP/Headers.pm), perl(HTTP/Headers/Util.pm), perl(HTTP/Request.pm), perl(HTTP/Request/Common.pm)
BuildRequires:  perl(IO/Handle.pm), perl(IO/Select.pm), perl(IO/Socket/IP.pm)
BuildRequires:  perl(LWP/ConnCache.pm), perl(LWP/UserAgent.pm), perl(POSIX.pm)
BuildRequires:  perl(Socket.pm), perl(Sys/Hostname.pm), perl(Test/More.pm), perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm), perl(URI.pm), perl(base.pm), perl(constant.pm), perl(strict.pm)
BuildRequires:  perl(vars.pm), perl(version.pm), perl(warnings.pm)
BuildRequires:  perl(CGI/Util.pm)

%description
Its main use should be to record and/or modify web sessions, so as to
help users create web robots, web testing suites, as well as proxy
systems than can transparently alter the requests to and answers from
an origin server.

%prep
%setup -q -n HTTP-Proxy-%{version}
%patch1 -p1
%patch2 -p1 -b .logging

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
#make test

%files
%doc Changes README eg/
%{perl_vendor_privlib}/HTTP/

%changelog
* Mon Oct 05 2020 Andrey Cherepanov <cas@altlinux.org> 0.304-alt3
- Disable tests.

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.304-alt2
- Initial build for Sisyphus

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.304-alt1_10
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.304-alt1_8
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.304-alt1_7
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.304-alt1_6
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.304-alt1_3
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.304-alt1_2
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.304-alt1_1
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.302-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_6
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_1
- fc import

