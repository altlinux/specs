%define _unpackaged_files_terminate_build 1
%define module_name Filter-signatures
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Filter/Simple.pm) perl(Pod/Markdown.pm) perl(Test/More.pm) perl(Text/Balanced.pm) perl(feature.pm) perl(warnings.pm) perl(warnings/register.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.19
Release: alt1
Summary: very simplicistic signatures for Perl < 5.20
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/C/CO/CORION/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
use Filter::signatures;
    no warnings 'experimental::signatures'; # does not raise an error
    use feature 'signatures'; # this now works on <5.16 as well
    
    sub hello( $name ) {
        print "Hello $name\n";
    }
    
    hello("World");
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.mkdn Changes README
%perl_vendor_privlib/F*

%changelog
* Fri Jul 28 2023 Igor Vlasenko <viy@altlinux.org> 0.19-alt1
- automated CPAN update

* Tue Oct 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- to Sisyphus as Spreadsheet-ReadSXC dep

* Fri Aug 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- updated by package builder

* Sat Aug 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Fri Jul 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- regenerated from template by package builder

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- regenerated from template by package builder

* Mon Mar 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- regenerated from template by package builder

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- regenerated from template by package builder

* Thu Dec 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Wed Oct 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Sun Sep 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

