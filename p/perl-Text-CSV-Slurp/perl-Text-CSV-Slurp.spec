# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Text-CSV-Slurp
%define upstream_version 1.03

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Convert CSV into an array of hashes, or an array of hashes into CSV
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(IO/File.pm)
BuildRequires: perl(IO/Scalar.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Most.pm)
BuildRequires: perl(Text/CSV.pm)
BuildRequires: perl(lib.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(vars.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
Convert CSV into an array of hashes, or an array of hashes into CSV.

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
%doc Changes LICENSE META.json META.yml  README
%perl_vendor_privlib/*

%changelog
* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_2
- update by mgaimport

* Sat May 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_1
- update by mgaimport

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Mon Sep 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_1
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_3
- update by mgaimport

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_2
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_1
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1
- mageia import by cas@ requiest

