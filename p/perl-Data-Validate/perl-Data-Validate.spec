%define bname Data-Validate
Name: perl-%bname
Version: 0.09
Release: alt1
Summary: Common data validation methods
Group: Development/Perl
License: Perl (GPL or Artistic)
URL: http://search.cpan.org/dist/%bname
Source: http://cpan.org.ua/authors/id/S/SO/SONNEN/%bname-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-perl perl-devel perl(Math/BigInt/FastCalc.pm)

%description
This module collects common validation routines to make input validation, and
untainting easier and more readable. Most of the functions are not much shorter
than their direct perl equivalent (and are much longer in some cases), but their
names make it clear what you're trying to test for.


%prep
%setup -q -n %bname-%version


%build
%perl_vendor_build


%install
%perl_vendor_install


%files
%doc Changes README
%perl_vendor_privlib/Data
%perl_vendor_privlib/auto/*


%changelog
* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Sun Jan 26 2014 Led <led@altlinux.ru> 0.08-alt1
- initial build
