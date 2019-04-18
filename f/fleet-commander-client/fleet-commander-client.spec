%define _unpackaged_files_terminate_build 1

%def_with check

Name: fleet-commander-client
Version: 0.10.2
Release: alt2

Summary: Fleet Commander Client
License: LGPLv3+ and LGPLv2+ and MIT and BSD
Group: System/Base
BuildArch: noarch

Url: https://github.com/fleet-commander/fc-client
Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: autoconf-archive
BuildRequires: python-module-dbus
BuildRequires: python-module-dbusmock
BuildRequires: python-module-mock
BuildRequires: python-module-pygobject

%if_with check
BuildRequires: libnm-gir
BuildRequires: libjson-glib-gir
%endif
Requires: libnm-gir

%description
Profile data retriever for Fleet Commander client hosts. Fleet Commander is an
application that allows you to manage the desktop configuration of a large
network of users and workstations/laptops.

%prep
%setup
%patch -p1

# for now skip tests which require real system/session dbus
grep -qs '^TESTS[[:space:]]*=.* 09_fcclient\.sh[[:space:]]*' tests/Makefile.am || exit 1
sed -i '/^TESTS[[:space:]]*=/{s/09_fcclient\.sh//g}' tests/Makefile.am

# runuser is not on user PATH
grep -qs '^AC_PATH_PROG(\[RUNUSER\], \[runuser\])$' configure.ac || exit 1
sed -i '/^AC_PATH_PROG(\[RUNUSER\], \[runuser\])$/{s/)$/, "$PATH:\/sbin")/g}' \
configure.ac

%build
%autoreconf
%configure \
    --with-systemdsystemunitdir=%_unitdir
%make_build

%install
%makeinstall_std

%check
%make check || { cat ./tests/test-suite.log; exit 1; }

%post
%post_service fleet-commander-client

%preun
%preun_service fleet-commander-client

%files
%doc README
%dir %_datadir/fleet-commander-client
%dir %_datadir/fleet-commander-client/python
%dir %_datadir/fleet-commander-client/python/fleetcommanderclient
%_datadir/fleet-commander-client/python/fleetcommanderclient/*.py
%dir %_datadir/fleet-commander-client/python/fleetcommanderclient/configadapters
%_datadir/fleet-commander-client/python/fleetcommanderclient/configadapters/*.py
%config(noreplace) %_sysconfdir/xdg/fleet-commander-client.conf
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.freedesktop.FleetCommanderClient.conf
%_unitdir/fleet-commander-client.service
%_datadir/dbus-1/system-services/org.freedesktop.FleetCommanderClient.service

%changelog
* Thu Mar 14 2019 Stanislav Levin <slev@altlinux.org> 0.10.2-alt2
- Fixed triggering FC dbus service by SSSD.

* Fri Jan 18 2019 Stanislav Levin <slev@altlinux.org> 0.10.2-alt1
- Initial build.

