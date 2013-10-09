%define _libexecdir /usr/libexec

Name: vzstats
Version: 0.5.2
Release: alt1
BuildArch: noarch
Summary: OpenVZ stats collection daemon

Group: System/Base
License: GPL2+
Url: http://stats.openvz.org
Source: %name-%version.tar
Source1: vzstats.filetrigger
Patch0: %name-%version-alt.patch

Requires: curl

%description
This is an OpenVZ component to gather OpenVZ usage and hardware statistics,
in order to improve the project.

%prep
%setup
%patch0 -p1

%build
%make %{?_smp_mflags}

%install
%makeinstall_std install-cronjob
# Needed for %%ghost in %%files section below
touch %buildroot%_sysconfdir/vz/.vzstats-uuid

install -Dp -m755 %SOURCE1 %buildroot%_rpmlibdir/vzstats.filetrigger

%files
%_sbindir/vzstats
%config %_sysconfdir/vz/vzstats.conf
%_sysconfdir/vz/essential.ca-bundle.crt
%ghost %config(missingok) %_sysconfdir/vz/.vzstats-uuid
%dir %_libexecdir/%name
%_libexecdir/%name
%exclude %_libexecdir/%name/vzversion-gentoo
%exclude %_libexecdir/%name/vzversion-deb
%exclude %_libexecdir/%name/vzversion-arch
%_sysconfdir/cron.monthly/*
%_rpmlibdir/vzstats.filetrigger
%_man8dir/%{name}.8.*
%doc README COPYING

%changelog
* Wed Oct  9 2013 Terechkov Evgenii <evg@altlinux.org> 0.5.2-alt1
- 0.5.2

* Wed May 15 2013 Terechkov Evgenii <evg@altlinux.org> 0.3.2-alt1
- 0.3.2

* Thu May  2 2013 Terechkov Evgenii <evg@altlinux.org> 0.2.1-alt1
- Initial build based on OpenVZ spec

* Fri Apr 26 2013 Kir Kolyshkin <kir@openvz.org> - 0.2.1-1
- fixed compatibility with older (as of RHEL5/4) userspace
- stricter checks for scripts permission and ownership

* Wed Apr 24 2013 Kir Kolyshkin <kir@openvz.org> - 0.2-1
- first public release
- added meminfo and ostemplates scripts

* Thu Apr  4 2013 Kir Kolyshkin <kir@openvz.org> - 0.1-1
- initial packaging
