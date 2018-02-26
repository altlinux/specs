%define dist Cache-FastMmap
Name: perl-%dist
Version: 1.39
Release: alt1

Summary: Uses an mmap'ed file to act as a shared memory interprocess cache
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-IO-Compress perl-devel

%description
In multi-process environments (eg mod_perl, forking daemons,
etc), it's common to want to cache information, but have that
cache shared between processes.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Cache
%perl_vendor_autolib/Cache

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.39-alt1
- 1.35 -> 1.39
- built for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.35-alt1.1
- rebuilt with perl 5.12

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 1.35-alt1
- 1.28 -> 1.35

* Fri Sep 05 2008 Michael Bochkaryov <misha@altlinux.ru> 1.28-alt1
- 1.28 version
- fix directory ownership violation

* Mon May 26 2008 Michael Bochkaryov <misha@altlinux.ru> 1.26-alt1
- 1.26 version

* Tue Mar 27 2007 Sir Raorn <raorn@altlinux.ru> 1.14-alt1
- first build for ALT Linux Sisyphus

