%define _unpackaged_files_terminate_build 1
%define _user _eggdrop
%define _group _eggdrop
%define _home %_localstatedir/%name

Name: eggdrop
Version: 1.9.4
Release: alt1

Summary: Eggdrop is an IRC bot, written in C
License: GPL-2.0
Group: Networking/IRC

Url: http://www.eggheads.org
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.README.ALT.UTF8
Source2: %name.init
Source3: %name.tmpfiles
Patch1: %name-fix-config-interpreter.patch
Patch2: %name-pathes.patch

BuildRequires: tcl-devel zlib-devel autoconf
BuildRequires: libssl-devel
%add_findreq_skiplist %_datadir/%name/scripts/*

%description
Eggdrop is an IRC bot, written in C.  If you don't know what IRC is,
this is probably not whatever you're looking for!  Eggdrop, being a
bot, sits on a channel and takes protective measures: to keep the
channel from being taken over (in the few ways that anything CAN),
to recognize banished users or sites and reject them, to recognize
privileged users and let them gain ops, etc.

%prep
%setup
%patch1 -p2
%patch2 -p1

%build
%autoreconf
%configure
make config
%make_build

%install
install -dm1770 %buildroot/run/%name
install -dm1770 %buildroot%_logdir/%name

mkdir -p %buildroot%_libdir/%name/
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_docdir/%name-%version/
mkdir -p %buildroot%_man1dir/
mkdir -p %buildroot%_logdir/%name

%make DEST=%buildroot%_datadir/%name install

# Move modules into /usr/lib*
mkdir -p %buildroot%_libdir
mv -f %buildroot%_datadir/%name/modules* %buildroot%_libdir/%name

# move binaries
mkdir -p %buildroot%_bindir
mv -f %buildroot%_datadir/%name/{%name,%name-%version} %buildroot%_bindir

# initscript
install -pDm0755 %SOURCE2 %buildroot%_initdir/%name

# manpage
install -m644 doc/man1/%name.1 %buildroot%_man1dir
rm -rf doc/man1

# Fix paths of example eggdrop.conf
sed -i  -e "s,scripts/,%_datadir/%name/scripts/,g" \
	-e "s,help/,%_datadir/%name/help/,g" \
	-e "s,modules/,%_libdir/%name/modules/,g" \
	-e "s,language/,%_datadir/%name/language/,g" \
	-e "s,text/,%_datadir/%name/text/,g" %name.conf
install -pDm0755 eggdrop.conf %buildroot%_sysconfdir/%name.conf
mkdir -p %buildroot%_home
ln -s ../../../etc/eggdrop.conf %buildroot%_home/eggdrop.conf

# README.ALT
install -pDm0644 %SOURCE1 README.ALT.UTF8

# scripts directory
install -dm1770 %buildroot%_home/scripts

# remove unnedded stuff
rm -rf %buildroot%_datadir/%name/doc

# install tmpfiles
install -Dpm644 %SOURCE3 %buildroot%_tmpfilesdir/%name.conf

%pre
/usr/sbin/groupadd -r -f %_group ||:
/usr/sbin/useradd -g %_group -c 'The eggdrop' \
        -d %_home -s /dev/null -r %_user >/dev/null 2>&1 ||:

%files
%doc doc/* README*
%dir %_libdir/%name
%dir %_datadir/%name/language
%dir %_libdir/%name/modules-%version
%dir %_datadir/%name/help
%dir %_datadir/%name/help/set
%dir %_datadir/%name/help/msg
%dir %_datadir/%name/scripts
%dir %_datadir/%name/text
%dir %attr(1770,root,%_group) %_home
%dir %attr(1770,root,%_group) %_home/scripts
%dir %attr(1770,root,%_group) /run/%name
%dir %attr(1770,root,%_group) %_logdir/%name
%config(noreplace) %_sysconfdir/%name.conf
%_initdir/%name
%_bindir/%name
%_bindir/%name-%version
%_libdir/%name/modules
%_libdir/%name/modules-%version/*.so
%_datadir/%name/*
%_home/eggdrop.conf
%_tmpfilesdir/%name.conf
%_man1dir/%name.1.*

%changelog
* Wed Dec 14 2022 Andrey Cherepanov <cas@altlinux.org> 1.9.4-alt1
- New version.

* Thu Aug 11 2022 Andrey Cherepanov <cas@altlinux.org> 1.9.3-alt1
- New version.
- Move eggdrop.conf to /etc.
- Make /run/eggdrop by eggrop tmpfile.

* Sun Mar 06 2022 Andrey Cherepanov <cas@altlinux.org> 1.9.2-alt1
- New version.

* Tue Jun 01 2021 Andrey Cherepanov <cas@altlinux.org> 1.9.1-alt1
- New version.

* Sun Mar 28 2021 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- New version.

* Sun Dec 27 2020 Andrey Cherepanov <cas@altlinux.org> 1.8.4-alt2
- Rebuild with latest autoconf.
- Fix License according to SPDX.

* Fri Dec 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.4-alt1
- New version.

* Thu Feb 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.3-alt1
- New version.

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1
- New version

* Mon Mar 27 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.1-alt1.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Mon Mar 27 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version

* Thu Jan 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- new version 1.8.0

* Tue Oct 06 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.21-alt3
- New version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6.19-alt2.qa1
- NMU: rebuilt for debuginfo.

* Mon May 18 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.6.19-alt2
- Security fix: eggdrop remote crash vulnerability (incomplete patch for
  CVE-2007-2807) (Closes: #20067)

* Sat Sep 27 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1.6.19-alt1
- 1.6.19

* Thu Mar 13 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.6.18-alt3
- Rebuild with libtcl8.5

* Thu Sep 20 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.6.18-alt2
- Security fix: CVE-2007-2807: Stack-based buffer overflow in
  mod/server.mod/servrmsg.c
- Recode README.ALT to utf8 and update it
- Create pseudouser on %%pre stage
- Install config to /var/lib/eggdrop
- Load module blowfish by default
- Change default pidfile path
- Add initscript
- Fix default directory for help and text

* Fri Nov 03 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.6.18-alt1
- 1.6.18
- Move architecture-independent files into %%_datadir/%%name
- Place binary into %%_bindir
- Fix paths in default config (sed + eggdrop-1.6.17-fc-conf.patch)
- Change default path to langdir in sources (eggdrop-1.6.17-fc-langdir.patch)
- Added README.ALT
- Minor spec cleanup

* Mon Sep 06 2004 Nazar Yurpeak <phoenix@altlinux.org> 1.6.17-alt2
- Updated form eggheads.org

* Thu Jul 29 2004 Nazar Yurpeak <phoenix@altlinux.org> 1.6.17-alt1
- New version

* Mon Oct 06 2003 Nazar Yurpeak <phoenix@altlinux.org> 1.6.15-alt2
- fixed BuildRequires
- fixed autobotchk script

* Tue May 06 2003 Nazar Yurpeak <phoenix@altlinux.ru> 1.6.15-alt1
- 1.6.15

* Sat Nov 23 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1.6.13-alt1
- new version
- fix URL
- clean %install

* Thu Oct 10 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1.6.12-alt3
- rebuild with tcl8.4.0
- remove aclocal.m4 patch

* Sat Aug 17 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1.6.12-alt2
- rebuild with gcc-3.2

* Tue Jul 30 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1.6.12-alt1
- new version

* Fri Jul 19 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1.6.10-alt3
- rebuild with gcc3.1
- fix spec

* Fri Jun 21 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1.6.10-alt1
- new version

* Wed Jun 20 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.6.4-alt1
- new version

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation

* Fri Nov 24 2000 Geoffrey Lee <sniltalk@mandrakesoft.com> 1.6.1-1mdk
- new and shiny source.
- fix the build for the new version.
- short_circuit_me_babe.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.4.4-2mdk
- automatically added BuildRequires

* Wed Jul 26 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.4-1mdk
- Release 1.4.4
- clean spec

* Wed Jul 26 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.4.3-2mdk
- BM + macroszification

* Wed Apr 19 2000 Daouda Lo <daouda@mandrakesoft.com> 1.4.3-1mdk
- big release 1.3.23 -> 1.4.3
- many bug fixes
- cleanup spec

* Tue Apr 18 2000 Daouda Lo <daouda@mandrakesoft.com> 1.3.23-5mdk
- fix group.
- spec cleanup.
- SMP build/check

* Thu Nov 04 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Forgot defattr

* Tue Nov 02 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Update bzip and SMP build macros
- Add botchk to docs

* Sat Jul 10 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- add default langfile patch
- Added a few posible optimizations i missed

* Fri Jul 9 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Initial rpm

