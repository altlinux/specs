Name: privoxy
Version: 3.0.16
Release: alt2

Summary: Privoxy - privacy enhancing proxy
License: GPLv2+
Group: Networking/WWW
Url: http://www.privoxy.org/
Packager: Sviatoslav Sviridov <svd@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.chroot.lib
Source2: %name.chroot.conf
Source3: %name.chroot.log
Source4: %name.chroot.all
Source5: %name.init
Source6: %name.log
Source7: %name.default.action

Patch1: %name-3.0.10-alt-config.patch

PreReq: chkconfig, shadow-utils, chrooted, coreutils

# Root directory for chrooted environment, must not be same as real system root.
%define ROOT /var/lib/%name

# Automatically added by buildreq on Thu Sep 19 2002
BuildRequires: docbook-style-dsssl libpcre-devel

%description
Privoxy is a web proxy with advanced filtering capabilities for protecting
privacy, filtering web page content, managing cookies, controlling access, and
removing ads, banners, pop-ups and other obnoxious Internet junk. Privoxy has a
very flexible configuration and can be customized to suit individual needs and
tastes. Privoxy has application for both stand-alone systems and multi-user
networks.

Privoxy is based on the Internet Junkbuster.
Privoxy runs in safe chrooted environment with own uid and gid.

%prep
%setup -n %name-%version

%patch1 -p2

cp -p $RPM_SOURCE_DIR/%name.{init,log,chroot.{lib,conf,log,all}} .
%__subst -p 's|%%name|%name|g; s|%%ROOT|%ROOT|g' %name.{init,log,chroot.{lib,conf,log,all}} config
#cp -p %SOURCE7 ./default.action.master

%build
%__autoheader
%__autoconf

export ac_cv_prog_GDB=yes
export ac_cv_prog_WDUMP=lynx
export ac_cv_prog_DB2HTML=db2html
export ac_cv_prog_JADEBIN=openjade
export ac_cv_prog_MAN2HTML=man2html
%configure

%make_build

%install
# From junkbuster.spec
install -pD -m755 %name %buildroot%_sbindir/%name
install -pD -m644 %name.1 %buildroot%_man8dir/%name.8
install -pD -m640 %name.log %buildroot%_sysconfdir/logrotate.d/%name
install -pD -m755 %name.init %buildroot%_initdir/%name

mkdir -p %buildroot%ROOT{%_sbindir,/lib,/var/{nis,yp/binding,log},%_sysconfdir/%name/templates}
install -p config trust {default,match-all,user}.action {default,user}.filter %buildroot%ROOT/%_sysconfdir/%name/
install -p templates/[a-z]* %buildroot%ROOT/%_sysconfdir/%name/templates/

install -pD -m750 %name.chroot.lib %buildroot%_sysconfdir/chroot.d/%name.lib
install -pD -m750 %name.chroot.conf %buildroot%_sysconfdir/chroot.d/%name.conf
install -pD -m750 %name.chroot.log %buildroot%_sysconfdir/chroot.d/%name.log
install -pD -m750 %name.chroot.all %buildroot%_sysconfdir/chroot.d/%name.all

touch %buildroot%ROOT{/var/log/{%name,jarfile},%_sysconfdir/{hosts,{host,nsswitch,resolv}.conf},/var/nis/NIS_COLD_START}

%pre
/usr/sbin/groupadd -r -f %name
/usr/sbin/useradd -r -g %name -d %ROOT -s /dev/null -c 'The Privoxy web proxy' %name >/dev/null 2>&1 ||:
if [ $1 -gt 1 ]; then
	/usr/sbin/usermod -d %ROOT %name
fi

%post
%_sysconfdir/chroot.d/%name.all force
%post_service %name
test -d %_sysconfdir/%name/ || ln -s %ROOT%_sysconfdir/%name %_sysconfdir/%name

%preun
%preun_service %name
if [ $1 = 0 ]; then
	rm -f %ROOT/lib/* %ROOT/var/yp/binding/*
	rm -f %_sysconfdir/%name
fi

# between 3.0.10 and 3.0.16 regular action file is renamed
%triggerun -- %name < 3.0.16
if [ $2 -gt 0 ]; then
    %__subst "s|^actionsfile standard.action|actionsfile match-all.action|g" %ROOT%_sysconfdir/%name/config
fi

%files
%config(noreplace) %_sysconfdir/logrotate.d/*
%config %_initdir/%name
%config %_sysconfdir/chroot.d/*
%_sbindir/*
%_mandir/man?/*
%doc README AUTHORS doc/webserver/user-manual/[a-z]*

%defattr(640,root,%name,710)
%dir %ROOT
%dir %ROOT/lib
%dir %ROOT%_sysconfdir
%dir %ROOT%_sysconfdir/%name
%ROOT%_sysconfdir/%name/templates
%config(noreplace) %ROOT%_sysconfdir/%name/config
%config(noreplace) %ROOT%_sysconfdir/%name/user.action
%config(noreplace) %ROOT%_sysconfdir/%name/user.filter
%config %ROOT%_sysconfdir/%name/default.action
%config %ROOT%_sysconfdir/%name/default.filter
%config %ROOT%_sysconfdir/%name/match-all.action
%config %ROOT%_sysconfdir/%name/trust
%dir %ROOT/var
%dir %ROOT/var/log
%dir %ROOT/var/nis
%ghost %ROOT/var/nis/NIS_COLD_START
%dir %ROOT/var/yp
%dir %ROOT/var/yp/binding

%defattr(644,root,root,710)
%ghost %ROOT%_sysconfdir/hosts
%ghost %ROOT%_sysconfdir/*.conf
%ghost %attr(660,root,%name) %ROOT/var/log/jarfile
%ghost %attr(660,root,%name) %ROOT/var/log/%name

%changelog
* Thu Jan 12 2012 Vitaly Lipatov <lav@altlinux.ru> 3.0.16-alt2
- add trigger for change actionsfile in config to new name (ALT bug #23489)
- privoxy.init: fix pidfile create (needed for monit)
- add link to config dir from /etc/privoxy

* Sun May 02 2010 Andrey Rahmatullin <wrar@altlinux.ru> 3.0.16-alt1
- 3.0.16

* Fri Sep 12 2008 Sviatoslav Sviridov <svd@altlinux.ru> 3.0.10-alt1
- Updated to 3.0.10
- Removed alt-tzset patch (applied in upstream)
- Updated alt-config patch

* Fri Mar 09 2007 Sviatoslav Sviridov <svd@altlinux.ru> 3.0.6-alt2
- Redirecting logrotate output to /dev/null (#8103)

* Sun Dec 03 2006 Sviatoslav Sviridov <svd@altlinux.ru> 3.0.6-alt1
- Updated to 3.0.6
- Updated default action file to v2.0 (#10228)
- Rediffed patches:
  + alt-tzset patch
  + alt-config.patch

* Wed Feb 04 2004 Sviatoslav Sviridov <svd@altlinux.ru> 3.0.3-alt1
- updated to 3.0.3
- actions file updated to 1.8

* Tue Sep 09 2003 Sviatoslav Sviridov <svd@altlinux.ru> 3.0.2-alt2
- added missed templates

* Tue Sep 09 2003 Sviatoslav Sviridov <svd@altlinux.ru> 3.0.2-alt1
- rewritten initscript to use start-stop-daemon
- Removed chroot patch (applied in upstream).
- Ensure tzset(3) is called before chroot(2) (missed in upstream).
- Using newer default.action file.
- Changes in %ROOT chroot:
  + only %_sysconfdir/%name/config and %_sysconfdir/%name/user.action
    marked 'noreplace'

* Thu Sep 19 2002 Dmitry V. Levin <ldv@altlinux.org> 3.0.0-alt2
- Ensure tzset(3) is called before chroot(2).
- Changes in %ROOT chroot:
  + removed %_sysconfdir/localtime;
  + added NIS/NIS+ support.
- Updated %name.chroot.* scripts (a la resolver chroot).
- Use subst instead of perl in build scripts.
- Cached in some unused values for configure, to cleanup buildrequires.

* Thu Aug 29 2002 Sviatoslav Sviridov <svd@altlinux.ru> 3.0.0-alt1
- new version relased

* Sat Jul 5 2002 Sviatoslav Sviridov <svd@altlinux.ru> 2.9.14-alt0.3
- fixed privoxy.croot.lib: don't copy libnsl and libpthread to chroot
- Don't include %ROOT%prefix to %files section

* Sat Jun 15 2002 Sviatoslav Sviridov <svd@altlinux.ru> 2.9.14-alt0.2
- fixed privoxy.croot.lib: copy nss libraries to chroot

* Fri Jun 10 2002 Sviatoslav Sviridov <svd@altlinux.ru> 2.9.14-alt0.1
- First build for ALT Linux distribution
- Added option --chroot to allow start privoxy chrooted

* Wed Apr 10 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.13-5
- Relisting template files on the %%files section

* Tue Apr 09 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-4
- Removed 'make dok'. Docs are all maintained in CVS (and tarball) now.

* Mon Apr 08 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-4
- Add templates/cgi-style.css, faq.txt, p_web.css, LICENSE
- Remove templates/blocked-compact.
- Add more docbook stuff to Builderquires.

* Thu Mar 28 2002 Sarantis Paskalis <sarantis@cnl.di.uoa.gr>
+ privoxy-2.9.13-3
- Include correct documentation file.

* Tue Mar 26 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-3
- Fix typo in Description.

* Tue Mar 26 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.13-3
- Added commentary asking to update the release value on the configure
  script

* Tue Mar 25 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-3
- Added the missing edit-actions-for-url-filter to templates.

* Mon Mar 25 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ privoxy-2.9.13-2
- Fixing Release number

* Sun Mar 24 2002 Hal Burgiss <hal@foobox.net>
+ privoxy-2.9.13-2
- Added faq to docs.

* Sun Mar 24 2002 Rodrigo Barbosa <rodrigob@suespammers.org>
+ privoxy-2.9.13-2
- Fixed the init files entries. Now we use %%ghost
- improved username (and groupname) handling on the %%pre section. By improved
  I mean: we do it by brute force now. Much easier to maintain. Yeah, you
  got it right. No more Mr. Nice Guy.
- Removed the userdel call on %%post. No need, once it's complety handled on
  the %%pre section

* Sun Mar 24 2002 Hal Burgiss <hal@foobox.net>
+ junkbusterng-2.9.13-1
  Added autoheader. Added autoconf to buildrequires.

* Sun Mar 24 2002 Hal Burgiss <hal@foobox.net>
+ junkbusterng-2.9.13-1
- Fixed build problems re: name conflicts with man page and logrotate.
- Commented out rc?d/* configs for time being, which are causing a build 
- failure. /etc/junkbuster is now /etc/privoxy. Stefan did other name 
- changes. Fixed typo ';' should be ':' causing 'rpm -e' to fail.

* Fri Mar 22 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbusterng-2.9.13-1
- References to the expression ijb where changed where possible
- New package name: junkbusterng (all in lower case, acording to
  the LSB recomendation)
- Version changed to: 2.9.13
- Release: 1
- Added: junkbuster to obsoletes and conflicts (Not sure this is
  right. If it obsoletes, why conflict ? Have to check it later)
- Summary changed: Stefan, please check and aprove it
- Changes description to use the new name
- Sed string was NOT changed. Have to wait to the manpage to
  change first
- Keeping the user junkbuster for now. It will require some aditional
  changes on the script (scheduled for the next specfile release)
- Added post entry to move the old logfile to the new log directory
- Removing "chkconfig --add" entry (not good to have it automaticaly
  added to the startup list).
- Added preun section to stop the service with the old name, as well
  as remove it from the startup list
- Removed the chkconfig --del entry from the conditional block on
  the preun scriptlet (now handled on the %files section)

* Thu Mar 21 2002 Hal Burgiss <hal@foobox.net>
- added ijb_docs.css to docs.

* Mon Mar 11 2002 Hal Burgiss <hal@foobox.net>
+ junkbuster-2.9.11-8 
- Take out --enable-no-gifs, breaks some browsers.

* Sun Mar 10 2002 Hal Burgiss <hal@foobox.net>
+ junkbuster-2.9.11-8 
- Add --enable-no-gifs to configure.

* Fri Mar 08 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-7
- Added BuildRequires to libtool.

* Tue Mar 06 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-6
- Changed the routined that handle the junkbust and junkbuster users on
  %%pre and %%post to work in a smoother manner
- %%files now uses hardcoded usernames, to avoid problems with package
  name changes in the future

* Tue Mar 05 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-5
- Added "make redhat-dok" to the build process
- Added docbook-utils to BuildRequires

* Tue Mar 05 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-4
- Changing man section in the manpage from 1 to 8
- We now require packages, not files, to avoid issues with apt

* Mon Mar 04 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-3
- Fixing permissions of the init script

* Mon Mar 04 2002 Rodrigo Barbosa <rodrigob@tisbrasil.com.br>
+ junkbuster-2.9.11-2
- General specfile fixup, using the best recomended practices, including:
	- Adding -q to %%setup
	- Using macros whereever possible
	- Not using wildchars on %%files section
	- Doubling the percentage char on changelog and comments, to
	  avoid rpm expanding them

* Sun Mar 03 2002 Hal Burgiss <hal@foobox.net>
- /bin/false for shell causes init script to fail. Reverting.

* Wed Jan 09 2002 Hal Burgiss <hal@foobox.net>
- Removed UID 73. Included user-manual and developer-manual in docs.
  Include other actions files. Default shell is now /bin/false.
  Userdel user=junkbust. ChangeLog was not zipped. Removed 
  RPM_OPT_FLAGS kludge.

* Fri Dec 28 2001 Thomas Steudten <thomas@steudten.ch>
- add paranoia check for 'rm -rf %%{buildroot}'
- add gzip to 'BuildRequires'

* Sat Dec  1 2001 Hal Burgiss <hal@foobox.net>
- actionsfile is now ijb.action.

* Tue Nov  6 2001 Thomas Steudten <thomas@steudten.ch>
- Compress manpage
- Add more documents for installation
- Add version string to name and source

* Wed Oct 24 2001 Hal Burigss <hal@foobox.net>
- Back to user 'junkbuster' and fix configure macro.

* Wed Oct 10 2001 Hal Burigss <hal@foobox.net>
- More changes for user 'junkbust'. Init script had 'junkbuster'.

* Sun Sep 23 2001 Hal Burgiss <hal@foobox.net>
- Change of $RPM_OPT_FLAGS handling. Added new HTML doc files.
- Changed owner of /etc/junkbuster to shut up PAM/xauth log noise.

* Thu Sep 13 2001 Hal Burgiss <hal@foobox.net>
- Added $RPM_OPT_FLAGS support, renaming of old logfile, and 
- made sure no default shell exists for user junkbust.

* Sun Jun  3 2001 Stefan Waldherr <stefan@waldherr.org>
- rework of RPM

* Mon Sep 25 2000 Stefan Waldherr <stefan@waldherr.org>
- CLF Logging patch by davep@cyw.uklinux.net
- Hal DeVore <haldevore@earthling.net> fix akamaitech in blocklist

* Sun Sep 17 2000 Stefan Waldherr <stefan@waldherr.org>
- Steve Kemp skx@tardis.ed.ac.uk's javascript popup patch.
- Markus Breitenbach breitenb@rbg.informatik.tu-darmstadt.de supplied
  numerous fixes and enhancements for Steve's patch.
- adamlock@netscape.com (Adam Lock) in the windows version:
  - Taskbar activity spinner always spins even when logging is
  turned off (which is the default) - people who don't
  like the spinner can turn it off from a menu option.
  - Taskbar popup menu has a options submenu - people can now
  open the settings files for cookies, blockers etc.
  without opening the JB window.
  - Logging functionality works again
  - Buffer overflow is fixed - new code uses a bigger buffer
  and snprintf so it shouldn't overflow anymore.
- Fixed userid swa, group learning problem while installing.
  root must build RPM.
- Added patch by Benjamin Low <ben@snrc.uow.edu.au> that prevents JB to
  core dump when there is no log file.
- Tweaked SuSE startup with the help of mohataj@gmx.net and Doc.B@gmx.de.
- Fixed man page to include imagefile and popupfile.
- Sanity check for the statistics function added.
- "Patrick D'Cruze" <pdcruze@orac.iinet.net.au>: It seems Microsoft
 are transitioning Hotmail from FreeBSD/Apache to Windows 2000/IIS.
 With IIS/5, it appears to omit the trailing \r\n from http header
 only messages.  eg, when I visit http://www.hotmail.com, IIS/5
 responds with a HTTP 302 redirect header.  However, this header
 message is missing the trailing \r\n.  IIS/5 then closes the
 connection.  Junkbuster, unfortunately, discards the header becomes
 it thinks it is incomplete - and it is.  MS have transmitted an
 incomplete header!
- Added bug reports and patch submission forms in the docs.

* Mon Mar 20 2000 Stefan Waldherr <stefan@waldherr.org>
       Andrew <anw@tirana.freewire.co.uk> extended the JB:
       Display of statistics of the total number of requests and the number
       of requests filtered by junkbuster, also the percentage of requests
       filtered. Suppression of the listing of files on the proxy-args page.
       All stuff optional and configurable.

* Sun Sep 12 1999 Stefan Waldherr <stefan@waldherr.org>
       Jan Willamowius (jan@janhh.shnet.org) fixed a bug in the 
       code which prevented the JB from handling URLs of the form
       user:password@www.foo.com. Fixed.

* Mon Aug  2 1999 Stefan Waldherr <stefan@waldherr.org>
	Blank images are no longer cached, thanks to a hint from Markus 
        Breitenbach <breitenb@rbg.informatik.tu-darmstadt.de>. The user 
        agent is NO longer set by the Junkbuster. Sadly, many sites depend 
        on the correct browser version nowadays. Incorporated many 
	suggestions from Jan "Yenya" Kasprzak <kas@fi.muni.cz> for the
        spec file. Fixed logging problem and since runlevel 2 does not 
        use networking, I replaced /etc/rc.d/rc2.d/S84junkbuster with
        /etc/rc.d/rc2.d/K09junkbuster thanks to Shaw Walker 
        <walker@netgate.net>. You should now be able to build this RPM as 
        a non-root user (mathias@weidner.sem.lipsia.de).

* Sun Jan 31 1999 Stefan Waldherr <stefan@waldherr.org>
	%%{_localstatedir}/log/junkbuster set to nobody. Added /etc/junkbuster/imagelist
	to allow more sophisticated matching of blocked images. Logrotate
	logfile. Added files for auto-updating the blocklist et al.

* Wed Dec 16 1998 Stefan Waldherr <stefan@waldherr.org>
	Configure blank version via config file. No separate blank
	version anymore. Added Roland's <roland@spinnaker.rhein.de>
	patch to show a logo instead of a blank area. Added a suggestion
	from Alex <alex@cocoa.demon.co.uk>: %%{_localstatedir}/lock/subsys/junkbuster.
	More regexps in the blocklist. Prepared the forwardfile for
	squid. Extended image regexp with help from gabriel 
	<somlo@CS.ColoState.EDU>.

* Thu Nov 19 1998 Stefan Waldherr <stefan@waldherr.org>
	All RPMs now identify themselves in the show-proxy-args page.
	Released Windoze version. Run junkbuster as nobody instead of
	root. 

* Fri Oct 30 1998 Stefan Waldherr <stefan@waldherr.org>
	Newest version. First release (hence the little version number
	mixture -- 2.0.2-0 instead of 2.0-7). This version tightens 
	security over 2.0.1; some multi-user sites will need to change 
	the listen-address in the configuration file. The blank version of
        the Internet Junkbuster has a more sophisticated way of replacing
	images. All RPMs identify themselves in the show-proxy-args page.

* Thu Sep 23 1998 Stefan Waldherr <stefan@waldherr.org>
	Modified the blocking feature, so that only GIFs and JPEGs are
	blocked and replaced but not HTML pages. Thanks to 
	"Gerd Flender" <plgerd@informatik.uni-siegen.de> for this nice
	idea. Added numerous stuff to the blocklist. Keep patches in
        seperate files and no longer in diffs (easier to maintain).

* Tue Jun 16 1998 Stefan Waldherr <swa@cs.cmu.edu>
        Moved config files to /etc/junkbuster directory, moved man page,
	added BuildRoot directive (Thanks to Alexey Nogin <ayn2@cornell.edu>)
        Made new version junkbuster-raw (which is only a stripped version of 
        the junkuster rpm, i.e. without my blocklist, etc.)

* Tue Jun 16 1998 (2.0-1)
	Uhm, not that much. Just a new junkbuster version that
	fixes a couple of bugs ... and of course a bigger 
	blocklist with the unique Now-less-ads-than-ever(SM)
	feature.
	Oh, one thing: I changed the default user agent to Linux -- no 
	need anymore to support Apple.

* Tue Jun 16 1998 (2.0-0)
	Now-less-ads-than-ever (SM)
	compiled with gcc instead of cc
	compiled with -O3, thus it should be a little faster
	show-proxy-args now works
	/etc/junkbuster.init wasn't necessary

* Tue Jun 16 1998 (1.4)
	some more config files were put into /etc
	The junkbuster-blank rpm returns a 1x1 pixel image, that gets 
	displayed by Netscape instead of the blocked image.
	Read http://www.waldherr.org/junkbuster/ for
	further info.

* Tue Jun 16 1998 (1.3)
	The program has been moved to /usr/sbin (from /usr/local/bin)
	Init- and stopscripts (/etc/rc.d/rc*) have been added so
	that the junkbuster starts automatically during bootup.
	The /etc/blocklist file is much more sophisticated. Theoretically
	one should e.g. browse all major US and German newspapers without
	seeing one annoying ad.
	junkbuster.init was modified. It now starts junkbuster with an
	additional "-r @" flag.
