%define dist File-Sync
Name: perl-%dist
Version: 0.09
Release: alt1.2

Summary: Perl access to fsync() and sync() function calls
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
File::Sync provides Perl interfaces to the Unix sync(2) and POSIX.1b
fsync(2) system calls.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/File
%perl_vendor_autolib/File

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1.1
- rebuilt with perl 5.12

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.09-alt1
- Initial build for ALT Linux Sisyphus

* Sun Jul 02 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.09-alt0
- First build
