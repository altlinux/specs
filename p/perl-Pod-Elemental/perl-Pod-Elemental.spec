## SPEC file for Perl module Pod::Elemental

%define real_name Pod-Elemental

Name: perl-Pod-Elemental
Version: 0.103006
Release: alt1

Summary: Perl module to work with nestable Pod elements

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Pod-Elemental/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-Algorithm-Diff perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-PerlIO-utf8_strict perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Text-Diff perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3-base
BuildRequires: perl-CPAN-Meta perl-MooseX-Types perl-Pod-Eventual perl-String-RewritePrefix perl-String-Truncate perl-Test-Deep perl-Test-Differences

%description
Perl module Pod::Elemental provides a system for treating a Pod
(plain old documentation) documents as trees of elements. This
model may be familiar from many other document systems,
especially the HTML DOM. Pod::Elemental's document object model
is much less sophisticated than the HTML DOM, but still makes
a lot of document transformations easy.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Pod/Elemental*

%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.103006-alt1
- New version

* Tue May 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.103005-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 0.103004-alt2
- Initial build for ALT Linux Sisyphus
