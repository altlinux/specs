## SPEC file for Perl module autobox::Junctions

%define real_name autobox-Junctions

Name: perl-autobox-Junctions
Version: 0.002
Release: alt1

Summary: Perl module for autoboxified junction-style operators

License: %lgpl21only
Group: Development/Perl

URL: http://search.cpan.org/dist/autobox-Junctions/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Data-OptList perl-Devel-Symdump perl-Encode perl-JSON-PP perl-Mixin-Linewise perl-Module-Metadata perl-Params-Util perl-Parse-CPAN-Meta perl-PerlIO-utf8_strict perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Eventual perl-Pod-Parser perl-Pod-Simple perl-Scope-Guard perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-devel perl-parent
BuildRequires: perl-Pod-Coverage-TrustPod perl-Syntax-Keyword-Junction perl-Test-CheckDeps perl-Test-NoTabs perl-Test-Pod perl-Test-Pod-Coverage perl-autobox

%description
Perl module autobox::Junctions is a simple autoboxifying wrapper
around Syntax::Keyword::Junction, that provides array and array
references with the functions provided by that package as
methods for arrays: any, all, one, and none.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/autobox/Junctions*

%changelog
* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.002-alt1
- New version

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.001-alt1
- Initial build for ALT Linux Sisyphus
