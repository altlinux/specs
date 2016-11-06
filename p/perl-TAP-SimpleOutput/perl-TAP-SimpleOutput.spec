## SPEC file for Perl module TAP::SimpleOutput

%define real_name TAP-SimpleOutput

Name: perl-TAP-SimpleOutput
Version: 0.004
Release: alt1

Summary: simple closure-driven TAP generator

License: %lgpl21only
Group: Development/Perl

URL: http://search.cpan.org/dist/TAP-SimpleOutput/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-devel
BuildRequires: perl-Sub-Exporter-Progressive perl-Test-CheckDeps

%description
Perl module TAP::SimpleOutput provides one function, counters(),
that returns a number of simple closures designed to help
output TAP easily and correctly, with a minimum of fuss.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/TAP*

%changelog
* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.004-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.003-alt1
- New version

* Fri Sep 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.002-alt2
- Rising release to override package from Autoimports/Sisyphus repository

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.002-alt1
- Initial build for ALT Linux Sisyphus
