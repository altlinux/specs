%define module Gnome2-Print

Name: perl-%module
Version: 1.000
Release: alt1.2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Perl wrappers for the Gnome Print utilities
License: LGPLv2+
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Gnome2/Gnome2-Print-%version.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011 (-bi)
BuildRequires: fonts-ttf-dejavu libgnomeprintui-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2-devel perl-podlators

%package devel
Summary: Perl wrappers for the Gnome Print utilities
Group: Development/Perl
Requires: %name = %version-%release
Requires: libgnomeprintui-devel
# Gnome2/Print/Install/Files.pm:deps
Requires: perl-Pango-devel
Requires: perl-Glib-devel
Requires: perl-Gtk2-devel
Requires: perl-Cairo-devel

%description
This module allows you to use the GNOME Print libraries within your
applications written using the gtk2-perl wrapper.  The GNOME Print libraries
(also known as libgnomeprint and libgnomeprintui) allow you to create
printable documents (using various frontends) and offer standard widgets in
order to mainatin a UI consistent for all GNOME applications.

%description devel
This module allows you to use the GNOME Print libraries within your
applications written using the gtk2-perl wrapper.  The GNOME Print libraries
(also known as libgnomeprint and libgnomeprintui) allow you to create
printable documents (using various frontends) and offer standard widgets in
order to mainatin a UI consistent for all GNOME applications.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# XXX Can't locate Gnome2/Print/Config.pm in @INC
%add_findreq_skiplist */Gnome2/Print/Config/Constants.pm

%files
%doc	AUTHORS NEWS README examples
%dir	%perl_vendor_archlib/Gnome2
	%perl_vendor_archlib/Gnome2/Print.pm
	%perl_vendor_autolib/Gnome2

%files devel
%dir	%perl_vendor_archlib/Gnome2
%dir	%perl_vendor_archlib/Gnome2/Print
%doc	%perl_vendor_archlib/Gnome2/Print/*.pod
	%perl_vendor_archlib/Gnome2/Print/Install

%doc	%perl_vendor_archlib/Gnome2/Print/Config
%doc	%perl_vendor_archlib/Gnome2/Print/Font

%changelog
* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 1.000-alt1.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 1.000-alt1.1
- rebuilt with perl 5.12

* Fri Aug 21 2009 Victor Forsyuk <force@altlinux.org> 1.000-alt1
- Initial build.
