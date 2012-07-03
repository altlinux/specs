%define dist Net-Ping
Name: perl-%dist
Version: 2.36
Release: alt1

Summary: Check a remote host for reachability
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-devel

%description
This module contains methods to test the reachability
of remote hosts on a network.

%prep
%setup -q -n %dist-%version

%ifdef __BTE
# skip network dependent test
grep -FZl '1..0 # Skip: network dependent test' t/*.t |xargs -r0 rm -v
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Net

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.36-alt1
- 2.35 -> 2.36
- rebuilt as plain src.rpm

* Tue Mar 03 2009 Alexey Tourbin <at@altlinux.ru> 2.35-alt1
- 2.33 -> 2.35

* Wed Nov 21 2007 Alexey Tourbin <at@altlinux.ru> 2.33-alt1
- 2.32 -> 2.33

* Sat Aug 04 2007 Alexey Tourbin <at@altlinux.ru> 2.32-alt1
- 2.31 -> 2.32

* Sat Jun 04 2005 Alexey Tourbin <at@altlinux.ru> 2.31-alt2
- patch from bleadperl: Improved ICMP_UNREACHABLE handling

* Mon Nov 08 2004 Alexey Tourbin <at@altlinux.ru> 2.31-alt1
- initial revision (perl-base offset; required only by net-snmp-utils)
