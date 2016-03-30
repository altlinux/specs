## SPEC file for Perl module AnyEvent::Graphite

%define real_name AnyEvent-Graphite

Name: perl-AnyEvent-Graphite
Version: 0.08
Release: alt1

Summary: Perl non-blocking Graphite client

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/AnyEvent-Graphite/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Wed Mar 30 2016
# optimized out: perl-AnyEvent perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-Guard perl-JSON-PP perl-Math-BigInt perl-Module-Metadata perl-Net-SNMP perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-common-sense perl-devel perl-parent perl-podlators python3
BuildRequires: perl-AnyEvent-SNMP perl-HTML-Parser perl-Module-Build

%description
Perl module AnyEvent::Graphite provides a non-blocking
event-driven Graphite client to poll Graphite data sources
or asyncronously post into them.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/AnyEvent/Graphite*

%_bindir/graphite_client

%changelog
* Wed Mar 30 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.08-alt1
- Initial build for ALT Linux Sisyphus
