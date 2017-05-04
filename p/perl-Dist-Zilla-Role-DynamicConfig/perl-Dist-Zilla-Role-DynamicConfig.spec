## SPEC file for Perl module Dist::Zilla::Role::DynamicConfig

%define real_name Dist-Zilla-Role-DynamicConfig

Name: perl-Dist-Zilla-Role-DynamicConfig
Version: 1.002
Release: alt4

Summary: Dist::Zilla role that accepts a dynamic configuration

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Role-DynamicConfig/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu May 04 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Singleton perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-DateTime perl-DateTime-Locale perl-DateTime-TimeZone perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-HTML-Parser perl-IO-String perl-IPC-Run3 perl-JSON-PP perl-JSON-XS perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-Perl-OSType perl-PerlIO-utf8_strict perl-Pod-Escapes perl-Pod-Eventual perl-Pod-Simple perl-Probe-Perl perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-podlators perl-unicore python-base python-modules python3
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla perl-JSON perl-Module-Build perl-PPI-XS perl-Ref-Util perl-Test-MockObject perl-Test-Script

%description
Perl module Dist::Zilla::Role::DynamicConfig provides a Dist::Zilla
role for a Plugin (or possibly other classes) that accepts a dynamic
configuration.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Role/DynamicConfig*

%changelog
* Thu May 04 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.002-alt4
- Initial build for ALT Linux Sisyphus
