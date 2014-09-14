## SPEC file for Perl module Facebook::Graph

Name: perl-Facebook-Graph
Version: 1.0801
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

# Automatically added by buildreq on Sun Sep 14 2014
# optimized out: perl-AnyEvent perl-AnyEvent-HTTP perl-App-Cmd perl-Archive-Tar perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Class-Singleton perl-Clone perl-Compress-Raw-Bzip2 perl-Compress-Raw-Zlib perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-DateTime perl-DateTime-Locale perl-DateTime-TimeZone perl-Devel-GlobalDestruction perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-File-Find-Rule perl-File-HomeDir perl-File-Which perl-File-pushd perl-Getopt-Long-Descriptive perl-Guard perl-HTTP-Date perl-HTTP-Message perl-Hash-Merge-Simple perl-IO-AIO perl-IO-Compress perl-IO-String perl-IO-Zlib perl-Import-Into perl-JSON perl-JSON-PP perl-JSON-XS perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-Moose-Autobox perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Net-SSLeay perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Perl-OSType perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-URI perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-common-sense perl-devel perl-libwww perl-namespace-autoclean perl-namespace-clean perl-parent perl-strictures perl-unicore
BuildRequires: perl-Any-Moose perl-AnyEvent-AIO perl-AnyEvent-HTTP-LWP-UserAgent perl-Class-XSAccessor perl-DateTime-Format-Strptime perl-Digest-SHA perl-Dist-Zilla perl-EV perl-MIME-Base64-URLSafe perl-Ouch perl-Variable-Magic

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
* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.0801-alt1
- New version

* Sat Oct 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.0600-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.0301-alt1
- Initial build for ALT Linux Sisyphus
