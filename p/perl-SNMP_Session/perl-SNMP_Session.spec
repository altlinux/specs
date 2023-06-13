%define _unpackaged_files_terminate_build 1
Name: perl-SNMP_Session
Version: 1.16
Release: alt1
Summary: Native SNMP support for Perl 5

License: perl
Group: Development/Perl
URL: http://www.switch.ch/misc/leinen/snmp/perl
BuildArch: noarch

Source0: %name-%version.tar.bz2

BuildRequires: perl-devel perl(Net/SNMP.pm)


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

%package  -n perl-Net_SNMP_util
Summary: Net_SNMP_util -- SNMP utilities using Net::SNMP
Group: Development/Perl

%description -n perl-Net_SNMP_util
The Net_SNMP_util module implements SNMP utilities using the Net::SNMP module.
It implements snmpget, snmpgetnext, snmpwalk, snmpset, snmptrap, and
snmpgetbulk.  The Net_SNMP_util module assumes that the user has a basic
understanding of the Simple Network Management Protocol and related network
management concepts.


%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Artistic README README.SNMP_util ChangeLog changes.html
%perl_vendor_privlib/S*
%perl_vendor_privlib/B*

%files -n perl-Net_SNMP_util
%perl_vendor_privlib/Net_SNMP_util.pm

%changelog
* Tue Jun 13 2023 Igor Vlasenko <viy@altlinux.org> 1.16-alt1
- new version

* Sun May 21 2023 Igor Vlasenko <viy@altlinux.org> 1.15-alt1
- new version

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
