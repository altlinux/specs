%define module	Net-SNMP

Name: perl-Net-SNMP
Version: 6.0.1
Release: alt2

Summary: Net::SNMP (module for perl) - Object oriented interface to SNMP
License: Artistic
Group: Development/Perl
URL: http://search.cpan.org/author/DTOWN/Net-SNMP-v%{version}

Source0: %module-v%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Mar 21 2011 (-bi)
BuildRequires: perl-Crypt-DES perl-Digest-HMAC perl-Math-BigInt perl-Module-Build perl-Socket6 perl(Digest/SHA1.pm)

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
The Net::SNMP module implements an object oriented interface to the
Simple Network Management Protocol.  Perl applications can use the
module to retrieve or update information on a remote host using the
SNMP protocol.  The module supports SNMP version-1, SNMP version-2c
(Community-Based SNMPv2), and SNMP version-3.  The Net::SNMP module
assumes that the user has a basic understanding of the Simple Network
Management Protocol and related network management concepts.
							
%prep
%setup -q -n %module-v%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/*
%doc MANIFEST README Changes
%perl_vendor_privlib/Net*

%changelog
* Mon Oct 24 2011 Igor Vlasenko <viy@altlinux.ru> 6.0.1-alt2
- fixed build (added BR:)

* Mon Mar 21 2011 Alexey Shabalin <shaba@altlinux.ru> 6.0.1-alt1
- 6.0.1

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 5.2.0-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jan 12 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.0-alt1
- 5.2.0

* Fri Dec 24 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 5.0.1-alt1
- new version -- 5.0.1

* Thu Dec 16 2004 Dmitry Lebkov <dlebkov@altlinux.ru> 4.1.2-alt2
- BuildRequires fixed

* Sat Sep 27 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 4.1.2-alt1
- new version -- 4.1.2

* Sun Sep 07 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 4.1.0-alt1
- new version -- 4.1.0
- rebuild with hasher
- add 'URL:' tag into spec-file

* Sun Mar 30 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 4.0.3-alt1
- initial package for ALT Linix
