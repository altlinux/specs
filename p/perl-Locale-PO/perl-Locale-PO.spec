%define dist Locale-PO
Name: perl-%dist
Version: 0.21
Release: alt1.1

Summary: Object-oriented interface to gettext po-file entries
License: %perl_license
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/A/AG/AGENT/Makefile-DOM-0.004.tar.gz
Source: %dist-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Fri Jan 15 2010
BuildRequires: perl-File-Slurp perl-devel

%description
This module provides methods for manipulating objects that represent
entries in a gettext po-file (untranslated and translated strings,
with associated comments). It can load and save complete po-files.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Locale/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jan 15 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.21-alt1
- initial build for Sisyphus

