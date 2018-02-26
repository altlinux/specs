%define module GnuPG-Interface

Name: perl-%module
Version: 0.44
Release: alt1

Summary: Supply object methods for interacting with GnuPG
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/GnuPG/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Jul 23 2011
BuildRequires: gnupg perl-Any-Moose perl-Math-BigInt-GMP perl-Module-Install perl-Mouse perl-autodie
BuildRequires: perl-Math-BigInt

%description
GnuPG::Interface and its associated modules are designed to provide an
object-oriented method for interacting with GnuPG, being able to perform
functions such as but not limited to encrypting, signing, decryption,
verification, and key-listing parsing.

%prep
%setup -n %module-%version
# some tests need to read from /dev/tty so will fail in ALT build environment
rm -f t/encrypt.t
rm -f t/get_public_keys.t
rm -f t/get_secret_keys.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/GnuPG

%changelog
* Fri Jul 22 2011 Victor Forsiuk <force@altlinux.org> 0.44-alt1
- 0.44

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.42-alt1.1
- rebuilt with perl 5.12

* Thu Oct 15 2009 Victor Forsyuk <force@altlinux.org> 0.42-alt1
- 0.42
- License is the same as for Perl itself, not just Artistic.
- Closes: #21928.

* Thu Dec 11 2008 Denis Smirnov <mithraen@altlinux.ru> 0.36-alt3
- cleanup spec

* Thu Dec 04 2008 Denis Smirnov <mithraen@altlinux.ru> 0.36-alt2
- fix build

* Sun Apr 13 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.36-alt1
- Build for Sisyphus (thanks to Igor Zubkov <icesik@altlinux.org>)
