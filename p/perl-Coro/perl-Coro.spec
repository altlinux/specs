# Spec file for Perl module Coro

Name: perl-Coro
Version: 6.10
Release: alt1

Summary: cooperative multitasking Perl module

%define real_name Coro

License: %perl_license
Group: Development/Perl

URL:  http://search.cpan.org/dist/Coro/

Packager: Nikolay Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar
Patch0: Coro-5.372-alt-EV_test_fix.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu Oct 18 2012 (-bi)
# optimized out: elfutils perl-AnyEvent perl-BDB perl-Guard perl-IO-AIO perl-Log-Agent perl-common-sense perl-devel perl-libnet python-base ruby
BuildRequires: gcc-c++ perl-AnyEvent-AIO perl-AnyEvent-BDB perl-EV perl-Event perl-Net-HTTP
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
cp -p Coro/libcoro/LICENSE LICENSE.libcoro

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes COPYING LICENSE.libcoro README
%perl_vendor_archlib/Coro*
%perl_vendor_autolib/Coro

%changelog
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
