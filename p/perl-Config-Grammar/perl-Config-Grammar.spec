%define dist Config-Grammar
Name: perl-%dist
Version: 1.13
Release: alt1

Summary: A grammar-based, user-friendly config parser

License: GPL-1.0-or-later OR Artistic-1.0-Perl
Group: Development/Perl
Url: https://metacpan.org/release/%dist

# Source-url: https://cpan.metacpan.org/authors/id/D/DS/DSCHWEI/%dist-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-perl perl-devel

%description
Config::Grammar is a module to parse configuration files with a
user-friendly grammar definition. It allows defining hierarchical
configuration sections, variable assignments, and tabular data.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendorlib/Config/

%changelog
* Thu Feb 05 2026 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- initial build for ALT Sisyphus
