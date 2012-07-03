## SPEC file for Perl module Ouch

Name: perl-Ouch
Version: 0.0401
Release: alt1

Summary: Perl class for exception handling

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Ouch/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Ouch
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-App-Cmd perl-Archive-Tar perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Uploader perl-Carp-Clan perl-Class-Load perl-Clone perl-Compress-Raw-Bzip2 perl-Compress-Raw-Zlib perl-Config-INI perl-Config-MVP perl-Data-Dump perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Eval-Closure perl-File-Find-Rule perl-File-HomeDir perl-File-Which perl-File-pushd perl-Getopt-Long-Descriptive perl-HTTP-Date perl-HTTP-Message perl-Hash-Merge-Simple perl-IO-Compress perl-IO-String perl-IO-Zlib perl-JSON-PP perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Pluggable perl-Module-Runtime perl-Moose perl-Moose-Autobox perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-Constants perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Classify perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Perl6-Junction perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Scope-Guard perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Install perl-Sub-Name perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-URI perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-devel perl-libwww perl-namespace-autoclean perl-namespace-clean perl-parent
BuildRequires: perl-Config-MVP-Reader-INI perl-Devel-StackTrace perl-Dist-Zilla perl-Test-Trap

%description
Perl module Ouch provides a class for exception handling that
doesn't require a lot of boilerplate, nor any up front
definition. This module intend to be faster, easier to use,
requires less typing, and has no prereqs, that Exception::Class
but still gives you much of that same functionality.


%prep
%setup  -n %real_name-%version
%patch0 -p1

# This creates Makefile.PL from dist.ini
/usr/bin/dzil build

%build
cd %real_name-%version
%perl_vendor_build

%install
cd %real_name-%version
%perl_vendor_install
cp README ..

%files
%doc README
%perl_vendor_privlib/Ouch*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.0401-alt1
- Initial build for ALT Linux Sisyphus

