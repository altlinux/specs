%define dist JSON-DWIW
Name: perl-%dist
Version: 0.47
Release: alt2

Summary: Flexible and fast JSON converter for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-JSON-DWIW-0.40-alt-deps.patch

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Math-BigInt perl-devel

%description
Other JSON modules require setting several parameters before
calling the conversion methods to do what I want.  This module
does things by default that I think should be done when working
with JSON in Perl.  This module also encodes and decodes faster
than JSON.pm and JSON::Syck in my benchmarks.

This means that any piece of data in Perl (assuming it's valid
unicode) will get converted to something in JSON instead of
throwing an exception.  It also means that output will be strict
JSON, while accepted input will be flexible, without having to
set any options.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README WhatsNew
%perl_vendor_archlib/JSON
%perl_vendor_autolib/JSON

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.47-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.42-alt1.1
- rebuilt with perl 5.12

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Tue May 04 2010 Alexey Tourbin <at@altlinux.ru> 0.40-alt1
- 0.38 -> 0.40
- alt-deps.patch: enabled dependencies on Math::BigInt and Math::BigFloat

* Mon Sep 28 2009 Michael Bochkaryov <misha@altlinux.ru> 0.38-alt1
- 0.38 version
  + fixed build for x86_64
  + added ascii, bare_solidus, and minimal_escaping options
  + miscelaneous fixes - see WhatsNew file

* Sat Sep 06 2008 Michael Bochkaryov <misha@altlinux.ru> 0.27-alt1
- 0.27 version
  + documented the is_valid_utf8() method
  + added the upgrade_to_utf8() method
  + added shell-style comment support to the from_json() method
  + documented comment support
- fix directory ownership violation

* Thu Jul 31 2008 Michael Bochkaryov <misha@altlinux.ru> 0.26-alt1
- 0.26 version build
  + fixed number parsing bug (rt.cpan.org #37541)
  + documented utility functions

* Mon May 26 2008 Michael Bochkaryov <misha@altlinux.ru> 0.24-alt1
- 0.24 version

* Sun Apr 13 2008 Michael Bochkaryov <misha@altlinux.ru> 0.23-alt1
- first build for ALT Linux Sisyphus

