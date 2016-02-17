# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Class/Accessor/Fast.pm) perl(ExtUtils/MakeMaker.pm) perl(Module/Build.pm) perl(base.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Devel-Backtrace
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_8

Summary:    Object-oriented backtrace
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class/Accessor.pm)
BuildRequires: perl(String/Escape.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Module/Build/Compat.pm)
BuildArch: noarch
Source44: import.info


%description
This class is a nice way to access all the information caller provides on a
given level.  It is used by L<Devel::Backtrace>, which generates an array of
all trace points.

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
%doc Changes META.yml LICENSE README
%perl_vendor_privlib/*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_8
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_5
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.12-alt1_1
- mageia import by cas@ requiest

