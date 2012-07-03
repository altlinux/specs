%define module Net-IP
Name: perl-%module
Version: 1.25
Release: alt3.1

Summary: Perl extension for manipulating IPv4/IPv6 addresses
License: GPL or Artistic
Group: Development/Perl

Url: %CPAN %module
Source: %url%module-%version.tar.gz
Patch0: %name-intip-0.patch

BuildArch: noarch

Packager: Sergey Kurakin <kurakin@altlinux.org>

# Automatically added by buildreq on Tue Dec 22 2009
BuildRequires: perl-Math-BigInt perl-devel

%description
Net::IP module designed to allow easy manipulation of IPv4
and IPv6 addresses. There is also a small application which
uses the IP.pm module: ipcount.pl. Basically, it's an IP address
mini-calculator, it can calculate the number of IP addresses
in a prefix or all the prefixes contained in a given range.

%prep
%setup -q -n %module-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes MANIFEST README
%_bindir/*
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Sun Nov 21 2010 Sergey Kurakin <kurakin@altlinux.org> 1.25-alt3.1
- fixed build with perl 5.12

* Tue Dec 22 2009 Sergey Kurakin <kurakin@altlinux.org> 1.25-alt3
- architecture changed to noarch (thanks to at@)

* Wed May  6 2009 Sergey Kurakin <kurakin@altlinux.org> 1.25-alt2
- fixed intip method (ALT #19941, CPAN #20265)

* Tue Dec  2 2008 Sergey Kurakin <kurakin@altlinux.org> 1.25-alt1
- 1.25
- build fixed (sisyphus_check: directory ownership)
- repocop issues fixed (spec-missing-packager,
  altlinux-policy-perl-noarch-pkg-has-dirs-in-arch)

* Tue Nov 15 2005 LAKostis <lakostis@altlinux.ru> 1.24-alt1
- initial package for ALT Linux.

