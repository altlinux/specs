%define dist IO-Epoll
Name: perl-%dist
Version: 0.03
Release: alt3.1.1.1.1

Summary: Scalable IO Multiplexing for Linux
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
The epoll(4) subsystem is a new variant of poll(2).  It is designed to
offer O(1) scalability over large numbers of watched file descriptors.

The epoll(2) API comprises 4 system calls: epoll_create(2), epoll_ctl(2),
epoll_wait(2) and epoll_pwait(2).  IO::Epoll provides a low-level API
which closely matches the underlying system calls.  It also provides a
higher-level layer designed to emulate the behavior of IO::Poll.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/IO
%perl_vendor_autolib/IO

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt3
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt2
- rebuilt for perl-5.16

* Mon Apr 02 2012 Dmitry V. Levin <ldv@altlinux.org> 0.03-alt1
- Updated to 0.03.

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.02-alt1.2
- updated to perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1.1
- rebuilt with perl 5.12

* Sat Feb 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.02-alt1
- Updated to 0.02.
- Specfile cleanup.

* Sun Jan 01 2006 LAKostis <lakostis at altlinux.ru> 0.01-alt1
- first build for Sisyphus;
- don't package man pages - use perldoc.
