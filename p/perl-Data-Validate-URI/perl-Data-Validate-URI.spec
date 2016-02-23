%define bname Data-Validate-URI
Name: perl-%bname
Version: 0.07
Release: alt1
Summary: Common url validation methods
Group: Development/Perl
License: Perl (GPL or Artistic)
URL: http://search.cpan.org/dist/%bname
Source: http://cpan.org.ua/authors/id/S/SO/SONNEN/%bname-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-perl perl-devel
BuildRequires: perl(AutoLoader.pm) perl(Data/Validate/Domain.pm) perl(Data/Validate/IP.pm)

%description
This module collects common URI validation routines to make input validation,
and untainting easier and more readable.
There are a number of other URI validation modules out there as well (see below.)
This one focuses on being fast, lightweight, and relatively 'real-world'. i.e.
it's good if you want to check user input, and don't need to parse out the URI/URL
into chunks.
Right now the module focuses on HTTP URIs, since they're arguably the most common.
If you have a specialized scheme you'd like to have supported, let me know.


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
* Tue Feb 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Sun Jan 26 2014 Led <led@altlinux.ru> 0.06-alt1
- initial build
