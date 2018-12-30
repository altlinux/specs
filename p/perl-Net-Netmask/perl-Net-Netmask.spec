%define _unpackaged_files_terminate_build 1
%define module Net-Netmask

Name: perl-%module
Version: 1.9104
Release: alt1

Summary: Perl module for manipulation and lookup of IP network blocks
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source0: http://www.cpan.org/authors/id/J/JM/JMASLAK/%{module}-%{version}.tar.gz
BuildArch: noarch

# Automatically added by buildreq on Sun Apr 10 2011
BuildRequires: perl-devel /usr/bin/pod2text perl(Test/UseAllModules.pm) perl(Test2/V0.pm) perl(Math/BigInt.pm)

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
%setup -q -n %{module}-%{version}

#Test2::V0 version 0.000111 required
[ %version = "1.9104" ] && rm t/ipv6_*

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO CONTRIBUTING README Changes LICENSE CODE_OF_CONDUCT.md
%perl_vendor_privlib/Net/*

%changelog
* Sun Dec 30 2018 Igor Vlasenko <viy@altlinux.ru> 1.9104-alt1
- automated CPAN update

* Fri Jun 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.9103-alt1
- automated CPAN update

* Wed Jun 06 2018 Igor Vlasenko <viy@altlinux.ru> 1.9101-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.9022-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.9021-alt1
- automated CPAN update

* Wed Oct 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.9019-alt1
- automated CPAN update

* Fri Sep 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.9018-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.9017-alt1
- automated CPAN update

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
