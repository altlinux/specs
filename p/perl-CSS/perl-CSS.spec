%define module CSS

Name: perl-%module
Version: 1.09
Release: alt1

Summary: Object oriented access to Cascading Style Sheets (CSS)
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/I/IA/IAMCAL/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 10 2011
BuildRequires: perl-Parse-RecDescent perl-devel

%description
This module can be used, along with a CSS::Parse::* module, to parse
CSS data and represent it as a tree of objects. Using a CSS::Adaptor::*
module, the CSS data tree can then be transformed into other formats.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CSS/
%perl_vendor_privlib/CSS.pm

%changelog
* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 1.09-alt1
- 1.09

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Victor Forsiuk <force@altlinux.org> 1.08-alt1
- 1.08
- Fix FTBFS (solution by Paul Howarth, taken from Fedora package).

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.07-alt2
- fix directory ownership violation

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.07-alt1
- first build for ALT Linux Sisyphus

