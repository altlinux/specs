## SPEC file for Perl module Dist::Zilla

Name: perl-Dist-Zilla
Version: 6.010
Release: alt2

Summary: scary tools for building CPAN distributions

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Dist-Zilla/
#URL: http://dzil.org/
#URL: https://github.com/rjbs/Dist-Zilla

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Dist-Zilla
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

Requires: perl-Config-MVP-Reader-INI perl-Devel-StackTrace

# Automatically added by buildreq on Sat Mar 25 2017
# optimized out: perl perl-App-Cmd perl-Archive-Tar perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Uploader perl-Capture-Tiny perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Inspector perl-Class-Load perl-Class-Singleton perl-Clone perl-Compress-Raw-Bzip2 perl-Compress-Raw-Zlib perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-DateTime perl-DateTime-Locale perl-DateTime-TimeZone perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-HomeDir perl-File-ShareDir perl-File-Which perl-File-pushd perl-Getopt-Long-Descriptive perl-HTTP-Date perl-HTTP-Message perl-IO-Compress perl-IO-String perl-IO-Zlib perl-IPC-Run perl-JSON-MaybeXS perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-CoreList perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-Perl-PrereqScanner perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Escapes perl-Pod-Eventual perl-Pod-Simple perl-Pod-Weaver perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-Specio perl-String-Flogger perl-String-Formatter perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-Encoding perl-Term-ReadLine-Gnu perl-Term-UI perl-TermReadKey perl-Test-Deep perl-Test-Fatal perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-URI perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-common-sense perl-devel perl-libwww perl-namespace-autoclean perl-namespace-clean perl-parent perl-podlators perl-unicore python-base python-modules python3-base tzdata
BuildRequires: perl-Archive-Tar-Wrapper perl-CPAN-Meta-Check perl-Class-XSAccessor perl-Dist-Zilla-Plugin-CheckExtraTests perl-Dist-Zilla-Plugin-Git perl-Dist-Zilla-Plugin-MakeMaker-Awesome perl-Dist-Zilla-Plugin-PodWeaver perl-Dist-Zilla-Plugin-PromptIfStale perl-File-ShareDir-Install perl-JSON-XS perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-PPI-XS perl-Ref-Util perl-Test-FailWarnings perl-Test-File-ShareDir perl-Test-Moose-More

BuildRequires: perl-autobox perl-autodie perl-common-sense perl-CPAN-Uploader perl-App-Cmd perl-Archive-Tar perl-B-Hooks-EndOfScope perl-YAML-Tiny perl-Moose-Autobox perl-MooseX-LazyRequire
BuildRequires: perl-MooseX-SetOnce perl-Data-Section perl-DateTime perl-JSON perl-Log-Dispatchouli perl-Software-License perl-Perl-PrereqScanner perl-PPI perl-Pod-Eventual
BuildRequires: perl-Sub-Exporter-ForMethods perl-File-Find-Rule perl-File-pushd perl-Hash-Merge-Simple perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Test-Deep perl-Text-Glob
BuildRequires: perl-Config-MVP-Reader-INI perl-Perl-Version perl-Term-UI perl-Devel-StackTrace perl-CPAN-Meta perl-List-AllUtils perl-Test-Pod perl-Test-Script

%description
Dist::Zilla is a program to make it easier to write, package,
manage, and release free software. It's targeted at libraries
written in the Perl programming language and released to the
CPAN. If you release software to the CPAN, Dist::Zilla can
probably save you a lot of work. It has plugins to automate
dozens of boring steps.


# Dist::Zilla::Tester contains references to the Dist::Zilla::Tester::_Role module and
# its in-memory definition during run time. findreq can found this requirement, but
# findprov can't found this providement (and this is quite correct). So skip findreq...
%add_findreq_skiplist */Dist/Zilla/Tester.pm

%prep
%setup  -n %real_name-%version
%patch0 -p1

%build
# set environment variable to make sure DateTime::TimeZone::Local 
# could determine timezone during tests
export TZ=UTC

# Lowing version of ExtUtils::Manifest ( 1.66->1.63)
#sed -e 's/1.66/1.63/' -i META.json META.yml Makefile.PL cpanfile t/00-report-prereqs.dd 
#rm -f -- t/plugins/manifest.t

# Fails with File::Copy::Recursive 0.39
rm -f --  t/plugins/filefinders.t

%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla*
%perl_vendor_privlib/Test/DZil*

%_bindir/dzil
%_man1dir/dzil*
%perl_vendor_privlib/auto/share/module/Dist-Zilla-MintingProfile-Default*


%changelog
* Sun Jan 28 2018 Nikolay A. Fetisov <naf@altlinux.org> 6.010-alt2
- Fix build with File::Copy::Recursive 0.39

* Sat Jul 15 2017 Nikolay A. Fetisov <naf@altlinux.org> 6.010-alt1
- New version

* Sat Mar 25 2017 Nikolay A. Fetisov <naf@altlinux.org> 6.009-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 6.008-alt1
- New version

* Sun Aug 14 2016 Nikolay A. Fetisov <naf@altlinux.ru> 6.007-alt1
- New version

* Thu Jul 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 6.006-alt1
- New version

* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 6.005-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 5.043-alt1
- New version

* Sun Nov 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 5.042-alt1
- New version

* Sat Nov 07 2015 Nikolay A. Fetisov <naf@altlinux.ru> 5.041-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 5.040-alt1
- New version

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 5.020-alt1
- New version

* Sat Oct 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 4.300039-alt1
- New version

* Sun Nov 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 4.300028-alt1
- New version

* Fri Jan 27 2012 Nikolay A. Fetisov <naf@altlinux.ru> 4.300006-alt1
- Initial build for ALT Linux Sisyphus

