%define dist Linux-Pid
Name: perl-%dist
Version: 0.04
Release: alt4.1.1.1.1

Summary: Get the native PID and the PPID on Linux
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel perl-threads

%description
Why should one use a module to get the PID and the PPID of a process
where there are the `$$' variable and the `getppid()' builtin ? (Not
mentioning the equivalent `POSIX::getpid()' and `POSIX::getppid()'
functions.)

In fact, this is useful on Linux, with multithreaded programs. Linux' C
library, using the linux thread model, returns different values of the
PID and the PPID from different threads. (Other thread models such as
NPTL don't have the same behaviour). This module forces perl to call the
underlying C functions `getpid()' and `getppid()'.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Linux
%perl_vendor_autolib/Linux

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- rebuilt for perl-5.14

* Thu Mar 10 2011 Denis Baranov <baraka@altlinux.ru> 0.04-alt1
- initial build for ALT Linux Sisyphus
