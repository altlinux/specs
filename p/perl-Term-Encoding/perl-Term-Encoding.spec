## SPEC file for Perl module Term::Encoding

Name: perl-Term-Encoding
Version: 0.02
Release: alt3

Summary: Perl module to detect encoding of the current terminal

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Term-Encoding/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Term-Encoding
Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Sep 14 2014
BuildRequires: perl-devel

%description
Term::Encoding is a simple module to detect an encoding the
current terminal expects, in various ways.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Term*


%changelog
* Wed Sep 17 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.02-alt3
- Rising release to override package from Autoimports/Sisyphus repository

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.02-alt1
- Initial build for ALT Linux Sisyphus

