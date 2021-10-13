# SPEC file for rex package

%define  version_suffix %nil

Name:    rex
Version: 1.13.4
Release: alt2

Summary: (R)?ex - Remote Execution Framework

License: %asl 2.0
Group:   System/Configuration/Other
URL:     http://rexify.org/
#URL:    https://github.com/RexOps/Rex

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-0.53.1-alt-fix_use.patch
Patch2:  %name-1.13.3-alt-fix_ssh_port.patch
Patch3:  %name-1.13.3-alt-fix_dmidecode.patch 

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Mar 14 2021
# optimized out: git-core libnss-myhostname libsasl2-3 lsb-release perl perl-App-Cmd perl-B-Hooks-EndOfScope perl-CPAN-Changes perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Capture-Tiny perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Inspector perl-Class-Load perl-Clone perl-Clone-Choose perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-DBI perl-Data-Dump perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-Zilla perl-Dist-Zilla-Plugin-Config-Git perl-Dist-Zilla-Plugin-MetaProvides perl-Dist-Zilla-Role-ModuleMetadata perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-Find-Rule perl-File-ShareDir perl-File-Which perl-File-chdir perl-File-pushd perl-Getopt-Long-Descriptive perl-Git-Wrapper perl-HTTP-Date perl-HTTP-Message perl-IO-Socket-IP perl-IO-String perl-IO-Stty perl-IO-Tty perl-IPC-Run perl-JSON-MaybeXS perl-JSON-PP perl-List-AllUtils perl-List-MoreUtils perl-List-MoreUtils-XS perl-List-SomeUtils perl-List-UtilsBy perl-Log-Dispatch perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-Has-Sugar perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Common perl-MooseX-Types-Perl perl-MooseX-Types-Stringlike perl-NetAddr-IP perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-Perl-PrereqScanner perl-Perl-Version perl-PerlIO-utf8_strict perl-Pod-Escapes perl-Pod-Simple perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Safe-Isa perl-Socket6 perl-Software-License perl-Sort-Versions perl-Specio perl-String-Errf perl-String-Flogger perl-String-Formatter perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Term-ANSIColor perl-Term-Encoding perl-TermReadKey perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Time-Piece perl-Try-Tiny perl-Type-Tiny perl-Types-Path-Tiny perl-URI perl-Unicode-Collate perl-Variable-Magic perl-XML-LibXML perl-XML-SAX perl-XML-SAX-Base perl-XML-Simple perl-YAML-Tiny perl-aliased perl-autodie perl-devel perl-libwww perl-namespace-autoclean perl-namespace-clean perl-parent perl-podlators python-modules python2-base python3 python3-base python3-module-paste rsync ruby ruby-stdlibs sh4 utf8proc
BuildRequires: curl iproute2 libnss-mymachines perl-AWS-Signature4 perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-Data-Validate-IP perl-Digest-HMAC perl-Dist-Zilla-Plugin-CheckExtraTests perl-Dist-Zilla-Plugin-ContributorsFile perl-Dist-Zilla-Plugin-DynamicPrereqs perl-Dist-Zilla-Plugin-Git perl-Dist-Zilla-Plugin-Git-Contributors perl-Dist-Zilla-Plugin-MakeMaker-Awesome perl-Dist-Zilla-Plugin-Meta-Contributors perl-Dist-Zilla-Plugin-MetaProvides-Package perl-Dist-Zilla-Plugin-NextVersion-Semantic perl-Dist-Zilla-Plugin-OSPrereqs perl-Dist-Zilla-Plugin-OptionalFeature perl-Dist-Zilla-Plugin-OurPkgVersion perl-Dist-Zilla-Plugin-PromptIfStale perl-Dist-Zilla-Plugin-Run perl-Dist-Zilla-Plugin-Test-CPAN-Changes perl-Dist-Zilla-Plugin-Test-Kwalitee perl-Dist-Zilla-Plugin-Test-MinimumVersion perl-Expect perl-File-LibMagic perl-File-ShareDir-Install perl-Hash-Merge perl-IPC-Shareable perl-Net-OpenSSH perl-Net-SFTP-Foreign perl-Net-SSH2 perl-PPI-XS perl-Parallel-ForkManager perl-Ref-Util perl-Ref-Util-XS perl-Sort-Naturally perl-String-Escape perl-Test-Output perl-Test-UseAllModules perl-YAML subversion wget

# Extra automatic dependencies, need to remove:
#BuildRequires: lsb-core lsb-release

# Missed by buildreq:
BuildRequires: perl-IPC-Shareable perl-XML-Simple

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


%package -n zsh-completion-rex
Summary:   Zsh completion for (R)?ex
Group:     Shells
BuildArch: noarch
Requires:  zsh
Requires:  %name = %EVR

%description -n zsh-completion-rex
Zsh completion for (R)?ex remote execution framework


%prep
%setup
%patch0 -p1

%patch1 -p0
%patch2
%patch3

## Fix dist.ini:
### Remove [NextRelease] section:
sed -e '/^\[NextRelease/,/^$/ d' -i dist.ini

### Replace [Git::GatherDir] with [GatherDir] one:
sed -e 's/^\[Git::GatherDir/[GatherDir/' -i dist.ini

# Force version for NextVersion::Semantic:
export V=%{version}

# This creates Makefile.PL from dist.ini
/usr/bin/dzil build

%build
cd Rex-%{version}%{version_suffix}

# Fix test to work with ALT perl 5.28.0 / PathTools 3.74
sed -e "/=> realpath/ s#/\*')#').'/*'#" -i t/rsync.t

%perl_vendor_build

%install
cd Rex-%{version}%{version_suffix}
%perl_vendor_install

install -dp %buildroot%_sysconfdir/bash_completion.d/
install -dp %buildroot%_datadir/zsh/site-functions/
install -p -m 644 ../share/rex-tab-completion.bash %buildroot%_sysconfdir/bash_completion.d/%name
install -p -m 644 ../share/rex-tab-completion.zsh  %buildroot%_datadir/zsh/site-functions/_%name
rm -f %buildroot%perl_vendor_privlib/auto/share/dist/Rex/*-completion.*

mv -f CONTRIBUTORS ../
mv -f ChangeLog    ../


%files
%doc ChangeLog README.md CONTRIBUTORS doc/Rexfile-example1
%doc doc/LICENSE

%_bindir/rex
%_bindir/rexify

%_man1dir/rex*

%perl_vendor_privlib/Rex*

%_sysconfdir/bash_completion.d/%name

%files -n zsh-completion-rex
%_datadir/zsh/site-functions/_%name


%changelog
* Wed Oct 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.13.4-alt2
- Remove libmagic bug workaround after closing 38497

* Sun Jul 11 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.13.4-alt1
- New version

* Sun Mar 14 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.13.3-alt1
- New version

* Sat Aug 08 2020 Nikolay A. Fetisov <naf@altlinux.org> 1.12.1-alt1
- New version

* Sun Jun 28 2020 Nikolay A. Fetisov <naf@altlinux.org> 1.11.0.1-alt1
- New version

* Wed Jun 10 2020 Nikolay A. Fetisov <naf@altlinux.org> 1.11.0-alt1
- New version

* Sat Dec 09 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.6.0-alt1
- New version

* Sun Sep 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.5.99-alt2
- Fix BuildRequires

* Sun Aug 13 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.5.99-alt1
- New version

* Mon Mar 20 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.5.0-alt1
- New version

* Tue Jul 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.1-alt3
- Fix backquotes escaping

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
