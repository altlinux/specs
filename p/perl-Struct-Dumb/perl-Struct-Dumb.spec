%define _unpackaged_files_terminate_build 1
%define module_name Struct-Dumb
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Module/Build.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test2/V0.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.14
Release: alt1
Summary: make simple lightweight record-like structures
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
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
%doc README Changes
%perl_vendor_privlib/S*

%changelog
* Sun Feb 12 2023 Igor Vlasenko <viy@altlinux.org> 0.14-alt1
- automated CPAN update

* Mon Aug 29 2022 Igor Vlasenko <viy@altlinux.org> 0.13-alt1
- automated CPAN update

* Wed Apr 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- moved to Sisyphus as dependency

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

