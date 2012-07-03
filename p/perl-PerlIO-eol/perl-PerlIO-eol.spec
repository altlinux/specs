%define dist PerlIO-eol
Name: perl-%dist
Version: 0.14
Release: alt1.3

Summary: PerlIO layer for normalizing line endings
License: GPL or Artistic
Group: Development/Perl

URL: http://www.cpan.org
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-devel

%description
This layer normalizes any of CR, LF, CRLF and Native into the designated
line ending. It works for both input and output handles.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/PerlIO
%perl_vendor_autolib/PerlIO

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt1.3
- disabled build dependency on perl-Module-Install

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt3
- fix directory ownership violation

* Sun Feb 26 2006 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt2
- remove noarch

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt1
- initial build for ALT Linux Sisyphus

