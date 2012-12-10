# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Object-Enum
%define upstream_version 0.072

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Perl Enum Replacement
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Object/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class/Accessor/Fast.pm)
BuildRequires: perl(Class/Data/Inheritable.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Sub/Exporter.pm)
BuildRequires: perl(Sub/Install.pm)
BuildRequires: perl(Test/More.pm)
BuildArch: noarch
Source44: import.info

%description
Implements enums in Perl in a robust manner.

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
%doc README Changes META.yml
%perl_vendor_privlib/*




%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.072-alt1_2
- mageia import by cas@ requiest

