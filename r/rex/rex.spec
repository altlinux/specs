# SPEC file for rex package

Name:    rex
Version: 1.4.1
Release: alt2

Summary: (R)?ex - Remote Execution Framework

License: Apache License 2.0
Group:   System/Configuration/Other
URL:     http://rexify.org/
#URL:    https://github.com/RexOps/Rex

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-0.53.1-alt-fix_use.patch
Patch2:  %name-1.4.0_01-perltidy.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Mon Jun 27 2016
# optimized out: libsasl2-3 lsb-release perl perl-Algorithm-Diff perl-App-Cmd perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Class-Method-Modifiers perl-Clone perl-Compiler-Lexer perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-DBI perl-Data-Dump perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Digest-SHA perl-Dist-Zilla perl-Dist-Zilla-Plugin-MetaProvides perl-Dist-Zilla-Util-ConfigDumper perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-File-Find-Rule perl-File-Find-Rule-Perl perl-File-Finder perl-File-HomeDir perl-File-Slurp perl-File-Which perl-File-pushd perl-Getopt-Long-Descriptive perl-HTTP-Date perl-HTTP-Message perl-IO-Socket-IP perl-IO-String perl-IO-Stty perl-IO-Tty perl-IPC-Run perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-MooseX-Types-Stringlike perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-Perl-MinimumVersion-Fast perl-Perl-PrereqScanner perl-Perl-Tidy perl-PerlIO-utf8_strict perl-Pod-Escapes perl-Pod-Eventual perl-Pod-Simple perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Safe-Isa perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Term-ANSIColor perl-Term-Encoding perl-TermReadKey perl-Test-Deep perl-Text-Diff perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-TimeDate perl-Try-Tiny perl-Types-Serialiser perl-URI perl-Variable-Magic perl-XML-LibXML perl-XML-SAX perl-XML-SAX-Base perl-YAML perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-libwww perl-namespace-autoclean perl-namespace-clean perl-parent perl-podlators perl-unicore python-base python-modules python3
BuildRequires: curl iproute2 libnss-myhostname libnss-mymachines lsb-core openssh-clients perl-AWS-Signature4 perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-Digest-HMAC perl-Dist-Zilla-Plugin-MakeMaker-Awesome perl-Dist-Zilla-Plugin-MetaProvides-Package perl-Dist-Zilla-Plugin-OSPrereqs perl-Dist-Zilla-Plugin-OurPkgVersion perl-Dist-Zilla-Plugin-Test-MinimumVersion perl-Dist-Zilla-Plugin-Test-Perl-Critic perl-Expect perl-Hash-Merge perl-JSON-XS perl-MooseX-Aliases perl-Net-OpenSSH perl-Net-SFTP-Foreign perl-Net-SSH2 perl-PPI-XS perl-Parallel-ForkManager perl-PathTools perl-Sort-Naturally perl-String-Escape perl-Test-MinimumVersion-Fast perl-Test-PerlTidy perl-Test-Pod perl-Test-UseAllModules perl-XML-Simple subversion wget

BuildRequires: perl-Digest-HMAC perl-IPC-Shareable

# Perl find-requires skips File::Spec::* modules, add File::Spec::Win32 manually
Requires: perl-PathTools

# Perl find-requires skips modules inside eval{}, add them manually
Requires: perl(Expect.pm) perl(Net/SSH2.pm) perl(Term/ANSIColor.pm)


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
cd Rex-%{version}
%perl_vendor_build

%install
cd Rex-%{version}
%perl_vendor_install

install -dp %buildroot%_sysconfdir/bash_completion.d/
install -p -m 644 ../misc/rex-tab-completion.bash %buildroot%_sysconfdir/bash_completion.d/%name

%files
%doc ChangeLog README.md CONTRIBUTORS doc/Rexfile-example1
%doc doc/LICENSE

%_bindir/rex
%_bindir/rexify

%_man1dir/rex*

%perl_vendor_privlib/Rex*

%_sysconfdir/bash_completion.d/%name

%changelog
* Sat Jul 16 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.1-alt2
- Adding missing Requires

* Sat Jul 16 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.1-alt1
- New version

* Tue Jun 28 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.0-alt3
- Updating to the development version 1.4.0_01
- Compatibility fixes for Net::SSH2

* Fri Jun 03 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.0-alt2
- Compatibility fixes for Net::SSH2 >= 0.59

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.0-alt1
- New version

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
