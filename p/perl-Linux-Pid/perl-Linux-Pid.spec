%define dist Linux-Pid
Name: perl-%dist
Version: 0.04
Release: alt2

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
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- rebuilt for perl-5.14

* Thu Mar 10 2011 Denis Baranov <baraka@altlinux.ru> 0.04-alt1
- initial build for ALT Linux Sisyphus
