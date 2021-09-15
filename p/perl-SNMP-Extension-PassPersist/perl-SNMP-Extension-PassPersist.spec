## SPEC file for Perl module SNMP::Extension::PassPersist

%define real_name SNMP-Extension-PassPersist

Name: perl-%real_name
Version: 0.07
Release: alt1

Summary: Generic pass/pass_persist extension framework for Net-SNMP

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/pod/SNMP::Extension::PassPersist

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses perl(Module/Build.pm)
BuildRequires: perl-IO-String perl-Sort-Key-OID
# for tests
BuildRequires: perl-JSON perl-Class-Accessor perl-List-MoreUtils perl-IPC-Run perl-Test-Pod perl-Test-Pod-Coverage

Requires: perl-IO-String perl-Sort-Key-OID

%description
This module is a framework for writing Net-SNMP extensions using the pass or
pass_persist mechanisms.

When in pass_persist mode, it provides a mechanism to spare ressources by
quitting from the main loop after a given number of idle cycles.

This module can use Sort::Key::OID when it is available, for sorting OIDs
faster than with the internal pure Perl function.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/SNMP/Extension/PassPersist*

%changelog
* Wed Sep 15 2021 L.A. Kostis <lakostis@altlinux.ru> 0.07-alt1
- Initial build for ALTLinux.

