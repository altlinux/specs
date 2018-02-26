%define dist Catalyst-Plugin-Session-Store-FastMmap
Name: perl-%dist
Version: 0.14
Release: alt2

Summary: FastMmap session storage backend
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011 (-bi)
BuildRequires: perl-Cache-FastMmap perl-Catalyst-Devel perl-Catalyst-Plugin-Session perl-Class-Accessor perl-Class-Data-Inheritable perl-Digest-SHA perl-Test-Pod perl-Test-Pod-Coverage

%description
Catalyst::Plugin::Session::Store::FastMmap is a fast session
storage plugin for Catalyst that uses an mmap'ed file to act as
a shared memory interprocess cache. It is based on
Cache::FastMmap.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Catalyst

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt2
- updated BuildRequires

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- 0.05 -> 0.13

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.05-alt1
- 0.05 version
- fix directory ownership violation

* Tue Mar 27 2007 Sir Raorn <raorn@altlinux.ru> 0.02-alt1
- first build for ALT Linux Sisyphus

