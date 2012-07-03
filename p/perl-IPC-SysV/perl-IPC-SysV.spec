%define dist IPC-SysV
Name: perl-%dist
Version: 2.03
Release: alt2

Summary: System V IPC constants and system calls
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 2.03-alt2
- rebuilt for perl-5.14

* Tue Nov 02 2010 Vladimir Lettiev <crux@altlinux.ru> 2.03-alt1
- initial build
