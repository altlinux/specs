# Spec file for Perl module Coro

Name: perl-Coro
Version: 6.511
Release: alt1

Summary: cooperative multitasking Perl module

%define real_name Coro

License: %perl_license
Group: Development/Perl

URL:  http://search.cpan.org/dist/Coro/

Packager: Nikolay Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar
Patch0: Coro-5.372-alt-EV_test_fix.patch
Patch1: Coro-6.48-rurban-perl-5.22.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu Jul 21 2016 (-bi)
# optimized out: elfutils perl perl-AnyEvent perl-BDB perl-Encode perl-Guard perl-IO-AIO perl-IO-Socket-IP perl-IO-Socket-SSL perl-Log-Agent perl-Net-HTTP perl-Net-SSLeay perl-URI perl-common-sense perl-devel perl-libnet python-base python-modules python3 rpm-build-python3 ruby ruby-stdlibs
BuildRequires: gcc-c++ perl-AnyEvent-AIO perl-AnyEvent-BDB perl-Canary-Stability perl-EV perl-Event

BuildRequires:  perl-Log-Agent perl-devel perl-libnet
# python-module-distribute python-module-zope rpm-build-ruby

%description
Coro is a large Perl module family that implements cooperative
multitasking in Perl. It supports filehandle and event
abstraction and also implements continuations as well as the
necessary directives to implement a slightly limited call/cc
in Perl.

%prep
%setup -q -n %real_name-%version
%patch
%patch1 -p4
cp -p Coro/libcoro/LICENSE LICENSE.libcoro

%build
%ifarch %arm
export CORO_INTERFACE=u
%endif
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes COPYING LICENSE.libcoro README
%perl_vendor_archlib/Coro*
%perl_vendor_autolib/Coro

%changelog
* Thu Jul 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 6.511-alt1
- New version

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 6.49-alt2.1
- rebuild with new perl 5.22.0

* Sun Nov 22 2015 Vladimir Lettiev <crux@altlinux.ru> 6.49-alt2
- Fixed build for perl 5.22 (based on patch from Reini Urban)

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 6.49-alt1
- New version

* Sun Jun 07 2015 Nikolay A. Fetisov <naf@altlinux.ru> 6.43-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 6.42-alt1
- New version

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 6.41-alt1.1
- rebuild with new perl 5.20.1

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 6.41-alt1
- New version

* Thu Feb 27 2014 Nikolay A. Fetisov <naf@altlinux.ru> 6.33-alt1
- New version

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 6.31-alt2
- built for perl 5.18

* Tue Jun 11 2013 Nikolay A. Fetisov <naf@altlinux.ru> 6.31-alt1
- New version

* Fri Mar 01 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.23-alt2
- explicitly select ucontext method on arm

* Mon Jan 07 2013 Nikolay A. Fetisov <naf@altlinux.ru> 6.23-alt1
- New version

* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 6.10-alt1
- New version

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 6.08-alt1
- 6.06 -> 6.08
- built for perl-5.16

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 6.06-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 6.06-alt1
- automated CPAN update

* Sat May 28 2011 Nikolay A. Fetisov <naf@altlinux.ru> 5.372-alt1
- New version
- Fix tests to build with current libpthread

* Sat Nov 27 2010 Nikolay A. Fetisov <naf@altlinux.ru> 5.25-alt1
- Initial build for ALT Linux Sisyphus
