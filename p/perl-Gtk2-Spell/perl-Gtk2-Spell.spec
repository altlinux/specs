%define dist Gtk2-Spell
Name: perl-%dist
Version: 1.04
Release: alt2.1.1.1.1

Summary: Perl bindings for GtkSpell with Gtk2
License: LGPL 2.1
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: libgtkspell-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2-devel xvfb-run

%description
Perl bindings to the 2.x series of the GtkSpell graphical user interface
library.  This module allows you to write perl applications that utilize
the GtkSpell library for mis-spelled word highlighting.

%prep
%setup  -n %dist-%version
sed -i- 's@1.00rc2@1.0@g' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	AUTHORS ChangeLog README
%dir	%perl_vendor_archlib/Gtk2
	%perl_vendor_archlib/Gtk2/Spell.pm
	%perl_vendor_autolib/Gtk2
# XXX devel?
%dir	%perl_vendor_archlib/Gtk2/Spell
	%perl_vendor_archlib/Gtk2/Spell/Install

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt2
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt1
- 1.03 -> 1.04
- built for perl-5.16

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt2.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt2.1
- rebuilt with perl 5.12

* Thu Aug 31 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.03-alt2
- Rebuild with perl-Gtk2-1.132-alt1 / perl-Cairo-0.91-alt1

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.03-alt1
- Initial build for ALT Linux
