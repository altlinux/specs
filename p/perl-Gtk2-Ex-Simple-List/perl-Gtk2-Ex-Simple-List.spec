## SPEC file for Perl module Gtk2::Ex:Simple::List
## Used in PodBrowser

%define version    0.50
%define release    alt1

Name: perl-Gtk2-Ex-Simple-List
Version: %version
Release: alt1.1

Summary: a simple interface to Gtk2's complex MVC list widget 

License: GPL or Artistic
Group: Development/Perl
URL: http://search.cpan.org/~rmcfarla/Gtk2-Ex-Simple-List/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Gtk2-Ex-Simple-List
Source: http://search.cpan.org/CPAN/authors/id/R/RM/RMCFARLA/Gtk2-Perl-Ex/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildPreReq: perl-devel fontconfig perl-Gtk2-devel

%description
Perl module  Gtk2::Ex::Simple::List is a simple interface to the
powerful but complex Gtk2::TreeView and Gtk2::ListStore modules,
implementing  list and tree  widgets using  tied arrays  to make 
thing simple and easy.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Gtk2/Ex/Simple/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.50-alt1
- Initial build for ALT Linux Sisyphus

* Thu Aug 10 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.50-alt0
- Initial build
