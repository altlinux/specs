# vim: set ft=spec: -*- rpm-spec -*-

# Wireshark has huge number of plugins that are not linked against most of the external libraries
# as they are loaded into wireshark/tshark processes which guarantee that linkage
%set_verify_elf_method unresolved=relaxed

Name: wireshark
Version: 1.6.8
Release: alt1

Summary: The BugTraq Award Winning Network Traffic Analyzer
Group: Monitoring
License: GPL
Url: http://www.wireshark.org/

Source: http://www.wireshark.org/download/src/%name-%version.tar
Source1: http://www.wireshark.org/download/docs/wsug_html_chunked.zip
Source2: %name.control

Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sun Dec 23 2007
BuildRequires: control doxygen flex gcc-c++ libadns-devel libcap-devel libcom_err-devel libgnutls-openssl-devel libgtk+2-devel libgcrypt-devel zlib-devel
BuildRequires: libkrb5-devel libpcap-devel libpcre-devel libportaudio2-devel libssl-devel python unzip xml-utils xsltproc liblua5-devel perl-Pod-Parser perl-devel

%package base
Summary: Wireshark base package
Group: Monitoring
Obsoletes: ethereal-libs < 0.10.10
Obsoletes: ethereal-base
Conflicts: libwiretap < %version-%release
Conflicts: libwiretap > %version-%release

%package gtk+
Summary: GTK+ GUI for Wireshark package
Group: Monitoring
Requires: %name-base = %version-%release
Provides: %name = %version-%release
Requires: url_handler
Obsoletes: ethereal
Obsoletes: ethereal-gtk+

%package -n tshark
Summary: Console GUI for Wireshark package
Group: Monitoring
Requires: %name-base = %version-%release
Obsoletes: tethereal

%package doc
Summary: Wireshark User's Guide
Group: Documentation
License: FDL
Conflicts: %name-base < %version-%release
Conflicts: %name-base > %version-%release
Obsoletes: ethereal-doc

%package -n libwiretap
Summary: A future replacement for libpcap
Group: System/Libraries

%package -n libwiretap-devel
Summary: Development environment for Wiretap library
Group: Development/C
Requires: libwiretap = %version-%release
Obsoletes: %name-devel

%description
Wireshark (formerly Ethereal) is a network protocol analyzer, or
"packet sniffer", that lets you capture and interactively browse
the contents of network frames. The goal of the project is to
create a commercial-quality packet analyzer for Unix, and the
most useful packet analyzer on any platform.

%description base
Wireshark (formerly Ethereal) is a network protocol analyzer, or
"packet sniffer", that lets you capture and interactively browse
the contents of network frames. The goal of the project is to
create a commercial-quality packet analyzer for Unix, and the
most useful packet analyzer on any platform.

This package lays base for libpcap, a packet capture and filtering
library, contains command-line utilities, plugins and documentation
for wireshark. A graphical user interface is packaged separately to
GTK+ package.

%description gtk+
This package contains GTK+ GUI ie. the wireshark -- application.

%description -n tshark
This package contains console wireshark application.

%description doc
Wireshark is one of those programs that many network managers
would love to be able to use, but they are often prevented from
getting what they would like from Wireshark because of the lack
of documentation.

This document is part of an effort by the Wireshark team to
improve the usability of Wireshark. 

%description -n libwiretap
Wiretap is a library that is being developed as a future replacement for
libpcap, the current standard Unix library for packet capturing.

%description -n libwiretap-devel
Wiretap is a library that is being developed as a future replacement for
libpcap, the current standard Unix library for packet capturing.

This package contains development files needed to develop wiretap-based
applications.

%prep
%setup -q
%__unzip -qa %_sourcedir/wsug_html_chunked.zip
%patch -p1

%build
%add_optflags -I%_includedir/pcre
./autogen.sh

export ac_cv_path_HTML_VIEWER=url_handler.sh
# Workaround for Lua 5.1 detection
export ac_cv_lib_lualib_luaL_openlib=no
%configure \
   --sysconfdir=%_sysconfdir/%name \
   --disable-static \
   --enable-shared \
   --disable-warnings-as-errors \
   \
   --enable-wireshark \
   --enable-gtk2 \
   --enable-tshark \
   --enable-editcap \
   --enable-capinfos \
   --enable-mergecap \
   --enable-text2pcap \
   --disable-idl2wrs \
   --enable-dftest \
   --enable-randpkt \
   --enable-dumpcap \
   --enable-rawshark \
   --enable-ipv6 \
   --disable-setuid-install \
   \
   --with-gnu-ld \
   --with-pic \
   --with-gnutls \
   --with-gcrypt \
   --without-libsmi \
   --with-pcap \
   --with-zlib \
   --with-pcre \
   --with-lua \
   --with-portaudio \
   --with-libcap \
   --with-ssl \
   --with-krb5 \
   --with-adns \
   --with-plugins=%_libdir/%name/plugins/%version \
   \
   CPPFLAGS="$CPPFLAGS -I%_includedir/pcre"
%make_build

%install
%make_install install DESTDIR=%buildroot
%__rm -f %buildroot%_libdir/%name/plugins/%version/*.la

%__mkdir_p %buildroot{%_controldir,%_menudir,%_datadir/applications,%_niconsdir,%_liconsdir,%_miconsdir}
%__cp -p wireshark.desktop %buildroot%_datadir/applications/%name.desktop
%__cp -p image/hi16-app-wireshark.png %buildroot%_miconsdir/wireshark.png
%__cp -p image/hi32-app-wireshark.png %buildroot%_niconsdir/wireshark.png
%__cp -p image/hi48-app-wireshark.png %buildroot%_liconsdir/wireshark.png

%__mkdir_p %buildroot%_includedir/wiretap
%__install -p -m644 wiretap/wtap.h %buildroot%_includedir/wiretap/wtap.h

%__install -p -m755 %_sourcedir/%name.control %buildroot%_controldir/%name-capture

%pre base
%pre_control %name-capture

%post base
%post_control -s relaxed %name-capture

%files base
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README* doc/README.*
%config %_controldir/%name-capture
%_bindir/capinfos
%_bindir/dftest
%attr(700,root,root) %verify(not mode,group) %_bindir/dumpcap
%_bindir/editcap
%_bindir/mergecap
%_bindir/randpkt
%_bindir/rawshark
%_bindir/text2pcap
%_man1dir/capinfos.*
%_man1dir/randpkt.*
%_man1dir/dftest.*
%_man1dir/dumpcap.*
%_man1dir/editcap.*
%_man1dir/mergecap.*
%_man1dir/rawshark.*
%_man1dir/text2pcap.*
%_man4dir/wireshark-filter.*
%_datadir/%name
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%dir %_libdir/%name/plugins/%version/
%_libdir/%name/plugins/%version/*
%_libdir/lib%name.so.*
%_libdir/libwsutil.so.*

%files gtk+
%_bindir/wireshark
%_man1dir/wireshark.*
%_datadir/applications/%name.desktop
%_miconsdir/wireshark.png
%_niconsdir/wireshark.png
%_liconsdir/wireshark.png

%files -n tshark
%_bindir/tshark
%_man1dir/tshark.*

%files doc
%doc wsug_html_chunked/*

%files -n libwiretap
%_libdir/libwiretap.so.*

%files -n libwiretap-devel
%_includedir/wiretap
%_libdir/libwiretap.so

%changelog
* Wed Jun 06 2012 Anton Farygin <rider@altlinux.ru> 1.6.8-alt1
- new version

* Fri Sep 16 2011 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- new version

* Thu Jun 09 2011 Anton Farygin <rider@altlinux.ru> 1.6.0-alt1
- new version

* Thu Mar 24 2011 Anton Farygin <rider@altlinux.ru> 1.4.4-alt2
- add zlib-devel requires

* Wed Mar 09 2011 Anton Farygin <rider@altlinux.ru> 1.4.4-alt1
- new version

* Wed Nov 24 2010 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- new version

* Thu Oct 14 2010 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- new version, fixed CVE-2010-3445 (closes: #24297)
- user guide updated

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- new version

* Fri Aug 20 2010 Anton Farygin <rider@altlinux.ru> 1.2.10-alt1
- new version

* Mon Jun 28 2010 Anton Farygin <rider@altlinux.ru> 1.2.9-alt1
- new version

* Thu Jan 28 2010 Anton Farygin <rider@altlinux.ru> 1.2.6-alt1
- new version, multiple vulnerabilities fixed by upstream (closes #20836)

* Fri Jun 19 2009 Alexander Bokovoy <ab@altlinux.org> 1.2.0-alt2
- Add LUA support for internal scripting
  -- Disabled by default, edit %_datadir/%name/init.lua to enable
- Include libwsutil.so.* into build

* Fri Jun 19 2009 Alexander Bokovoy <ab@altlinux.org> 1.2.0-alt1
- [1.2.0]

* Sat May 23 2009 Alexander Bokovoy <ab@altlinux.org> 1.0.8-alt1
- [1.0.8]
 + PCNFSD dissector crashes fixed, no proper CVE number yet

* Sun Apr 26 2009 Alexander Bokovoy <ab@altlinux.org> 1.0.7-alt1
- [1.0.7]
 + CVE-2009-1210
 + CVE-2009-1267
 + CVE-2009-1268
 + CVE-2009-1269

* Fri Oct 24 2008 Sir Raorn <raorn@altlinux.ru> 1.0.4-alt1
- [1.0.4]
 + CVE-2008-4685
 + CVE-2008-4684
 + CVE-2008-4683
 + CVE-2008-4682
 + CVE-2008-4681
 + CVE-2008-4680

* Fri Sep 05 2008 Sir Raorn <raorn@altlinux.ru> 1.0.3-alt1
- [1.0.3]
 + The NCP dissector was susceptible to a number of problems,
   including buffer overflows and an infinite loop.
 + Wireshark could crash while uncompressing zlib-compressed
   packet data.
 + Wireshark could crash while reading a Tektronix .rf5 file.

* Mon Jul 14 2008 Sir Raorn <raorn@altlinux.ru> 1.0.2-alt1
- [1.0.2]
 + Some crashes fixed before they were submitted to CVE list

* Wed Jul 02 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt1
- [1.0.1]
 + CVE-2008-1563
 + CVE-2008-1562  	
 + CVE-2008-1561

* Sun Mar 30 2008 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt1
- [1.0.0] (YAY!)
 + Some crashes fixed before they were submitted to CVE list
- User Guide updated

* Mon Mar 10 2008 Sir Raorn <raorn@altlinux.ru> 0.99.8-alt1
- [0.99.8]
 + CVE-2008-1072
 + CVE-2008-1071
 + CVE-2008-1070
- User Guide updated
- New tool rawshark(1)
- Traffic capture now control(8)led by %name-capture facility

* Sun Dec 23 2007 Sir Raorn <raorn@altlinux.ru> 0.99.7-alt1
- [0.99.7]
 + CVE-2007-6451
 + CVE-2007-6450
 + CVE-2007-6441
 + CVE-2007-6439
 + CVE-2007-6438
 + CVE-2007-6121
 + CVE-2007-6120
 + CVE-2007-6119
 + CVE-2007-6118
 + CVE-2007-6117
 + CVE-2007-6116
 + CVE-2007-6115
 + CVE-2007-6114
 + CVE-2007-6113
 + CVE-2007-6112
 + CVE-2007-6111
- Enabled kerberos, gcrypt and gnutls support
- Enabled RTP player for VoIP captures

* Tue Jul 10 2007 Sir Raorn <raorn@altlinux.ru> 0.99.6-alt2
- Use url_handler for default webbrowser (closes: #11692)

* Fri Jul 06 2007 Sir Raorn <raorn@altlinux.ru> 0.99.6-alt1
- [0.99.6]
 + CVE-2007-3389
 + CVE-2007-3390
 + CVE-2007-3391
 + CVE-2007-3392
 + CVE-2007-3393

* Sun Feb 04 2007 Sir Raorn <raorn@altlinux.ru> 0.99.5-alt1
- [0.99.5]
 + CVE-2007-0459
 + CVE-2007-0458
 + CVE-2007-0457
 + CVE-2007-0456
- User Guide updated

* Sat Nov 04 2006 Sir Raorn <raorn@altlinux.ru> 0.99.4-alt1
- [0.99.4]

* Tue Jul 18 2006 Sir Raorn <raorn@altlinux.ru> 0.99.2-alt1
- [0.99.2]
 + CVE-2006-3627
 + CVE-2006-3628
 + CVE-2006-3628
 + CVE-2006-3628
 + CVE-2006-3628
 + CVE-2006-3629
 + CVE-2006-3630
 + CVE-2006-3628
 + CVE-2006-3631
 + CVE-2006-3632
- Renaamed from ethereal to wireshark, added Obsoletes
- Rediffed all patches
- Updated buildrequires

* Wed Apr 26 2006 Sir Raorn <raorn@altlinux.ru> 0.99.0-alt1
- [0.99.0]
- User Guide updated

* Sun Mar 19 2006 Sir Raorn <raorn@altlinux.ru> 0.10.14-alt2
- libethereal should be linked with libadns and libm
- %%_iconsdir -> %%_niconsdir

* Wed Dec 28 2005 Sir Raorn <raorn@altlinux.ru> 0.10.14-alt1
- [0.10.14]

* Thu Oct 20 2005 Sir Raorn <raorn@altlinux.ru> 0.10.13-alt1
- [0.10.13]

* Mon Oct 10 2005 Sir Raorn <raorn@altlinux.ru> 0.10.12-alt2
- Fix unexpanded macros
- Changed -doc group to Documentation

* Sat Jul 30 2005 Sir Raorn <raorn@altlinux.ru> 0.10.12-alt1
- [0.10.12]
- Updated EUG
- Added patches from debian:
  + diameter_vendors
  + drop-capabilities
  + giop-buffer

* Tue May 10 2005 Sir Raorn <raorn@altlinux.ru> 0.10.11-alt1
- [0.10.11]

* Tue Mar 15 2005 Sir Raorn <raorn@altlinux.ru> 0.10.10-alt1
- [0.10.10]
- Fixed:
   + CAN-2005-0699
   + CAN-2005-0704
   + CAN-2005-0705
- ethereal-devel and idl2eth are unusable.  Dropped
- libwiretap is back

* Sat Jan 22 2005 Sir Raorn <raorn@altlinux.ru> 0.10.9-alt1
- [0.10.9]
- Fixed:
   + CAN-2004-1139
   + CAN-2004-1140
   + CAN-2004-1141
   + CAN-2004-1142
   + CAN-2005-0006
   + CAN-2005-0007
   + CAN-2005-0008
   + CAN-2005-0009
   + CAN-2005-0010
   + CAN-2005-0084
- Debian fixes:
  * Fixed dissect_cmip_InvokeIDType declaration (FTBFS with gcc-4.0)
  * epan/dissectors/packet-giop.c: fixed segfault with some GIOP packets
  * ethereal_gen.py: fixed some includes
- ALT fixes (based on Debian):
  * epan/prefs.c: changed default font to "Fixed 11"
  * epan/prefs.c: Use url_handler.sh as default browser
- Removed -kde subpackage (obsoleted by -gtk+) (closes: #5859)
- Removed -consolehelper subpackage.  Running ethereal with root privileges
  is insecure, do it at your own risc (closes: #3520)
- Added menu entry and icons (closes: #5006)
- SNMP support disabled due to overbloated dependencies
- Separated -libs and -devel. Header files list borrowed from Debian
- libwiretap-devel is now obsoleted by ethereal-devel
- Packaged idl2eth utility (idl2eth package)

* Fri Sep 03 2004 Sir Raorn <raorn@altlinux.ru> 0.10.6-alt1
- [0.10.6]
- Moved libwiretap to seperate subpackage
- Added libwiretap-devel
- Added EUG (in -doc subpackage)

* Thu Jul 08 2004 Stanislav Ievlev <inger@altlinux.org> 0.10.5-alt1
- 1.10.5

* Sat May 15 2004 Alexander Bokovoy <ab@altlinux.ru> 0.10.4-alt1
- 0.10.4

* Fri Apr 02 2004 Alexander Bokovoy <ab@altlinux.ru> 0.10.3-alt2
- Fixed:
   + Some libraries were missing

* Thu Apr 01 2004 Alexander Bokovoy <ab@altlinux.ru> 0.10.3-alt1
- 0.10.3
- Removed:
   + %name-gnome subpackage (outdated and non-usable anymore)

* Tue Feb 24 2004 Alexander Bokovoy <ab@altlinux.ru> 0.10.2-alt1
- 0.10.2
- Removed:
   + Stock icons (added into the release tarball finally)
   + Makefile patch
- Added:
   + mergecap, idl2eth, text2pcap and their man-pages
   + man page for ethereal-filter

* Fri Feb 20 2004 Alexander Bokovoy <ab@altlinux.ru> 0.10.1-alt1
- 0.10.1 
- Fixed:
   + Wrong dependencies between makefiles
- Added:
   + Missing stock GTK+ 2.2.4 icons used by Ethereal

* Thu Nov 06 2003 Alexander Bokovoy <ab@altlinux.ru> 0.9.16-alt1
- 0.9.16
- Fixed:
   + CAN-2003-0925
   + CAN-2003-0926
   + CAN-2003-0927
- Added:
   + --enable Master switch allows to build this package for 
     ALT Linux Master 2.2
   + Build GTK+ 2.x frontend instead of GTK+ 1.x
- Updated:
   + PAM entry to follow current PAM policy in ALT Linux Sisyphus

* Tue Jun 17 2003 Alexander Bokovoy <ab@altlinux.ru> 0.9.13-alt1
- Updated to 0.9.13, fixes a number of vulnerabilities.
- Added plugins path to findprov lib path

* Tue Mar 11 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.11-alt1
- Updated to 0.9.11:
  "This release fixes  the packaging, and adds minor updates
  and fixes for the following protocols:
  AFS, OpenBSD enc(4), RTP, SCSI, SIP, SMPP, SSH
  IA64 support has been improved."

* Mon Mar 10 2003 Alexander Bokovoy <ab@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Mon Dec 09 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Tue Oct 01 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.7-alt1
- New version
- Fixed:
    + Usermode bindings fixed
    + %name-usermode name is changed to %name-consolehelper

* Wed Aug 21 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.6-alt1
- Security update [CAN-2002-0834]
- Group changed to Monitoring

* Thu Apr 18 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.3-alt1
- Security update

* Wed Jan 23 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.0-alt1
- First build for ALT Linux

* Mon Jan 07 2002 Henri Gomez <hgomez@slib.fr>
- 0.9.0
- built on Redhat 6.2 + updates
- Too many updates to report here, take a look in NEWS

* Tue Oct 23 2001 Henri Gomez <hgomez@slib.fr>
- 0.8.20

* Thu Jul 20 2001 Henri Gomez <hgomez@slib.fr>
- 0.8.19
- RPM built on Redhat 6.2, updates, rpm 3.0.5 and ucd-snmpd 4.2
  against libpcap 0.6.2 (tcpdump 3.6.2) and openssl 0.9.6

* Thu May 17 2001 Henri Gomez <hgomez@slib.fr>
- 0.8.18
- Many improvement, take a look at NEWS in %%doc
- Reduced the changelog history in .spec

* Thu Apr 26 2001 Henri Gomez <hgomez@slib.fr>
- rebuilt under Redhat 6.2 + updates
- reverted from rpm 4.0.2 to 3.0.5 for better compatibility with Redhat 6.x
- thanks Riku for the great refactory of the spec

* Thu Apr 26 2001 Riku Meskanen <mesrik@iki.fi>
- new binary package rearrangement, separated stuff that needs X11
- I changed, and I'm proposing group to Applications/Network for now ... as
  the /usr/share/doc/rpm-*/GROUPS 'official' list does not have appropriate
  group for networking applications and leads them to be scattered around.
  The tcpdump is now at System/Internet and nmap from Applications/System,
  the X11/* group is now on current distros mostly dead ... the X11/* tree
  seems to still live on contrib packages. Well if it's necessary to show X11
  in group-name, I would rather suggest then Applications/Network{,ing}/X11
  would make more sense and keep all applications closer together and all
  it's bits and bobs easier locatable on multiple packages are built from
  one source package.

* Mon Apr 23 2001 Riku Meskanen <mesrik@iki.fi>
- rebuilt for RedHat 7.1
- created support for usermode
- added icons & config files for gnome and kde desktop integration
- added %%dir %%_libdir/ethereal/plugins to get clean uninstall
- further spec file minor cleaning, converted absolute paths to
  macros for better relocatability

* Sun Apr 16 2001  Henri Gomez <hgomez@slib.fr>
- 0.8.17 (grabbed corrected 0.8.17a archive)
- RPM built on Redhat 6.2, updates, rpm 4.0

* Tue Mar 06 2001 Henri Gomez <hgomez@slib.fr>
- 0.8.16
- RPM built on Redhat 6.1, updates, rpm 3.0.5 and libpcap-0.4-19
- ucd-snmp used 0.4.2-5 (added -lcrypto)

