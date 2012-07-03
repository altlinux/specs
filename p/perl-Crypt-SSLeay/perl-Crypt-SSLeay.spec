%define dist Crypt-SSLeay
Name: perl-%dist
Version: 0.58
Release: alt3

Summary: OpenSSL glue that provides LWP https support
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libssl-devel perl-Test-Pod

%description
This perl module provides support for the https protocol under LWP, so
that a LWP::UserAgent can make https GET & HEAD & POST requests. Please
see perldoc LWP for more information on POST requests.

%prep
%setup -q -n %dist-%version

%ifdef __buildreqs
mv t/02-live.t t/02-live.t.orig
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Crypt
%perl_vendor_archlib/Net
%perl_vendor_autolib/Crypt

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.58-alt3
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.58-alt2
- rebuilt as plain src.rpm

* Mon Oct 04 2010 Alexey Tourbin <at@altlinux.ru> 0.58-alt1.1
- rebuilt for perl-5.12

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.58-alt1
- 0.57 -> 0.58
- built for perl-5.12
- disabled build dependency on perl-libwww

* Sun Aug 24 2008 Alexey Tourbin <at@altlinux.ru> 0.57-alt2
- rebuilt with libssl.so.7

* Wed Nov 14 2007 Alexey Tourbin <at@altlinux.ru> 0.57-alt1
- 0.56 -> 0.57

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 0.56-alt1
- 0.54 -> 0.56

* Wed Apr 18 2007 Alexey Tourbin <at@altlinux.ru> 0.54-alt1
- 0.53 -> 0.54

* Sun Jan 21 2007 Alexey Tourbin <at@altlinux.ru> 0.53-alt1
- 0.51 -> 0.53
- adapted for git and built with gear

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.51-alt2.1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.51-alt2.1
- Rebuilt with openssl-0.9.7d.

* Mon Oct 06 2003 Andrey Brindeew <abr@altlinux.ru> 0.51-alt2
- Packager tag updated
- Both Summary and Description was updated
- Url tag added

* Fri Aug 01 2003 Sir Raorn <raorn@altlinux.ru> 0.51-alt1
- Built for Sisyphus

