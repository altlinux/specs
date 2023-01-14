## SPEC file for Perl module Pod::Elemental::Transformer::List

%define real_name Pod-Elemental-Transformer-List

Name: perl-Pod-Elemental-Transformer-List
Version: 0.102001
Release: alt1

Summary: Perl module to transform :list regions in POD

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Pod-Elemental-Transformer-List/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-Algorithm-Diff perl-B-Hooks-EndOfScope perl-Carp-Clan perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Runtime perl-Moose perl-MooseX-Types perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-PerlIO-utf8_strict perl-Pod-Eventual perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Text-Diff perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3-base
BuildRequires: perl-Pod-Elemental perl-Test-Differences

%description
Perl module Pod::Elemental::Transformer::List transforms :list
regions into =over/=back to save typing.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Pod/Elemental/Transformer/List*

%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.102001-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.102000-alt3
- Initial build for ALT Linux Sisyphus
