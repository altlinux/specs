## SPEC file for Perl module Dist::Zilla::Util::Test::KENTNL

%define real_name Dist-Zilla-Util-Test-KENTNL

Name: perl-Dist-Zilla-Util-Test-KENTNL
Version: 1.005014
Release: alt1

Summary: KENTNL's DZil plugin testing tool

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Util-Test-KENTNL/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Mar 19 2017
# optimized out: perl perl-Algorithm-Diff perl-App-Cmd perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Capture-Tiny perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-XSAccessor perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-Which perl-File-pushd perl-Getopt-Long-Descriptive perl-IPC-Run perl-Iterator perl-Iterator-Util perl-JSON-MaybeXS perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Term-Encoding perl-Test-Deep perl-Test-Fatal perl-Text-Balanced perl-Text-Diff perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3-base
BuildRequires: perl-Archive-Tar-Wrapper perl-Data-DPath perl-Dist-Zilla-Plugin-CheckExtraTests perl-Dist-Zilla-Plugin-PromptIfStale perl-JSON-XS perl-Ref-Util perl-Test-Differences perl-Test-TempDir-Tiny perl-recommended

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
* Sat Mar 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.005014-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.005013-alt1
- New version

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.005012-alt1
- New version

* Mon Nov 03 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.004002-alt1
- New version

* Thu Oct 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.004000-alt1
- New version

* Thu Oct 02 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.003003-alt1
- New version

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.003002-alt1
- Initial build for ALT Linux Sisyphus
