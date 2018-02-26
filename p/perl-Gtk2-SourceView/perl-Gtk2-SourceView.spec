%define module Gtk2-SourceView
%def_without test

Name: perl-%module
Version: 1.000
Release: alt2.1

Summary: Perl wrappers for the GtkSourceView widget
License: LGPLv2+
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-SourceView-%version.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011 (-bi)
BuildRequires: gcc-c++ libgtksourceview1-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gnome2-Print-devel perl-podlators

%description
Perl bindings to the 1.x series of the GtkSourceView widget libraries. This
module allows you to write Perl applications that utilize the GtkSourceView
library for source editing.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	AUTHORS NEWS README
%dir	%perl_vendor_archlib/Gtk2
	%perl_vendor_archlib/Gtk2/SourceView.pm
	%perl_vendor_autolib/Gtk2
# XXX devel?
%dir	%perl_vendor_archlib/Gtk2/SourceView
%doc	%perl_vendor_archlib/Gtk2/SourceView/*.pod
	%perl_vendor_archlib/Gtk2/SourceView/Install

%changelog
* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.000-alt2.1
- rebuilt for perl-5.14

* Mon Mar 28 2011 Victor Forsiuk <force@altlinux.org> 1.000-alt2
- Fix BuildRequires.

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 1.000-alt1.1
- rebuilt with perl 5.12

* Fri Aug 21 2009 Victor Forsyuk <force@altlinux.org> 1.000-alt1
- Initial build.
