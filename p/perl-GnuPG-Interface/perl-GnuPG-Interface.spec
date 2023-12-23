%define _unpackaged_files_terminate_build 1
%define module GnuPG-Interface

Name: perl-%module
Version: 1.04
Release: alt1

Summary: Supply object methods for interacting with GnuPG
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/B/BP/BPS/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Jul 23 2011
BuildRequires: gnupg perl-Any-Moose perl-Math-BigInt-GMP perl-Module-Install perl-Mouse perl-autodie perl(Moo.pm) perl(MooX/late.pm) perl(MooX/HandlesVia.pm) perl(Data/Perl/Role/Collection/Array.pm)
BuildRequires: perl-Math-BigInt

%description
GnuPG::Interface and its associated modules are designed to provide an
object-oriented method for interacting with GnuPG, being able to perform
functions such as but not limited to encrypting, signing, decryption,
verification, and key-listing parsing.

%prep
%setup -q -n %{module}-%{version}
# some tests need to read from /dev/tty so will fail in ALT build environment
rm -f t/encrypt.t
rm -f t/get_public_keys.t
rm -f t/get_secret_keys.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/GnuPG

%changelog
* Sat Dec 23 2023 Igor Vlasenko <viy@altlinux.org> 1.04-alt1
- automated CPAN update

* Mon Sep 25 2023 Igor Vlasenko <viy@altlinux.org> 1.03-alt1
- automated CPAN update

* Tue Apr 13 2021 Igor Vlasenko <viy@altlinux.org> 1.02-alt1
- automated CPAN update

* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- automated CPAN update

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
