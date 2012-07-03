%define dist Lchown
Name: perl-%dist
Version: 1.01
Release: alt1

Summary: Perl interface to the lchown(2) system call
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
The Lchown module provides a perl interface to the lchown(2) UNIX system
call, on systems that support lchown.  The lchown(2) call is used to
change the ownership and group of symbolic links.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Lchown*
%perl_vendor_autolib/Lchown

%changelog
* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- initial revision
