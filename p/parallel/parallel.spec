Name: parallel
Version: 20120622
Release: alt1

Summary: A shell tool for executing jobs in parallel
License: GPLv3
Group: File tools

Url: http://www.gnu.org/software/parallel
Source: http://ftp.gnu.org/gnu/parallel/%name-%version.tar.bz2
Source100: parallel.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Oct 23 2011
# optimized out: alternatives apt apt-repo-tools ash ash-static cpio cpio-static cvs cvsps dbus dbus-tools-gui diffstat ed elfutils faketime find-static fontconfig gear git-core gitk gnupg groff-base groff-ps hasher hwclock iptables iputils ipv6calc less libgpg-error libncurses-devel lzop mkfontscale module-init-tools nfs-utils openssh-clients openssh-common perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators pkg-config python-base python-devel python-module-Pygments python-module-distribute python-module-docutils python-module-sphinx raptor rpcbind rpm-build-compat rpm-utils rsync setarch shadow-groups shared-mime-info sisyphus_check srpmcmp strace su sysvinit-utils tcl termutils time tk unzip vim-common vim-minimal vitmp vixie-cron xsltproc xxd xz
BuildRequires: GConf aptitude bzr cdrkit-utils desktop-file-utils dev86 elinks etersoft-build-utils girar-utils git-cvs iproute2 isomd5sum kernel-build-tools lftp man mc mkfontdir mkimage net-tools passwd perl-Digest-SHA perl-Pod-Parser perl-Unicode-Map perl-Unicode-Map8 perl-devel recode rpm-build-mozilla.org schedutils screen subversion telnet tla tree vim-console virtualbox vzfree wget xauth xlsfonts zsh

BuildRequires: perl-podlators perl-devel
BuildArch: noarch

%description
GNU parallel is a shell tool for executing jobs in parallel
locally or using remote machines. A job is typically a single
command or a small script that has to be run for each of the
lines in the input. The typical input is a list of files, a list
of hosts, a list of users, a list of URLs, or a list of tables.

%prep
%setup

%build
%configure
%make

%install
%makeinstall
rm -r %buildroot%_defaultdocdir/%name/

%files
%doc README NEWS src/*.html
%_bindir/*
%_man1dir/*

%changelog
* Sat Jun 23 2012 Michael Shigorin <mike@altlinux.org> 20120622-alt1
- new version (watch file uupdate)

* Tue May 22 2012 Michael Shigorin <mike@altlinux.org> 20120522-alt1
- new version (watch file uupdate)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 20120422-alt2
- added watch file

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 20120422-alt1
- 20120422

* Fri Mar 23 2012 Michael Shigorin <mike@altlinux.org> 20120322-alt1
- 20120322 (bugfixes only, no new features)

* Tue Feb 28 2012 Michael Shigorin <mike@altlinux.org> 20120222-alt1
- 20120222

* Sun Jan 22 2012 Michael Shigorin <mike@altlinux.org> 20120122-alt1
- 20120122

* Thu Dec 22 2011 Michael Shigorin <mike@altlinux.org> 20111222-alt1
- 20111222

* Wed Nov 23 2011 Michael Shigorin <mike@altlinux.org> 20111122-alt1
- 20111122

* Sun Oct 23 2011 Michael Shigorin <mike@altlinux.org> 20111022-alt1
- 20111022

* Mon Aug 22 2011 Michael Shigorin <mike@altlinux.org> 20110822-alt1
- 20110822

* Fri Jul 22 2011 Michael Shigorin <mike@altlinux.org> 20110722-alt1
- 20110722

* Wed Jun 22 2011 Michael Shigorin <mike@altlinux.org> 20110622-alt1
- 20110622

* Sun May 22 2011 Michael Shigorin <mike@altlinux.org> 20110522-alt1
- 20110522

* Fri Apr 22 2011 Michael Shigorin <mike@altlinux.org> 20110422-alt1
- 20110422

* Tue Mar 22 2011 Michael Shigorin <mike@altlinux.org> 20110322-alt1
- 20110322

* Tue Feb 08 2011 Michael Shigorin <mike@altlinux.org> 20110205-alt1
- 20110205

* Sun Jan 23 2011 Michael Shigorin <mike@altlinux.org> 20110122-alt1
- 20110122

* Wed Dec 22 2010 Michael Shigorin <mike@altlinux.org> 20101222-alt1
- 20101222

* Sat Dec 04 2010 Michael Shigorin <mike@altlinux.org> 20101202-alt1
- 20101202

* Thu Nov 18 2010 Michael Shigorin <mike@altlinux.org> 20101113-alt1
- 20101113

* Thu Sep 23 2010 Michael Shigorin <mike@altlinux.org> 20100922-alt1
- 20100922

* Tue Sep 07 2010 Michael Shigorin <mike@altlinux.org> 20100906-alt1
- 20100906
  + added sem(1) and sql(1)

* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 20100722-alt1
- built for ALT Linux (based on cooker spec)
- include HTML documentation
- noarch

* Thu Jul 29 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100722-3mdv2011.0
+ Revision: 563194
- fix summary with "shell tool", recommended by upstream.
- fix summary (thanks Samuel Verschelde)

* Sat Jul 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100722-1mdv2011.0
+ Revision: 557949
- fix description (it's a perl tool!)
- update to 20100722

  + Jani Välimaa <wally@mandriva.org>
    - split one-liner description to a multiple lines
    - fix one file appearing twice in file list

* Fri Jul 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100620-2mdv2011.0
+ Revision: 554151
- Add Require

* Fri Jul 16 2010 Sandro Cazzaniga <kharec@mandriva.org> 20100620-1mdv2011.0
+ Revision: 554150
- import parallel

