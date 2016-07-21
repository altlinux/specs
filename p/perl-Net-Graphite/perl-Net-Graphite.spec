## SPEC file for Perl module Net::Graphite

%define real_name Net-Graphite

Name: perl-Net-Graphite
Version: 0.17
Release: alt1

Summary: Perl module with interface for Graphite

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Net-Graphite/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Mar 29 2016
# optimized out: python3 python3-base
BuildRequires: perl-Encode perl-devel

%description
Perl module Net::Graphite provides interface for Graphite,
http://graphite.readthedocs.org/

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Net/Graphite*

%changelog
* Thu Jul 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.17-alt1
- New version

* Tue Mar 29 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.16-alt1
- Initial build for ALT Linux Sisyphus
