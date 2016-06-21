## SPEC file for Perl module Dist::Zilla::Role::Bootstrap

Name: perl-Dist-Zilla-Role-Bootstrap
Version: 1.001003
Release: alt1

Summary: Dist::Zilla module with shared logic for bootstrap things

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Dist-Zilla-Role-Bootstrap/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Dist-Zilla-Role-Bootstrap
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Class-Method-Modifiers perl-Config-MVP perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Encode perl-Eval-Closure perl-File-Copy-Recursive perl-File-pushd perl-Import-Into perl-List-AllUtils perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moo perl-Moose perl-Moose-Autobox perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Common perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Perl-OSType perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-aliased perl-autobox perl-autobox-Core perl-autobox-Junctions perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-strictures
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla perl-List-UtilsBy perl-MooseX-AttributeShortcuts perl-Path-Tiny perl-Variable-Magic

%description
Perl module Dist::Zilla::Role::Bootstrap provides a Dist::Zilla
methods with shared logic for bootstrap things.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla*

%changelog
* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.001003-alt1
- New version

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.001002-alt1
- New version

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.000003-alt1
- Initial build for ALT Linux Sisyphus
