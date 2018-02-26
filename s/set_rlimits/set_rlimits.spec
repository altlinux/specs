# $Id$
#
%define name set_rlimits
%define version 1.2.0

Name: %name
Version: %version
Release: alt1

Summary: %name - allow non-priviledged access to realtime scheduling
License: GPL
Group: System/Configuration/Other
URL: http://www.physics.adelaide.edu.au/~jwoithe
Source: %url/%name-%version.tgz

Obsoletes: set_rtlimits <= 1.1.0

%description
set_rlimits  allows  controlled  access  to  realtime  scheduling  for
selected  users  and  programs  under  kernel  2.6.12  or  later.   The
set_rlimits binary needs to be installed setuid root, but it only runs
with elevated priviledges to set the resource limits.

%prep
%setup

%build
set CFLGAS=$RPM_OPT_FLAGS 
gcc $CFLAGS -o %name %name.c

%install
%__mkdir_p %buildroot{%_man8dir,%_sysconfdir,%_bindir}

%__install -m644 %name.8 %buildroot%_man8dir
%__install -m644 %name.conf %buildroot%_sysconfdir
%__install -m4750 %name %buildroot%_bindir

%files
%attr(4710,root,audio) %_bindir/%name
%config(noreplace) %_sysconfdir/%name.conf
%_man8dir/*
%doc README Changelog

%changelog
* Mon Apr 04 2006 LAKostis <lakostis at altlinux.ru> 1.2.0-alt1
- new version 1.2.0 with new name.

* Sat Aug 06 2005 LAKostis <lakostis at altlinux.ru> 1.1.0-alt1.1
- fix permissions according build policy.

* Wed Aug 03 2005 LAKostis <lakostis at altlinux.ru> 1.1.0-alt1
- initial build for Sisyphus.

