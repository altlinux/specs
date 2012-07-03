%define dist Filesys-Df
Name: perl-%dist
Version: 0.92
Release: alt1.2

Summary: Perl extension for filesystem disk space information
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
This module provides a way to obtain filesystem disk space
information.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Filesys
%perl_vendor_autolib/Filesys

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.92-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.92-alt1.1
- rebuilt with perl 5.12

* Tue Apr 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.92-alt1
- initial build for ALT Linux Sisyphus
