%define _unpackaged_files_terminate_build 1
%define dist PerlIO-eol
Name: perl-%dist
Version: 0.17
Release: alt1

Summary: PerlIO layer for normalizing line endings
License: GPL or Artistic
Group: Development/Perl

URL: http://www.cpan.org
Source0: http://www.cpan.org/authors/id/S/SH/SHLOMIF/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: libcxx-devel perl-devel

%description
This layer normalizes any of CR, LF, CRLF and Native into the designated
line ending. It works for both input and output handles.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/PerlIO
%perl_vendor_autolib/PerlIO

%changelog
* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- rebuild with new perl 5.24.1

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt3
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt2
- rebuilt for perl-5.16

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

