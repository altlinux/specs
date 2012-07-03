%define dist Device-SerialPort
Name: perl-%dist
Version: 1.04
Release: alt2

Summary: Linux/POSIX emulation of Win32::SerialPort functions
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel perl-podlators

%description
This module provides an object-based user interface essentially
identical to the one provided by the Win32::SerialPort module.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes
%_bindir/modemtest
%_man1dir/modemtest.1*
%perl_vendor_archlib/Device
%perl_vendor_autolib/Device

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.04-alt2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt1.1.1
- rebuilt with perl 5.12

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1.1
- NMU for unknown reason

* Tue Apr 15 2008 Michael Bochkaryov <misha@altlinux.ru> 1.04-alt1
- first build for ALT Linux Sisyphus
