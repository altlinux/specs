%define _unpackaged_files_terminate_build 1
%define module_name Test-Timer
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(Carp.pm) perl(English.pm) perl(Error.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Module/Build.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/Builder.pm) perl(Test/Builder/Module.pm) perl(Test/CPAN/Changes.pm) perl(Test/Exception.pm) perl(Test/Kwalitee.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(Test/Tester.pm) perl(Test/Fatal.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators perl(JSON/PP.pm)

Name: perl-%module_name
Version: 2.09
Release: alt1
Summary: a test module to test/assert response times
Group: Development/Perl
License: artistic_2
URL: http://logiclab.jira.com/wiki/display/TESTT/Home

Source0: http://www.cpan.org/authors/id/J/JO/JONASBN/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_privlib/T*

%changelog
* Mon Jan 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Thu Sep 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- to Sisyphus

* Sun Aug 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- regenerated from template by package builder

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- regenerated from template by package builder

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

