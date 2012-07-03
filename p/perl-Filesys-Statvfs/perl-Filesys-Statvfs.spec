%define dist Filesys-Statvfs
Name: perl-%dist
Version: 0.82
Release: alt1

Summary: Perl extension for statvfs() and fstatvfs()
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: perl-devel

%description
Interface for statvfs() and fstatvfs()

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
* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 0.82-alt1
- initial reivision
