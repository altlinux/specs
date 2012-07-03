%define module Net-Netmask

Name: perl-%module
Version: 1.9016
Release: alt1

Summary: Perl module for manipulation and lookup of IP network blocks
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Net/%module-%version.tar.gz
BuildArch: noarch

# Automatically added by buildreq on Sun Apr 10 2011
BuildRequires: perl-devel

%description
Net::Netmask parses and understands IPv4 CIDR blocks. It's built with an
object-oriented interface. Nearly all functions are methods that operate on a
Net::Netmask object. There are methods that provide the nearly all bits of
information about a network block that you might want. There are also functions
to put a network block into a table and then later lookup network blocks by IP
address in that table. There are functions to turn a IP address range into a
list of CIDR blocks. There are functions to turn a list of CIDR blocks into a
list of IP addresses. There is a function for sorting by text IP address.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/*

%changelog
* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 1.9016-alt1
- 1.9016

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.9015-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jan 19 2007 Victor Forsyuk <force@altlinux.org> 1.9015-alt1
- 1.9015

* Tue Aug 16 2005 Denis Ovsienko <pilot@altlinux.ru> 1.9012-alt1
- new version
- restored lost manpage

* Tue Apr 05 2005 Denis Ovsienko <pilot@altlinux.ru> 1.9011-alt2
- spec cleanup

* Fri Mar 25 2005 Denis Ovsienko <pilot@altlinux.ru> 1.9011-alt1
- initial ALTLinux build
