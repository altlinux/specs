%global import_path github.com/grafana/grafana

%global _unpackaged_files_terminate_build 1
%define _runtimedir /run
%def_enable prebuilded_frontend

Name:		grafana
Version:	9.3.4
Release:	alt1
Summary:	Metrics dashboard and graph editor

Group:		Development/Other
License:	AGPL-3.0-only AND Apache-2.0
URL:		https://grafana.com

Source: %name-%version.tar
Patch: %name-%version.patch

Source100: %name-server.sysconfig
#Source101: %%name.logrotate
Source102: %name-server.init
Source103: %name-server.service
Source104: %name.tmpfiles


#ExclusiveArch: %%go_arches
# on ppc64le error:
# error Command failed with signal "SIGXCPU"
ExclusiveArch: %ix86 x86_64 %arm aarch64 mipsel riscv64
BuildRequires(pre): rpm-build-golang rpm-macros-nodejs
%if_disabled prebuilded_frontend
BuildRequires: npm
BuildRequires: node >= 14 node-devel node-gyp
%endif
BuildRequires: wire
BuildRequires: fontconfig libfreetype
BuildRequires: /proc

%description
Grafana is an open source, feature rich metrics dashboard and graph editor
for Graphite, Elasticsearch, OpenTSDB, Prometheus and InfluxDB.

%prep
# Build the Front-end Assets
# $ node .yarn/releases/yarn-3.2.0.cjs install
# $ git add .pnp.cjs .pnp.loader.mjs .yarn -f
# $ git commit -n --no-post-rewrite -m "add node js modules"

# Test build
# $ export NODE_OPTIONS="--max-old-space-size=8192" # Increase to 8 GB
# $ node .yarn/releases/yarn-3.2.0.cjs run build
# $ node .yarn/releases/yarn-3.2.0.cjs run plugins:build-bundled
#
# Go vendors modules
# $ go mod vendor -v
# $ git add -f vendor
# $ git commit -n --no-post-rewrite -m "update go modules by go mod vendor"

%setup -q
%patch -p1

%build

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export npm_config_devdir="$PWD/node_modules/.node-gyp"
export VERSION=%version
export COMMIT=%release
export BRANCH=altlinux

#%%golang_prepare
#cd .gopath/src/%%import_path
mkdir -p $BUILDDIR/src/github.com/grafana
ln -s %_builddir/%name-%version \
    $BUILDDIR/src/%import_path

pushd $BUILDDIR/src/%import_path

%if_disabled prebuilded_frontend

%ifarch %arm %ix86 %mips32 %mipsn32
export NODE_OPTIONS=--max_old_space_size=2048
%endif
#npm rebuild
#npm run build
#go run build.go build-frontend
node .yarn/releases/yarn-3.2.0.cjs run build
node .yarn/releases/yarn-3.2.0.cjs run plugins:build-bundled
%endif

wire gen -tags oss ./pkg/server ./pkg/cmd/grafana-cli/runner

#GO111MODULE=off CGO_ENABLED=1 go run build.go build
#%%golang_build pkg/cmd/*
CGO_ENABLED=1 go install -ldflags " -s -w  \
    -X main.version=$VERSION \
    -X main.commit=$COMMIT \
    -X main.buildBranch=$BRANCH \
    " -a ./pkg/cmd/grafana-server

CGO_ENABLED=1 go install -ldflags " -s -w  \
    -X main.version=$VERSION \
    -X main.commit=$COMMIT \
    -X main.buildBranch=$BRANCH \
    " -a ./pkg/cmd/grafana-cli

popd

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"
export GOFLAGS="-mod=vendor"

pushd $BUILDDIR/src/%import_path
# Install Front-end Assets
install -d -m 755 %buildroot%_datadir/%name
cp -pr conf %buildroot%_datadir/%name/
cp -pr public %buildroot%_datadir/%name/
%golang_install
popd

rm -rf -- %buildroot/usr/src
rm -f -- %buildroot%_bindir/govendor
rm -f -- %buildroot%_bindir/release_publisher
rm -f -- %buildroot%_bindir/slow_proxy
#TODO: package alert_webhook_listener
rm -f -- %buildroot%_bindir/alert_webhook_listener

# Install config files
install -p -D -m 640 conf/sample.ini %buildroot%_sysconfdir/%name/%name.ini
install -p -D -m 640 conf/ldap.toml %buildroot%_sysconfdir/%name/ldap.toml
mkdir -p %buildroot%_sysconfdir/%name/provisioning/{dashboards,datasources,notifiers}
install -p -D -m 640 conf/provisioning/dashboards/sample.yaml %buildroot%_sysconfdir/%name/provisioning/dashboards/sample.yaml
install -p -D -m 640 conf/provisioning/datasources/sample.yaml %buildroot%_sysconfdir/%name/provisioning/datasources/sample.yaml
install -p -D -m 640 conf/provisioning/notifiers/sample.yaml %buildroot%_sysconfdir/%name/provisioning/notifiers/sample.yaml

# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 750 %buildroot%_sharedstatedir/%name
install -d -m 755 %buildroot%_sharedstatedir/%name/plugins
# Install pid directory
install -d -m 775 %buildroot%_runtimedir/%name
# Install sysconfig
install -p -D -m 644 %SOURCE100 %buildroot%_sysconfdir/sysconfig/%name-server
# Install logrotate
#install -p -D -m 644 %%SOURCE101 %%buildroot%%_logrotatedir/%%name
# Install sysv init scripts
install -p -D -m 755 %SOURCE102 %buildroot%_initdir/%name-server
# Install systemd unit services
install -p -D -m 644 %SOURCE103 %buildroot%_unitdir/%name-server.service
install -p -D -m 644 %SOURCE104 %buildroot%_tmpfilesdir/%name.conf

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name -c 'Grafana Daemon' \
    -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name-server
# create grafana.db with secure permissions on new installations
# otherwise grafana-server is creating grafana.db on first start
# with world-readable permissions, which may leak encrypted datasource
# passwords to all users (if the secret_key in grafana.ini was not changed)
if [ "$1" = 1 ] && [ ! -f %_sharedstatedir/%name/grafana.db ]; then
    touch %_sharedstatedir/%name/grafana.db
fi
 
# apply secure permissions to grafana.db if it exists
# (may not exist on upgrades, because users can choose between sqlite/mysql/postgres)
if [ -f %_sharedstatedir/%name/grafana.db ]; then
    chown %name:%name %_sharedstatedir/%name/grafana.db
    chmod 640 %_sharedstatedir/%name/grafana.db
fi

%preun
%preun_service %name-server

%files
%doc CHANGELOG.md LICENSE README.md
%_bindir/%name-cli
%_bindir/%name-server
%config(noreplace) %_sysconfdir/sysconfig/%name-server
%_initdir/%name-server
%_unitdir/%name-server.service
%_tmpfilesdir/%name.conf
%dir %attr(0750, root, %name) %_sysconfdir/%name
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning/dashboards
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning/datasources
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning/notifiers
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.ini
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/ldap.toml
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/provisioning/*/*.yaml
#%%config(noreplace) %%_logrotatedir/%%name
%dir %attr(0775, root, %name) %_logdir/%name
%dir %attr(0750, %name, %name) %_sharedstatedir/%name
%dir %attr(0755, %name, %name) %dir %_sharedstatedir/%name/plugins
%_datadir/%name

%changelog
* Wed Jan 25 2023 Alexey Shabalin <shaba@altlinux.org> 9.3.4-alt1
- 9.3.4

* Wed Dec 07 2022 Alexey Shabalin <shaba@altlinux.org> 9.3.1-alt1
- 9.3.1
- Fixes:
  + CVE-2022-32149
  + CVE-2022-27664
  + CVE-2022-35957
  + CVE-2022-36062
  + CVE-2022-31107
  + CVE-2022-31097
  + CVE-2022-29170

* Tue Apr 26 2022 Alexey Shabalin <shaba@altlinux.org> 8.5.0-alt1
- 8.5.0
- Use pre-builded frontend
- Fixes:
  + CVE-2022-24812
  + CVE-2022-21702
  + CVE-2022-21703
  + CVE-2022-21713
  + CVE-2021-43813
  + CVE-2021-43815
  + CVE-2021-41244
  + CVE-2021-41174

* Thu Dec 09 2021 Alexey Shabalin <shaba@altlinux.org> 8.1.8-alt1
- 8.1.8 (Fixes: CVE-2021-43798, CVE-2021-39226)

* Sat Aug 21 2021 Alexey Shabalin <shaba@altlinux.org> 8.1.2-alt1
- 8.1.2

* Wed Aug 18 2021 Alexey Shabalin <shaba@altlinux.org> 8.1.1-alt1
- 8.1.1

* Fri Apr 23 2021 Alexey Shabalin <shaba@altlinux.org> 7.5.4-alt1
- 7.5.4

* Sat Jan 23 2021 Alexey Shabalin <shaba@altlinux.org> 7.3.7-alt1
- 7.3.7

* Wed Aug 19 2020 Alexey Shabalin <shaba@altlinux.org> 7.1.3-alt1
- 7.1.3

* Sat Jul 04 2020 Alexey Shabalin <shaba@altlinux.org> 7.0.5-alt1
- 7.0.5

* Thu Jun 04 2020 Alexey Shabalin <shaba@altlinux.org> 7.0.3-alt1
- 7.0.3 (Fixes: CVE-2020-13379)

* Fri May 29 2020 Alexey Shabalin <shaba@altlinux.org> 7.0.1-alt1
- 7.0.1

* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 6.7.3-alt1
- 6.7.3
- create grafana.db on first installation
- change permissions of /var/lib/grafana to 750 (Fixes: CVE-2020-12458)
- change permissions of /var/lib/grafana/grafana.db to 640 and
  user/group grafana:grafana (CVE-2020-12458)

* Mon Mar 02 2020 Alexey Shabalin <shaba@altlinux.org> 6.6.2-alt1
- 6.6.2

* Sat Sep 07 2019 Alexey Shabalin <shaba@altlinux.org> 6.3.5-alt2
- fixed perm of /run/grafana in tmpfiles config
- not package /run/grafana

* Thu Sep 05 2019 Alexey Shabalin <shaba@altlinux.org> 6.3.5-alt1
- 6.3.5

* Fri Aug 30 2019 Alexey Shabalin <shaba@altlinux.org> 6.3.4-alt1
- 6.3.4 (Fixes: CVE-2019-15043)

* Tue Aug 13 2019 Alexey Shabalin <shaba@altlinux.org> 6.3.2-alt1
- 6.3.2

* Fri Jul 19 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.5-alt2
- build for all arches

* Fri Jul 12 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.5-alt1
- 6.2.5

* Thu Mar 28 2019 Alexey Shabalin <shaba@altlinux.org> 6.0.2-alt1
- 6.0.2

* Fri Mar 01 2019 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt2
- fix show version in webui
- change runtimedir from /var/run/grafana to /run/grafana

* Wed Feb 27 2019 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt1
- 6.0.0

* Wed Jan 23 2019 Alexey Shabalin <shaba@altlinux.org> 5.4.3-alt1
- 5.4.3

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 5.4.2-alt1
- 5.4.2

* Mon Oct 15 2018 Alexey Shabalin <shaba@altlinux.org> 5.3.0-alt1
- 5.3.0

* Thu Jun 21 2018 Alexey Shabalin <shaba@altlinux.ru> 5.1.4-alt2
- update init script and systemd unit
- fix package files and config

* Wed Jun 20 2018 Alexey Shabalin <shaba@altlinux.ru> 5.1.4-alt1
- 5.1.4

* Wed Feb 14 2018 Alexey Shabalin <shaba@altlinux.ru> 4.6.3-alt1
- 4.6.3

* Mon Dec 04 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.2-alt1
- 4.6.2

* Mon Oct 30 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.0-alt1
- 4.6.0

* Fri Oct 13 2017 Alexey Shabalin <shaba@altlinux.ru> 4.5.2-alt1
- 4.5.2

* Mon Aug 28 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt2
- fix start options for systemd and sysvinit

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt1
- 4.4.3
- fix pidfile path in systemd unit
- fix run with sysv init script

* Tue Aug 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.2-alt1
- 4.4.2
- fix systemd unit
- rm phantomjs blob

* Thu Jul 27 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt2
- fix service name in post and preun

* Tue Jul 25 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt1
- First build for ALTLinux.
