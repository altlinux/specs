%define dist Locale-Maketext-Simple
Name: perl-%dist
Version: 0.21
Release: alt3

Summary: Simple interface to Locale::Maketext::Lexicon
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Always loaded in eval; but *-Lexicon is obese!
#Requires: perl-Locale-Maketext perl-Locale-Maketext-Lexicon

# Automatically added by buildreq on Sat Feb 26 2011
BuildRequires: perl-Locale-Maketext perl-Locale-Maketext-Lexicon perl-devel

%description
This module is a simple wrapper around Locale::Maketext::Lexicon,
designed to alleviate the need of creating Language Classes for
module authors.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Locale

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.21-alt3
- disabled deps on perl-Locale-Maketext and perl-Locale-Maketext-Lexicon

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 0.21-alt2
- added deps on perl-Locale-Maketext and perl-Locale-Maketext-Lexicon

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt2
- fix directory ownership violation

* Sun Jun 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt1
- new version 0.16 (with rpmrb script) - fix bug #11940
- add url to Source, update description

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt1
- first build for ALT Linux Sisyphus
