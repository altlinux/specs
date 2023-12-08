%define module_name Net-DNS-Resolver-Mock
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Net/DNS/Packet.pm) perl(Net/DNS/Question.pm) perl(Net/DNS/Resolver.pm) perl(Net/DNS/ZoneFile.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Test/Pod.pm) perl(base.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.20230216
Release: alt2
Summary: Mock a DNS Resolver object for testing
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MB/MBRADSHAW/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
A subclass of Net::DNS::Resolver which parses a zonefile for it's data source. Primarily for use in testing.

=for markdown [![Code on GitHub](https://img.shields.io/badge/github-repo-blue.svg)](https://github.com/marcbradshaw/Net-DNS-Resolver-Mock)

=for markdown [![Build Status](https://travis-ci.org/marcbradshaw/Net-DNS-Resolver-Mock.svg?branch=master)](https://travis-ci.org/marcbradshaw/Net-DNS-Resolver-Mock)

=for markdown [![Open Issues](https://img.shields.io/github/issues/marcbradshaw/Net-DNS-Resolver-Mock.svg)](https://github.com/marcbradshaw/Net-DNS-Resolver-Mock/issues)

=for markdown [![Dist on CPAN](https://img.shields.io/cpan/v/Net-DNS-Resolver-Mock.svg)](https://metacpan.org/release/Net-DNS-Resolver-Mock)

=for markdown [![CPANTS](https://img.shields.io/badge/cpants-kwalitee-blue.svg)](http://cpants.cpanauthors.org/dist/Net-DNS-Resolver-Mock)
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/N*

%changelog
* Fri Dec 08 2023 Igor Vlasenko <viy@altlinux.org> 1.20230216-alt2
- moved to Sisyphus as perl-Mail-DKIM dep

* Sat Feb 18 2023 Igor Vlasenko <viy@altlinux.org> 1.20230216-alt1
- updated by package builder

* Thu Aug 18 2022 Igor Vlasenko <viy@altlinux.org> 1.20220817-alt1
- updated by package builder

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 1.20200215-alt1
- updated by package builder

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.20171219-alt1
- regenerated from template by package builder

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.20171031-alt1
- regenerated from template by package builder

* Thu Aug 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.20170814-alt1
- initial import by package builder

