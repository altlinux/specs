Name: hylafax
Version: 5.2.7
Release: alt8

Summary: HylaFAX(tm) is a sophisticated enterprise strength fax package
License: LGPL-style
Group: Communications

Url: http://hylafax.sourceforge.net/
Source: %name.tar
Source1: hylafax-v4.1-cron_entries.tar
Source2: hylafax-v4.1-defaults.tar
Source3: hylafax-v4.1-dialrules_extras.tar
Source6: hylafax-v4.1-logrotate
Source7: hylafax-server.init
Source8: hylafax-v4.1-hyla.conf
Patch1: hylafax.jbig.patch
Packager: Denis Smirnov <mithraen@altlinux.ru>

Requires: ghostscript >= 5.5
Requires: libtiff >= 3.5.5-7
Requires: gawk >= 3.0.6
Requires: lib%name = %version-%release

BuildPreReq: ghostscript-classic jbig-utils
# Automatically added by buildreq on Sun Jan 02 2011 (-bi)
BuildRequires: gcc-c++ ghostscript-classic libjbig-devel libjpeg-devel libldap-devel libpam-devel libtiff-devel libtiff-utils man mgetty postfix sharutils zlib-devel
BuildRequires: glibc-devel-static

BuildRequires(pre): /proc

%add_findreq_skiplist %_sbindir/faxsetup
%define faxspool %_spooldir/fax

%description
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools.
The fax clients may reside on machines different from the server
and client implementations exist for a number of platforms including
windows.

You need this package if you are going to install hylafax-client
and/or hylafax server.

%package server
Summary: The files for the HylaFAX(tm) fax server
Group: %group
Requires: %name = %version-%release
Requires: libtiff-utils
Requires: mgetty
Requires: mgetty-voice
Requires: ghostscript-utils
Conflicts: efax
Conflicts: mgetty-sendfax
AutoReq: yes, noshell
PreReq: /var/lock/serial

%description server
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools.
The fax clients may reside on machines different from the server
and client implementations exist for a number of platforms including
windows.

This is the server portion of HylaFAX.

%package client
Summary: The files for the HylaFAX(tm) fax client
Group: %group
Requires: %name = %version-%release
Requires: fonts-type1-htmldoc
AutoReq: yes, noshell
Conflicts: mgetty-sendfax

%description client
HylaFAX(tm) is a sophisticated enterprise-strength fax package for
class 1 and 2 fax modems on unix systems. It provides spooling
services and numerous supporting fax management tools.
The fax clients may reside on machines different from the server
and client implementations exist for a number of platforms including
windows.

This is the client portion of HylaFAX.

%package -n lib%name
Summary: Hylafax libraries
Group: %group
AutoReq: yes, noshell
Obsoletes: lib%name-devel < %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name
HylaFAX(tm) is a sophisticated enterprise-strength fax package
for class 1 and 2 fax modems on unix systems. It provides
spooling services and numerous supporting fax management tools.

The fax clients may reside on machines different from the server
and client implementations exist for a number of platforms
including windows.

This package contains shared libraries for HylaFAX.

#package -n lib%name-devel
#Summary: Hylafax libraries
#Group: %group
#AutoReq: yes, noshell
#Requires: lib%name = %version-%release

#description -n lib%name-devel
#HylaFAX(tm) is a sophisticated enterprise-strength fax package for
#class 1 and 2 fax modems on unix systems. It provides spooling
#services and numerous supporting fax management tools.
#The fax clients may reside on machines different from the server
#and client implementations exist for a number of platforms including
#windows.

#This is the shared librairies of HylaFAX.

%prep
%setup -c -a 1 -a 2 -a 3
%patch1

%build
export INSTALLROOT=%buildroot
./configure \
    --with-DIR_BIN=%_bindir \
    --with-DIR_SBIN=%_sbindir \
    --with-DIR_LIB=%_libdir \
    --with-DIR_LIBEXEC=%_sbindir \
    --with-DIR_LIBDATA=%_datadir/fax \
    --with-DIR_LOCKS=%_var/lock \
    --with-TIFFINC=%_includedir \
    --with-TIFFBIN=%_bindir \
    --with-DIR_MAN=%_mandir \
    --with-PATH_GSRIP=%_bindir/gs \
    --with-DBLIBINC=%_includedir \
    --with-LIBTIFF="-ltiff -ljpeg -lz" \
    --with-DIR_SPOOL=%faxspool \
    --with-AFM=no \
    --with-AWK=%_bindir/gawk \
    --with-PATH_VGETTY=/sbin/vgetty \
    --with-PATH_GETTY=/sbin/mgetty \
    --with-HTML=yes \
    --with-PAGESIZE=A4 \
    --with-PATH_DPSRIP=%faxspool/bin/ps2fax \
    --with-PATH_IMPRIP=%_datadir/fax/psrip \
    --with-SYSVINIT=%_initdir/hylafax \
    --with-INTERACTIVE=no \
	--with-LIBDIR=%_libdir \
	--with-INSTALLROOT=%buildroot

#NO SMP
%make OPTIMIZER="%optflags"

%install
install -d -pm755 %buildroot%_sysconfdir/{logrotate.d,cron.hourly,cron.daily}
install -d -pm755 %buildroot{%_initdir,%_bindir,%_sbindir,%_libdir}
install -d -pm755 %buildroot%_datadir/fax
install -d -pm755 %buildroot%faxspool/{etc,config/defaults,bin}
install -d -pm755 %buildroot%_mandir/{man1,man5,man8}

%make -e \
	FAXUSER=`id -u` \
	FAXGROUP=`id -g` \
	SYSUSER=`id -u` \
	SYSGROUP=`id -g` \
	BIN=%buildroot%_bindir \
	SBIN=%buildroot%_sbindir \
	LIBDIR=%buildroot%_libdir \
	LIBDATA=%buildroot%_datadir/fax \
	LIBEXEC=%buildroot%_sbindir \
	SPOOL=%buildroot%faxspool \
	MAN=%buildroot%_mandir \
	ROOT=%buildroot \
	INSTALLROOT=%buildroot \
	INSTALL_ROOT=%buildroot install

# some hacks
sed -i "s!/usr%_sysconfdir/inetd.conf!%_sysconfdir/inetd.conf!g" %buildroot%_sbindir/faxsetup
sed -i "s!%_libdir/aliases!%_sysconfdir/aliases!g" %buildroot%_sbindir/faxsetup

# init
install %SOURCE7 -pm755  %buildroot%_initdir/hylafax-server

# defaults
install -m 644 defaults/* %buildroot%faxspool/config/defaults/

# hyla.conf
install %SOURCE8 -pm644 %buildroot%_datadir/fax/hyla.conf

# cron entries
install -pm755 hylafax_daily.cron  %buildroot%_sysconfdir/cron.daily/hylafax
install -pm755 hylafax_hourly.cron %buildroot%_sysconfdir/cron.hourly/hylafax

# logrotate
install -pm755 %SOURCE6 %buildroot%_sysconfdir/logrotate.d/hylafax-server

# dialrules extras
install -m 644 dialrules_extras/dialrules* %buildroot%faxspool/etc

(cd %buildroot%faxspool/bin; ln -s ps2fax.gs ps2fax)

# Since now the html doc dir is managed by the doc macro and not installed
# by HylaFAX, the CVS stuff need to be deleted
#find ./html -type d -name CVS |xargs rm -fr
#find ./html -type d | xargs chmod 755
#find html \( -type f -name .cvsignore -o -name "Makefile*" \) | xargs rm -f

# Some tools (manpage, man2html, unquote)
rm -f html/tools/{unquote,man2html}

# If Linux, what else...? :-), delete unnecessary files
%ifos linux
rm -f %buildroot%_sbindir/{faxsetup.irix,faxsetup.bsdi}
%endif
chmod 0755 %buildroot/%_sbindir/*
chmod 0755 %buildroot/%_bindir/*
mkdir -p %buildroot%faxspool/bin
mkdir -p %buildroot%faxspool/client
mkdir -p %buildroot%faxspool/config
mkdir -p %buildroot%faxspool/dev
mkdir -p %buildroot%faxspool/etc
mkdir -p %buildroot%faxspool/info
mkdir -p %buildroot%faxspool/log
mkdir -p %buildroot%faxspool/recvq
mkdir -p %buildroot%faxspool/status
mkdir -p %buildroot%faxspool/sendq
mkdir -p %buildroot%faxspool/doneq
mkdir -p %buildroot%faxspool/docq
mkdir -p %buildroot%faxspool/tmp
mkdir -p %buildroot%faxspool/pollq
mkdir -p %buildroot%faxspool/archive

%post client
%_sbindir/faxsetup -client

%post server
%post_service %name-server

# Adding faxgetty entry to %_sysconfdir/inittab
#logger adding FaxGetty entry to %_sysconfdir/inittab
#cat %_sysconfdir/inittab | grep -i "faxgetty entry" || \
#echo -e "# FaxGetty Entry\n#t0:23:respawn:%_sbindir/faxgetty ttyS0" >> %_sysconfdir/inittab
#echo "Please run \"%_sbindir/faxsetup -server\" to configure your fax server"

%preun server
%preun_service %name-server
%files
%doc README TODO VERSION COPYRIGHT
%_sbindir/faxsetup
%_sbindir/faxsetup.linux
%_sbindir/edit-faxcover
%_sbindir/faxlock

%files client
#%_datadir/fax/faxcover_example_sgi.ps
%_bindir/sendfax
%_bindir/sendpage
%_bindir/faxstat
%_bindir/faxalter
%_bindir/faxcover
%_bindir/faxmail
%_bindir/faxrm
%_sbindir/textfmt
%_datadir/fax/pagesizes
%_datadir/fax/faxcover.ps
%_datadir/fax/typerules
%_datadir/fax/hyla.conf
%_man1dir/*

%files server
%config(noreplace) %_initdir/hylafax*
%config(noreplace) %_sysconfdir/cron.daily/hylafax*
%config(noreplace) %_sysconfdir/cron.hourly/hylafax*
%config(noreplace) %_sysconfdir/logrotate.d/hylafax*
%attr(-,uucp,uucp) %dir %faxspool
%attr(-,uucp,uucp) %dir %faxspool/bin
%attr(-,uucp,uucp) %dir %faxspool/client
%attr(-,uucp,uucp) %dir %faxspool/config
%attr(-,uucp,uucp) %dir %faxspool/dev
%attr(-,uucp,uucp) %dir %faxspool/etc
#attr(-,uucp,uucp) %dir %faxspool%_sysconfdir/templates
%attr(-,uucp,uucp) %dir %faxspool/info
%attr(-,uucp,uucp) %dir %faxspool/log
%attr(-,uucp,uucp) %dir %faxspool/recvq
%attr(-,uucp,uucp) %dir %faxspool/status
%attr(-,uucp,uucp) %dir %faxspool/sendq
%attr(-,uucp,uucp) %dir %faxspool/doneq
%attr(-,uucp,uucp) %dir %faxspool/docq
%attr(-,uucp,uucp) %dir %faxspool/tmp
%attr(-,uucp,uucp) %dir %faxspool/pollq
%attr(-,uucp,uucp) %dir %faxspool/archive

#attr(-,uucp,uucp) %faxspool/FIFO
#attr(-,root,root) %faxspool/COPYRIGHT
%attr(-,uucp,uucp) %config(noreplace) %faxspool%_sysconfdir/xferfaxlog
%attr(-,uucp,uucp) %config(noreplace) %faxspool%_sysconfdir/hosts.hfaxd
%attr(-,uucp,uucp) %config(noreplace) %faxspool%_sysconfdir/lutRS18.pcf
%attr(-,uucp,uucp) %config(noreplace) %faxspool%_sysconfdir/dpsprinter.ps
%attr(-,uucp,uucp) %config(noreplace) %faxspool%_sysconfdir/cover.templ
%attr(-,uucp,uucp) %config(noreplace) %faxspool%_sysconfdir/dialrules*

#attr(-,uucp,uucp) %config(noreplace) %faxspool%_sysconfdir/templates/*

%attr(0755,root,root) %faxspool/bin/*
%faxspool/config/*

%_sbindir/hfaxd
%_sbindir/hylafax
%_sbindir/faxdeluser
%_sbindir/faxadduser
%_sbindir/choptest
%_sbindir/cqtest
%_sbindir/dialtest
%_sbindir/faxabort
%_sbindir/faxaddmodem
%_sbindir/faxanswer
%_sbindir/faxconfig
%_sbindir/faxcron
%_sbindir/faxgetty
%_sbindir/faxinfo
%_sbindir/faxmodem
%_sbindir/faxmsg
%_sbindir/faxq
%_sbindir/faxqclean
%_sbindir/faxquit
%_sbindir/faxsend
%_sbindir/faxstate
%_sbindir/faxwatch
%_sbindir/lockname
%_sbindir/ondelay
%_sbindir/pagesend
%_sbindir/probemodem
%_sbindir/recvstats
%_sbindir/tagtest
%_sbindir/tiffcheck
%_sbindir/tsitest
%_sbindir/typetest
%_sbindir/xferfaxstats

%_datadir/fax/faxmail.ps
%_datadir/fax/hfaxd.conf
%_datadir/fax/faxmail/application/octet-stream
%_datadir/fax/faxmail/application/pdf
%_datadir/fax/faxmail/image/tiff

%_man5dir/*
%_man8dir/*

%files -n lib%name
%_libdir/*.so.*

#files -n lib%name-devel
#doc html/*
#_libdir/*.so

%changelog
* Sat May 14 2011 Denis Smirnov <mithraen@altlinux.ru> 5.2.7-alt8
- bugfixes:
  + Fix loop in status (ALT #25580).
  + Add requires to ghostscript-utils (ALT #25598).
  + Add requires to fonts-type1-htmldoc (ALT #25596).
  + remove old unused code in initscript (ALT #25581).

* Mon Jan 03 2011 Denis Smirnov <mithraen@altlinux.ru> 5.2.7-alt7
- fix build

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 5.2.7-alt6
- auto rebuild

* Tue Jan 05 2010 Denis Smirnov <mithraen@altlinux.ru> 5.2.7-alt5
- spec cleanup (thanks to mike@)
- make scripts 0755 (ALT #21867)

* Sat Aug 29 2009 Denis Smirnov <mithraen@altlinux.ru> 5.2.7-alt4
- add conflicts hylafax-server -> mgetty-sendfax

* Fri Jul 03 2009 Denis Smirnov <mithraen@altlinux.ru> 5.2.7-alt3
- add conflict to efax

* Mon Dec 15 2008 Denis Smirnov <mithraen@altlinux.ru> 5.2.7-alt2
- fix build without hylafax requires

* Sun Dec 14 2008 Denis Smirnov <mithraen@altlinux.ru> 5.2.7-alt1
- improve faxq's FIFO parsing resiliancy (6 Aug 2008)
- invoke SetupPrivateTmp from notify, faxrcvd, and pollrcvd (21 Jul 2008)
- version update

* Sat Aug 02 2008 Denis Smirnov <mithraen@altlinux.ru> 5.2.6-alt0.1
- hylafax+ 5.2.6

* Fri Dec 07 2007 Denis Smirnov <mithraen@altlinux.ru> 5.2.0-alt0.1
- Move to hylafax+ codebase

* Sat Sep 22 2007 Denis Smirnov <mithraen@altlinux.ru> 4.3.2-alt3
- fixes for new find-requires (thanks to at@)

* Wed Apr 18 2007 Denis Smirnov <mithraen@altlinux.ru> 4.3.2-alt2
- rebuild (for x86_64 build)

* Sun Feb 18 2007 Denis Smirnov <mithraen@altlinux.ru> 4.3.2-alt1
- upstream update

* Thu Feb 15 2007 Denis Smirnov <mithraen@altlinux.ru> 4.3.0-alt0.10
- not start hylafax by default

* Wed Feb 07 2007 Denis Smirnov <mithraen@altlinux.ru> 4.3.0-alt0.9
- fix unresolved symbols (thanks to Damir Shayhutdinov)

* Thu Jan 11 2007 Denis Smirnov <mithraen@altlinux.ru> 4.3.0-alt0.8
- LSB initscript
- start after iaxmodem if it exists

* Wed Dec 27 2006 Denis Smirnov <mithraen@altlinux.ru> 4.3.0-alt0.7
- rebuild with new dbus

* Fri Nov 17 2006 Denis Smirnov <mithraen@altlinux.ru> 4.3.0-alt0.6
- second try to not search requires for shell scripts

* Tue Oct 31 2006 Denis Smirnov <mithraen@altlinux.ru> 4.3.0-alt0.5
- not search requires for shell scripts

* Fri Oct 27 2006 Denis Smirnov <mithraen@altlinux.ru> 4.3.0-alt0.4
- and one else try to fix initscript

* Wed Oct 25 2006 Denis Smirnov <mithraen@altlinux.ru> 4.3.0-alt0.3
- fix spool dirs creation

* Wed Oct 25 2006 Denis Smirnov <mithraen@altlinux.ru> 4.3.0-alt0.2
- fix rights for executables
- fix requires for hylafax-server
- create dirs that needed for hylafax

* Sat Oct 14 2006 Denis Smirnov <mithraen@altlinux.ru> 4.3.0-alt0.1
- get from orphaned, version update

* Wed Oct 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.1.5-alt1
- 4.1.5
- Rebuilt in new environment
- Rebuilt without svgalib

* Mon Aug 05 2002 Stanislav Ievlev <inger@altlinux.ru> 4.1.3-alt1
- update (bugfixes?) 'cause this is package without maintainer
- light spec cleanup

* Tue Oct 16 2001 Konstantin Volckov <goldhead@altlinux.ru> 4.1-ipl1mdk
- Changes for new /var/lock/serial scheme
- 4.1
- Added optimization patch
- Fixed filelist
- Fixed Requires

* Mon Apr 16 2001 AEN <aen@logic> 4.10-ipl0.9mdk
- security patch

* Sun Mar 4 2001 AEN <aen@logic.ru> 4.1.0-ipl0.8mdk
- back to Christian's spec
- RE adaptation

* Tue Feb 27 2001 Christian Zoffoli <czoffoli@linux-mandrake.com> 4.1-0.8mdk
- beta 3
- fix a typo

* Fri Jan 26 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.1-0.7mdk
- from Christian Zoffoli <czoffoli@linux-mandrake.com>
	- cvs-20001203
	- many changes in spec
	- new init script

* Thu Dec 07 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.1-0.6mdk
- new lib scheme
- make rpmlint happier (remove ~30 errors and ~40 warning, ie 50%% of all my
  packages errors and warnings)

* Wed Nov 08 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.1-0.5mdk
- remove CVS garbage
- uses optimizations

* Wed Nov 08 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.1-0.4mdk
- build release

* Mon Sep 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 4.1-0.3mdk
- remove duplicate installation of sysvinit script through configure/makefile
- make it /var/lock/subsys compliant
- use _initrddir

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.1-0.2mdk
- automatically added BuildRequires

* Fri Aug 04 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.1-0.1mdk
- Christian Zoffoli <czoffoli@linux-mandrake.com> :
	* cleaning in spec
	* added faxadduser faxdeluser
	* updated to cvs 20000801
	* changes in spec
	* new hylafax init script

* Mon Jul 31 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 4.0pl2.rjc11-5mdk
- removed group
- fixed man (comp. with other distro)
- fixed macros
- changed permissions
- fixed fonts
- fixed doc / html install
- spec restyling
- added libtiff 3.5 support (patch tiff-3.5-interfaces.patch - adapted)
- added posix-rename.patch
- added cvtDateTime.patch
- added tagline-patch (adapted)
- fixed libtiff 3.5 test
- added some dialrules
- fixed ldconfig in main package (making rpmlint happier)

* Wed Jul 19 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.0pl2.rjc11-4mdk
- BM

* Tue May  9 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 4.0pl2.rjc11-3mdk
- Add a lot of fixes from Christian Zoffoli <czoffoli@littlepenguin.org>.

* Thu Apr 06 2000 Christopher Molnar <molnarc@mandrakesoft.com> 4.0pl2.rjc11-2mdk
  - changed group to Communications
  - bzipped patch files and additional source files
  - cleaned up spec file a bit

* Tue Feb 22 2000 Brian J. Murrell <spec-maint@interlinx.bc.ca>4.0p12-1mdk
  - customized for Mandrake 7.0
  - split into common, client and server subpackages
  - use urw-fonts package instead of ghostscript-fonts
  - patch up to rjc11 from CVS
  - change --with-DIR_AFM to --with-FONTMAP while configuring
  - prompt the "yes" into configure
  - force make install to install the startup script for the server
  - modify to support a "DESTDIR" install
  - put execute permissions on the created shared libs
  - change the compress manpages code to be much simpler
  - have the %post for server and client either run or prompt faxsetup
	to be run
  - update URL pointer

* Tue Sep 29 1998 Darren Nickerson <darren@info.tpc.int>
  - added security fix proposed by Carsten Hoeger <choeger@suse.de> for
	potential race condition  reported by Tobias Richter
	<tsr@cave.isdn.cs.tu-berlin.de>
* Wed Sep 9 1998 Darren Nickerson <darren@info.tpc.int>
  - built the RPM on Redhat-5.0 to avoid dependency problems with libjpeg
	and libstdc++.
* Tue May 26 1998 Darren Nickerson <darren@info.tpc.int>
  - removed .orig files from patch - they were 90 percent of it
  - removed oversimplified /dev/modem assumptions
  - faxcron was invoking xferstats, instead of new xferfaxstats - fixed
  - revised faxcron's manpage
  - HylaFAX was still writing etc/xferlog. Changed to etc/xferfaxlog as
	advertised by all supporting docs and scripts.
  - added hourly faxqclean and daily faxcron cron jobs, and xferlog rotation
  - hfaxd no longer hard-wired as running from inetd, faxsetup will handle this
  - no longer assumes /dev/modem and blindly inserts inittab entry
  - change naming scheme to differentiate rh4/rh5
  - move documentation back into main rpm, instead of sub-packages
  - added Robert Colquhoun's textfmt-mailer patch
  - increased margin on LHS, was too close and getting clipped
  - make faxsetup warn that modem class = modem pool, not Class1/2/2.0
  - use HylaFAX's init script, startup with new protocol only and no snpp
  - added -DFIXEDMEDIA to last command in ps2fax.gs, as posted
	by "Alan Sparks" <asparks@nss.harris.com>
  - added fixhtml patch, removed release from the doc dir, now just version
  - added Nico's skel patch, for class1/2/2.0 modem prototype files
  - added Robert Colquhoun's patch to hfaxd's tagline generation
  - fixes to build on 5.1, contributed by Richard Sharpe <sharpe@ns.aus.com>
  - faxrcvd now treated as a config file, preserved as .rpmsave
  - fixed ghostscript dependency to require fonts-std, not fonts.
  - remove requirement for mawk - use gawk instead.
  - faxsetup now detects is hfaxd is not driven from inetd, and starts it
	when restarting faxq using SysV init script (Robert Colquhoun)

* Wed Mar 04 1998 Markus Pilzecker <mp@rhein-neckar.netsurf.de>
  - took ldconfig call out ouf %install section
  - minimized and compressed patch
  - arch rpm buildable as ordinary user
  - diverted subpackages for [un]compressed man pages
  - diverted subpackage for html documentation

* Thu Jan 22 1998 Bernd Johannes Wuebben <wuebben@kde.org>
  - hylafax-4.0-8
  - A previous version of this spec file was handed to me by
    Ramana Juvvadi (juvvadi@lekha.org)
    who unfortunately can no longer provide rpms of hylafax.
    Thanks so much for you work Ramana!
    Bernd

* Fri Oct 24 1997 Ramana Juvvadi (juvvadi@lekha.org)
  - hylafax-4.0-6
