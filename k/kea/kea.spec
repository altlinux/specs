%define _unpackaged_files_terminate_build 1
%filter_from_requires /^\/usr\/bin\/mysql$/d
%filter_from_requires /^\/usr\/bin\/psql$/d

%define _localstatedir /var
%define _runstatedir /run

Name: kea
Version: 3.0.3
Release: alt1
Summary: DHCPv4, DHCPv6 and DDNS server from ISC

License: MPL-2.0 and BSL-1.0
Group: System/Servers
Url: https://kea.isc.org
Vcs: https://github.com/isc-projects/kea
Source0: %name-%version.tar
Source1: kea-dhcp4.service
Source2: kea-dhcp6.service
Source3: kea-dhcp-ddns.service
Source4: kea-ctrl-agent.service
#Patch: %%name-%%version.patch

Requires: %name-admin
Requires: %name-dhcp-ddns
Requires: %name-dhcp4
Requires: %name-dhcp6
Requires: %name-hooks

BuildRequires(pre): rpm-macros-python3 rpm-macros-meson
BuildRequires: meson >= 1.1.0 rpm-build-python3
BuildRequires: boost-devel boost-interprocess-devel boost-asio-devel
BuildRequires: gcc-c++ bison flex
BuildRequires: libssl-devel
BuildRequires: libkrb5-devel
BuildRequires: libmysqlclient-devel
BuildRequires: postgresql-devel
BuildRequires: liblog4cplus-devel
BuildRequires: procps libgtest-devel
BuildRequires: /usr/bin/xmllint
BuildRequires: python3-devel
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme

%description
DHCP implementation from Internet Systems Consortium, Inc. that features fully
functional DHCPv4, DHCPv6 and Dynamic DNS servers.
Both DHCP servers fully support server discovery, address assignment, renewal,
rebinding and release. The DHCPv6 server supports prefix delegation. Both
servers support DNS Update mechanism, using stand-alone DDNS daemon.

%package common
Summary: Kea shared libraries, LFC, and runstate files used by Kea DHCP server
Group: System/Servers
Requires: lib%name = %EVR
Conflicts: %name < 3.0.0

%description common
Contains the Lease File Cleanup script, and various
things that are neededby the services.

%package admin
Summary: Database administration tools for Kea DHCP server
Group: System/Servers
Requires: %name-common = %EVR
Requires: python3-module-%name
Provides: %name-shell = %EVR
Obsoletes: %name-shell < %EVR

%description admin
To manage the databases, Kea provides the kea-admin tool. It can initialize a
new backend, check its version number, perform a backend upgrade, and dump
lease data to a text file.
This package also contains the Kea shell, which provides a way to communicate
with the Kea Control Agent from the CLI. It is a simple command-line,
scripting-friendly, text client that is able to connect to the CA, send it
commands with parameters, retrieve theresponses, and display them.

%package dhcp-ddns
Summary: Kea DHCP Dynamic DNS Server
Group: System/Servers
Requires: %name-common = %EVR

%description dhcp-ddns
The Kea DHCP-DDNS Server (kea-dhcp-ddns, known informally as D2) conducts the
client side of the Dynamic DNS protocol (DDNS, defined in RFC 2136) on behalf
of the DHCPv4 and DHCPv6 servers (kea-dhcp4 and kea-dhcp6 respectively). The
DHCP servers construct DDNS update requests, known as NameChangeRequests
(NCRs), based on DHCP lease change events and then post them to D2. D2 attempts
to match each request to the appropriate DNS server(s) and carries out the
necessary conversation with those servers to update the DNS data.

%package dhcp4
Summary: Kea IPv4 DHCP Server
Group: System/Servers
Requires: %name-common = %EVR

%description dhcp4
The Kea DHCPv4 Server.

%package dhcp6
Summary: Kea IPv6 DHCP Server
Group: System/Servers
Requires: %name-common = %EVR

%description dhcp6
The Kea DHCPv6 Server.

%package ctrl-agent
Summary: Kea Control Agent - REST service for controlling Kea DHCP server
Group: System/Servers
Requires: %name-common = %EVR

%description ctrl-agent
The Kea Control Agent (CA) is a daemon which exposes a RESTful control
interface for managing Kea servers. The daemon can receive control commands
over HTTP and either forward these commands to the respective Kea servers or
handle these commands on its own. Control Agent is deprecated and will
be removed from future releases.

%package perfdhcp
Summary: Kea Optional Utils - perfdhcp
Group: System/Servers

%description perfdhcp
perfdhcp is a DHCP benchmarking tool. It provides a way to measure the
performance of DHCP servers by generating large amounts of traffic from
multiple simulated clients. It is able to test both IPv4 and IPv6 servers, and
provides statistics concerning response times and the number of requests that
are dropped.

%package -n lib%name-devel
Summary: Development headers and libraries for Kea DHCP server
Group: Development/Other
Requires: lib%name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
Header files and API documentation.

%package hooks
Summary: Hooks libraries for kea
Group: System/Servers
Requires: %name-common = %EVR

%description hooks
Hooking mechanism allow Kea to load one or more dynamically-linked libraries
(known as "hooks libraries") and, at various points in its processing
("hook points"), call functions in them.  Those functions perform whatever
custom processing is required. This package contains the following hooks:
ha (high availability), bootp, stat-cmds, run-script,
lease-cmds, flex-option, perfmon, class-cmds, ddns-tuning, flex-id,
forensic-log, host-cache, host-cmds, lease-query, limits, ping-check,
radius, subnet-cmds.

%package gss-tsig
Summary: Kea GSS-TSIG hook library
Group: System/Servers
Requires: %name-common = %EVR

%description gss-tsig
Kea is an IPv4 and IPv6 DHCP server developed by Internet Systems Consortium.
This package provides GSS-TSIG hook library, intended to be loaded by
DHCP-DDNS server.
It provides GSS-API with Kerberos support and can be used to integrate
with Windows Active Directory.

%package mysql
Summary: MySQL hook library for Kea
Group: System/Servers
Requires: %name-common = %EVR

%description mysql
This package contains the MySQL hook library for Kea.

%package pgsql
Summary: PostgreSQL hook library for Kea
Group: System/Servers
Requires: %name-common = %EVR

%description pgsql
This package contains the PostgreSQL hook library for Kea.

%package doc
Summary: Documents for Kea dhcp
Group: Documentation
BuildArch: noarch

%description doc
Documents for Kea dhcp.

%package -n lib%name
Summary: Shared libraries used by Kea DHCP server
Group: System/Libraries
Provides: %name-libs = %EVR

%description -n lib%name
This package contains shared libraries used by Kea DHCP server.

%package -n python3-module-%name
Summary: Python3 management connector for ISC KEA DHCP server
Group: Development/Python3
BuildArch: noarch
%add_python3_path %python3_sitelibdir_noarch/%name
%allow_python3_import_path %python3_sitelibdir_noarch/%name

%description -n python3-module-%name
Python3 management connector for ISC KEA DHCP server.
KEA is an IPv4 and IPv6 DHCP server developed by Internet Systems Consortium.

This package provides Python3 connector.

%prep
%setup
#%%patch -p1

sed -i -e "s|%version-git|%version|" meson.build

%build
export KEA_PKG_VERSION_IN_CONFIGURE=%release
export KEA_PKG_TYPE_IN_CONFIGURE="rpm"
%meson \
    -D runstatedir=%_runstatedir \
    -D crypto=openssl \
    -D krb5=enabled \
    -D mysql=enabled \
    -D postgresql=enabled \
    -D netconf=disabled \
    -D tests=enabled \
    -D install_umask=0022 \
    %nil
%meson_build
%__meson_build doc

%install
%meson_install

# remove keactrl
rm -v %buildroot%_sysconfdir/kea/keactrl.conf
rm -v %buildroot%_sbindir/keactrl
rm -v %buildroot%_mandir/man8/keactrl.8

# remove netconf files
rm -v %buildroot%_mandir/man8/kea-netconf.8

# Install systemd units
install -Dpm 0644 %SOURCE1 %buildroot%_unitdir/kea-dhcp4.service
install -Dpm 0644 %SOURCE2 %buildroot%_unitdir/kea-dhcp6.service
install -Dpm 0644 %SOURCE3 %buildroot%_unitdir/kea-dhcp-ddns.service
install -Dpm 0644 %SOURCE4 %buildroot%_unitdir/kea-ctrl-agent.service

# Start empty lease databases
mkdir -p %buildroot%_sharedstatedir/kea
touch %buildroot%_sharedstatedir/kea/kea-leases4.csv
touch %buildroot%_sharedstatedir/kea/kea-leases6.csv

rm -rf %buildroot%_datadir/kea/meson-info

# install /usr/lib/tmpfiles.d/kea.conf
mkdir -p %buildroot%_tmpfilesdir
cat > %buildroot%_tmpfilesdir/%name.conf <<EOF
# kea needs existing /run/kea/ to create logger_lockfile and pidfile there
# See tmpfiles.d(5) for details
d /run/kea 0750 _kea _kea -
EOF

# change log destination from /var/log/... to STDOUT and enable shortened log format
sed -i'' 's/"output":.*/"output": "stdout",/;s@// "pattern":\([^,]*\),*@"pattern":\1@' \
    %buildroot%_sysconfdir/%name/kea-ctrl-agent.conf \
    %buildroot%_sysconfdir/%name/kea-dhcp6.conf \
    %buildroot%_sysconfdir/%name/kea-dhcp4.conf \
    %buildroot%_sysconfdir/%name/kea-dhcp-ddns.conf

%check
# TODO: disable mysql and pgsql tests
%meson_test ||:

%pre common
groupadd -r -f _kea
useradd -M -r -d %_sharedstatedir/%name -s /bin/false -c "Kea DHCP service user" -g _kea _kea >/dev/null 2>&1 ||:

%post ctrl-agent
%post_systemd kea-ctrl-agent.service
%preun ctrl-agent
%preun_systemd kea-ctrl-agent.service

%post dhcp-ddns
%post_systemd kea-dhcp-ddns.service
%preun dhcp-ddns
%preun_systemd kea-dhcp-ddns.service

%post dhcp4
%post_systemd kea-dhcp4.service
%preun dhcp4
%preun_systemd kea-dhcp4.service

%post dhcp6
%post_systemd kea-dhcp6.service
%preun dhcp6
%preun_systemd kea-dhcp6.service

%files
%doc COPYING

%files common
%doc COPYING
%_sbindir/kea-lfc
%_man8dir/kea-lfc.*
%_tmpfilesdir/%name.conf
%dir %_libdir/%name
%dir %_libdir/%name/hooks
%dir %attr(0750, root, _kea) %_sysconfdir/%name
%dir %attr(0755, _kea, _kea) %_sharedstatedir/%name
%dir %attr(0750, _kea, _kea) %_logdir/%name

%files perfdhcp
%_sbindir/perfdhcp
%_man8dir/perfdhcp.*

%files admin
%_sbindir/kea-admin
%_man8dir/kea-admin.*
%dir %_datadir/kea
%_datadir/kea/api
%_datadir/kea/scripts
%_sbindir/kea-shell
%_man8dir/kea-shell.*

%files ctrl-agent
%_sbindir/kea-ctrl-agent
%_unitdir/kea-ctrl-agent.service
%_man8dir/kea-ctrl-agent.*
%attr(0640,root,_kea) %config(noreplace) %_sysconfdir/%name/kea-ctrl-agent.conf

%files dhcp-ddns
%_sbindir/kea-dhcp-ddns
%_unitdir/kea-dhcp-ddns.service
%_man8dir/kea-dhcp-ddns.*
%attr(0640,root,_kea) %config(noreplace) %_sysconfdir/%name/kea-dhcp-ddns.conf

%files dhcp4
%_sbindir/kea-dhcp4
%_unitdir/kea-dhcp4.service
%_man8dir/kea-dhcp4.*
%attr(0640,root,_kea) %config(noreplace) %_sysconfdir/%name/kea-dhcp4.conf
%attr(0640,_kea,_kea) %config(noreplace) %_sharedstatedir/%name/kea-leases4.csv

%files dhcp6
%_sbindir/kea-dhcp6
%_unitdir/kea-dhcp6.service
%_man8dir/kea-dhcp6.*
%attr(0640,root,_kea) %config(noreplace) %_sysconfdir/%name/kea-dhcp6.conf
%attr(0640,_kea,_kea) %config(noreplace) %_sharedstatedir/%name/kea-leases6.csv

%files -n lib%name-devel
%_bindir/kea-msg-compiler
%_includedir/%name
%_libdir/lib%name-*.so
%_pkgconfigdir/%name.pc

%files hooks
%dir %_sysconfdir/%name/radius
%_sysconfdir/%name/radius/dictionary
%_libdir/%name/hooks
%exclude %_libdir/%name/hooks/libddns_gss_tsig.so
%exclude %_libdir/%name/hooks/libdhcp_mysql.so
%exclude %_libdir/%name/hooks/libdhcp_pgsql.so

%files gss-tsig
%_libdir/%name/hooks/libddns_gss_tsig.so

%files mysql
%_libdir/lib%name-mysql.so.*
%_libdir/%name/hooks/libdhcp_mysql.so

%files pgsql
%_libdir/lib%name-pgsql.so.*
%_libdir/%name/hooks/libdhcp_pgsql.so

%files doc
%doc %_datadir/doc/%name

%files -n lib%name
%_libdir/lib%name-*.so.*
%exclude %_libdir/lib%name-mysql.so.*
%exclude %_libdir/lib%name-pgsql.so.*

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name

%changelog
* Mon Mar 30 2026 Anton Farygin <rider@altlinux.org> 3.0.3-alt1
- 3.0.2 -> 3.0.3 (Fixes: CVE-2026-3608)

* Fri Nov 07 2025 Anton Farygin <rider@altlinux.com> 3.0.2-alt1
- 3.0.1 -> 3.0.2 (Fixes: CVE-2025-11232)

* Tue Oct 07 2025 Anton Farygin <rider@altlinux.com> 3.0.1-alt2
- fixed typo in changelog

* Fri Sep 05 2025 Anton Farygin <rider@altlinux.com> 3.0.1-alt1
- 3.0.0 -> 3.0.1 (Fixes: CVE-2025-40779)
- fixed typo in dhcp4 service (Closes: #55877)
- fixed incorrect ownership of kea-leases*.csv files (Closes: #55878)

* Fri Aug 08 2025 Anton Farygin <rider@altlinux.com> 3.0.0-alt2
- moved hooks directory to common package
- control sockets moved from /tmp to /run/kea
- set install_umask to 0022 during build to ensure consistent file permissions
- added standard runtime, state, log, and control socket directories to Kea
  systemd units and enabled optional configuration overrides via /etc/sysconfig/kea

* Fri Jun 27 2025 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- 3.0.0
- split package to common, admin, dhcp-ddns, dhcp4, dhcp6, ctrl-agent
- add perfdhcp, gss-tsig, mysql, pgsql packages

* Wed Jun 11 2025 Andrey Limachko <liannnix@altlinux.org> 2.7.9-alt1
- 2.7.9

* Mon May 19 2025 Andrey Limachko <liannnix@altlinux.org> 2.7.8-alt1
- 2.7.8

* Wed Apr 16 2025 Andrey Limachko <liannnix@altlinux.org> 2.7.7-alt1
- 2.7.7

* Thu Aug 22 2024 Alexey Shabalin <shaba@altlinux.org> 2.6.1-alt1
- 2.6.1

* Fri Jun 07 2024 Alexey Shabalin <shaba@altlinux.org> 2.6.0-alt1
- 2.6.0

* Wed Dec 06 2023 Alexey Shabalin <shaba@altlinux.org> 2.4.1-alt1
- 2.4.1

* Mon Oct 16 2023 Alexey Shabalin <shaba@altlinux.org> 2.4.0-alt2
- fixed execute kea-shell (fix define python3 site-packages path)

* Fri Aug 18 2023 Alexey Shabalin <shaba@altlinux.org> 2.4.0-alt1
- 2.4.0
- build with gssapi support

* Mon Aug 08 2022 Alexey Shabalin <shaba@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Apr 11 2022 Alexey Shabalin <shaba@altlinux.org> 2.0.2-alt1
- 2.0.2

* Mon Oct 18 2021 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt1
- 2.0.0

* Thu Aug 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.2-alt3
- Rebuilt with boost-1.77.0.

* Fri Jun 04 2021 Alexey Shabalin <shaba@altlinux.org> 1.8.2-alt2
- fixed build docs with new sphinx

* Fri Jan 29 2021 Alexey Shabalin <shaba@altlinux.org> 1.8.2-alt1
- 1.8.2

* Tue Nov 10 2020 Alexey Shabalin <shaba@altlinux.org> 1.8.1-alt1
- 1.8.1

* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.2-alt3
- fix kea-shell package
- move docs to doc package

* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.2-alt2
- split kea-shell to separate package
- filter mysql and psql from requires
- update systemd units

* Wed Mar 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.2-alt1
- 1.6.2

* Thu Feb 06 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.1-alt1
- Initial build
