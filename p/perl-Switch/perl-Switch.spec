%define dist Switch
Name: perl-%dist
Version: 2.16
Release: alt2

Summary: A switch statement for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: Switch-2.16-rt-60380.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-Filter perl-Text-Balanced perl-devel

%description
Switch.pm provides the syntax and semantics for an explicit case
mechanism for Perl.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Switch.pm

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 2.16-alt2
- applied patch from rt.cpan.org #60380

* Sun Dec 19 2010 Alexey Tourbin <at@altlinux.ru> 2.16-alt1
- 2.14 -> 2.16

* Tue Mar 03 2009 Alexey Tourbin <at@altlinux.ru> 2.14-alt1
- 2.13 -> 2.14

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 2.13-alt1
- 2.10 -> 2.13

* Wed Dec 15 2004 Alexey Tourbin <at@altlinux.ru> 2.10-alt1
- initial revision (split from perl-base)
