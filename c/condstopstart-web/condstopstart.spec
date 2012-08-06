# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: condstopstart-web
Version: 0.2
Release: %branch_release alt1

Summary: Condstopstart for web serwers
License: %gpl2plus
Group: System/Configuration/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: web-command.sh
Source10: tmpfiles.conf

Requires: %condstopstart_subsysdir
Requires: %condstopstart_subsysrundir
Provides: %condstopstart_webdir
Provides: %condstopstart_webrundir

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-condstopstart
BuildPreReq: rpm-build-licenses

%description
%summary

%install
install -d %buildroot%condstopstart_webdir/
install -d %buildroot%condstopstart_webrundir/

# Generate web-cond*
for condcommand in condstop condstart condstop-rpm condstart-rpm; do
	condcommandfile="%buildroot%_sbindir/web-$condcommand"
	install -m 755 -pD %SOURCE0 $condcommandfile
	sed -ri "
		s|@COMMAND@|$condcommand|g
		s|@SCRIPTSDIR@|%condstopstart_webdir|g
		s|@RUNDIR@|%condstopstart_webrundir|g
	" $condcommandfile
done

install -D %SOURCE10 %buildroot%_sysconfdir/%name
sed -i "
	s|@RUNDIR@|%condstopstart_webrundir|g
" %buildroot%_sysconfdir/%name

%files
%config %_sysconfdir/%name
%attr(755,root,root) %dir %condstopstart_webdir/
%attr(755,root,root) %dir %condstopstart_webrundir/
%_sbindir/*

%changelog
* Mon Aug 06 2012 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Add %%_sysconfdir/%%name (Closes: #27608)

* Mon Feb 13 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus
