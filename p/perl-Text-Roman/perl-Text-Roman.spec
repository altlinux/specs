# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Text-Roman
%define upstream_version 3.5

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_6

Summary:    Allows conversion between Roman and Arabic algarisms
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Find.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Simple.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
This package supports both conventional Roman algarisms (which range from 1 to
3999) and Milhar Romans, a variation which uses a bar across the algarism to
indicate multiplication by 1,000. For the purposes of this module, acceptable
syntax consists of an underscore suffixed to the algarism e.g. IV_V = 4,005.
The term Milhar apparently derives from the Portuguese word for "thousands" and
the range of this notation extends the range of Roman numbers to 3999 x 1000 +
3999 = 4,002,999.

Note: the functions in this package treat Roman algarisms in a case-insensitive
manner such that "VI" == "vI" == "Vi" == "vi".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml  README eg
%{perl_vendor_privlib}/Text

%changelog
* Sun Jan 07 2018 Igor Vlasenko <viy@altlinux.ru> 3.5-alt3_6
- to Sisyphus as biber dep

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 3.5-alt2_6
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 3.5-alt2_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 3.5-alt2_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.5-alt2_3
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 3.5-alt2_2
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_2
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_1
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1_1
- converted for ALT Linux by srpmconvert tools

