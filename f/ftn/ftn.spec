Name: ftn
Version: 2.2
Release: alt5

Summary: The basic directory layout for FTN system
License: Public Domain
Group: System/Base

BuildArch: noarch
Obsoletes: fidonet
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>

%description
This is the core of FTN system. This package contains the basic
directory layout for FTN system, including the correct permissions
for the directories.

%prep
%install
# Configuration files
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_localstatedir/%name
# Flags and semaphores
mkdir -p %buildroot%_localstatedir/%name/flags
mkdir -p %buildroot%_localstatedir/%name/files
# Fileechoes (should't it be somewhere in /var/ftp/pub?)
mkdir -p %buildroot%_localstatedir/%name/files/public
# Passtrough Fileechoes
mkdir -p %buildroot%_localstatedir/%name/files/passthr
# Fileecho dupes
mkdir -p %buildroot%_localstatedir/%name/files/dupes
# this is fechoprocessor-specific
mkdir -p %buildroot%_localstatedir/%name/files/magic
mkdir -p %buildroot%_localstatedir/%name/mail
# FTS-0001 netmail
mkdir -p %buildroot%_localstatedir/%name/mail/NETMAIL
# Echomail messagebases
mkdir -p %buildroot%_localstatedir/%name/mail/echo
# Local messagebases
mkdir -p %buildroot%_localstatedir/%name/mail/local
# Nodelists
mkdir -p %buildroot%_localstatedir/%name/nodelist
# TMPDIR
mkdir -p %buildroot%_localstatedir/%name/tmp
# Logs
mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_spooldir/%name
# Insecure inbound
mkdir -p %buildroot%_spooldir/%name/in
# Local inbound
mkdir -p %buildroot%_spooldir/%name/in/local
# Secure inbound
mkdir -p %buildroot%_spooldir/%name/in/secure
# Temp inbound
mkdir -p %buildroot%_spooldir/%name/in/temp
mkdir -p %buildroot%_spooldir/%name/out
# Amiga-style outbound
mkdir -p %buildroot%_spooldir/%name/out/aso
# Fileechoes (passthrough files)
mkdir -p %buildroot%_spooldir/%name/out/files
# Long-boxes
mkdir -p %buildroot%_spooldir/%name/out/longbox
# Temp outbound
mkdir -p %buildroot%_spooldir/%name/out/temp
# Bink-style outbound
mkdir -p %buildroot%_spooldir/%name/out/zone

# ~ftn/.i18n - no cyrillic mess in logs (overridable)
cat <<__EOF > %buildroot%_localstatedir/%name/.i18n
LANGUAGE=POSIX
LANG=POSIX
LC_ALL=POSIX
LINGUAS=POSIX
__EOF

%pre
/usr/sbin/groupadd -r -f %name ||:
/usr/sbin/useradd -r -g %name -G uucp -M -d %_localstatedir/%name -s /bin/sh -n %name &>/dev/null ||:

%files
%defattr(644,root,%name,750)
%dir %attr(750,%name,%name) %_sysconfdir/%name
%config(noreplace) %_localstatedir/%name/.i18n
%dir %_localstatedir/%name
%dir %attr(3730,%name,%name) %_localstatedir/%name/flags
%dir %_localstatedir/%name/files
%dir %attr(750,%name,%name) %_localstatedir/%name/files/public
%dir %attr(750,%name,%name) %_localstatedir/%name/files/passthr
%dir %attr(750,%name,%name) %_localstatedir/%name/files/dupes
%dir %attr(750,%name,%name) %_localstatedir/%name/files/magic
%dir %_localstatedir/%name/mail
%dir %attr(3770,%name,%name) %_localstatedir/%name/mail/NETMAIL
%dir %attr(750,%name,%name) %_localstatedir/%name/mail/echo
%dir %attr(750,%name,%name) %_localstatedir/%name/mail/local
%dir %attr(750,%name,%name) %_localstatedir/%name/nodelist
%dir %attr(700,%name,%name) %_localstatedir/%name/tmp
%dir %_logdir/%name
%dir %_spooldir/%name
%dir %attr(750,%name,%name) %_spooldir/%name/in
%dir %attr(750,%name,%name) %_spooldir/%name/in/local
%dir %attr(750,%name,%name) %_spooldir/%name/in/secure
%dir %attr(750,%name,%name) %_spooldir/%name/in/temp
%dir %attr(750,%name,%name) %_spooldir/%name/out
%dir %attr(750,%name,%name) %_spooldir/%name/out/aso
%dir %attr(750,%name,%name) %_spooldir/%name/out/files
%dir %attr(750,%name,%name) %_spooldir/%name/out/longbox
%dir %attr(750,%name,%name) %_spooldir/%name/out/temp
%dir %attr(750,%name,%name) %_spooldir/%name/out/zone

%changelog
* Fri Feb 27 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.2-alt5
- Return package to Sisyphus

* Sat Feb 01 2003 Sir Raorn <raorn@altlinux.ru> 2.2-alt4
- Added packager tag
- ftn's shell changet to /bin/sh

* Thu Nov 14 2002 Albert R. Valiev <darkstar@altlinux.ru> 2.2-alt3
- changed and added some directories for fileechoprocessor

* Sun Oct 27 2002 Sir Raorn <raorn@altlinux.ru> 2.2-alt2
- SPP fixes (thanx to ldv)

* Sat Aug 17 2002 Sir Raorn <raorn@altlinux.ru> 2.2-alt1
- .i18n for pseudouser ftn
- Added some directories for fileechoprocessor
- Spec cleanup

* Fri Apr 12 2002 Sir Raorn <raorn@altlinux.ru> 2.1-alt2
- Obsoletes: fidonet
- Some comments added

* Mon Dec 03 2001 Sir Raorn <raorn@altlinux.ru> 2.1-alt1
- Built for Sisyphus

