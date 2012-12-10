# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Devel-Platform-Info
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Retrieve Solaris platform metadata
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(IO/File.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
This module is a wrapper to the drivers which can determine platform
metadata regarding the currently running operating system.

The intention of this distribution is to provide key identifying components
regarding the platform currently being used, for the CPAN Testers test
reports. Currently the reports do not often contain enough information to
help authors understand specific failures, where the platform may be a
factor.

However, it is hoped that this distribution will find more uses far beyond
the usage for CPAN Testers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml  README examples
%perl_vendor_privlib/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.11-alt1_1
- mageia import by cas@ requiest

