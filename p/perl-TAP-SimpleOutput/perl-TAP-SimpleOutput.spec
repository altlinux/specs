## SPEC file for Perl module TAP::SimpleOutput

%define real_name TAP-SimpleOutput

Name: perl-TAP-SimpleOutput
Version: 0.009
Release: alt1

Summary: simple closure-driven TAP generator

License: %lgpl21only
Group: Development/Perl

URL: http://search.cpan.org/dist/TAP-SimpleOutput/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Feb 19 2017
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Data-OptList perl-Encode perl-JSON-PP perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Sub-Install perl-Try-Tiny perl-devel python-base python-modules python3-base
BuildRequires: perl-Class-Load perl-Perl-Version perl-Sub-Exporter-Progressive perl-Test-CheckDeps

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
* Sun Feb 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.009-alt1
- New version

* Sat Jan 21 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.008-alt1
- New version

* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.004-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.003-alt1
- New version

* Fri Sep 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.002-alt2
- Rising release to override package from Autoimports/Sisyphus repository

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.002-alt1
- Initial build for ALT Linux Sisyphus
