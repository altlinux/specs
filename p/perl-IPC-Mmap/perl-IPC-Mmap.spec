%define dist IPC-Mmap
Name: perl-IPC-Mmap
Version: 0.21
Release: alt2

Summary: Minimal unified mmap for POSIX and Win32
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-IPC-SysV perl-devel perl-threads

%description
Provides a minimal interface to POSIX mmap(), and its
Win32 equivalent. Abstract base class that is used by
the IPC::Mmap::POSIX and IPC::Mmap::Win32 implementations.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/IPC
%perl_vendor_autolib/IPC

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.21-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1.1
- rebuilt with perl 5.12

* Thu Apr 29 2010 Mikhail Pokidko <pma@altlinux.org> 0.14-alt1
- initial build for ALT Linux Sisyphus
