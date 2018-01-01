%define _unpackaged_files_terminate_build 1
%define dist Test-ClassAPI
Name: perl-%dist
Version: 1.07
Release: alt1

Summary: Provides basic first-pass API testing for large class trees
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Class-Inspector perl-Config-Tiny perl-Params-Util perl-devel

%description
For many APIs with large numbers of classes, it can be very useful to be
able to do a quick once-over to make sure that classes, methods, and
inheritance is correct, before doing more comprehensive testing. This
module aims to provide such a capability.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test

%changelog
* Mon Jan 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.06-alt2
- disabled build dependency on perl-Module-Install

* Tue Apr 26 2011 Alexey Tourbin <at@altlinux.ru> 1.06-alt1
- 1.02 -> 1.06

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.02-alt2
- fix directory ownership violation

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 1.02-alt1
- first build for ALT Linux Sisyphus
