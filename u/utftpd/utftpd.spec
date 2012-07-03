Name: utftpd
Version: 0.2.4
Release: alt2
Packager: Sergey Y. Afonin <asy@altlinux.ru>

Summary: utftpd - Enhanced TFTP server
License: GPL
Group: System/Servers
Url: http://www.ohse.de/uwe/software/utftpd.html
Source0: ftp://ftp.ohse.de/uwe/releases/%name-%version.tar.gz
Source1: %name-xinetd-udp
Source2: %name.conf
Source3: %{name}_makeconfig
Source4: %name-altlinux.readme

Source10: %name.changelog.pld

Conflicts: tftp-server

%description
utftpd is a server for the trivial file transfer protocol (TFTP) with
finer grained access control then the standard UNIX tftpd.

Description with the features GNU utftpd has:
 - support for IP based access control. utftpd can assign the right to
   read, create or overwrite a file (or files in a directory) on a
   per-host base.
 - support for revision control. utftpd can checkin/out files under
   SCCS (Source Code Control System) or RCS (Revision Control System) 
   version control. This was one of the main reasons to write it: version 
   control is the easiest way to restore the configuration our IP routers 
   (Ascends, Ciscos) had yesterday or some weeks ago. This is, of course, 
   optional.
 - support for the blksize option (RFC 2348). Allows packets larger
   than the usual 512 bytes, and is _somewhat_ more efficient (especially
   on a directly connected network).
 - support for the timeout option (RFC 2349) No support for the tsize
   option of RFC 2349 now.

%package client
Summary: utftpd - a TFTP client
Group: Networking/File transfer
Conflicts: tftp

%description client
utftp - TFTP client of utftpd 

%prep
%setup -q

%__sed -e 's|@@SYSCONFDIR@@|%_sysconfdir|' < %SOURCE4 > %_builddir/%name-%version/AltLinux.readme

%build
%configure
%make_build

%install
%__install -d $RPM_BUILD_ROOT/{%_sysconfdir/xinetd.d,%_localstatedir/tftp}

%make_install install DESTDIR=$RPM_BUILD_ROOT

%__install -p -m 640 %SOURCE1 $RPM_BUILD_ROOT%_sysconfdir/xinetd.d/utftpd-udp
%__install -p -m 640 %SOURCE2 $RPM_BUILD_ROOT%_sysconfdir/utftpd.conf

%__sed -e 's|@@SYSCONFDIR@@|%_sysconfdir|' < %SOURCE3 > $RPM_BUILD_ROOT%_sbindir/utftpd_makeconfig
%__chmod 700 $RPM_BUILD_ROOT%_sbindir/utftpd_makeconfig

touch $RPM_BUILD_ROOT%_sysconfdir/{utftpd.cdb,utftpd.tmp}

%pre
/usr/sbin/groupadd -rf tftp
/usr/sbin/useradd -r -g tftp -d /dev/null -s /dev/null -n tftp &>/dev/null ||:

%files
%ghost %_sysconfdir/utftpd.cdb
%ghost %_sysconfdir/utftpd.tmp
%_sbindir/utftpd
%_sbindir/utftpd_*
%dir %attr(1770,root,tftp) %_localstatedir/tftp
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/utftpd.conf
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/xinetd.d/utftpd-udp
%_mandir/man5/utftpd*.5*
%_mandir/man8/utftpd*.8*
%doc AUTHORS ChangeLog NEWS README README.cvs sample.config AltLinux.readme

%files client
%_bindir/utftp
%_mandir/man1/utftp.1*

%changelog
* Tue Jan 10 2006 Sergey Y. Afonin <asy@altlinux.ru> 0.2.4-alt2
- fix: set sticky bit to /var/lib/tftp
- change: move changelog of PLD package to utftpd.changelog.pld
  for resolve build error "unprintable package information".
  The file is not add to binary packages.

* Thu Apr 01 2004 Sergey Y. Afonin <asy@altlinux.ru> 0.2.4-alt1
- remove PL comments
- add utftpd_makeconfig script
- more changes in "utftpd.spec" for ALT Linux
- chroot after starting
- add small qui”k start documentation "altlinux.readme"

* Wed Jan 13 2004 asy 0.2.4-asy
- initial changes in spec-file of PLD Linux (Revision 1.53  2002/11/22 08:12:06  kloczek) 
  for ALT Linux Sisyphus (20040106):
- change inetd config to xinetd config
