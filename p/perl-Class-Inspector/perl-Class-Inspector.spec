%define dist Class-Inspector
Name: perl-%dist
Version: 1.25
Release: alt2

Summary: Get information about a class and its structure
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Pod-Escapes perl-devel

%description
Class::Inspector allows you to get information about a loaded class.
Most or all of this information can be found in other ways, but they
aren't always very friendly, and usually involve a relatively high level
of Perl wizardry, or strange and unusual looking code. Class::Inspector
attempts to provide an easier, more friendly interface to this
information.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Class

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.25-alt2
- disabled build dependency on perl-Module-Install

* Tue Apr 26 2011 Alexey Tourbin <at@altlinux.ru> 1.25-alt1
- 1.24 -> 1.25

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.23 -> 1.24

* Sat Jun 14 2008 Vitaly Lipatov <lav@altlinux.ru> 1.23-alt1
- new version 1.23 (with rpmrb script)

* Thu Jan 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.18-alt1
- new version 1.18 (with rpmrb script)

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 1.08-alt1
- first build for ALT Linux Sisyphus
