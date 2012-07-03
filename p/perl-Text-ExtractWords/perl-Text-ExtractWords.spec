%define dist Text-ExtractWords
Name: perl-%dist
Version: 0.08
Release: alt2.2

Summary: Perl extension for extract words from strings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
The aim of this module is to extract the words from the texts or mails
to identify spam.  But it can be used for another purpose.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Text
%perl_vendor_autolib/Text

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.08-alt2.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt2.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.08-alt2
- fix directory ownership violation
- disable man packaging

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.08-alt1
- initial build for ALT Linux Sisyphus

