%define module Jevix
%define m_distro %module
%define _enable_test 1

Name: perl-Jevix
Version: 0.9.7
Release: alt1

Summary: HTML/XHTML filter and typograph for Perl

License: MIT
Group: Development/Perl
Url: http://jevix.ru/project/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://jevix.ru/distributions/perl/jevix-perl-%version.zip
Source: %name-%version.tar

# Automatically added by buildreq on Wed Feb 03 2010 (-bi)
BuildRequires: perl-Encode

%description
HTML/XHTML filter and typograph for Perl

%prep
%setup

%install
mkdir -p %buildroot%perl_vendor_privlib/
cp -a Jevix/ %buildroot%perl_vendor_privlib/

%files
%doc readme.txt sample.pl testsUtf.pl
%perl_vendor_privlib/Jevix/

%changelog
* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- initial build for ALT Linux Sisyphus

