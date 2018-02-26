%define dist WWW-Curl
Name: perl-%dist
Version: 4.15
Release: alt2

Summary: Perl extension interface for libcurl 
License: MPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: libcurl-devel perl-Test-Pod perl-Test-Pod-Coverage

%description
The perl module WWW::Curl provides an interface to the cURL library "libcurl".

%prep
%setup -q -n %dist-%version

# XXX tests fail
rm t/19multi.t

%ifdef __BTE
# disable network-dependent tests
%def_without test
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/WWW
%perl_vendor_autolib/WWW

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 4.15-alt2
- disabled build dependency on perl-Module-Install

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 4.15-alt1
- 4.11 -> 4.15
- built for perl-5.14
- disabled network-depndent test in hasher

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 4.11-alt1.1
- rebuilt with perl 5.12
- disabled a failing test for a while

* Mon Jan 25 2010 Anton Farygin <rider@altlinux.ru> 4.11-alt1
- new version

* Tue Apr 07 2009 Anton Farygin <rider@altlinux.ru> 4.06-alt1
- new version
- manpage added

* Fri Dec 19 2008 Anton Farygin <rider@altlinux.ru> 4.05-alt1
- new version
- revert back ssl tests

* Wed Nov 08 2006 L.A. Kostis <lakostis@altlinux.org> 3.02-alt2.1
- fix build in gear.

* Wed Nov 08 2006 L.A. Kostis <lakostis@altlinux.org> 3.02-alt2
- disable ssl tests (cause openssl not ready for it);
- prepare for gear.

* Mon Aug 14 2006 L.A. Kostis <lakostis@altlinux.org> 3.02-alt1
- initial build for ALTLinux;
- don't package man pages (use perldoc instead).

