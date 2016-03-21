# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Catalyst-Plugin-Redirect
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_7

Summary:    Redirect for Catalyst used easily is offered
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst.pm)
BuildArch: noarch
Source44: import.info


%description
Redirect for Catalyst used easily is offered.

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
%doc META.yml Changes README
%perl_vendor_privlib/*

%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt3_7
- to Sisyphus

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.02-alt2_3
- rebuild to get rid of unmets

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_3
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_1
- converted for ALT Linux by srpmconvert tools

