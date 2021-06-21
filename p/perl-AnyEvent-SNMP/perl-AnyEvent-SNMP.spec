## SPEC file for Perl module AnyEvent::SNMP

%define real_name AnyEvent-SNMP

Name: perl-AnyEvent-SNMP
Version: 6.02
Release: alt2

Summary: Perl adaptor to integrate Net::SNMP into AnyEvent

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/AnyEvent-SNMP/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Mar 31 2020
# optimized out: perl perl-AnyEvent perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Math-BigInt perl-Parse-CPAN-Meta perl-common-sense perl-parent python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-Net-SNMP perl-devel

BuildRequires: perl-Math-BigInt perl-AnyEvent perl-common-sense

Patch: AnyEvent-SNMP-6.02-perl532.patch

%description
Perl module AnyEvent::SNMP implements an alternative event
dispatcher for Net::SNMP, using AnyEvent as a backend.
This integrates Net::SNMP into AnyEvent. That means you can
make non-blocking Net::SNMP calls and as long as other parts
of your program also use AnyEvent (or some event loop
supported by AnyEvent), they will run in parallel.

%prep
%setup -q -n %real_name-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/AnyEvent/SNMP*

%changelog
* Mon Jun 21 2021 Igor Vlasenko <viy@altlinux.org> 6.02-alt2
- NMU: fixed build with perl 5.32+

* Tue Mar 31 2020 Nikolay A. Fetisov <naf@altlinux.org> 6.02-alt1
- New version

* Wed Mar 30 2016 Nikolay A. Fetisov <naf@altlinux.ru> 6.0-alt1
- Initial build for ALT Linux Sisyphus
