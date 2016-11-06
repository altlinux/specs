## SPEC file for Perl module Ouch

Name: perl-Ouch
Version: 0.0410
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

# Automatically added by buildreq on Sat Jun 13 2015
# optimized out: perl-App-Cmd perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Load perl-Class-Method-Modifiers perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-Dump perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-File-Find-Rule perl-File-HomeDir perl-File-Which perl-File-pushd perl-Getopt-Long-Descriptive perl-HTML-Parser perl-Hash-Merge-Simple perl-IO-String perl-IPC-Run perl-Import-Into perl-JSON-PP perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-Moose-Autobox perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-Perl-OSType perl-PerlIO-utf8_strict perl-Pod-Escapes perl-Pod-Eventual perl-Pod-Simple perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Term-Encoding perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-podlators perl-strictures perl-unicore
BuildRequires: perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-Dist-Zilla perl-Module-Build perl-Test-Trap

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
* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.0410-alt1
- New version

* Sat Jun 13 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.0409-alt1
- New version

* Sat Oct 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.0408-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.0401-alt1
- Initial build for ALT Linux Sisyphus

