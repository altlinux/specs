%define dist Gtk2-Spell
Name: perl-%dist
Version: 1.03
Release: alt2.2

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
* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt2.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt2.1
- rebuilt with perl 5.12

* Thu Aug 31 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.03-alt2
- Rebuild with perl-Gtk2-1.132-alt1 / perl-Cairo-0.91-alt1

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.03-alt1
- Initial build for ALT Linux
