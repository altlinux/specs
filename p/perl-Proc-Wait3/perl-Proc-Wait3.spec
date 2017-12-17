%define _unpackaged_files_terminate_build 1
%define dist Proc-Wait3
Name: perl-%dist
Version: 0.05
Release: alt1.1.1.1

Summary: Perl wrapper around the wait3(1) system call
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/C/CT/CTILMES/Proc-Wait3-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-devel

%description
Proc::Wait3 is a simple perl wrapper around the wait3(1) system call.
It reaps dead children like wait(), but also reports on the resource
usage of the child.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%perl_vendor_archlib/Proc
%perl_vendor_autolib/Proc

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt3
- rebuilt for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- rebuilt for perl-5.14

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1
- initial build
