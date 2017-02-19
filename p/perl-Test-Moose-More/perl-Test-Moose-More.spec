## SPEC file for Perl module Test::Moose::More

%define real_name Test-Moose-More

Name: perl-Test-Moose-More
Version: 0.043
Release: alt1

Summary: more tools for testing Moose packages

License: %lgpl21only
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-Moose-More/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Jun 06 2015
# optimized out: perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-JSON-PP perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-clean perl-parent
BuildRequires: perl-Moose perl-Perl-Version perl-Syntax-Keyword-Junction perl-TAP-SimpleOutput perl-Test-CheckDeps perl-aliased perl-namespace-autoclean

%description
Perl module Test::Moose::More contains a number of additional
tests that can be employed against Moose classes/roles. It is
intended to replace Test::Moose in your tests, and re-exports
any tests that it has and we do not, yet.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test*

%changelog
* Sun Feb 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.043-alt1
- New version

* Tue Feb 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.042-alt1
- New version

* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.038-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.037-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.035-alt1
- New version

* Sat Jun 06 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.029-alt1
- New version

* Sun Nov 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.025-alt1
- New version

* Fri Sep 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.024-alt2
- Rising release to override package from Autoimports/Sisyphus repository

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.024-alt1
- Initial build for ALT Linux Sisyphus
