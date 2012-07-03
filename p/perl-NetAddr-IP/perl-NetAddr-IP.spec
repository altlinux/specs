%define module NetAddr-IP

Name: perl-%module
Version: 4.059
Release: alt1

Summary: Manages IP addresses and subnets
License: Artistic
Group: Development/Perl

URL: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIKER/%module-%version.tar.gz
Patch1: NetAddr-IP-4.059-version.patch

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Pod-Coverage perl-Socket6 perl-Test-Pod

# Use of this module is now optional and its availability tested inside eval
# so find-requires can't automatically add this requirement. IPv6 is knocking
# on the door, so we add this deliberately:
Requires: perl-Socket6

%description
Manages IPv4 and IPv6 addresses and subnets.

%prep
%setup -n %module-%version
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/NetAddr
%perl_vendor_autolib/NetAddr

%changelog
* Fri Mar 09 2012 Victor Forsiuk <force@altlinux.org> 4.059-alt1
- 4.059

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 4.048-alt1
- 4.048
- built for perl-5.14

* Sat Aug 13 2011 Victor Forsiuk <force@altlinux.org> 4.044-alt1
- 4.044

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 4.043-alt1
- 4.043

* Tue Nov 23 2010 Victor Forsiuk <force@altlinux.org> 4.037-alt1
- 4.037

* Tue Nov 16 2010 Victor Forsiuk <force@altlinux.org> 4.035-alt1
- 4.035

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 4.030-alt1.1
- rebuilt with perl 5.12

* Mon Sep 13 2010 Victor Forsiuk <force@altlinux.org> 4.030-alt1
- 4.030

* Mon Nov 30 2009 Victor Forsyuk <force@altlinux.org> 4.027-alt1
- 4.027

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 4.022-alt1
- 4.022

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 4.011-alt1
- 4.011

* Wed Jul 25 2007 Victor Forsyuk <force@altlinux.org> 4.007-alt1
- 4.007

* Mon May 14 2007 Victor Forsyuk <force@altlinux.org> 4.004-alt1
- Initial build.
