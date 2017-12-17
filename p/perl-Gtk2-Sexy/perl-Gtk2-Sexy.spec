%define dist Gtk2-Sexy
Name: perl-%dist
Version: 0.05
Release: alt3.1.1.1.1

Summary: Perl interface to the sexy widget collection
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: libenchant-devel libsexy-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2-devel perl-Module-Install perl-podlators xvfb-run

%description
This module allows a perl developer to access the widgets of the sexy
widget collection, which currently includes the following widgets:

SexyIconEntry is a GtkEntry with support for inline icons.
SexySpellEntry is a GtkEntry with inline spell checking.
SexyUrlLabel is a GtkLabel with support for embedded hyperlinks.

%prep
%setup -q -n %dist-%version

%ifndef _build_display
%def_without test
%endif

%build
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%doc	ChangeLog README examples
%dir	%perl_vendor_archlib/Gtk2
	%perl_vendor_archlib/Gtk2/Sexy.pm
	%perl_vendor_autolib/Gtk2
# XXX devel?
%dir	%perl_vendor_archlib/Gtk2/Sexy
%doc	%perl_vendor_archlib/Gtk2/Sexy/*.pod
	%perl_vendor_archlib/Gtk2/Sexy/Install

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt3
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt2
- rebuilt for perl-5.16

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt1.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Tue Nov 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- new version 0.04 (with rpmrb script)

* Sat Nov 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt2
- fix directory ownership violation
- disable man packaging

* Sat Dec 15 2007 Vitaly Lipatov <lav@altlinux.ru> 0.02-alt1
- initial build for ALT Linux Sisyphus

