%define module Goo-Canvas

Name: perl-%module
Version: 0.06
Release: alt3.1.1.1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Perl interface to the GooCanvas
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Goo/%module-%version.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: libgoocanvas-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2-devel perl-podlators

%description
Perl interface to the GooCanvas.

%prep
%setup -n %module-%version

%build
%perl_vendor_build 

%install
%perl_vendor_install

%files
%doc	Changes README demo
%dir	%perl_vendor_archlib/Goo
	%perl_vendor_archlib/Goo/Canvas.pm
%doc	%perl_vendor_archlib/Goo/Canvas.pod
	%perl_vendor_autolib/Goo
# XXX devel?
%dir	%perl_vendor_archlib/Goo/Canvas
%doc	%perl_vendor_archlib/Goo/Canvas/*.pod
	%perl_vendor_archlib/Goo/Canvas/Install

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt3
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt2
- rebuilt for perl-5.16

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt1.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1.1
- rebuilt with perl 5.12

* Fri Aug 07 2009 Victor Forsyuk <force@altlinux.org> 0.06-alt1
- Initial build.
