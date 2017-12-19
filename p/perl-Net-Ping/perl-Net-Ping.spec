%define _unpackaged_files_terminate_build 1
%define dist Net-Ping
Name: perl-%dist
Version: 2.63
Release: alt1

Summary: Check a remote host for reachability
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RU/RURBAN/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-devel perl(CPAN/Meta.pm) perl(Text/Template.pm)

%description
This module contains methods to test the reachability
of remote hosts on a network.

%prep
%setup -q -n %{dist}-%{version}

%ifdef __BTE
# skip network dependent test
grep -FZl '1..0 # Skip: network dependent test' t/*.t |xargs -r0 rm -v
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md README.md.PL
%perl_vendor_privlib/Net

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.63-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.61-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.59-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.58-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.57-alt1
- automated CPAN update

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 2.56-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.55-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.52-alt1
- automated CPAN update

* Thu Sep 05 2013 Igor Vlasenko <viy@altlinux.ru> 2.41-alt1
- automated CPAN update

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
