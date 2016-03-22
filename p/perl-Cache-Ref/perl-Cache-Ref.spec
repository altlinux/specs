# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Cache-Ref
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt4_7

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Cache/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Hash/Util/FieldHash/Compat.pm)
BuildRequires: perl(List/Util.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Moose/Role.pm)
BuildRequires: perl(MooseX/Role/Parameterized.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Test/Moose.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(namespace/autoclean.pm)
BuildRequires: perl(ok.pm)
BuildArch: noarch
Source44: import.info


%description
Unlike the CHI manpage which attempts to address the problem of caching
things persistently, this module implements in memory caching, designed
primarily for *shared references* in memory.

This collection of classes implements a number of semi related algorithms.

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
%doc Changes META.yml LICENSE README META.json
%perl_vendor_privlib/*

%changelog
* Tue Mar 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4_7
- to Sisyphus

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.04-alt3_3
- rebuild to get rid of unmets

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04-alt2_2
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_1
- converted for ALT Linux by srpmconvert tools

