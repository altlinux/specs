## SPEC file for Perl module Dist::Zilla::Util::Test::KENTNL

%define real_name Dist-Zilla-Util-Test-KENTNL

Name: perl-Dist-Zilla-Util-Test-KENTNL
Version: 1.003003
Release: alt1

Summary: KENTNL's DZil plugin testing tool

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Util-Test-KENTNL/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: perl-Algorithm-Diff perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Method-Modifiers perl-Class-XSAccessor perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-File-Copy-Recursive perl-File-Find-Rule perl-File-HomeDir perl-File-Which perl-File-pushd perl-Hash-Merge-Simple perl-Import-Into perl-Iterator perl-Iterator-Util perl-JSON perl-JSON-XS perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-Moose-Autobox perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Perl-OSType perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Test-Deep perl-Text-Balanced perl-Text-Diff perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-strictures perl-unicore
BuildRequires: perl-Data-DPath perl-Dist-Zilla perl-Path-Tiny perl-Test-Differences perl-Test-Fatal perl-Variable-Magic

%description
Perl module Dist::Zilla::Util::Test::KENTNL provides a methods
to test Dist::Zilla plugins.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Util/Test/KENTNL*

%changelog
* Thu Oct 02 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.003003-alt1
- New version

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.003002-alt1
- Initial build for ALT Linux Sisyphus
