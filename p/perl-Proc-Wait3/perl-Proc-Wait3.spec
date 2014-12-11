%define dist Proc-Wait3
Name: perl-%dist
Version: 0.04
Release: alt4.1

Summary: Perl wrapper around the wait3(1) system call
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
