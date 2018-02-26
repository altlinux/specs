%define dist File-ReadBackwards
Name: perl-%dist
Version: 1.05
Release: alt1

Summary: Read a file backwards by lines

License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/U/UR/URI/File-ReadBackwards-1.05.tar.gz

BuildArch: noarch

# Added by buildreq2 on Mon Jul 17 2006
BuildRequires: perl-devel

%description
This module reads a file backwards line by line. It is simple to use,
memory efficient and fast. It supports both an object and a tied handle
interface.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.04-alt1
- initial revision
