%define dist Linux-Inotify2
Name: perl-%dist
Version: 1.22
Release: alt2

Summary: Scalable directory/file change notification
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-common-sense perl-devel

%description
This module implements an interface to the Linux 2.6.13 and later
Inotify file/directory change notification system.

%prep
%setup -q -n %dist-%version

# wrong cancel return value?
sed -i- 's/watch->cancel,/watch->cancel || 1,/' t/01_inotify.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Linux
%perl_vendor_autolib/Linux

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.22-alt2
- rebuilt for perl-5.14
- disabled $watch->cancel test for now

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.21-alt2.1
- rebuilt with perl 5.12

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 1.21-alt2
- Fixed directory packaging

* Tue Apr 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.21-alt1
- New version

* Fri Feb 20 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- Build for ALT
