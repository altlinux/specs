%define dist Coro
Name: perl-%dist
Version: 6.06
Release: alt2

Summary: cooperative multitasking Perl module
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: Coro-5.372-alt-EV_test_fix.patch

# Automatically added by buildreq on Wed Oct 19 2011 (-bi)
BuildRequires: perl-AnyEvent-AIO perl-AnyEvent-BDB perl-EV perl-Event perl-Log-Agent perl-Net-HTTP perl-devel perl-libnet

%description
Coro is a large Perl module family that implements cooperative
multitasking in Perl. It supports filehandle and event
abstraction and also implements continuations as well as the
necessary directives to implement a slightly limited call/cc
in Perl.

%prep
%setup -q -n %dist-%version
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
* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 6.06-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 6.06-alt1
- automated CPAN update

* Sat May 28 2011 Nikolay A. Fetisov <naf@altlinux.ru> 5.372-alt1
- New version
- Fix tests to build with current libpthread

* Sat Nov 27 2010 Nikolay A. Fetisov <naf@altlinux.ru> 5.25-alt1
- Initial build for ALT Linux Sisyphus
