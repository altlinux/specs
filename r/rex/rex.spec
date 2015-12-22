# SPEC file for rex package

Name:    rex
Version: 1.3.3
Release: alt1

Summary: (R)?ex - Remote Execution Framework

License: Apache License 2.0
Group:   System/Configuration/Other
URL:     http://rexify.org/
#URL:    https://github.com/RexOps/Rex

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-0.53.1-alt-fix_use.patch
Patch2:  %name-0.53.1-sudo_backquotes.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Dec 20 2015
# optimized out: libsasl2-3 lsb-release perl-App-Cmd perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Class-Method-Modifiers perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-DBI perl-Data-Dump perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-Zilla perl-Dist-Zilla-Plugin-MetaProvides perl-Dist-Zilla-Util-ConfigDumper perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-File-Find-Rule perl-File-HomeDir perl-File-Which perl-File-pushd perl-Getopt-Long-Descriptive perl-HTTP-Date perl-HTTP-Message perl-IO-Socket-IP perl-IO-String perl-IO-Stty perl-IO-Tty perl-IPC-Run perl-JSON-PP perl-List-AllUtils perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-MooseX-Types-Stringlike perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-Perl-OSType perl-Perl-PrereqScanner perl-PerlIO-utf8_strict perl-Pod-Escapes perl-Pod-Eventual perl-Pod-Simple perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Safe-Isa perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Term-ANSIColor perl-Term-Encoding perl-TermReadKey perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-TimeDate perl-Try-Tiny perl-Types-Serialiser perl-URI perl-Variable-Magic perl-YAML perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-libwww perl-namespace-autoclean perl-namespace-clean perl-parent perl-podlators perl-unicore
BuildRequires: curl iproute2 lsb-core perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-Digest-SHA perl-Dist-Zilla-Plugin-MakeMaker-Awesome perl-Dist-Zilla-Plugin-MetaProvides-Package perl-Dist-Zilla-Plugin-OSPrereqs perl-Dist-Zilla-Plugin-OurPkgVersion perl-Dist-Zilla-Plugin-Test-MinimumVersion perl-Dist-Zilla-Plugin-Test-Perl-Critic perl-Expect perl-Hash-Merge perl-JSON-XS perl-Net-OpenSSH perl-Net-SFTP-Foreign perl-Net-SSH2 perl-PPI-XS perl-Parallel-ForkManager perl-PathTools perl-Sort-Naturally perl-String-Escape perl-Test-Pod perl-Test-UseAllModules perl-XML-LibXML perl-XML-Simple subversion wget

BuildRequires: perl-Digest-HMAC perl-IPC-Shareable

# Perl find-requires skips File::Spec::* modules, add File::Spec::Win32 manually
Requires: perl-PathTools


# Template files does't contains a proper Perl code
%add_findreq_skiplist */Commands/templates/*

%description
(R)?ex is a tool to ease the execution of commands on multiple
remote servers. It allows to manage all boxes from a central
point through the complete process of configuration management
and software deployment.

%prep
%setup
%patch0 -p1

%patch1 -p0
%patch2 -p0

# This creates Makefile.PL from dist.ini
/usr/bin/dzil build

%build
cd Rex-%version
%perl_vendor_build

%install
cd Rex-%version
%perl_vendor_install


%files
%doc ChangeLog README.md CONTRIBUTORS doc/Rexfile-example1
%doc doc/LICENSE

%_bindir/rex
%_bindir/rexify

%_man1dir/rex*

%perl_vendor_privlib/Rex*


%changelog
* Tue Dec 22 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.3-alt1
- New version

* Wed Feb 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.44.3-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.43.7-alt1
- New version

* Sun May 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.41.3-alt1
- New version

* Sun Apr 21 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.41.2-alt2
- Fix backquotes in remote sudo() calls

* Sun Apr 21 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.41.2-alt1
- New version

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.41.1-alt1
- New version

* Sat Feb 09 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.39.0-alt1
- New version

* Sun Feb 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.38.0-alt1
- New version

* Mon Jan 07 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.37.0-alt1
- New version

* Sat Dec 15 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.34.2-alt1
- New version

* Tue Nov 27 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.34.1-alt1
- New version

* Wed Nov 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.34.0-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.33.1-alt1
- New version

* Sat Aug 25 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.32.0-alt1
- New version

* Wed Aug 15 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.31.4-alt1
- New version

* Sun Aug 12 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.30.0-alt1
- Initial build for ALT Linux Sisyphus
