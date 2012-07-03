%define dist Unix-Mknod
Name: perl-%dist
Version: 0.04
Release: alt1

Summary: Perl extension for mknod, major, minor, and makedev
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: perl-devel

%description
This module allows access to the device routines major()/minor()/makedev()
that may or may not be macros in .h files.  It also allows access to the
mknod(2) system call.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Unix
%perl_vendor_autolib/Unix

%changelog
* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision
