# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
%add_findreq_skiplist %perl_vendor_privlib/Tapper/Config.pm
BuildRequires: perl-Tapper
%define upstream_name    Tapper-Config
%define upstream_version 4.1.3

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_3

Summary:    Tapper - Context sensitive configuration hub for all Tapper libs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(Hash/Merge/Simple.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
Tapper-Config provides a context-sensitive configuration hub for all Tapper
libraries.

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
* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

