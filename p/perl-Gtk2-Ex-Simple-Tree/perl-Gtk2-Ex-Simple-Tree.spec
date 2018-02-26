%define module Gtk2-Ex-Simple-Tree

Name: perl-%module
Version: 0.50
Release: alt1.1

Summary: A simple interface to Gtk2's complex MVC tree widget
License: LGPLv2.1+
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Gtk2/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Aug 21 2009 (-bi)
BuildRequires: perl-Gtk2-Ex-Simple-List perl-Gtk2-devel

%description
Simple::Tree is a simple interface to the powerful but complex Gtk2::TreeView
and Gtk2::TreeStore combination, implementing using tied arrays to make thing
simple and easy.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Gtk2/Ex

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 21 2009 Victor Forsyuk <force@altlinux.org> 0.50-alt1
- Initial build.
