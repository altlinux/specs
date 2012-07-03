%define dist DBD-ODBC
Name: perl-%dist
Version: 1.31
Release: alt2

Summary: Perl DBD module for interfacing with ODBC databases
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-DBD-ODBC-1.29-alt-pod.patch

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libunixODBC-devel perl-DBI-devel perl-Test-NoWarnings perl-Test-Pod perl-Test-Pod-Coverage

%description
This module is needed to access ODBC databases from within Perl.
The module uses the unixODBC manager to connect to the database.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build -o %_prefix

%install
%perl_vendor_install

%files
%dir	%perl_vendor_archlib/DBD
	%perl_vendor_archlib/DBD/ODBC.pm
%dir	%perl_vendor_archlib/DBD/ODBC
%doc	%perl_vendor_archlib/DBD/ODBC/*.pod
	%perl_vendor_autolib/DBD

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.31-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Tue Apr 05 2011 Alexey Tourbin <at@altlinux.ru> 1.29-alt1
- 1.27 -> 1.29

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 1.27-alt1
- 1.24 -> 1.27

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.24-alt1.1
- rebuilt with perl 5.12

* Sun May 16 2010 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.23 -> 1.24

* Fri Sep 11 2009 Alexey Tourbin <at@altlinux.ru> 1.23-alt1
- 1.22 -> 1.23

* Fri Jun 12 2009 Alexey Tourbin <at@altlinux.ru> 1.22-alt1
- 1.21 -> 1.22

* Wed Apr 29 2009 Alexey Tourbin <at@altlinux.ru> 1.21-alt1
- 1.20 -> 1.21

* Wed Apr 22 2009 Alexey Tourbin <at@altlinux.ru> 1.20-alt1
- 1.19 -> 1.20

* Fri Apr 03 2009 Alexey Tourbin <at@altlinux.ru> 1.19-alt1
- 1.18 -> 1.19

* Fri Feb 27 2009 Alexey Tourbin <at@altlinux.ru> 1.18-alt1
- 1.17 -> 1.18

* Wed Sep 24 2008 Alexey Tourbin <at@altlinux.ru> 1.17-alt1
- 1.16_2 -> 1.17

* Sun Sep 07 2008 Alexey Tourbin <at@altlinux.ru> 1.16_2-alt1
- 1.15 -> 1.16_2

* Sun Mar 02 2008 Alexey Tourbin <at@altlinux.ru> 1.15-alt1
- 1.13 -> 1.15
- fixed build on x86_64

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 1.13-alt1
- 1.12 -> 1.13
- manual pages not packaged (use perldoc)

* Mon Nov 08 2004 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- initial revision
