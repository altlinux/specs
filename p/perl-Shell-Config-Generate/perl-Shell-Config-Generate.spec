%define module_name Shell-Config-Generate
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Shell/Guess.pm) perl(Test2/API.pm) perl(Test2/Mock.pm) perl(Test2/V0.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.31
Release: alt2
Summary: Portably generate config for any shell
Group: Development/Perl
License: perl
URL: https://metacpan.org/pod/Shell::Config::Generate

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PL/PLICEASE/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE author.yml Changes example
%perl_vendor_privlib/S*

%changelog
* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2
- to Sisyphus

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- regenerated from template by package builder

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- regenerated from template by package builder

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- regenerated from template by package builder

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- regenerated from template by package builder

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- regenerated from template by package builder

* Tue Apr 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- regenerated from template by package builder

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- regenerated from template by package builder

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- regenerated from template by package builder

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial import by package builder

