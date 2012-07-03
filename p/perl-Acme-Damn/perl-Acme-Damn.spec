%define dist Acme-Damn
Name: perl-%dist
Version: 0.04
Release: alt1.2

Summary: 'Unbless' Perl objects
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Test-Exception

%description
Acme::Damn provides a single routine, damn(), which takes a blessed
reference (a Perl object), and *unblesses* it, to return the original
reference. I can't think of any reason why you might want to do this, but
just because it's of no use doesn't mean that you shouldn't be able to do
it.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Acme
%perl_vendor_autolib/Acme

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt1.2
- rebuilt for perl-5.14

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1.1
- rebuilt with perl 5.12

* Sun Sep 20 2009 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- initial build for ALT Linux Sisyphus

