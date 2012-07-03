%define dist BSD-Resource
Name: perl-%dist
Version: 1.2904
Release: alt3

Summary: BSD process resource limit and priority functions
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Test-Pod

%description
A module providing an interface for testing and setting process
limits and priorities.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_archlib/BSD
%perl_vendor_autolib/BSD

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.2904-alt3
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.2904-alt2
- rebuilt as plain src.rpm

* Mon Sep 26 2011 Igor Vlasenko <viy@altlinux.ru> 1.2904-alt1.1
- removed unused BR dependencies.

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.2904-alt1
- automated CPAN update

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.29-alt1.1
- rebuilt for perl-5.12

* Thu May 15 2008 Alexey Tourbin <at@altlinux.ru> 1.29-alt1
- 1.28 -> 1.29

* Tue Feb 27 2007 Alexey Tourbin <at@altlinux.ru> 1.28-alt2
- fixed setrlimit test for lowest possible hard limits

* Sun Jan 21 2007 Alexey Tourbin <at@altlinux.ru> 1.28-alt1
- 1.24 -> 1.28
- imported into git and adapted for gear
- test suite issues resolved upstream (cpan #13130, #13131)

* Tue Jun 07 2005 Alexey Tourbin <at@altlinux.ru> 1.24-alt2
- fixed [sg]etpriority.t assumptions about current priority (cpan #13130)
- fixed setrlimit.t attemptes to increase hard limits (cpan #13131)
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.24-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Mar 05 2004 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.24

* Mon Oct 20 2003 Alexey Tourbin <at@altlinux.ru> 1.23-alt1
- 1.23
- disable [sg]etpriority tests as they assume current priority being zero

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 1.22-alt1
- 1.22

* Fri Nov 01 2002 Stanislav Ievlev <inger@altlinux.ru> 1.17-alt1
- Inital build for ALT
