%define _unpackaged_files_terminate_build 1
%define dist File-FcntlLock
Name: perl-%dist
Version: 0.22
Release: alt1.1.1.1.1

Summary: File locking with fcntl(2)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/J/JT/JTT/File-FcntlLock-%{version}.tar.gz

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1.1
- rebuild with new perl 5.20.1

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt2
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- 0.12 -> 0.14
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt2
- rebuilt for perl-5.14

* Sun Jan 23 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- initial revision
