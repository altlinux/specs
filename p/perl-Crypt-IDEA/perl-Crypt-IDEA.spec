%define dist Crypt-IDEA
Name: perl-%dist
Version: 1.08
Release: alt3

Summary: Perl interface to IDEA block cipher
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
rm %buildroot%perl_vendor_archlib/Crypt/._test.pl

%files
%doc README changes
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
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
