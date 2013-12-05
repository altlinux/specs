# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(FindBin.pm) perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Class-Forward
%define upstream_version 0.100006

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2_2

Summary:    A class dispatcher that handles namespaces like paths
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildArch:  noarch
Source44: import.info

%description
Class::Forward is designed to simply return class names or dispatch method
calls using shorthand. It uses file-system path specification conventions
to match against class namespaces.

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
%doc Changes LICENSE META.yml  README
%perl_vendor_privlib/*

%changelog
* Thu Dec 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.100006-alt2_2
- Sisyphus build

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.100006-alt1_2
- mga update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.100006-alt1_1
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.100005-alt1_1
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_1
- converted for ALT Linux by srpmconvert tools

