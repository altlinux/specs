## SPEC file for Perl module Dist::Zilla::Plugin::OurPkgVersion

%define real_name Dist-Zilla-Plugin-OurPkgVersion

Name: perl-Dist-Zilla-Plugin-OurPkgVersion
Version: 0.07
Release: alt1

Summary: Dist::Zilla plugin for package version management

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-OurPkgVersion/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Dec 20 2015
# optimized out: perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Class-Method-Modifiers perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-Find-Rule-Perl perl-File-pushd perl-IO-String perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-Perl-OSType perl-PerlIO-utf8_strict perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla perl-JSON-XS perl-PPI-XS perl-Test-Version

%description
Perl module Dist::Zilla::Plugin::OurPkgVersion provides
an alternative to Dist::Zilla::Plugin::PkgVersion and
uses some code from that module.
It is designed to use a the more readable format our
$VERSION = $version; as well as not change then number
of lines of code in your files, which will keep your
repository more in sync with your CPAN release.
It also allows you slightly more freedom in how you
specify your version.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/OurPkgVersion*

%changelog
* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.07-alt1
- New version

* Sun Jan 10 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt2
- Bump release to override package from autoimports/Sisyphus repository

* Sun Dec 20 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt1
- Initial build for ALT Linux Sisyphus
