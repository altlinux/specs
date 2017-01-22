## SPEC file for Perl module Dist::Zilla::Plugin::CheckExtraTests

%define real_name Dist-Zilla-Plugin-CheckExtraTests

Name: perl-Dist-Zilla-Plugin-CheckExtraTests
Version: 0.029
Release: alt1

Summary: Dist::Zilla plugin to check xt tests before release 

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-CheckExtraTests/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-App-Cmd perl-Archive-Tar perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Capture-Tiny perl-Carp-Clan perl-Class-Load perl-Compress-Raw-Bzip2 perl-Compress-Raw-Zlib perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-File-Copy-Recursive perl-File-Find-Rule perl-File-Which perl-File-pushd perl-IO-Compress perl-IO-String perl-IO-Zlib perl-IPC-Run perl-JSON-PP perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-aliased perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3-base
BuildRequires: perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-Dist-Zilla perl-Path-Iterator-Rule perl-Test-Requires

%description
Perl module Dist::Zilla::Plugin::CheckExtraTests is a Dist:Zilla
plugin to run all xt tests before release. Dies if any fail.
Sets RELEASE_TESTING and AUTHOR_TESTING.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/*

%changelog
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 0.029-alt1
- Initial build for ALT Linux Sisyphus
