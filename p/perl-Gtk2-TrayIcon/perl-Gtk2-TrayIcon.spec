%define dist Gtk2-TrayIcon
Name: perl-Gtk2-TrayIcon
Version: 0.06
Release: alt2.2

Summary: %dist Perl module
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2-devel xvfb-run

%description
This module allows a Perl developer to embed an arbitrary widget in a
System Tray like the Gnome notification area.

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
	%perl_vendor_archlib/Gtk2/TrayIcon.pm
	%perl_vendor_autolib/Gtk2
# XXX devel?
%dir	%perl_vendor_archlib/Gtk2/TrayIcon
	%perl_vendor_archlib/Gtk2/TrayIcon/Install

%changelog
* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt2.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt2.1
- rebuilt with perl 5.12

* Wed Nov 19 2008 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt2
- fix directory ownership violation
- update buildreq

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- new version 0.06 (with rpmrb script)

* Tue Mar 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt2
- return from orphaned, cleanup spec, add Source Url
- update buildreq

* Wed Mar 16 2005 LAKostis <lakostis at altlinux.ru> 0.04-alt1.1
- cleanup buildreq/requires.
- add missing requires for -devel package.

* Sun Mar 7 2005 LAKostis <lakostis at altlinux.ru> 0.04-alt1
- first build for Sisyphus
- manual pages not packaged (use perldoc)
- always run tests (by utilizing xvfb-run)
