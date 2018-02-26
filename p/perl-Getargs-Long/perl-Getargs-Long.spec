%define module_name Getargs-Long

Name: perl-%module_name
Version: 1.1003
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: %module_name module for perl
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/modules/by-module/Getargs/%module_name-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Aug 01 2008
BuildRequires: perl-Log-Agent perl-Module-Install

%description
The "Getargs::Long" module allows usage of named parameters in function calls,
along with optional argument type-checking. It provides an easy way to get at
the parameters within the routine, and yields concise descriptions for the
common cases of all-mandatory and all-optional parameter lists.

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Getargs/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.1003-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 1.1003-alt1
- 1.1003

* Tue Jul 03 2007 Victor Forsyuk <force@altlinux.org> 1.1001-alt1
- Initial build.
