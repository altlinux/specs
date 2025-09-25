%define _unpackaged_files_terminate_build 1

%define builder_user  stapler-builder
%define builder_group stapler-builder

Name: stplr
Version: 0.0.27
Release: alt2

Summary: Universal package build and management system for Linux
License: GPL-3.0-or-later
Group: System/Configuration/Packaging
Url: https://stplr.dev
Vcs: https://altlinux.space/stapler/stplr.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

Requires: sysctl-conf-userns

BuildRequires(pre): rpm-macros-golang rpm-macros-systemd
BuildRequires: rpm-build-golang

%description
Stapler is a universal package build and management system for Linux 
that makes installing programs easier and more convenient. It is a 
fork of the ALR project, which, in turn, is based on LURE. Stapler 
allows you to install packages from your own repositories, as well 
as use the system package manager to work with packages that are 
not in its repositories.

%prep
%setup -a1
%autopatch -p1

%build
%make_build GIT_VERSION=v%version GENERATE=0

%install
%makeinstall_std PREFIX=%_prefix POST_INSTALL=0

%pre
%_sbindir/groupadd -r -f %builder_user
%_sbindir/useradd -M -r -d %_cachedir/%name -s /sbin/nologin -c "Stapler Builder" -g %builder_group %builder_user >/dev/null 2>&1 ||:

%files
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%attr(0755,%builder_user,%builder_group) %_cachedir/%name
%attr(0755,root,root) %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.toml
%doc README.md

%changelog
* Thu Sep 25 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.0.27-alt2
- Add requires sysctl-conf-userns (ALT#56136).

* Sat Aug 30 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.0.27-alt1
- New version 0.0.27.

* Fri Jul 18 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.0.26-alt1
- Initial build.

