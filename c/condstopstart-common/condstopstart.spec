# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: condstopstart-common
Version: 0.3
Release: %branch_release alt1

Summary: Common dirs for condstopstart-*
License: %gpl2plus
Group: System/Configuration/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source10: tmpfiles.conf

Provides: %condstopstart_subsysdir
Provides: %condstopstart_subsysrundir

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-condstopstart
BuildPreReq: rpm-build-licenses

%description
%summary

%install
install -d %buildroot%condstopstart_subsysdir/
install -d %buildroot%condstopstart_subsysrundir/

install -D %SOURCE10 %buildroot%_sysconfdir/tmpfiles.d/%name
sed -i "
	s|@RUNDIR@|%condstopstart_subsysrundir|g
" %buildroot%_sysconfdir/tmpfiles.d/%name

%files
%config %_sysconfdir/tmpfiles.d/%name
%attr(755,root,root) %dir %condstopstart_subsysdir/
%attr(755,root,root) %dir %condstopstart_subsysrundir/

%changelog
* Tue Aug  07 2012 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt1
- Fix: move %%_sysconfdir/%%name to %%_sysconfdir/tmpfiles.d/%%name

* Mon Aug 06 2012 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Add %%_sysconfdir/%%name (Closes: #27607)

* Fri Feb 10 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus
