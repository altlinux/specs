%define _unpackaged_files_terminate_build 1
%define dist Lingua-EN-Inflect-Phrase
Name: perl-%dist
Version: 0.18
Release: alt1

Summary: Inflect short English Phrases
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RK/RKITOVER/Lingua-EN-Inflect-Phrase-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Lingua-EN-Inflect-Number perl-Lingua-EN-Tagger perl-Pod-Escapes perl-devel perl(Lingua/EN/FindNumber.pm) perl(Test/NoWarnings.pm) perl(Lingua/EN/Number/IsOrdinal.pm)

%description
Attempts to pluralize or singularize short English phrases.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Lingua

%changelog
* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- 0.04 -> 0.10

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision
