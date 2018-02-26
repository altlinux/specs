%define dist Crypt-Twofish
Name: perl-%dist
Version: 2.14
Release: alt1.2

Summary: The Twofish Encryption Algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Crypt-CBC perl-devel

%description
Twofish is a 128-bit symmetric block cipher with a variable length (128,
192, or 256-bit) key, developed by Counterpane Labs. It is unpatented
and free for all uses, as described at
<URL:http://www.counterpane.com/twofish.html>.

This module implements Twofish encryption. It supports the Crypt::CBC
interface, with the functions described below. It also provides an
interface that is call-compatible with Crypt::Twofish 1.0, but its use
in new code is strongly discouraged.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 2.14-alt1.2
- rebuitl for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.14-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt2
- fix directory ownership violation

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt1
- first build for ALT Linux Sisyphus
