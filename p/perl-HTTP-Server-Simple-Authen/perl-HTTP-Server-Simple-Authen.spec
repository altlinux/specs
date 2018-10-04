Name:           perl-HTTP-Server-Simple-Authen
Version:        0.04
Release:        alt2
Summary:        Authentication plugin for HTTP::Server::Simple
# https://rt.cpan.org/Public/Bug/Display.html?id=71033
# You can redistribute it and/or modify it under the same terms as Perl itself.
License:        GPL+ or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/HTTP-Server-Simple-Authen
Source0:        https://cpan.metacpan.org/modules/by-module/HTTP/HTTP-Server-Simple-Authen-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Authen/Simple.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTTP/Server/Simple.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Authen/Simple/Passwd.pm)
BuildRequires:  perl(MIME/Base64.pm)

Requires:       perl(Authen/Simple.pm) >= 0.040
Requires:       perl(HTTP/Server/Simple.pm) >= 0.160
Requires:       perl(Test/More.pm) >= 0.320

%description
HTTP::Server::Simple::Authen is an HTTP::Server::Simple plugin to allow
HTTP authentication. Authentication scheme is pluggable and you can use
whatever Authentication protocol that Authen::Simple supports.

%prep
%setup -q -n HTTP-Server-Simple-Authen-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%check
make test

%files
%doc Changes
%{perl_vendor_privlib}/HTTP/Server/Simple/*

%changelog
* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.04-alt2
- Initial build for Sisyphus.

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_19
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_18
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_17
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_16
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_15
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_14
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_13
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_12
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_11
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_8
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_6
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_4
- update to new release by fcimport

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- fc import

