%define dist Text-Soundex
Name: perl-%dist
Version: 3.03
Release: alt1.2

Summary: Implementation of the Soundex algorithm as described by Knuth
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
This module implements the soundex algorithm as described by Donald Knuth
in Volume 3 of The Art of Computer Programming.  The algorithm is intended
to hash words (in particular surnames) into a small space using a simple model
which approximates the sound of the word when spoken by an English speaker.
Each word is reduced to a four character string, the first character being
an upper case letter and the remaining three being digits.

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
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 3.03-alt1.2
- rebuilt for perl-5.14
- rebuilt as plain src.rpm

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 3.03-alt1.1
- rebuilt with perl 5.12

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 3.03-alt1
- 3.02 -> 3.03

* Sat Mar 24 2007 Alexey Tourbin <at@altlinux.ru> 3.02-alt1
- initial revision (detached from perl-base)
