%define dist Cache-Memcached-Fast
Name: perl-%dist
Version: 0.19
Release: alt1.2

Summary: Perl client for memcached
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-IO-Compress perl-Test-Pod perl-Test-Pod-Coverage

%description
Cache::Memcahced::Fast is a Perl client for memcached, a memory cache
daemon (http://www.danga.com/memcached/).  Module core is implemented
in C and tries hard to minimize number of system calls and to avoid
any key/value copying for speed.  As a result, it has very low CPU
consumption.

API is largely compatible with Cache::Memcached, original pure Perl
client, most users of the original module may start using this module
by installing it and adding "::Fast" to the old name in their scripts
(see "Compatibility with Cache::Memcached" section in the module
documentation for full details).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_autolib/Cache
%perl_vendor_archlib/Cache

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.19-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.19-alt1.1
- rebuilt with perl 5.12

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.19-alt1
- New version 0.19

* Mon Mar 08 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.17-alt1
- New version 0.17

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.16-alt1
- New version 0.16

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.13-alt1
- New version 0.13

* Sat May 24 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.10-alt1
- New version

* Sun Mar 02 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.08-alt1
- Initial build for ALT Linux Sisyphus
