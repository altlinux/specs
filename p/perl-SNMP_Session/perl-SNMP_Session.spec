Name: perl-SNMP_Session
Version: 1.12
Release: alt1
Summary: Native SNMP support for Perl 5

License: GPL
Group: Development/Perl
URL: http://www.switch.ch/misc/leinen/snmp/perl
Packager: Maxim Bodyansky <maximbo@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar.bz2

BuildRequires: perl-devel


%description
This package contains Perl 5 modules SNMP_Session.pm, BER.pm, 
and SNMP_util.pm which, when used together, provide rudimentary 
access to remote SNMP (v1/v2) agents.

This module differs from existing SNMP packages in that it is 
completely stand-alone, i.e. you don't need to have another 
SNMP package such as Net-SNMP. It is also written entirely in 
Perl, so you don't have to compile any C modules. It uses the 
Perl 5 Socket.pm module and should therefore be very portable, 
even to non-Unix systems.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/S*
%perl_vendor_privlib/B*

%changelog
* Tue Jan 05 2010 Denis Smirnov <mithraen@altlinux.ru> 1.12-alt1
- 1.12 (ALT #17841)

* Wed Dec 16 2009 Igor Vlasenko <viy@altlinux.ru> 1.08-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for perl-SNMP_Session
  * postclean-05-filetriggers for spec file

* Thu Dec 04 2008 Denis Smirnov <mithraen@altlinux.ru> 1.08-alt2
- fix build

* Fri Mar 03 2006 Maxim Bodyansky <maximbo@altlinux.ru> 1.08-alt1
- Initial build for ALT Linux Sisyphus
