## SPEC file for Perl module Dist::Zilla

Name: perl-Dist-Zilla
Version: 4.300006
Release: alt1

Summary: scary tools for building CPAN distributions

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Dist-Zilla/
#URL: http://dzil.org/
#URL: https://github.com/rjbs/dist-zilla

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Dist-Zilla
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

BuildRequires: perl-Config-MVP-Reader-INI perl-Perl-Version perl-Term-UI perl-Devel-StackTrace
Requires: perl-Config-MVP-Reader-INI perl-Devel-StackTrace

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-Carp-Clan perl-Class-Inspector perl-Class-Load perl-Class-Singleton perl-Clone perl-Compress-Raw-Bzip2 perl-Compress-Raw-Zlib perl-Data-OptList perl-Data-Section perl-DateTime-Locale perl-DateTime-TimeZone perl-Devel-GlobalDestruction perl-Encode perl-Eval-Closure perl-File-Which perl-HTTP-Date perl-HTTP-Message perl-IO-Compress perl-IO-String perl-IO-Zlib perl-JSON perl-JSON-XS perl-List-MoreUtils perl-Log-Dispatch perl-MRO-Compat perl-Math-Round perl-Mixin-Linewise perl-Module-Pluggable perl-Module-Runtime perl-Moose perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-Types perl-Number-Compare perl-PPI perl-Package-Constants perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Classify perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Perl6-Junction perl-Role-HasMessage perl-Role-Identifiable perl-Scope-Guard perl-String-Flogger perl-String-Formatter perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Install perl-Sub-Name perl-Term-ReadKey perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-URI perl-Variable-Magic perl-aliased perl-autobox perl-common-sense perl-devel perl-libwww perl-namespace-autoclean perl-namespace-clean perl-parent
BuildRequires: perl-App-Cmd perl-Archive-Tar perl-CPAN-Uploader perl-Config-INI perl-Config-MVP perl-DateTime perl-File-Copy-Recursive perl-File-Find-Rule perl-File-HomeDir perl-File-ShareDir perl-File-ShareDir-Install perl-File-pushd perl-Hash-Merge-Simple perl-Log-Dispatchouli perl-Moose-Autobox perl-MooseX-LazyRequire perl-MooseX-SetOnce perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Perl-PrereqScanner perl-Pod-Eventual perl-Software-License perl-Sub-Exporter-ForMethods perl-Term-ReadLine-Gnu perl-Test-Deep perl-Test-Fatal perl-YAML-Tiny perl-autodie

%description
Dist::Zilla is a program to make it easier to write, package,
manage, and release free software. It's targeted at libraries
written in the Perl programming language and released to the
CPAN. If you release software to the CPAN, Dist::Zilla can
probably save you a lot of work. It has plugins to automate
dozens of boring steps.


# Excluding Dist/Zilla/Tester.pm due to unrecognized Dist::Zilla::Tester::_Role inside it
%add_findreq_skiplist */Dist/Zilla/Tester.pm

%prep
%setup  -n %real_name-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla*
%perl_vendor_privlib/Test/DZil*

%_bindir/dzil
%perl_vendor_privlib/auto/share/module/Dist-Zilla-MintingProfile-Default*


%changelog
* Fri Jan 27 2012 Nikolay A. Fetisov <naf@altlinux.ru> 4.300006-alt1
- Initial build for ALT Linux Sisyphus

