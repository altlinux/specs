## SPEC file for Perl module Cache::Memcached::Fast

Name: perl-Cache-Memcached-Fast
Version: 0.25
Release: alt2.1

Summary: Perl client for memcached

License: %perl_license
Group: Development/Perl

%define real_name Cache-Memcached-Fast
URL: http://search.cpan.org/dist/Cache-Memcached-Fast/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Sep 14 2014
# optimized out: libcloog-isl4 perl-Compress-Raw-Zlib perl-Devel-Symdump perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel
BuildRequires: perl-IO-Compress perl-Test-Pod perl-Test-Pod-Coverage

%description
Cache::Memcahced::Fast is a Perl client for memcached, a memory cache
daemon (http://www.danga.com/memcached/).  Module core is implemented
in C and tries hard  to minimize number of system calls  and to avoid
any key/value copying for speed.  As a result, it has very low CPU
consumption.

API is largely compatible with  Cache::Memcached,  original pure Perl
client, most users of the original module may start using this module
by installing it and adding "::Fast" to the old name in their scripts
(see "Compatibility with Cache::Memcached" section in the module
documentation for full details).

%prep
%setup -q -n %real_name-%version

%build
export NPROCS=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%exclude /.perl.req
%perl_vendor_autolib/Cache
%perl_vendor_archlib/Cache

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2.1
- rebuild with new perl 5.26.1

* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2
- NMU: set NPROCS=1 for multicore builds (preparing for perl 5.26)

* Sun Mar 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.25-alt1
- New version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1.1
- rebuild with new perl 5.22.0

* Sat Jan 10 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.23-alt1
- New version 0.23

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1.1
- rebuild with new perl 5.20.1

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.22-alt1
- New version 0.22

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.21-alt2
- built for perl 5.18

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.21-alt1
- New version 0.21

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.19-alt2
- rebuilt for perl-5.16

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
