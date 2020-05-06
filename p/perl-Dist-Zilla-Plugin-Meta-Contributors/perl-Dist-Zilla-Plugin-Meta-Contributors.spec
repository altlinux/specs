## SPEC file for Perl module Dist::Zilla::Plugin::Meta::Contributors

%define real_name Dist-Zilla-Plugin-Meta-Contributors

Name: perl-Dist-Zilla-Plugin-Meta-Contributors
Version: 0.003
Release: alt2

Summary: Perl module to generate x_contributors section in distribution metadata

License: %asl
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Zilla-Plugin-Meta-Contributors

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Wed May 06 2020
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-IO-String perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla perl-PPI-XS perl-Ref-Util perl-Ref-Util-XS

%description
Perl module Dist::Zilla::Plugin::Meta::Contributors generates
an x_contributors section in distribution metadata.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/Meta/Contributors*

%changelog
* Wed May 06 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.003-alt2
- Bump release to override autoimport package

* Wed May 06 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.003-alt1
- Initial build for ALT Linux Sisyphus
