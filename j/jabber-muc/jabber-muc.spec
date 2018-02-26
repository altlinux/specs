%define _libexecdir /usr/libexec
%define realname mu-conference
%define username _muc
%define revision r51

Name: jabber-muc
Version: 0.8
Release: alt0.3.%revision

Summary: MU-Conference service for Jabber (using JCR)
Group: System/Servers
License: GPL
Url: https://gna.org/projects/mu-conference/
Packager: Alexey Sidorov <alexsid@altlinux.ru>

Source: %{realname}.tar.bz2
Source1: jabber-muc.xml
Source2: %name.init
Source3: %name.adapter
Patch1: mu-conference-0.7.0-alt-config_room_defaults.patch
Patch2: mu-conference-0.7.0-alt-opt_max_num.patch
Patch3: mu-conference-0.7-ru-hack.patch

BuildPreReq: jabber-common
# Automatically added by buildreq on Thu May 10 2007
BuildRequires: glib2-devel libexpat-devel libidn-devel libMySQL-devel zlib-devel

Obsoletes: jabberd2-muc
Provides: jabberd2-muc
Requires: jabber-common >= 0.2 xmlstarlet

%description
Jabber MultiUser Conference service (MUC).

%prep
%setup -q -n %realname
%patch1 -p1
%patch2 -p1

#enable this for russian transcription of room's config dialog
#patch3 -p1

%build
%make

%install 
mkdir -p %buildroot%_libexecdir/
cp src/%realname %buildroot%_libexecdir/
mkdir -p %buildroot%_spooldir/%name/
mkdir -p %buildroot%_logdir/%name/
mkdir -p %buildroot%_var/run/%name/

#mkdir -p %buildroot%_sysconfdir/%name/
install -pD -m640 %SOURCE1 %buildroot%_sysconfdir/%name/muc.xml

#mkdir -p %buildroot%_initdir/
install -pD -m755 %SOURCE2 %buildroot%_initdir/%name

install -pD -m0755 %SOURCE3 %buildroot%_jabber_component_dir/%name

%pre
%_sbindir/groupadd -r -f %username 2>/dev/null ||:
%_sbindir/useradd -r -g %username -c 'jabber transport' -d %_spooldir/%name \
-s /dev/null %username 2>/dev/null ||:

%post
%_jabber_config
%post_service %name

%preun
%preun_service %name

%files
%doc ChangeLog README AUTHORS FAQ README.sql COPYING TODO XEP0045_SUPPORT
%doc scripts/* mu-conference.sql style.css
%attr(0640,root,%username) %config(noreplace) %_sysconfdir/%name/muc.xml
%_libexecdir/*
%_initdir/*
%attr(2770,root,%username) %dir %_spooldir/%name/
%attr(2770,root,%username) %dir %_logdir/%name/
%attr(2770,root,%username) %dir %_var/run/%name/
%_jabber_component_dir/*

%changelog
* Thu Jan 24 2008 Alexey Sidorov <alexsid@altlinux.ru> 0.8-alt0.3.r51
- update jabber-config adapter (use xmlstarlet)
- New SVN revision:
- Patch by Smoku to hide empty rooms from disco/browse lists.

* Tue Dec 04 2007 Alexey Sidorov <alexsid@altlinux.ru> 0.8-alt0.2.r50
- New SVN revision

* Sun Jun 17 2007 Alexey Sidorov <alexsid@altlinux.ru> 0.8-alt0.1.r29
- New version and SVN revision
- Changed versioning scheme

* Sun May 27 2007 Alexey Sidorov <alexsid@altlinux.ru> 0.7.0-alt0.2.RC1
- Release candidate

* Tue Apr 24 2007 Alexey Sidorov <alexsid@altlinux.ru> 0.7.0-alt0.1.r8
- New SVN revision
- ALT Linux Jabber Policy package
- jcr included
- Added patch mu-conference-0.7.0-alt-opt_max_num.patch (<zerg@>)
- Added to srpm, but not enabled patch mu-conference-0.7-ru-hack.patch,
  Russian transcription of room's config dialog (<zerg@>)
- added spool dir for initial start with default config
- clearing unnecessary macros from spec

* Thu Dec 29 2005 Andrei Bulava <abulava@altlinux.ru> 0.6.0-alt2
- added config_room_defaults.patch, which introduced an incompatibility with
  the official version to implement the long standing feature request 
  http://jabberstudio.org/projects/mu-conference/features/view.php?id=3107
  regarding corporate configuration options (see example config for details)
- fixed permissions and ownership of configuration files

* Thu Dec 15 2005 Andrei Bulava <abulava@altlinux.ru> 0.6.0-alt1
- initial build for ALT Linux (thanks to Pavel Boldin <bp@> for good starting
  points)

