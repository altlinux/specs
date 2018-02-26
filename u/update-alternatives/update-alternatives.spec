# $Id: update-alternatives.spec,v 1.2 2003/05/09 14:49:04 ldv Exp $

Name: update-alternatives
Version: 1.8.3
Release: alt1

Summary: Maintain symbolic links determining default commands
License: GPL
Group: System/Configuration/Packaging
BuildArch: noarch

Source: %name-%version.tar.bz2

Provides: %_sbindir/%name
PreReq: rpm > 0:4.0.4-alt18

%description
update-alternatives creates, removes, maintains and displays
information about the symbolic links comprising the %distribution
alternatives system.

It is possible for several programs fulfilling the same or similar
functions to be installed on a single system at the same time.  For
example, many systems have several text editors installed at once.
This gives choice to the users of a system, allowing each to use a
different editor, if desired, but makes it difficult for a program
to make a good choice of editor to invoke if the user has not
specified a particular preference.

%prep
%setup -q

%install
%__mkdir_p $RPM_BUILD_ROOT{%_sbindir,%_man8dir}
%__install -p -m755 %name $RPM_BUILD_ROOT%_sbindir/
%__install -p -m644 %name.8 $RPM_BUILD_ROOT%_man8dir/
%__mkdir_p $RPM_BUILD_ROOT{%_sysconfdir,%_localstatedir/rpm}/alternatives

%files
%_sbindir/%name
%attr(755,root,root) %_sysconfdir/alternatives
%attr(755,root,root) %_localstatedir/rpm/alternatives
%_mandir/man?/*

%changelog
* Fri May 09 2003 Dmitry V. Levin <ldv@altlinux.org> 1.8.3-alt1
- Initial revision as separate separate package.
