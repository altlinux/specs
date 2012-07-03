# SPEC file for building Perl module Config-Std

%define real_name Config-Std

Name: perl-Config-Std
Version: 0.900
Release: alt1

Summary: Perl module for work with configuration files

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~bricker/Config-Std/
BuildArch: noarch

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Mar 08 2010
BuildRequires: perl-Class-Std perl-Module-Build perl-PerlIO perl-Test-Pod perl-Test-Pod-Coverage

BuildRequires: perl-version

%description
Perl module Config::Std implements loading and saving configuration
files in a standard format.

The configuration language is deliberately simple and limited,
and the module works hard to preserve as much information (section
order, comments, etc.) as possible when a configuration file is
updated.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes

%perl_vendor_privlib/Config/Std*

%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.900-alt1
- New version 0.900

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Mar 08 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.0.7-alt1
- New version 0.0.7

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.0.5-alt1
- New version 0.0.5

* Wed Dec 10 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.0.4-alt2
- Rebuild with current RPM

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.0.4-alt1
- Initial build for ATL Linux Sisyphus
