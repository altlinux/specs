## SPEC file for Perl module MooseX::Types::Stringlike

%define real_name MooseX-Types-Stringlike

Name: perl-MooseX-Types-Stringlike
Version: 0.003
Release: alt1

Summary: Moose type constraints for strings or string-like objects

License: %asl 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/MooseX-Types-Stringlike/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Dec 06 2015
# optimized out: perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent
BuildRequires: perl-CPAN-Meta perl-MooseX-Types

%description
Perl module MooseX::Types::Stringlike provides a more general
version of the Str type. If coercions are enabled, it will
accepts objects that overload stringification and coerces
them into strings.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MooseX/Types/Stringlike*

%changelog
* Sun Dec 06 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.003-alt1
- Initial build for ALT Linux Sisyphus
