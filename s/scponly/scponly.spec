Name: scponly
Version: 4.8
Release: alt2

Summary: Limited shell for secure file transfers
License: GPL
Group: Networking/Remote access
Url: http://sublimation.org/%name
Source: http://prdownloads.sourceforge.net/%name/%name-%version.tgz
Patch0: scponly-install.patch
Patch1: scponly-4.8-elif-gcc44.patch

Summary(ru_RU.KOI8-R): Усечённый интерпретатор команд для удалённого доступа через scp/sftp/rsync/...
Packager: Ilya Mashkin <oddity@altlinux.ru>
%define shell_list        %_sysconfdir/shells
%define sftp_server_path  %_libexecdir/openssh/sftp-server

%def_enable  restrictive_names
%def_enable  wildcards
%def_enable  gftp_compat
%def_enable  winscp_compat
%def_enable  scp_compat
%def_enable  unison_compat
%def_enable  rsync_compat
%def_enable  chrooted_binary
%def_enable  svn_compat
%def_enable  svnserv_compat
%def_enable  passwd_compat

%define tr_() %(echo '%*' | tr -- '_' '-')

%define se_restrictive_names %{subst_enable restrictive_names}
%define se_gftp_compat       %{subst_enable gftp_compat}
%define se_winscp_compat     %{subst_enable winscp_compat}
%define se_scp_compat        %{subst_enable scp_compat}
%define se_unison_compat     %{subst_enable unison_compat}
%define se_rsync_compat      %{subst_enable rsync_compat}
%define se_chrooted_binary   %{subst_enable chrooted_binary}
%define se_svn_compat        %{subst_enable svn_compat}
%define se_svnserv_compat    %{subst_enable svnserv_compat}
%define se_passwd_compat     %{subst_enable passwd_compat}

%description
"scponly" is an alternative "shell" (of sorts) for system administrators
who would like to provide access to remote users to both read and write
local files without providing any remote execution privileges. Functionally,
it is best described as a wrapper to the tried-and-true ssh suite.

scponly validates remote requests by examining the third argument passed
to the shell upon login (the first argument is the shell itself, and the second
is "-c").  The only commands allowed are "scp", "sftp-server" and "ls". 
Arguments to these commands are passed along unmolested.

Some features are:
- compatibility with sftp, WinSCP 2.0/3.0, gftp, rsync, Unison, Subversion.
- chroot: scponly can chroot to the user's home directory
  (or any other directory the user has permissions for),
  disallowing access to the rest of the filesystem.
- logging: scponly logs time, client IP address, username,
  and the actual request to syslog.

%description -l ru_RU.KOI8-R
"scponly" является интепретатором командной строки (т.н. shell).
Его следует назначать пользователям, которым нужно удалённо читать
и писать файлы через SFTP/SCP (протокол для передачи файлов с компьютера
на компьютер через SSH), но без права запуска команд на удалённом сервере
(главное назначение SSH). Схожей цели служит псевдо-шелл ftponly,
назначаемый пользователям, работающим с файлами на сервере через FTP.

Ключевые возможности:
- совместимость с sftp, WinSCP, gftp, rsync, Unison, Subversion,
- смена корневого каталога (chroot) для предотвращения доступа
  за пределы домашнего каталога пользователя,
- детальное протоколирование выполняемых действий через syslog.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%__cp -p Makefile.in Makefile.in.orig
%__subst 's,${INSTALL} -o 0 -g 0,${INSTALL},' Makefile.in

%build

%configure --with-sftp-server=%sftp_server_path \
	scponly_PROG_PASSWD=%_bindir/passwd     \
	scponly_PROG_USERADD=%_sbindir/useradd  \
	scponly_PROG_UNISON=%_bindir/unison     \
	scponly_PROG_RSYNC=%_bindir/rsync       \
	scponly_PROG_SVNSERV=%_bindir/svnserve  \
	scponly_PROG_SVN=%_bindir/svn           \
	scponly_PROG_SCP=%_bindir/scp           \
	scponly_PROG_SFTP_SERVER=%_libexecdir/openssh/sftp-server \
	%{subst_enable wildcards}  \
	%tr_ %se_gftp_compat   %se_winscp_compat  %se_scp_compat      \
	%tr_ %se_unison_compat %se_rsync_compat   %se_chrooted_binary \
	%tr_ %se_svn_compat    %se_svnserv_compat %se_passwd_compat   \
	%tr_ %se_restrictive_names

# Presented on any system by default (even in hasher) and assigned implicitly..
#	scponly_PROG_LS
#	scponly_PROG_RM
#	scponly_PROG_LN
#	scponly_PROG_MV
#	scponly_PROG_CHMOD
#	scponly_PROG_CHOWN
#	scponly_PROG_CHGRP
#	scponly_PROG_MKDIR
#	scponly_PROG_RMDIR
#	scponly_PROG_PWD
#	scponly_PROG_GROUPS
#	scponly_PROG_ID
#	scponly_PROG_ECHO

%make_build

%install
%makeinstall CONFDIR=%buildroot%_sysconfdir/%name

%post
for f in \
    %_bindir/%name \
%if_enabled chrooted_binary
    %_sbindir/%{name}c \
%endif
; do
    %__grep -q "^$f\$" %shell_list && continue
    echo $f >> %shell_list
done

%preun
for f in \
    %_bindir/%name \
%if_enabled chrooted_binary
    %_sbindir/%{name}c \
%endif
; do
    %__grep -q "^$f\$" %shell_list || continue
    %__grep -v "^$f\$" %shell_list > %shell_list.uninstall_%name
    %__cat %shell_list.uninstall_%name > %shell_list
    %__rm -f %shell_list.uninstall_%name
done

%files
%_bindir/%name
%if_enabled chrooted_binary
%_sbindir/%{name}c
%endif
%_sysconfdir/%name
%_man8dir/%name.*
%doc AUTHOR BUILDING-JAILS.TXT CHANGELOG CONTRIB COPYING README TODO build_extras/setup_chroot.sh.RH9

%changelog
* Sun Jul 19 2009 Ilya Mashkin <oddity@altlinux.ru> 4.8-alt2
- fix build with gcc
- Add patch to prevent restriction bypass using OpenSSH's scp options -F
  and -o (CVE-2007-6415)

* Tue Feb  5 2008 Ilya G. Evseev <evseev@altlinux.ru> 4.8-alt1
- Updated to new version 4.8, fixes CVE-2007-6415 problem
- Change source URL to SourceForge

* Wed Feb  1 2006 Ilya G. Evseev <evseev@altlinux.ru> 4.6-alt1
- Updated to new version 4.6, containing all previous patches

* Mon Jan  9 2006 Ilya G. Evseev <evseev@altlinux.ru> 4.3-alt2
- Added patch for working Unison in chrooted environment:
  https://lists.ccs.neu.edu/pipermail/scponly/2006-January/001071.html
- Added (but not applied) obsoleted patch for working WinSCP in SCP mode:
  https://lists.ccs.neu.edu/pipermail/scponly/2005-December/001029.html

* Fri Dec 30 2005 Ilya G. Evseev <evseev@altlinux.ru> 4.3-alt1
- Updated to new version 4.3 with critical security fixes
- Apply patch from http://bugs.gentoo.org/show_bug.cgi?id=116526

* Wed Nov 16 2005 Ilya G. Evseev <evseev@altlinux.ru> 4.1-alt1
- Initial build for ALTLinux

## EOF ##
