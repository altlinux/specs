%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl-devel perl-podlators perl(TAP/Formatter/HTML.pm)
# END SourceDeps(oneline)
BuildRequires: perl(YAML/Syck.pm) perl(parent.pm)
%define upstream_name    Tapper-TAP-Harness
%define upstream_version 5.0.5

Name:       perl-%{upstream_name}
Version:    5.0.5
Release:    alt1

Summary:    Tapper - Tapper specific TAP handling
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/T/TA/TAPPER/Tapper-TAP-Harness-%{version}.tar.gz

BuildRequires: perl(Archive/Tar.pm)
BuildRequires: perl(Class/XSAccessor.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(Directory/Scratch.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(IO/Scalar.pm)
BuildRequires: perl(IO/String.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(TAP/DOM.pm)
BuildRequires: perl(TAP/Parser.pm)
BuildRequires: perl(TAP/Parser/Aggregator.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(YAML/Tiny.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
This package provides a Tapper-specific TAP handling.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.json META.yml Changes LICENSE README
%perl_vendor_privlib/*




%changelog
* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.5-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1
- automated CPAN update

* Mon Dec 28 2015 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1
- automated CPAN update

* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_5
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

