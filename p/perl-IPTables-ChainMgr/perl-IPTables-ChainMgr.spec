%define dist IPTables-ChainMgr
Name: perl-%dist
Version: 0.9
Release: alt1

Summary: Perl extension for manipulating iptables policies
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Oct 20 2011
BuildRequires: perl-IPTables-Parse perl-Net-IPv4Addr perl-devel

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
* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 0.9-alt1
- initial revision
