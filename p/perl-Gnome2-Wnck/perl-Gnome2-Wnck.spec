%define module Gnome2-Wnck

Name: perl-%module
Version: 0.16
Release: alt1.2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Perl interface to the Window Navigator Construction Kit
License: LGPL
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Gnome2/%module-%version.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: libwnck-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2-devel perl-podlators

%description
This module allows a Perl developer to use the Window Navigator Construction Kit
library (libwnck for short) to write tasklists and pagers.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	NEWS README
%dir	%perl_vendor_archlib/Gnome2
	%perl_vendor_archlib/Gnome2/Wnck.pm
	%perl_vendor_autolib/Gnome2
# XXX devel?
%dir	%perl_vendor_archlib/Gnome2/Wnck
%doc	%perl_vendor_archlib/Gnome2/Wnck/*.pod
	%perl_vendor_archlib/Gnome2/Wnck/Install

%changelog
* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 0.16-alt1.2
- rebuilt for perl-5.14

* Tue Nov 09 2010 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt1.1
- rebuilt with perl 5.12

* Fri Aug 07 2009 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- Initial build.
