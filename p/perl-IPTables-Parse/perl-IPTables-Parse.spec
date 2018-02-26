%define dist IPTables-Parse
Name: perl-%dist
Version: 0.7
Release: alt1

Summary: Perl extension for parsing iptables firewall rulesets
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Oct 20 2011
BuildRequires: perl-devel

%description
The IPTables::Parse package provides an interface to parse iptables rules
on Linux systems through the direct execution of iptables commands, or from
parsing a file that contains an iptables policy listing.  You can get the
current policy applied to a table/chain, look for a specific user-defined
chain, check for a default DROP policy, or determing whether or not logging
rules exist.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/IPTables

%changelog
* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 0.7-alt1
- initial revision
