%define module Gtk2-GladeXML-Simple

Name: perl-%module
Version: 0.32
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: A clean object-oriented interface to Gtk2::GladeXML
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Gtk2/%module-%version.tar.gz

BuildArch: noarch
# Automatically added by buildreq on Fri Aug 21 2009 (-bi)
BuildRequires: perl-Gtk2-GladeXML perl-XML-SAX perl-devel

%description
Gtk2::GladeXML::Simple is a module that provides a clean and easy interface for
Gnome/Gtk2 and Glade applications using an object-oriented syntax.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/*
%perl_vendor_privlib/Gtk2

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 21 2009 Victor Forsyuk <force@altlinux.org> 0.32-alt1
- Initial build.
