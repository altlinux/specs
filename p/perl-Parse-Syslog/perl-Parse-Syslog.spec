%define module Parse-Syslog

Name: perl-%module
Version: 1.10
Release: alt1.1

Summary: Parse-Syslog perl module
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Parse/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Jan 09 2008
BuildRequires: perl-File-Tail perl-IO-stringy perl-devel

%description
Parse::Syslog presents a simple interface to parse syslog files.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Jan 09 2008 Victor Forsyuk <force@altlinux.org> 1.10-alt1
- 1.10

* Thu Sep 07 2006 Victor Forsyuk <force@altlinux.ru> 1.09-alt1
- 1.09

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.03-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Sep 15 2004 Victor Forsyuk <force@altlinux.ru> 1.03-alt1
- Initial build for Sisyphus.
