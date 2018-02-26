%define dist Gnome2-Canvas

Name: perl-%dist
Version: 1.002
Release: alt3.2

Summary: Gnome2-Canvas Perl module
License: LGPL
Group: Development/Perl

URL: http://search.cpan.org/dist/Gnome2-Canvas/
Source: http://www.cpan.org/modules/by-module/Gnome2/%dist-%version.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: fonts-ttf-dejavu libgnomecanvas-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2-devel perl-podlators xvfb-run

%package devel
Summary: Gnome2-Canvas Perl module (development files)
License: LGPL
Group: Development/Perl
Requires: %name = %version-%release
Requires: libgnomecanvas-devel
# Gnome2/Canvas/Install/Files.pm:deps
Requires: perl-Pango-devel
Requires: perl-Glib-devel
Requires: perl-Gtk2-devel
Requires: perl-Cairo-devel

%description
The Gnome2::Canvas module allows a perl developer to use the GnomeCanvas
widget with Gtk2-Perl.

%description devel
The Gnome2::Canvas module allows a perl developer to use the GnomeCanvas
widget with Gtk2-Perl.

This package contains Gnome2-Canvas development files and documentation
for developers (overview of internals and internal API reference).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%doc 	AUTHORS NEWS README canvas_demo
%dir	%perl_vendor_archlib/Gnome2
	%perl_vendor_archlib/Gnome2/Canvas.pm
%doc	%perl_vendor_archlib/Gnome2/Canvas.pod
	%perl_vendor_autolib/Gnome2

%files devel
%dir	%perl_vendor_archlib/Gnome2
%dir	%perl_vendor_archlib/Gnome2/Canvas
%doc	%perl_vendor_archlib/Gnome2/Canvas/*.pod
	%perl_vendor_archlib/Gnome2/Canvas/Install

%changelog
* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 1.002-alt3.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 1.002-alt3.1
- rebuilt with perl 5.12

* Tue Apr 10 2007 Victor Forsyuk <force@altlinux.org> 1.002-alt3
- Drop build dependency on non-distributable fonts-ttf-ms.

* Tue Feb 13 2007 Victor Forsyuk <force@altlinux.org> 1.002-alt2
- Adopted an orphan.
- Refresh build requires.

* Mon Mar 14 2005 LAKostis <lakostis at altlinux.ru> 1.002-alt1.1
- fix build requires.
- fix URL entry.
- add missing requires to -devel package.

* Sun Mar 07 2005 LAkostis <lakostis at altlinux.ru> 1.002-alt1
- manual pages not packaged (use perldoc)
- first build for Sisyphus.

