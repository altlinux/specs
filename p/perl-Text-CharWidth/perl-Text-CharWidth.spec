%define dist Text-CharWidth
Name: perl-%dist
Version: 0.04
Release: alt4.1.1.1.1

Summary: Get number of occupied columns of a string on terminal
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
This is a module to provide equivalent feature as wcwidth(3) and
wcswidth(3).  This also provides mblen(3) equivalent subroutine.

mbwidth() and mbswidth() are provided subroutines corresponding
wcwidth(3) and wcswidth(3) in C language.  The prefix "mb" expresses
that they handles "multibyte character" in C meaning, i.e., character
encoding specified by LC_CTYPE locale.

These subroutines are used to get the width of characters on terminal.
Though most characters have width of 1, there are exceptions.
Fullwidth characters are characters with width of 2.  Most of east
Asian characters such as Hiragana, Katakana, Hangul, Han Ideogram
are fullwidth.  Combining characters are characters with width of 0.
Unicode has many combining characters like diacritical marks.  There
are languages which need combining characters such as Thai and
Vietnamese.

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt4
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt2.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt2
- fix directory ownership violation
- disable man packaging

* Fri Feb 17 2006 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- initial build for ALT Linux Sisyphus

