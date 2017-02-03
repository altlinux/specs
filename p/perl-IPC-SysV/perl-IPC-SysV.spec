%define _unpackaged_files_terminate_build 1
%define dist IPC-SysV
Name: perl-%dist
Version: 2.07
Release: alt1.1

Summary: System V IPC constants and system calls
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MH/MHX/IPC-SysV-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
IPC::Semaphore - Provides an object interface to using SysV IPC semaphores
IPC::Msg - Provides an object interface to using SysV IPC messages
IPC::SysV - Provides the constants required to use the system SysV IPC calls

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%perl_vendor_archlib/IPC
%perl_vendor_autolib/IPC

%changelog
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.07-alt1.1
- rebuild with new perl 5.24.1

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.07-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.04-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.04-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 2.04-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 2.03-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 2.03-alt2
- rebuilt for perl-5.14

* Tue Nov 02 2010 Vladimir Lettiev <crux@altlinux.ru> 2.03-alt1
- initial build
