## SPEC file for Perl module Gtk2::Ex:PrintDialog
## Used in PodBrowser

%define version    0.03
%define release    alt1

Name: perl-Gtk2-Ex-PrintDialog
Version: %version
Release: alt1.1

Summary: Perl dialog for printing data in GTK+ applications
Summary(ru_RU.UTF-8): диалог печати из приложений GTK+ на Perl

License: GPL or Artistic
Group: Development/Perl
URL: http://search.cpan.org/~gbrown/Gtk2-Ex-PrintDialog/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

%define real_name Gtk2-Ex-PrintDialog
Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBROWN/%real_name-%version.tar.gz
BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: perl-devel fontconfig perl-Exporter-Cluster 
BuildPreReq: perl-Gtk2 perl-Locale-gettext perl-Net-CUPS

%description
Perl module Gtk2::Ex::PrintDialog implements a dialog widget
that can be used  to print  PostScript data.  It is intended
to be a lightweight and pure-perl alternative to the 
Gnome2::Print libraries.

The dialog is intended to comply with the GNOME Human Interface
Guidelines (HIG).  It allows the user  to print  to any printer 
installed on the system, or to an external command such as lpr, 
or to print a PostScript or PDF file.

# Rigth now ths module doesn't contain usable tests
%def_without test

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%exclude /.perl.req
%perl_vendor_privlib/Gtk2/Ex/PrintDialog*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon May 07 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.03-alt1
- New version 0.03

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.02-alt1
- Initial build for ALT Linux Sisyphus

* Thu Aug 10 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.02-alt0
- Initial build
