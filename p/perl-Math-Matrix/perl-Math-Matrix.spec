# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Config.pm) perl(Test.pm) perl(overload.pm) perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Math-Matrix
%define upstream_version 0.8

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_4

Summary:    Matrix data type (transpose, multiply etc)
License:    GPL or Artistic
Group:      Development/Perl
Source0:     http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz
Url:        http://search.cpan.org/dist/%{upstream_name}

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl-devel
BuildArch:  noarch
Source44: import.info

%description
The following methods are available: concat, transpose, etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc META.yml  README
%perl_vendor_privlib/*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_4
- update by mgaimport

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- update by mgaimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- moved to Sisyphus

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_4
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_3
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_2
- converted for ALT Linux by srpmconvert tools

