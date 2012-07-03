%define dist Gtk2-GladeXML
Name: perl-%dist
Version: 1.007
Release: alt1.2

Summary: Create user interfaces directly from Glade XML files
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: fonts-ttf-dejavu libglade-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2-devel xvfb-run

%description
Glade is a free user interface builder for GTK+ and GNOME. After designing
a user interface with glade-2 the layout and configuration are saved in an
XML file.  libglade  is a library which knows how to build and hook up the
user interface described in the Glade XML file at application run time.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%doc	AUTHORS NEWS README examples
%dir	%perl_vendor_archlib/Gtk2
	%perl_vendor_archlib/Gtk2/GladeXML.pm
	%perl_vendor_autolib/Gtk2
# XXX devel?
%dir	%perl_vendor_archlib/Gtk2/GladeXML
	%perl_vendor_archlib/Gtk2/GladeXML/Install

%changelog
* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 1.007-alt1.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 1.007-alt1.1
- rebuilt with perl 5.12

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.007-alt1
- Nev version 1.007

* Fri May 16 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.006-alt2
- Fix directories ownership

* Mon Mar 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.006-alt1
- Revives from orphaned
- New version 1.006
  - small bugfixes
  - adding new examples

* Sat Jun 18 2005 Alexey Tourbin <at@altlinux.ru> 1.005-alt1
- 1.004 -> 1.005

* Thu Feb 03 2005 Alexey Tourbin <at@altlinux.ru> 1.004-alt1
- 1.00 -> 1.004
- manual pages not packaged (use perldoc)
- always run tests (by utilizing xvfb-run)
- updated BuildRequires (with buildreq)

* Mon Aug 09 2004 Alexey Tourbin <at@altlinux.ru> 1.00-alt1
- initial revision
- license: LGPL
