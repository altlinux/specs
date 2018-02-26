%define module_name IP-Country

Name: perl-%module_name
Version: 2.27
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Classes for fast lookup of country codes from IP addresses for Perl
License: Perl
Group: Development/Perl

URL: %CPAN %module_name
Source: http://www.cpan.org/modules/by-module/IP/%module_name-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Jan 22 2010
BuildRequires: perl-Geo-IP-PurePerl perl-Geography-Countries perl-devel

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
Finding the home country of a client using only the IP address can be difficult.
Looking up the domain name associated with that address can provide some help,
but many IP address are not reverse mapped to any useful domain, and the most
common domain (.com) offers no help when looking for country.

This module comes bundled with a database of countries where various IP
addresses have been assigned. Although the country of assignment will probably
be the country associated with a large ISP rather than the client herself, this
is probably good enough for most log analysis applications, and under test has
proved to be as accurate as reverse-DNS and WHOIS lookup.

%prep
%setup -n %module_name-%version

%build
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/*
%_man1dir/*
%perl_vendor_privlib/IP

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.27-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jan 22 2010 Victor Forsyuk <force@altlinux.org> 2.27-alt1
- 2.27

* Wed Jul 22 2009 Victor Forsyuk <force@altlinux.org> 2.26-alt1
- 2.26 (build closes ALT#20847).

* Wed Jun 25 2008 Victor Forsyuk <force@altlinux.org> 2.25-alt1
- 2.25

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 2.24-alt1
- 2.24

* Wed Feb 07 2007 Victor Forsyuk <force@altlinux.org> 2.23-alt1
- 2.23

* Tue Jun 13 2006 Victor Forsyuk <force@altlinux.ru> 2.21-alt1
- 2.21

* Wed Oct 05 2005 Victor Forsyuk <force@altlinux.ru> 2.20-alt1
- Initial build.
