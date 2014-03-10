%define _unpackaged_files_terminate_build 1
%define dist Attribute-Handlers
Name: perl-%dist
Version: 0.96
Release: alt1

Summary: Simpler definition of attribute handlers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SM/SMUELLER/Attribute-Handlers-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Oct 03 2011
BuildRequires: perl-devel perl(parent.pm)

%description
This module, when inherited by a package, allows that package's class to
define attribute handler subroutines for specific attributes. Variables
and subroutines subsequently defined in that package, or in packages
derived from that package may be given attributes with the same names as
the attribute handler subroutines, which will then be called in one of
the compilation phases (i.e. in a BEGIN, CHECK, INIT, or END block).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes demo
%perl_vendor_privlib/Attribute

%changelog
* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- automated CPAN update

* Mon Oct 03 2011 Alexey Tourbin <at@altlinux.ru> 0.91-alt1
- 0.88 -> 0.91
- rebuilt as plain src.rpm

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.88-alt1.1
- rebuilt for perl-5.12

* Thu Apr 08 2010 Alexey Tourbin <at@altlinux.ru> 0.88-alt1
- 0.87 -> 0.88

* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 0.87-alt1
- 0.85 -> 0.87

* Tue Jun 16 2009 Alexey Tourbin <at@altlinux.ru> 0.85-alt1
- 0.80 -> 0.85

* Tue Nov 04 2008 Alexey Tourbin <at@altlinux.ru> 0.80-alt1
- 0.78+ -> 0.80

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 0.78-alt2
- updated from perl-5.9 branch (at change 29414)

* Tue Dec 14 2004 Alexey Tourbin <at@altlinux.ru> 0.78-alt1
- initial revision (split off from perl-base)
- updated to 0.78_01 from perl-5.8.6
