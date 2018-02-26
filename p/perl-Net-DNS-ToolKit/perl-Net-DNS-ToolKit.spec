%define module Net-DNS-ToolKit

# issues with req parsing:
%add_findreq_skiplist */Net/DNS/ToolKit/RR/AFSDB.pm

Name: perl-%module
Version: 0.45
Release: alt1

Summary: Tools for working with DNS packets
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIKER/%module-%version.tar.gz

# Automatically added by buildreq on Sun Mar 25 2012
BuildRequires: perl-Net-DNS-Codes perl-NetAddr-IP perl-devel

%description
Routines to pick apart, examine and put together DNS packets. They can be used
for diagnostic purposes or as building blocks for DNS applications such as DNS
servers and clients or to allow user applications to interact directly with
remote DNS servers.

%prep
%setup -n %module-%version

%build
NPROCS=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 0.45-alt1
- 0.45

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 0.43-alt2
- rebuilt for perl-5.14

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 0.42-alt1.1
- rebuilt with perl 5.12
- fixed build

* Fri Dec 25 2009 Victor Forsyuk <force@altlinux.org> 0.42-alt1
- 0.42

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 0.41-alt1
- 0.41

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.36-alt1
- 0.36

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 0.35-alt1
- 0.35

* Fri Oct 26 2007 Victor Forsyuk <force@altlinux.org> 0.34-alt1
- 0.34

* Thu Jul 05 2007 Victor Forsyuk <force@altlinux.org> 0.31-alt1
- Initial build.
