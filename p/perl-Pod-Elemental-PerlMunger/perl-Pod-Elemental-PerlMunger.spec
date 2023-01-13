## SPEC file for Perl module Pod::Elemental::PerlMunger

%define real_name Pod-Elemental-PerlMunger

Name: perl-Pod-Elemental-PerlMunger
Version: 0.200007
Release: alt1

Summary: Perl module that takes a string of Perl and rewrites its documentation

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Pod-Elemental-PerlMunger/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Clone perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-IO-String perl-List-MoreUtils perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Runtime perl-Moose perl-MooseX-Types perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-PerlIO-utf8_strict perl-Pod-Eventual perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3-base
BuildRequires: perl-CPAN-Meta perl-PPI-XS perl-Pod-Elemental perl-Test-Differences

%description
Perl module Pod::Elemental::PerlMunger is a thing that takes
a string of Perl and rewrites its documentation.
This role is to be included in classes that rewrite the
documentation of a Perl document, stripping out all the Pod,
munging it, and replacing it into the Perl.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Pod/Elemental/PerlMunger*

%changelog
* Fri Jan 13 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.200007-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 0.200006-alt2
- Initial build for ALT Linux Sisyphus
