Name: tkabber
Version: 0.11.1
Release: alt4

Summary: Tkabber is an open source Jabber Client.
License: GPL
Group: Networking/Instant messaging
Url: http://tkabber.jabber.ru/ru/

BuildArch: noarch
BuildRequires(pre): rpm-build-tcl >= 0.2.1-alt2
BuildRequires: cpio tcl

Requires: tcl-gpg tcl-udp tcl-tksystray >= 0.2
Conflicts: tkabber-plugins < 0.11.1-alt2

Source0: %name-%version-%release.tar

%description
Tkabber provides a Tcl/Tk interface to the Jabber instant messaging
and presence service.
Wtiting in Tcl/Tk, used TclLib and BWidget, working on Linux, FreeBSD,
NetBSD, Solaris and Windows 98/2000/XP.

%prep
%setup
sed -i 's,@version@,%version-%release,' tkabber.tcl

%install
mkdir -p %buildroot%_bindir %buildroot%_datadir/%name
cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
#\\
exec wish "\$0" -name %name "\$@"
set ::env(TKABBER_SITE_PLUGINS) %_datadir/%name-plugins
source %_datadir/%name/%name.tcl

EOF
chmod +x %buildroot%_bindir/%name

(cd altlinux && find . -type f |cpio -pmd %buildroot%_datadir)
find . -type f -not '(' -name \*..\* \
    -o -name tkabber.spec \
    -o -regex \./\\..\+ \
    -o -regex \./altlinux/.\+ \
    -o -regex \./\[A-Z\]\[^/\.\]\+ \
    -o -regex \./doc/.\+ \
    -o -regex \./contrib/.\+ \
    -o -regex \./examples/.\+ ')' | cpio -pmd %buildroot%_datadir/%name

gzip -9nf ChangeLog

%files
%doc INSTALL ChangeLog.* COPYING README doc/* contrib examples 
%_bindir/%name
%_datadir/%name
%_liconsdir/*
%_miconsdir/*
%_niconsdir/*
%_desktopdir/%name.desktop

%changelog
* Mon Dec 27 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.1-alt4
- updated to svn rev.1974

* Fri Aug 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.1-alt3
- updated to svn rev.1835

* Thu Jan 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.1-alt2
- updated to svn rev.1633

* Fri Oct 17 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.1-alt1
- 0.11.1 released

* Sun Jun  8 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt1
- 0.11.0 released

* Fri May 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt0.1
- svn rev.1445

* Sat Feb 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt0.3
- svn rev.1377
- switch to tDom xml parser

* Thu Nov  1 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt0.2
- updated to svn rev.1295, near 0.10.1beta2 release

* Fri Oct 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt3
- rebuilt according to recent rpm-build-tcl changes
- updated to svn rev.1276

* Sun Aug  5 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt2
- updated to svn rev.1171

* Thu Apr 12 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt1
- 0.10.0 released

* Wed Mar  7 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt0.2
- updated to svn rev.1023, near 0.10.0beta2 release

* Sat Feb 24 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt0.1
- updated to svn rev.968, near 0.10.0beta1 release

* Sat Dec 23 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9-alt4
- updated to svn rev.833

* Sun Nov 12 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9-alt3
- updated to svn rev.792
- patches rebased & applied:
  + tkabber-0.9.9-alt-ext-xml.patch
  + tkabber-0.9.9-alt-md5clash.patch
  + tkabber-0.9.9-alt-findreq.patch
  + tkabber-0.9.9-alt-systray.patch

* Thu Jul 13 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9-alt2
- fixed build on x86_64

* Sun Jul  2 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9-alt1
- 0.9.9 released

* Thu Aug 25 2005 Sergey Kalinin  <banzaj@altlinux.ru> 0.9.8-alt1
- initial release

* Wed Jul  6 2005 Sergey Kalinin  <banzaj@altlinux.ru> 0.9.7-alt3
- setting "ssj::options(one-passphrase) 1"

* Fri Aug  6 2004 Sergey Kalinin  <banzaj@altlinux.ru> 0.9.7-alt2
- URL view in $BROWSER fix
- conrib and examles moved in %_defaultdocdir

* Thu Jul 29 2004 Sergey Kalinin  <banzaj@altlinux.ru> 0.9.7-alt1
- Updated support for file transfer (JEP-0095, JEP-0096, JEP-0047, JEP-0065)
- Support for colored nicks and messages in conference
- Better multiple logins support
- Updated support for xml:lang
- Support for IDNA (RFC3490)
- Many fixes and enhancements
				     
* Wed Feb 25 2004 Sergey Kalinin  <banzaj@altlinux.ru> 0.9.6beta-alt3
- url_handler support

* Thu Oct 23 2003 Sergey Kalinin  <banzaj@altlinux.ru> 0.9.6beta-alt2
- BROWSER variable setting

* Thu Oct 23 2003 Sergey Kalinin  <banzaj@altlinux.ru> 0.9.6beta-alt1
- Multiple logins support
- History now splitted by month
- Animated emoteicons support
- Many user interface improvements
- More XMPP support
- More translations
- Bugfixes 

