%define _unpackaged_files_terminate_build 1
%define dist IPTables-ChainMgr
Name: perl-%dist
Version: 1.6
Release: alt1

Summary: Perl extension for manipulating iptables policies
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MR/MRASH/IPTables-ChainMgr-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Oct 20 2011
BuildRequires: perl-IPTables-Parse perl-Net-IPv4Addr perl-devel perl(NetAddr/IP.pm)

%description
The IPTables::ChainMgr package provide an interface to manipulate iptables
policies on Linux systems through the direct execution of iptables commands.
Although making a perl extension of libiptc provided by the iptables project
is possible (and has been done by the IPTables::libiptc module available
from CPAN), it is also easy enough to just execute iptables commands
directly in order to both parse and change the configuration of the policy.
Further, this simplifies installation since the only external requirement
is (in the spirit of scripting) to be able to point IPTables::ChainMgr at
an installed iptables binary instead of having to compile against a library.

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
* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1
- automated CPAN update

* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- automated CPAN update

* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 0.9-alt1
- initial revision
