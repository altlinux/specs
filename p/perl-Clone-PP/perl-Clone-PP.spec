# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Benchmark.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name	 Clone-PP
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2_3

Summary:	Recursively copy Perl datatypes
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Clone/%{upstream_name}-%{upstream_version}.tar.bz2


BuildArch:	noarch
Source44: import.info


%description
This module provides a general-purpose clone function to make deep
copies of Perl data structures. It calls itself recursively to copy
nested hash, array, scalar and reference types, including tied
variables and objects.

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
%defattr(644,root,root,755)
%doc README
%{perl_vendor_privlib}/Clone

%changelog
* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2_3
- Sisyphus build

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_3
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_1
- converted for ALT Linux by srpmconvert tools

