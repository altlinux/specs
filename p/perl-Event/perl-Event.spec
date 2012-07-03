%define dist Event

Name: perl-%dist
Version: 1.20
Release: alt2

Summary: Event loop processing
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
The Event module provide a central facility to watch for various types
of events and invoke a callback when these events occur. The idea is to
delay the handling of events so that they may be dispatched in priority
order when it is safe for callbacks to execute.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_archlib/Event*
%perl_vendor_autolib/Event

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.20-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 1.18-alt1
- 1.18

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.13-alt1.1
- rebuilt with perl 5.12

* Mon Jun 21 2010 Victor Forsiuk <force@altlinux.org> 1.13-alt1
- 1.13

* Wed Jun 25 2008 Victor Forsyuk <force@altlinux.org> 1.11-alt1
- 1.11

* Wed Jun 06 2007 Victor Forsyuk <force@altlinux.org> 1.09-alt1
- 1.09

* Sat Jan 20 2007 Victor Forsyuk <force@altlinux.org> 1.08-alt1
- 1.08
- Package man pages.

* Mon Aug 07 2006 Alexey Tourbin <at@altlinux.ru> 1.06-alt1
- 1.02 -> 1.06

* Thu Dec 23 2004 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- NMU: 0.87 -> 1.02 (#5604)
- deparse.patch not needed due to rpm-build-perl enhancements
- manual pages not packaged (use perldoc)
- specfile cleanup

* Sun Oct 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.87-alt2
- deparse patch by at@.

* Thu Feb 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.87-alt1
- First build for Sisyphus.
