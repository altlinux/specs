%global _unpackaged_files_terminate_build 1
%def_enable prebuilded_frontend

Name: prometheus
Version: 3.12.0
Release: alt1
Summary: Prometheus monitoring system and time series database

Group: Development/Other
License: Apache-2.0
Url: https://prometheus.io
Vcs: https://github.com/prometheus/prometheus.git

Source0: %name-%version.tar
Source1: vendor-%version.tar
Source2: %name.sysconfig
Source3: %name.init
Source4: %name.service
Source5: %name.tmpfiles
Source6: %name.yml
Patch0: %name-%version-%release.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25
%if_disabled prebuilded_frontend
BuildRequires: rpm-build-nodejs
%endif

Requires: %name-common = %EVR

%description
Prometheus is an open-source systems monitoring and alerting toolkit.

Prometheus's main features are:
 - a multi-dimensional data model with time series data
   identified by metric name and key/value pairs
 - a flexible query language to leverage this dimensionality
 - no reliance on distributed storage; single server nodes are autonomous
 - time series collection happens via a pull model over HTTP
 - pushing time series is supported via an intermediary gateway
 - targets are discovered via service discovery or static configuration
 - multiple modes of graphing and dashboarding support
 - support for hierarchical and horizontal federation

%package common
Summary: Common package for Prometheus
Group: Development/Other
BuildArch: noarch

%description common
Prometheus is an open-source systems monitoring and alerting toolkit.

This package contains the common files and settings for Prometheus.

%prep
%setup -a 1
%patch0 -p1
# Build the Front-end Assets
# $ cd web/ui
# $ npm install
# $ git add -f node_modules
# $ git commit -n --no-post-rewrite -m "add node js modules"

%build
%if_disabled prebuilded_frontend
#building React app
pushd web/ui
npm run build
popd
%endif

export BUILDDIR="$PWD/.gopath"
export GOPATH="$BUILDDIR:%go_path"
export TAGS="netgo,builtinassets"
export LDFLAGS="-X github.com/prometheus/common/version.Version=%version  \
         -X github.com/prometheus/common/version.Revision=%release \
         -X github.com/prometheus/common/version.Branch=tarball      \
         -X github.com/prometheus/common/version.BuildDate=$(date -u +%%Y%%m%%d)"
# writing assets
gofmt -w web/ui
scripts/compress_assets.sh
# building project
%golang_build cmd/*

%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1
mkdir -p %buildroot{%_initdir,%_unitdir,%_tmpfilesdir,%_sysconfdir/sysconfig,{%_sysconfdir,%_datadir,%_localstatedir}/%name}

%golang_install

#install -m0755 prometheus %buildroot%_bindir/%name
#install -m0755 promtool %buildroot%_bindir/promtool
install -m0640 %SOURCE6 %buildroot%_sysconfdir/%name/%name.yml
install -m0640 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0755 %SOURCE3 %buildroot%_initdir/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service
install -m0644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf

# Build man pages.
mkdir -p %buildroot%_man1dir
%buildroot%_bindir/prometheus --help-man > \
    %buildroot%_man1dir/prometheus.1
%buildroot%_bindir/promtool --help-man > \
    %buildroot%_man1dir/promtool.1
sed -i '/^  /d; /^.SH "NAME"/,+1c.SH "NAME"\nprometheus \\- The Prometheus monitoring server' \
    %buildroot%_man1dir/prometheus.1
sed -i '/^  /d; /^.SH "NAME"/,+1c.SH "NAME"\npromtool \\- Tooling for the Prometheus monitoring system' \
    %buildroot%_man1dir/promtool.1

%check
export LDFLAGS="-X github.com/prometheus/common/version.Version=%version \
        -X github.com/prometheus/common/version.Revision=%release \
        -X github.com/prometheus/common/version.Branch=tarball \
        -X github.com/prometheus/common/version.BuildDate=$(date -u +%%Y%%m%%d)"
for dir in cmd/*; do
    [ -d "$dir" ] || continue
    pushd "$dir"
        %gotest
    popd
done


%pre common
%_sbindir/groupadd -r -f %name > /dev/null 2>&1 ||:
%_sbindir/useradd -r -g %name -d %_localstatedir/%name -s /dev/null -c "Prometheus services" %name > /dev/null 2>&1 ||:
%_sbindir/usermod -a -G proc %name ||:

%post
%post_service %name

%preun
%preun_service %name
%files
%doc LICENSE README.md docs documentation/examples
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/sysconfig/%name
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/*
%_man1dir/*

%files common
%dir %attr(0750, root, %name) %_sysconfdir/%name
%_tmpfilesdir/%name.conf
%dir %attr(0750, %name, %name) %_localstatedir/%name

%changelog
* Mon Jun 25 2026 Artyom Sinyugin <writers@altlinux.org> 3.12.0-alt1
- New version 3.12.0.
- Restrict default web listener to localhost.
- Harden systemd service and tighten permissions on configs and state dirs.

* Fri Jan 23 2026 Artyom Sinyugin <writers@altlinux.org> 3.9.1-alt1
- 3.9.1

* Fri Aug 29 2025 Artyom Sinyugin <writers@altlinux.org> 3.5.0-alt1
- New version 3.5.0.

* Sat Jun 28 2025 Artyom Sinyugin <writers@altlinux.org> 3.4.1-alt2
- fix prebuilt web UI (ALT#54920)

* Thu Jun 19 2025 Artyom Sinyugin <writers@altlinux.org> 3.4.1-alt1
- 3.4.1

* Fri Feb 14 2025 Artyom Sinyugin <writers@altlinux.org> 3.1.0-alt1
- 3.1.0

* Mon Aug 26 2024 Alexey Shabalin <shaba@altlinux.org> 2.54.0-alt1
- 2.54.0

* Mon Apr 01 2024 Alexey Shabalin <shaba@altlinux.org> 2.51.1-alt1
- 2.51.1
- add more hardening options to systemd serrvice
- add default node exporter 9100 port to config
- /var/run -> /run in tmpfile

* Fri Oct 06 2023 Alexey Shabalin <shaba@altlinux.org> 2.47.1-alt1
- 2.47.1

* Thu Jul 27 2023 Alexey Shabalin <shaba@altlinux.org> 2.46.0-alt1
- 2.46.0

* Tue Dec 06 2022 Alexey Shabalin <shaba@altlinux.org> 2.40.5-alt1
- 2.40.5

* Fri Jul 30 2021 Alexey Shabalin <shaba@altlinux.org> 2.28.0-alt1
- 2.28.0 (Fixes: CVE-2021-29622)

* Tue Jan 26 2021 Alexey Shabalin <shaba@altlinux.org> 2.24.1-alt1
- 2.24.1.

* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 2.18.1-alt2
- add user prometheus to proc group

* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 2.18.1-alt1
- 2.18.1.

* Sat Apr 18 2020 Alexey Shabalin <shaba@altlinux.org> 2.17.1-alt1
- 2.17.1

* Wed Mar 18 2020 Alexey Shabalin <shaba@altlinux.org> 2.16.0-alt1
- 2.16.0 (Fixes: CVE-2019-10215)

* Wed Jul 17 2019 Alexey Shabalin <shaba@altlinux.org> 2.11.1-alt1
- 2.11.1

* Wed Mar 06 2019 Alexey Shabalin <shaba@altlinux.org> 2.7.2-alt1
- 2.7.2

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 2.6.1-alt1
- 2.6.1

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt2
- move adduser, tmpfiles and /etc/prometheus to prometheus-common package
- update systemd unit

* Tue May 08 2018 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt1
- Initial build for ALT.
