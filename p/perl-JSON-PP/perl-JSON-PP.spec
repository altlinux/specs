%define dist JSON-PP
Name: perl-%dist
Version: 2.27200
Release: alt1

Summary: JSON::XS compatible pure-Perl module
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MA/MAKAMAKA/JSON-PP-2.27200.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 28 2011
BuildRequires: perl-Math-BigInt perl-Tie-IxHash perl-devel

%description
JSON::PP was inculded in JSON distribution (CPAN module).
It comes to be a perl core module in Perl 5.14.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/JSON
%_bindir/json_pp

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.27200-alt1
- automated CPAN update

* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 2.27105-alt1
- initial revision
