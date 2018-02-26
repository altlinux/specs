# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: moodle-plugins-tools
Version: 0.1
Release: %branch_release alt1

Summary: Moodle plugins configuration tools
License: %gpl2plus
Group: System/Configuration/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source10: mt-plugins.conf.php
Source20: mt-plugins-setparams.php
Source21: mt-plugins-setauth.php

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-moodle

%description
%summary

%install
install -pD -m0755 %SOURCE10 %buildroot%_sysconfdir/sysconfig/mt-plugins
install -pD -m0755 %SOURCE20 %buildroot%_sbindir/mt-plugins-setparams
install -pD -m0755 %SOURCE21 %buildroot%_sbindir/mt-plugins-setauth

sed -i '
s|%%_sysconfdir|%_sysconfdir|g
s|%%_sbindir|%_sbindir|g
s|%%webserver_group|%webserver_group|g
s|%%moodle_datadir|%moodle_datadir|g
s|%%moodle_dir|%moodle_dir|g
' %buildroot%_sbindir/mt-* %buildroot%_sysconfdir/sysconfig/*

%files
%config(noreplace) %_sysconfdir/sysconfig/*
%_sbindir/mt-*

%changelog
* Sun May 06 2012 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux Sisyphus
