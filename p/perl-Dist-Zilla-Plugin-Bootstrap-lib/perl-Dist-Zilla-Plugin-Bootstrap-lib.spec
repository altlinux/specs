## SPEC file for Perl module Dist::Zilla::Plugin::Bootstrap::lib

Name: perl-Dist-Zilla-Plugin-Bootstrap-lib
Version: 1.001000
Release: alt1

Summary: a minimal boot-strapping for Dist::Zilla Plug-ins

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-Bootstrap-lib/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Dist-Zilla-Plugin-Bootstrap-lib
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: perl-Algorithm-Diff perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Method-Modifiers perl-Class-XSAccessor perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-DPath perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-StackTrace perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-File-Copy-Recursive perl-File-pushd perl-Hash-Merge-Simple perl-Import-Into perl-Iterator perl-Iterator-Util perl-JSON perl-JSON-XS perl-List-AllUtils perl-List-MoreUtils perl-List-UtilsBy perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-Moose-Autobox perl-MooseX-AttributeShortcuts perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Common perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-Perl-OSType perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Test-Deep perl-Test-Differences perl-Test-Fatal perl-Text-Balanced perl-Text-Diff perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-YAML-Tiny perl-aliased perl-autobox perl-autobox-Core perl-autobox-Junctions perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-strictures perl-unicore
BuildRequires: perl-Dist-Zilla-Role-Bootstrap perl-Dist-Zilla-Util-Test-KENTNL perl-Variable-Magic

%description
Perl module Dist::Zilla::Plugin::Bootstrap::lib provides
a minimal boot-strapping for Dist::Zilla Plug-ins.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin*

%changelog
* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.001000-alt1
- Initial build for ALT Linux Sisyphus
