%define dist Net-IP-Match

Name: perl-%dist
Version: 1.101700
Release: alt2

Summary: Efficiently match IP addresses against IP ranges
License: %perl_license
Group: Development/Perl

Url: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MA/MARCEL/Net-IP-Match-1.101700.tar.gz

BuildArch: noarch

BuildPreReq: /proc rpm-build-licenses

# Automatically added by buildreq on Sat Aug 22 2009
BuildRequires: perl-Filter-Simple perl-devel

%description
This module provides you with an efficient way to match an IP address against
one or more IP ranges. Speed is the key issue here. If you have to check several
million IP addresses, as can happen with big logs, every millisecond counts.
If your way to check an address involves a method call and some temporary
variables, a lot of time is burnt. In such a time-critical loop you don't
want to make subroutine calls at all, as they involve stack operations.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes

%perl_vendor_privlib/Net/IP/*

%changelog
* Wed Nov 17 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.101700-alt2
- removed macro %%perl_vendor_man3dir from spec
- removed Packager from spec

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.101700-alt1
- automated CPAN update

* Sat Aug 22 2009 Sergey Y. Afonin <asy@altlinux.ru> 0.03-alt1
- Initial build for ALTLinux 
