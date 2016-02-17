# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    App-Rad
%define upstream_version 1.05

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_5

Summary:    Extend the App::Rad framework!
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Attribute/Handlers.pm)
BuildRequires: perl(B/Deparse.pm)
BuildRequires: perl(Carp.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(FindBin.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
App::Rad aims to be a simple yet powerful framework for developing your
command-line applications. It can easily transform your Perl _one-liners_
into reusable subroutines than can be called directly by the user of your
program.

It also tries to provide a handy interface for your common command-line
tasks. *If you have a feature request to easen out your tasks even more,
please drop me an email or a RT feature request.*

Extending App::Rad - Plugins!
    App::Rad plugins can be loaded by naming them as arguments to the 'use
    App::Rad' statement. Just ommit the 'App::Rad::Plugin' prefix from the
    plugin name. For example:

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
%doc Changes META.json META.yml  README
%perl_vendor_privlib/*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_3
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_2
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_1
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  1.04-alt1_1
- mageia import by cas@ requiest

