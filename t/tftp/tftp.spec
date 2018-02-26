%def_enable largefile
%def_with tcpwrappers
%def_with remap
%def_with readline
%def_with ipv6

Name: tftp
%define dname %{name}d
Version: 5.0
Release: alt4
Summary: The client for the Trivial File Transfer Protocol (TFTP)
License: BSD
Group: Networking/File transfer
URL: http://www.kernel.org/pub/software/network/%name
Source0: %url/%name-hpa-%version.tar
Source1: %name.xinetd.in
Source2: %dname.init.in
Source3: %dname.sysconfig.in
Patch: %name-%version-%release.patch
%define sys_user %name
%define sys_group %name
%define bootdir %_localstatedir/%{name}boot
Packager: Led <led@altlinux.ru>

%{?_with_tcpwrappers:BuildRequires: libwrap-devel}
%{?_with_readline:BuildRequires: libreadline-devel}

%description
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations. This package provides the user interface
for TFTP, which allows users to transfer files to and from a remote
machine. This program, and TFTP, provide very little security, and
should not be enabled unless it is expressly needed.


%package -n %{name}d
Summary: The server for the Trivial File Transfer Protocol (TFTP)
Group: System/Servers
Provides: %name-server-common = %version-%release
Conflicts: %name-server < 5.0-alt1

%description -n %{name}d
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations. This package provides the server for
TFTP, which allows users to transfer files to and from a remote
machine. TFTP provides very little security, and should not be enabled
unless it is expressly needed.


%package server-standalone
Summary: The server for the Trivial File Transfer Protocol (TFTP) - standalone mode
Group: System/Servers
BuildArch: noarch
Requires: %{name}d >= 0.49-alt1
Conflicts: %name-server = 0.49-alt1

%description server-standalone
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations. This package provides the server for
TFTP, which allows users to transfer files to and from a remote
machine. TFTP provides very little security, and should not be enabled
unless it is expressly needed.
This package provides script for run TFTP server in standalone mode
with /sbin/service, disabled by default on a ALT Linux systems.


%package server-xinetd
Summary: The server for the Trivial File Transfer Protocol (TFTP) - xinetd mode
Group: System/Servers
Provides: %name-server = %version-%release
Obsoletes: %name-server < %version-%release
BuildArch: noarch
Requires: %{name}d
Conflicts: %name-server < 5.0-alt1

%description server-xinetd
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations. This package provides the server for
TFTP, which allows users to transfer files to and from a remote
machine. TFTP provides very little security, and should not be enabled
unless it is expressly needed.
This package provides script for run TFTP server via xinetd, disabled
by default on a ALT Linux systems.


%package doc
Summary: Documentation for TFTP server and client
Group: Documentation
BuildArch: noarch

%description doc
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations.
This package provides documentation for TFTP client and server.


%prep
%setup -n %name-hpa-%version
%patch -p1
install -m 0644 %SOURCE1 ./%name.xinetd.in
install -m 0644 %SOURCE2 ./%dname.init.in
install -m 0644 %SOURCE3 ./%dname.sysconfig.in


%build
%define _optlevel s
%autoreconf
%configure \
    %{subst_enable largefile} \
    %{subst_with tcpwrappers} \
    %{subst_with remap} \
    %{subst_with readline} \
    %{subst_with ipv6}

%make_build

for f in %name.xinetd %dname.sysconfig %dname.init; do
    sed 's|@USER@|%sys_user|g;s|@BOOTDIR@|%bootdir|g' $f.in > $f
done

bzip2 --best --keep --force CHANGES


%install
%make_install INSTALLROOT=%buildroot install
ln -sf {in.,%buildroot%_sbindir/}%dname
install -D -m 0640 %name.xinetd %buildroot%_sysconfdir/xinetd.d/%name
install -D -m 0644 %dname.sysconfig %buildroot%_sysconfdir/sysconfig/%dname
install -D -m 0755 %dname.init %buildroot%_initdir/%dname
install -d -m 0755 %buildroot{%bootdir,%_docdir/%name-%version}
install -m 0644 CHANGES.* README* %buildroot%_docdir/%name-%version/


%post -n %{name}d
%_sbindir/groupadd -rf %sys_group ||:
%_sbindir/useradd -r -g %sys_group -d /dev/null -s /dev/null -n %sys_user &>/dev/null ||:

%post server-standalone
%post_service %dname ||:

%preun server-standalone
%preun_service %dname ||:


%files
%_bindir/*
%_man1dir/*


%files -n %{name}d
%_sbindir/*
%_man8dir/*
%dir %bootdir


%files server-standalone
%config(noreplace) %_sysconfdir/sysconfig/*
%_initdir/*


%files server-xinetd
%config(noreplace) %_sysconfdir/xinetd.d/*


%files doc
%_docdir/%name-%version


%changelog
* Wed Jul 27 2011 Damir Shayhutdinov <damir@altlinux.ru> 5.0-alt4
- Fixed possible buffer overflow, and compiler warning about
  buffer overflow (Closes: #25954)

* Tue Jun 14 2011 Damir Shayhutdinov <damir@altlinux.ru> 5.0-alt3
- Fix buffer overflow in utimeout option (CVE 2011-2199, closes #25753)

* Mon Feb 01 2010 Led <led@altlinux.ru> 5.0-alt2
- fixed start standalone in system without IPv6 support

* Mon Mar 02 2009 Led <led@altlinux.ru> 5.0-alt1
- 5.0:
  + Implement the "rollover" option, for clients which want block
    number to rollover to anything other than zero
  + Correctly disable PMTU in standalone mode
- added subpackages %{name}d, %name-server-xinetd (instead %name-server),
  %name-server-standalone

* Sun Feb 01 2009 Led <led@altlinux.ru> 0.49-alt1
- 0.49
- cleaned up spec
- fixed Group
- added init script for standalone mode
- %name: print newline during quit by Ctrl+D

* Fri Feb 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.48-alt1
- new version

* Mon Feb 20 2006 Anton Farygin <rider@altlinux.ru> 0.42-alt1
- new version

* Mon Jan 16 2006 Anton Farygin <rider@altlinux.ru> 0.41-alt1
- new version

* Mon Jun 27 2005 Anton Farygin <rider@altlinux.ru> 0.40-alt2
- summary fixed (#5597)

* Thu Oct 28 2004 Anton Farygin <rider@altlinux.ru> 0.36-alt2
- fixed possible remote buffer overflows

* Fri Apr 23 2004 Anton Farygin <rider@altlinux.ru> 0.36-alt1
- new version (0.36)

* Sun May 04 2003 Rider <rider@altlinux.ru> 0.33-alt1
- new version

* Sun Nov 10 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.29-alt3
- Rebuilt with new shared libwrap
- Updated buildrequires

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.29-alt2
- Added malta patch from RH
- Rebuilt in new environment
- Moved /tftpboot to /var/lib/tftpboot

* Mon Jun 17 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.29-alt1
- 0.29
- Removed netkit client

* Fri Dec 07 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.17-ipl4mdk
- Changed xinet.d config file

* Wed Dec 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.17-ipl3mdk
- Rebuild for Sisyphus
- New version of hpa (0.20)
- Added patch from Mandrake
- Some spec cleanup
- Added optimization

* Thu Oct 19 2000 Dmitry V. Levin <ldv@fandra.org> 0.17-ipl2mdk
- RE adaptions.

* Sat Sep 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.17-2mdk
- Add hpa version of tftp.
- Add xinetd support.
- Split server and client.

* Fri Aug 04 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.17-1mdk
- rebuild with shiny new version
- _sbindir_ macro

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.16-3mdk
- macros, BM, _spechelper_

* Mon Apr 17 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 0.16-2mdk
- fix changelog, blame me not Chris Molnar for damage...

* Mon Apr 17 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 0.16-1mdk
- version 0.16
- fixed Source URL
- added documentation

* Mon Apr 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.15-2mdk
- Fixed groups

* Sat Nov 06 1999 John Buswell <johnb@mandrakesoft.com>
- 0.15
- Removed version dependencies from spec file
- Build Release

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Wed Apr  7 1999 Jeff Johnson <jbj@redhat.com>
- tftpd should truncate file when overwriting (#412)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added check for getpwnam() failure

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
