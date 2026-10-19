%define _libexecdir %prefix/libexec
%define netdatauser netdata

# OpenTelemetry metrics and logs plugin (Rust)
%def_with otel
# eBPF plugin downloads a libbpf fork and prebuilt eBPF programs
%def_without ebpf

Name: netdata
Version: 2.12.1
Release: alt1

Summary: Real-time performance monitoring, done right!

License: GPL-3.0-or-later
Group: Monitoring
ExclusiveArch: x86_64 aarch64
Url: https://github.com/netdata/netdata

Packager: Vitaly Lipatov <lav@altlinux.ru>

# full tarball with submodules
# Source-url: https://github.com/netdata/netdata/releases/download/v%version/netdata-v%version.tar.gz
Source: %name-%version.tar

# vendored Go modules and Rust crates (.gear/predownloaded-preinstall-hook)
Source1: %name-development-%version.tar

# only ext/recover is used (it is not a part of libsqlite3), see .gear/postdownload-hook
%define sqlite_src_ver 3530300
# Source2-url: https://www.sqlite.org/2026/sqlite-src-%sqlite_src_ver.zip
Source2: sqlite-src.tar

Source3: netdata.sysusers

# PLD: use system SQLite (+ ext/recover sources), Judy, libsensors and libbacktrace
# git://git.pld-linux.org/packages/netdata.git
Patch1: netdata-system-libs.patch
# Gentoo: use system dlib
# https://distfiles.gentoo.org/pub/dev/arthurzam@gentoo.org/net-analyzer/netdata/netdata-2.11.1-system-libs.patch.xz
Patch2: netdata-system-dlib.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake gcc-c++ ninja-build
BuildRequires: rpm-build-python3
BuildRequires: libuuid-devel libuv-devel zlib-devel liblz4-devel libzstd-devel
BuildRequires: libbrotli-devel libssl-devel libcurl-devel
BuildRequires: libjson-c-devel libyaml-devel libpcre2-devel
BuildRequires: libjudy-devel libcap-devel libmnl-devel libelf-devel
BuildRequires: libsqlite3-devel libbacktrace-devel libsensors3-devel
BuildRequires: libprotobuf-devel protobuf-compiler libabseil-cpp-devel
BuildRequires: libsnappy-devel
BuildRequires: libsystemd-devel
BuildRequires: dlib-devel
BuildRequires: libcups-devel
BuildRequires: libfreeipmi-devel
BuildRequires: libnetfilter_acct-devel
BuildRequires: libmongoc-devel
BuildRequires: golang
%if_with otel
BuildRequires: rust-cargo corrosion
%endif

Obsoletes: netdata-web < %EVR

AutoReq: yes, noshell

%add_findreq_skiplist %_libexecdir/%name/charts.d/*.sh
# a shell/python polyglot: shell.req can not parse it
%add_findreq_skiplist %_libexecdir/%name/plugins.d/python.d.plugin
# private python.d modules: scan them for requirements, provide nothing
%add_python3_path %_libexecdir/%name/python.d
%add_python3_self_prov_path %_libexecdir/%name/python.d
%add_python3_self_prov_path %_libexecdir/%name/python.d/python_modules
%filter_from_provides /^python3(python_modules[.)]/d
# optional collector (pandas.chart.py)
%add_python3_req_skip pandas
# python 2 fallback in third_party/ordereddict.py
%add_python3_req_skip UserDict

%description
netdata is the fastest way to visualize metrics. It is a resource
efficient, highly optimized system for collecting and visualizing any
type of realtime timeseries data, from CPU usage, disk activity, SQL
queries, API calls, web site visitors, etc.

netdata tries to visualize the truth of now, in its greatest detail,
so that you can get insights of what is happening now and what just
happened, on your systems and applications.

The web interface of Netdata Cloud is not included: it is distributed
under a non-free license (NCUL1). The agent provides the REST API
(/api/v1, /api/v2, /api/v3); metrics are available at
/api/v1/allmetrics?format=prometheus for Prometheus or VictoriaMetrics
with Grafana.

%package plugin-go
Summary: The go.d metrics collection plugin for netdata
Group: Monitoring
Requires: %name = %EVR

%description plugin-go
go.d.plugin for netdata: data collection modules written in Go
for a large number of applications and services.

%package plugin-scripts
Summary: The scripts.d plugin (Nagios plugins compatibility) for netdata
Group: Monitoring
Requires: %name = %EVR

%description plugin-scripts
scripts.d.plugin for netdata: runs Nagios compatible check scripts.

%package plugin-pythond
Summary: The python.d metrics collection plugin for netdata
Group: Monitoring
Requires: %name = %EVR
# python.d.plugin is skipped by find-requires (see above)
Requires: /usr/bin/python3

%description plugin-pythond
python.d.plugin for netdata: data collection modules written in Python.

%package plugin-chartsd
Summary: The charts.d metrics collection plugin for netdata
Group: Monitoring
Requires: %name = %EVR

%description plugin-chartsd
charts.d.plugin for netdata: data collection modules written in Bash.

%package plugin-cups
Summary: The Common Unix Printing System (CUPS) plugin for netdata
Group: Monitoring
Requires: %name = %EVR

%description plugin-cups
This is the Common Unix Printing System plugin for the netdata daemon.

Use this plugin to enable metrics collection from cupsd, the daemon
running when CUPS is enabled on the system.

%package plugin-freeipmi
Summary: The FreeIPMI metrics collection plugin for netdata
Group: Monitoring
Requires: %name = %EVR

%description plugin-freeipmi
freeipmi.plugin for netdata: IPMI sensors and events monitoring.

%package plugin-nfacct
Summary: The NFACCT metrics collection plugin for netdata
Group: Monitoring
Requires: %name = %EVR

%description plugin-nfacct
nfacct.plugin for netdata: netfilter accounting and connection
tracking metrics.

%if_with otel
%package plugin-otel
Summary: The OpenTelemetry metrics and logs plugin for netdata
Group: Monitoring
Requires: %name = %EVR

%description plugin-otel
otel-plugin for netdata: OpenTelemetry (OTLP) metrics and logs receiver.
%endif

%prep
%setup -a1 -a2
%patch1 -p1
%patch2 -p1
# the bundled pyyaml3 is removed in %%install: use the system yaml module
sed -i -e '/^try:$/{N;N;N;s|^try:\n    from pyyaml3 import SafeLoader as YamlSafeLoader\nexcept ImportError:\n    from yaml import SafeLoader as YamlSafeLoader|from yaml import SafeLoader as YamlSafeLoader|}' \
	src/collectors/python.d.plugin/python_modules/bases/loaders.py
grep -q '^from yaml import SafeLoader as YamlSafeLoader$' src/collectors/python.d.plugin/python_modules/bases/loaders.py
# prebuilt helper of the disabled IBM plugin
rm -v src/go/plugin/ibm.d/protocols/websphere/jmx/websphere_jmx_helper.jar

%build
export GOFLAGS="-mod=vendor -trimpath -buildmode=pie"
export GOPROXY=off GOTOOLCHAIN=local GOCACHE=$PWD/.go-cache
%if_with otel
export CARGO_HOME=$PWD/.cargo-home CARGO_NET_OFFLINE=true
mkdir -p $CARGO_HOME
sed -e "s|^directory = .*|directory = \"$PWD/vendor\"|" cargo-vendor-config.toml > $CARGO_HOME/config.toml
%endif
%cmake -G Ninja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_INSTALL_PREFIX=/ \
	-DBUILD_FOR_PACKAGING=ON \
	-DNETDATA_PACKAGING_FORMAT=rpm \
	-DFETCHCONTENT_FULLY_DISCONNECTED=ON \
	-DFETCHCONTENT_TRY_FIND_PACKAGE_MODE=ALWAYS \
	-DCMAKE_DISABLE_FIND_PACKAGE_Git=ON \
	-DNETDATA_SQLITE_RECOVER_SOURCE_DIR=$PWD/sqlite-src/ext/recover \
	-DUSE_MOLD=OFF \
	-DUSE_LTO=OFF \
	-DENABLE_DASHBOARD=OFF \
	-DENABLE_SENTRY=OFF \
	-DENABLE_WEBRTC=OFF \
	-DENABLE_JEMALLOC=OFF \
	-DENABLE_MIMALLOC=OFF \
	-DENABLE_LIBBACKTRACE=ON \
	-DENABLE_BUNDLED_JSONC=OFF \
	-DENABLE_BUNDLED_YAML=OFF \
	-DENABLE_BUNDLED_PROTOBUF=OFF \
	-DENABLE_ML=ON \
	-DENABLE_DBENGINE=ON \
	-DENABLE_EXPORTER_PROMETHEUS_REMOTE_WRITE=ON \
	-DENABLE_EXPORTER_MONGODB=ON \
	-DENABLE_PLUGIN_GO=ON \
	-DENABLE_ND_MCP=ON \
	-DENABLE_PLUGIN_SCRIPTS=ON \
	-DENABLE_PLUGIN_STATSD=OFF \
	-DENABLE_PLUGIN_PYTHON=ON \
	-DENABLE_PLUGIN_CHARTS=ON \
	-DENABLE_PLUGIN_APPS=ON \
	-DENABLE_PLUGIN_CUPS=ON \
	-DENABLE_PLUGIN_FREEIPMI=ON \
	-DENABLE_PLUGIN_NFACCT=ON \
	-DENABLE_PLUGIN_CGROUP_NETWORK=ON \
	-DENABLE_PLUGIN_DEBUGFS=ON \
	-DENABLE_PLUGIN_LOCAL_LISTENERS=ON \
	-DENABLE_PLUGIN_NETWORK_VIEWER=ON \
	-DENABLE_PLUGIN_PERF=ON \
	-DENABLE_PLUGIN_SLABINFO=ON \
	-DENABLE_PLUGIN_SYSTEMD_JOURNAL=ON \
	-DENABLE_PLUGIN_SYSTEMD_UNITS=ON \
	-DENABLE_NETDATA_JOURNAL_FILE_READER=OFF \
	-DENABLE_PLUGIN_XENSTAT=OFF \
	-DENABLE_PLUGIN_IBM=OFF \
	-DENABLE_PLUGIN_NETFLOW=OFF \
%if_with otel
	-DENABLE_PLUGIN_OTEL=ON \
%else
	-DENABLE_PLUGIN_OTEL=OFF \
%endif
%if_with ebpf
	-DENABLE_PLUGIN_EBPF=ON \
%else
	-DENABLE_PLUGIN_EBPF=OFF \
%endif
	%nil
%cmake_build

%install
export GOFLAGS="-mod=vendor -trimpath -buildmode=pie"
export GOPROXY=off GOTOOLCHAIN=local GOCACHE=$PWD/.go-cache
%if_with otel
export CARGO_HOME=$PWD/.cargo-home CARGO_NET_OFFLINE=true
%endif
%cmake_install

# self-updater, uninstaller, support files for other init systems
rm -v %buildroot%_libexecdir/%name/netdata-updater.sh
rm -v %buildroot%_libexecdir/%name/netdata-uninstaller.sh
rm -v %buildroot%_libexecdir/%name/install-service.sh
rm -v %buildroot%_sysconfdir/%name/netdata-updater.conf
rm -v %buildroot/usr/lib/%name/conf.d/netdata-updater.conf
rm -v %buildroot%_unitdir/netdata-updater.service
rm -v %buildroot%_unitdir/netdata-updater.timer
rm -rv %buildroot/usr/lib/%name/system/
# ALT does not enable services by presets
rm -v %buildroot%_presetdir/50-netdata.preset
# packaged as %%doc
rm -rv %buildroot%_defaultdocdir/%name/

# use system python modules instead of the bundled copies
rm -rv %buildroot%_libexecdir/%name/python.d/python_modules/pyyaml3
rm -rv %buildroot%_libexecdir/%name/python.d/python_modules/urllib3

# our sysusers file (the same as upstream one) is used in %%pre
install -m 644 %SOURCE3 %buildroot%_sysusersdir/%name.conf

# Do not send anonymous usage statistics (telemetry) to Netdata Inc.
touch %buildroot%_sysconfdir/%name/.opt-out-from-anonymous-statistics

%pre
%sysusers_create_package %name %SOURCE3

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE REDISTRIBUTED.md
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/netdata.conf
%_sysconfdir/%name/.opt-out-from-anonymous-statistics
%_sysconfdir/%name/.install-type
%_sysconfdir/%name/edit-config
%dir %_sysconfdir/%name/health.d/
%dir %_sysconfdir/%name/statsd.d/
%dir %_sysconfdir/%name/custom-plugins.d/
%dir %_sysconfdir/%name/ssl/
%config(noreplace) %_logrotatedir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%_sysusersdir/%name.conf
%dir /usr/lib/systemd/journald@netdata.conf.d/
/usr/lib/systemd/journald@netdata.conf.d/netdata.conf
%_sbindir/%name
%_sbindir/netdatacli
%_sbindir/netdata-claim.sh
%_sbindir/netdata-support-bundle
%_sbindir/nd-run
%_sbindir/nd-mcp
%_sbindir/log2journal
%_sbindir/systemd-cat-native
%dir /usr/lib/%name/
%dir /usr/lib/%name/conf.d/
/usr/lib/%name/conf.d/*.conf
/usr/lib/%name/conf.d/health.d/
/usr/lib/%name/conf.d/log2journal.d/
/usr/lib/%name/conf.d/schema.d/
/usr/lib/%name/conf.d/statsd.d/
/usr/lib/%name/conf.d/vnodes/
%exclude /usr/lib/%name/conf.d/charts.d.conf
%exclude /usr/lib/%name/conf.d/python.d.conf
%exclude /usr/lib/%name/conf.d/go.d.conf
%exclude /usr/lib/%name/conf.d/scripts.d.conf
%dir %_libexecdir/%name/
%dir %_libexecdir/%name/plugins.d/
%_libexecdir/%name/plugins.d/alarm-notify.sh
%_libexecdir/%name/plugins.d/anonymous-statistics.sh
%_libexecdir/%name/plugins.d/cgroup-network-helper.sh
%_libexecdir/%name/plugins.d/get-kubernetes-labels.sh
%_libexecdir/%name/plugins.d/loopsleepms.sh.inc
%_libexecdir/%name/plugins.d/system-info.sh
%_libexecdir/%name/plugins.d/tc-qos-helper.sh
%_libexecdir/%name/plugins.d/ioping.plugin
%_libexecdir/%name/plugins.d/cgroup-name
%_libexecdir/%name/plugins.d/systemd-units.plugin
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/cgroup-network
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/local-listeners
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/ndsudo
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/network-viewer.plugin
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/apps.plugin
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/debugfs.plugin
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/perf.plugin
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/slabinfo.plugin
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/systemd-journal.plugin
%dir %_datadir/%name/
%_datadir/%name/build-info-cmake-cache.gz
%_datadir/%name/web/
%attr(0770,%netdatauser,%netdatauser) %dir %_cachedir/%name/
%attr(0755,%netdatauser,root) %dir %_logdir/%name/
%attr(0770,%netdatauser,%netdatauser) %dir %_sharedstatedir/%name/
%attr(0770,%netdatauser,%netdatauser) %dir %_sharedstatedir/%name/registry/
%attr(0770,%netdatauser,%netdatauser) %dir %_sharedstatedir/%name/cloud.d/

%files plugin-go
/usr/lib/%name/conf.d/go.d.conf
/usr/lib/%name/conf.d/go.d/
%dir %_sysconfdir/%name/go.d/
%_libexecdir/%name/plugins.d/go.d.plugin
%_libexecdir/%name/plugins.d/snmp-trap-profile-gen

%files plugin-scripts
/usr/lib/%name/conf.d/scripts.d.conf
/usr/lib/%name/conf.d/scripts.d/
%_libexecdir/%name/plugins.d/scripts.d.plugin

%files plugin-pythond
/usr/lib/%name/conf.d/python.d.conf
/usr/lib/%name/conf.d/python.d/
%dir %_sysconfdir/%name/python.d/
%_libexecdir/%name/plugins.d/python.d.plugin
%_libexecdir/%name/python.d/

%files plugin-chartsd
/usr/lib/%name/conf.d/charts.d.conf
/usr/lib/%name/conf.d/charts.d/
%dir %_sysconfdir/%name/charts.d/
%_libexecdir/%name/plugins.d/charts.d.plugin
%_libexecdir/%name/plugins.d/charts.d.dryrun-helper.sh
%_libexecdir/%name/charts.d/

%files plugin-cups
%attr(0750,root,%netdatauser) %_libexecdir/%name/plugins.d/cups.plugin

%files plugin-freeipmi
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/freeipmi.plugin

%files plugin-nfacct
%attr(4710,root,%netdatauser) %_libexecdir/%name/plugins.d/nfacct.plugin

%if_with otel
%files plugin-otel
%attr(0750,root,%netdatauser) %_libexecdir/%name/plugins.d/otel-plugin
/usr/lib/%name/conf.d/otel.yaml
/usr/lib/%name/conf.d/otel.d/
%endif

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 2.12.1-alt1
- new version 2.12.1 (restore the package in Sisyphus)
- switch to cmake, use system libraries:
  + dlib, sqlite, Judy, libsensors, libbacktrace, protobuf
- build go.d.plugin, scripts.d.plugin, nd-mcp (vendored Go modules)
- build otel-plugin (vendored Rust crates)
- split plugins with extra dependencies to subpackages
- create the system user with sysusers.d
- drop netdata-web: the Netdata Cloud UI is not free (NCUL1)
- ExclusiveArch: x86_64 aarch64 (Go plugins do not build on i586)
  + plugin-chartsd, plugin-pythond are not noarch (they require netdata)
- updated BuildRequires for the cmake build:
  + added corrosion, dlib-devel, golang, libabseil-cpp-devel
  + added libbacktrace-devel, libbrotli-devel, libcurl-devel
  + added libelf-devel, libfreeipmi-devel, libmongoc-devel
  + added libpcre2-devel, libsensors3-devel, libsqlite3-devel
  + added libsystemd-devel, libzstd-devel, ninja-build
  + added protobuf-compiler, rpm-build-cmake, rpm-macros-cmake
  + added rust-cargo
  + removed bash4, libmosquitto-devel, libwebsockets-devel
  + removed rpm-build-intro, rpm-macros-intro-conflicts

* Mon Nov 20 2023 Vitaly Lipatov <lav@altlinux.ru> 1.43.2-alt3
- restore distutils patch (ALT bug 48184)

* Fri Nov 10 2023 Vitaly Lipatov <lav@altlinux.ru> 1.43.2-alt2
- fix libexecdir using for conf.d (ALT bug 48381)

* Tue Nov 07 2023 Vitaly Lipatov <lav@altlinux.ru> 1.43.2-alt1
- new version 1.43.2 (with rpmrb script)
- fix conf.d placement (ALT bug 48291)

* Wed Nov 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1.43.0-alt2
- add fix to build without distutils (ALT bug 48184)

* Sun Oct 22 2023 Vitaly Lipatov <lav@altlinux.ru> 1.43.0-alt1
- new version 1.43.0 (with rpmrb script)

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1.41.0-alt1
- new version 1.41.0 (with rpmrb script)

* Sun May 21 2023 Vitaly Lipatov <lav@altlinux.ru> 1.39.1-alt1
- new version 1.39.1 (with rpmrb script)
- add BR: libyaml-devel

* Sat May 06 2023 Vitaly Lipatov <lav@altlinux.ru> 1.38.1-alt1
- new version 1.38.1 (with rpmrb script)

* Fri Jan 20 2023 Vitaly Lipatov <lav@altlinux.ru> 1.37.1-alt1
- new version 1.37.1 (with rpmrb script)

* Sun Feb 13 2022 Vitaly Lipatov <lav@altlinux.ru> 1.33.0-alt1
- new version 1.33.0 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.32.1-alt1
- new version 1.32.1 (with rpmrb script)

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.31.0-alt2
- drop bundled urllib3

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.31.0-alt1
- new version 1.31.0 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 1.30.1-alt1
- new version 1.30.1 (with rpmrb script)

* Sat Feb 27 2021 Vitaly Lipatov <lav@altlinux.ru> 1.29.3-alt1
- new version 1.29.3 (with rpmrb script)
- build without new anomalies plugin (wait for pyod module)

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.26.0-alt1
- new version 1.26.0 (with rpmrb script)

* Mon Oct 12 2020 Vitaly Lipatov <lav@altlinux.ru> 1.25.0-alt2
- use python3 only
- move cups plugin to separate package
- move web static files to separate noarch subpackage
- update BR: libjudy-devel, libcap-devel, libssl-devel, libjson-c-devel

* Tue Sep 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.25.0-alt1
- new version 1.25.0 (with rpmrb script)

* Mon Aug 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.24.0-alt1
- new version 1.24.0 (with rpmrb script)

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.23.2-alt1
- new version 1.23.2 (with rpmrb script)

* Thu Jun 25 2020 Vitaly Lipatov <lav@altlinux.ru> 1.23.0-alt1
- new version 1.23.0 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.22.1-alt1
- new version 1.22.1 (with rpmrb script)

* Sat Mar 21 2020 Vitaly Lipatov <lav@altlinux.ru> 1.20.0-alt1
- new version 1.20.0 (with rpmrb script)

* Sun Dec 08 2019 Vitaly Lipatov <lav@altlinux.ru> 1.19.0-alt1
- new version (1.19.0) with rpmgs script

* Tue Oct 29 2019 Vitaly Lipatov <lav@altlinux.ru> 1.18.1-alt1
- new version 1.18.1 (with rpmrb script)

* Sat Oct 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.17.1-alt1
- new version 1.17.1 (with rpmrb script)

* Thu Sep 26 2019 Vitaly Lipatov <lav@altlinux.ru> 1.17.0-alt1
- new version 1.17.0 (with rpmrb script)

* Tue Jul 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.16.0-alt1
- new version 1.16.0 (with rpmrb script)

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.15.0-alt1
- new version 1.15.0 (with rpmrb script)

* Fri May 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1.14.0-alt1
- new version 1.14.0 (with rpmrb script)

* Thu Mar 21 2019 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt1
- new version 1.13.0 (with rpmrb script)

* Fri Mar 08 2019 Vitaly Lipatov <lav@altlinux.ru> 1.12.1-alt1
- new version 1.12.1 (with rpmrb script)

* Sun Dec 23 2018 Vitaly Lipatov <lav@altlinux.ru> 1.11.1-alt1
- new version 1.11.1 (with rpmrb script)

* Wed Nov 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- new version 1.11.0 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt2
- adopt logrotate conf for ALT

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Mon Feb 26 2018 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt2
- fix pid file path in service file
- cleanup spec

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt2
- use bash4 for all shells scripts
- cleanup spec, change user/group to %netdatauser

* Tue Oct 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Thu Jul 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version (1.7.0) with rpmgs script

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- build new version

* Tue Mar 07 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt3
- replace shell to /bin/bash4 only on ALT
- fill version.txt with commit id for the release

* Fri Mar 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- split postgres module to a subpackage
- fix log dir permission

* Mon Feb 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)
- pack python modules (ALT bug 32662)
- pack /etc/netdata/charts.d/ (ALT bug 32663)
- set bash4 for bash4 using scripts (ALT bug 32663)

* Sat Oct 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- fix packing

* Sat Oct 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Mon Sep 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Thu May 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Linux Sisyphus

* Mon May 16 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.2.0-1
- netdata is now 30%% faster.
- netdata now has a registry (my-netdata menu on the dashboard).
- netdata now monitors Linux containers.
- Several more improvements, new features and bugfixes.
* Wed Apr 20 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.1.0-1
- Several new features (IPv6, SYNPROXY, Users, Users Groups).
- A lot of bug fixes and optimizations.
* Tue Mar 22 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.0.0-1
- First public release.
* Sun Nov 15 2015 Alon Bar-Lev <alonbl@redhat.com> - 0.0.0-1
- Initial add.
