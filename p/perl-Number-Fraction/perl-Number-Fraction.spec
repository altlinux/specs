# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-macros-mageia-compat
BuildRequires: perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Number-Fraction
%define upstream_version v3.0.3

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    3.0.3
Release:    alt1_1

Summary:    Perl extension to model fractions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/Number/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Moo.pm)
BuildRequires: perl(MooX/Types/MooseLike/Base.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Warn.pm)
BuildRequires: perl(overload.pm)
BuildArch:  noarch
Source44: import.info

%description
Number::Fraction allows you to work with fractions (i.e. rational numbers)
in your Perl programs in a very natural way.

It was originally written as a demonstration of the techniques of
overloading.

If you use the module in your program in the usual way

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make_build test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml  README
%perl_vendor_privlib/*

%changelog
* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_1
- update by mgaimport

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1
- automated CPAN update

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1_3
- update by mgaimport

* Sun Mar 11 2018 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1_1
- update by mgaimport

* Fri Mar 09 2018 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_6
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_3
- update by mgaimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2_2
- moved to Sisyphus

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_2
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1_1
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_1
- converted for ALT Linux by srpmconvert tools

