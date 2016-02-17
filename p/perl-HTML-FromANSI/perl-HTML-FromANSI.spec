# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(Scalar/Util.pm) perl(base.pm) perl(ok.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    HTML-FromANSI
%define upstream_version 2.03

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_7

Summary:    Mark up ANSI sequences as HTML
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(HTML/Entities.pm)
BuildRequires: perl(Term/VT102/Boundless.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/use/ok.pm)
BuildArch: noarch
Source44: import.info

%description
This small module converts ANSI text sequences to corresponding HTML codes,
using stylesheets to control color and blinking properties.

It exports 'ansi2html()' by default, which takes an array, joins it it into
a single scalar, and returns its HTML rendering.

From version 2.00 an object oriented api which is safer for multiple uses
(no more manipulation of shared '%%Options') is available. It is reccomended
that you no longer import any functions by doing:

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
%doc Changes META.yml
%perl_vendor_privlib/*
/usr/bin/ansi2html
/usr/share/man/man1/ansi2html.1*



%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1_1
- mageia import by cas@ requiest

