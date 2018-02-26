## SPEC file for Perl module CGI-Expand

%define real_name  CGI-Expand

Name: perl-CGI-Expand
Version: 2.03
Release: alt1

Summary: converts a CGI query into structured data

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/CGI-Expand/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar
BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Oct 10 2010
BuildRequires: perl-CGI perl-Test-Exception

%description
Perl module CGI::Expand converts a CGI query into structured data
using a dotted name convention similar to TT2.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/CGI*

%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 2.03-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 2.02-alt1
- Initial build for ALT Linux Sisyphus
