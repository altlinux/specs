%define module_name Shell-Guess
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Test/More.pm) perl(Unix/Process.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt2
Summary: Make an educated guess about the shell in use
Group: Development/Perl
License: perl
URL: https://metacpan.org/pod/Shell::Guess

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
%doc README LICENSE Changes author.yml
%perl_vendor_privlib/S*

%changelog
* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- to Sisyphus

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Thu Aug 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Tue May 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- regenerated from template by package builder

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

