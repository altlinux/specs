%define dist Unix-Mknod
Name: perl-%dist
Version: 0.04
Release: alt3.1.1.1.1

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt3
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt2
- rebuilt for perl-5.16

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision
