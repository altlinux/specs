%define _unpackaged_files_terminate_build 1
%define module_name Mail-AuthenticationResults
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(Pod/Coverage/TrustPod.pm) perl(Scalar/Util.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(base.pm) perl(lib.pm) perl(strict.pm) perl(warnings.pm) perl(JSON.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.20230112
Release: alt1
Summary: Object Oriented Authentication-Results header class
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MB/MBRADSHAW/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Object Oriented Authentication-Results email headers

=for markdown [![Code on GitHub](https://img.shields.io/badge/github-repo-blue.svg)](https://github.com/marcbradshaw/Mail-AuthenticationResults)

=for markdown [![Build Status](https://travis-ci.org/marcbradshaw/Mail-AuthenticationResults.svg?branch=master)](https://travis-ci.org/marcbradshaw/Mail-AuthenticationResults)

=for markdown [![Open Issues](https://img.shields.io/github/issues/marcbradshaw/Mail-AuthenticationResults.svg)](https://github.com/marcbradshaw/Mail-AuthenticationResults/issues)

=for markdown [![Dist on CPAN](https://img.shields.io/cpan/v/Mail-AuthenticationResults.svg)](https://metacpan.org/release/Mail-AuthenticationResults)

=for markdown [![CPANTS](https://img.shields.io/badge/cpants-kwalitee-blue.svg)](http://cpants.cpanauthors.org/dist/Mail-AuthenticationResults)

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README README.md Changes
%perl_vendor_privlib/M*

%changelog
* Mon Jan 16 2023 Igor Vlasenko <viy@altlinux.org> 2.20230112-alt1
- automated CPAN update

* Fri Sep 17 2021 Igor Vlasenko <viy@altlinux.org> 2.20210915-alt1
- automated CPAN update

* Fri Jan 15 2021 Igor Vlasenko <viy@altlinux.ru> 2.20210112-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.20200824.1-alt1
- automated CPAN update

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 1.20200331.1-alt1
- automated CPAN update

* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 1.20200108-alt1
- automated CPAN update

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.20180923-alt2
- to Sisyphus as MAIL-DCIM dep

* Tue Oct 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.20180923-alt1
- regenerated from template by package builder

* Mon May 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.20180518-alt1
- regenerated from template by package builder

* Sat Mar 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.20180328-alt1
- regenerated from template by package builder

* Wed Mar 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.20180314-alt1
- regenerated from template by package builder

* Sat Feb 17 2018 Igor Vlasenko <viy@altlinux.ru> 1.20180215-alt1
- regenerated from template by package builder

* Tue Feb 13 2018 Igor Vlasenko <viy@altlinux.ru> 1.20180211-alt1
- regenerated from template by package builder

* Sun Jan 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.20180113-alt1
- regenerated from template by package builder

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.20171226-alt1
- initial import by package builder

