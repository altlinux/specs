## SPEC file for Perl module Dist::Zilla::Plugin::Bootstrap::lib

Name: perl-Dist-Zilla-Plugin-Bootstrap-lib
Version: 1.001002
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

# Automatically added by buildreq on Sat Mar 25 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-File-Copy-Recursive perl-File-pushd perl-JSON-MaybeXS perl-List-UtilsBy perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Deep perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3-base
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla-Role-Bootstrap perl-JSON-XS perl-Ref-Util

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
* Sat Mar 25 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.001002-alt1
- New version

* Sun Mar 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.001001-alt1
- New version

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.001000-alt2
- Updating BuildRequires

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.001000-alt1
- Initial build for ALT Linux Sisyphus
