## SPEC file for Perl module Facebook::Graph

Name: perl-Facebook-Graph
Version: 1.1101
Release: alt1

Summary: Perl interface to the Facebook Graph API

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Facebook-Graph/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Facebook-Graph
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses
Requires: perl-LWP-Protocol-https perl-Mozilla-CA

# Automatically added by buildreq on Sat Mar 19 2016
# optimized out: perl-App-Cmd perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Class-Method-Modifiers perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-DateTime perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-File-Find-Rule perl-File-HomeDir perl-File-Which perl-File-pushd perl-Getopt-Long-Descriptive perl-HTTP-Date perl-HTTP-Message perl-IO-Socket-IP perl-IO-Socket-SSL perl-IO-String perl-IPC-Run perl-JSON-PP perl-JSON-XS perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Net-HTTP perl-Net-HTTPS perl-Net-SSLeay perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Term-Encoding perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-URI perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-libwww perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python3 python3-base
BuildRequires: perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-DateTime-Format-Strptime perl-Digest-SHA perl-Dist-Zilla perl-JSON perl-LWP-Protocol-https perl-MIME-Base64-URLSafe perl-Ouch perl-PPI-XS

# Disabling tests inside hasher: network support is needed for accessing Facebook API.
%ifdef __BTE
    %def_without test
%endif

%description
Perl module Facebook::Graph provides a fast and easy way to
integrate Perl apps with Facebook.

This is a Perl interface to the Facebook Graph API
http://developers.facebook.com/docs/api. With this module you
can currently query public Facebook data, query privileged
Facebook data, and build a privileged Facebook application.


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
cp README Changes ..

%files
%doc README Changes
%perl_vendor_privlib/Facebook/Graph*

%changelog
* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.1101-alt1
- New version

* Sat Dec 05 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.1100-alt2
- Updating BuildRequires to fix package build

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.1100-alt1
- New version

* Sat Jun 13 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.1000-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.0801-alt1
- New version

* Sat Oct 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.0600-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.0301-alt1
- Initial build for ALT Linux Sisyphus
