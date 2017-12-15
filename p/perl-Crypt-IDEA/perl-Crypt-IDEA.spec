%define dist Crypt-IDEA
Name: perl-%dist
Version: 1.10
Release: alt2.1.1.1.1

Summary: Perl interface to IDEA block cipher
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DP/DPARIS/Crypt-IDEA-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
This is Crypt::IDEA version %version, an XS-based implementation
of the patent-encumbered IDEA cryptography algorithm.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# Remove MacOS junk.
rm -f %buildroot%perl_vendor_archlib/Crypt/._test.pl

%files
%doc README changes
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.10-alt2
- built for perl 5.18

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt4
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.08-alt3
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt2.qa1.1
- rebuilt with perl 5.12

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.08-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * macos-resource-fork-file-in-package for perl-Crypt-IDEA
  * postclean-05-filetriggers for spec file

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.08-alt2
- fix directory ownership violation

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.08-alt1
- new version 1.08 (with rpmrb script)

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.02-alt1
- first build for ALT Linux Sisyphus
