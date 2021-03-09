## SPEC file for Perl module Dist::Zilla::Plugin::NextVersion::Semantic

%define real_name Dist-Zilla-Plugin-NextVersion-Semantic

Name: perl-Dist-Zilla-Plugin-NextVersion-Semantic
Version: 0.2.6
Release: alt1

Summary: Perl module to semantic-wise update the next version

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Zilla-Plugin-NextVersion-Semantic

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Wed May 06 2020
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Inspector perl-Class-Load perl-Class-Singleton perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-DateTime perl-DateTime-Locale perl-DateTime-TimeZone perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-ShareDir perl-File-Which perl-File-pushd perl-IPC-Run perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-List-MoreUtils-XS perl-List-SomeUtils perl-List-UtilsBy perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-Formatter perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Sub-Uplevel perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4 tzdata
BuildRequires: perl-Archive-Tar-Wrapper perl-CPAN-Changes perl-Class-XSAccessor perl-Dist-Zilla perl-List-AllUtils perl-Perl-Version perl-Ref-Util perl-Ref-Util-XS perl-Test-Exception

%description
Perl module Dist::Zilla::Plugin::NextVersion::Semantic increases
the distribution's version according to the semantic versioning
rules (see http://semver.org/) by inspecting the changelog.

%prep
%setup -q -n %real_name-%version

%build
# For tests:
export TZ=UTC

%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.mkdn Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/NextVersion/Semantic*
%perl_vendor_privlib/Dist/Zilla/Plugin/PreviousVersion/Changelog*
%perl_vendor_privlib/Dist/Zilla/Role/YANICK*

%changelog
* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.2.6-alt1
- New version

* Sat May 09 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.2.5-alt2
- Bump release to override autoimports package

* Wed May 06 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.2.5-alt1
- Initial build for ALT Linux Sisyphus
