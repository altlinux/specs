%define dist File-FcntlLock
Name: perl-%dist
Version: 0.12
Release: alt2

Summary: File locking with fcntl(2)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
FcntlLock is a module to do file locking in an object oriented fashion
using the fcntl(2) system call. This allows locks on parts of a file as
well as on the whole file and overcomes some known problems with flock(2),
on which Perls flock() function is based.

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
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt2
- rebuilt for perl-5.14

* Sun Jan 23 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- initial revision
