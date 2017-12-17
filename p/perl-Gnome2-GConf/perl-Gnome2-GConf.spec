%define dist Gnome2-GConf
Name: perl-%dist
Version: 1.044
Release: alt6.1.1.1.1

Summary: Perl wrappers for the GConf configuration engine
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-Gnome2-1.044-alt-fix-build.patch

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: libGConf-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Glib-devel perl-podlators xvfb-run

BuildRequires: GConf

%description
This module allows you to use the GConf configuration system in order to
store/retrieve the configuration of an application.  GConf is a powerful
configuration manager based on a user daemon that handles a set of key and
value pairs, and notifies any changes of the value to every program that
monitors those keys.  GConf is used by GNOME 2.x.

%prep
%setup -q -n %dist-%version
%patch -p2

%ifndef _build_display
%def_without test
%endif

%build
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%doc	AUTHOR NEWS README
%dir	%perl_vendor_archlib/Gnome2
	%perl_vendor_archlib/Gnome2/GConf.pm
	%perl_vendor_autolib/Gnome2
# XXX devel?
%dir	%perl_vendor_archlib/Gnome2/GConf
%doc	%perl_vendor_archlib/Gnome2/GConf/*.pod
	%perl_vendor_archlib/Gnome2/GConf/Install

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.044-alt6.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.044-alt6.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.044-alt6.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.044-alt6.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.044-alt6
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.044-alt5
- rebuilt for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.044-alt4
- rebuilt for perl-5.14

* Mon Sep 12 2011 Radik Usupov <radik@altlinux.org> 1.044-alt3
- initial build for ALT Linux Sisyphus

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 1.044-alt2.1
- rebuilt with perl 5.12

* Wed Nov 19 2008 Vitaly Lipatov <lav@altlinux.ru> 1.044-alt2
- fix directory ownership violation
- remove man pages
- update buildreqs

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.044-alt1
- new version 1.044 (with rpmrb script)

* Sun Jun 10 2007 Vitaly Lipatov <lav@altlinux.ru> 1.043-alt1
- initial build for ALT Linux Sisyphus

