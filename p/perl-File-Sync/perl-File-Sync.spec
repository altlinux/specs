%define dist File-Sync
Name: perl-%dist
Version: 0.11
Release: alt2.1.1.1.1

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt2
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- 0.09 -> 0.11
- built for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1.1
- rebuilt with perl 5.12

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.09-alt1
- Initial build for ALT Linux Sisyphus

* Sun Jul 02 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.09-alt0
- First build
