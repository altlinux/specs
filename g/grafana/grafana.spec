%global import_path github.com/grafana/grafana
%global commit 989bf2067c199ffd2aa38a29f2c4e12cea689925

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*


Name:		grafana
Version:	4.6.2
Release:	alt1%ubt
Summary:	Metrics dashboard and graph editor

Group:		Development/Other
License:	ASL 2.0
URL:		https://grafana.com

Source: %name-%version.tar
Source2: %name-%version.linux-x64.tar

Source100: %name-server.sysconfig
#Source101: %name.logrotate
Source102: %name-server.init
Source103: %name-server.service
Source104: %name.tmpfiles


#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64
BuildRequires(pre): rpm-build-golang rpm-build-ubt
BuildRequires: npm yarn
BuildRequires: fontconfig libfreetype
BuildRequires: /proc

%add_verify_elf_skiplist %_datadir/%name/vendor/phantomjs/phantomjs

%description
Grafana is an open source, feature rich metrics dashboard and graph editor
for Graphite, Elasticsearch, OpenTSDB, Prometheus and InfluxDB.

%prep
%setup -q
tar -xf %SOURCE2

%build
# Important!!!
# The %%builddir/.gopath created by the hands. It contains the dependencies required for your project.
# This is necessary because the gdm cannot work with the vendor directory and always tries to update
# all dependencies from the external servers. So, we can't use Makefile to compile.
#
# $ export GOPATH="$PWD/.gopath"
# $ git rm -rf -- "$GOPATH"
# $ make
# $ find $GOPATH -type d -name .git |xargs rm -rf --
# $ git add "$GOPATH"
# Build the Front-end Assets
# $ npm install -g yarn
# $ yarn install --pure-lockfile
# $ npm install -g grunt-cli
# $ grunt release
# move from dist to .gear/grafana-X.X.X.linux-x64.tar

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

%golang_build pkg/cmd/*
#go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./...

#npm run build

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"


pushd .gopath/src/%import_path
%golang_install
popd

rm -rf -- %buildroot/usr/src
rm -f -- %buildroot%_bindir/govendor

# Install prebuilded Front-end Assets
install -d -m 755 %buildroot%_datadir
cp -pr %name-%version %buildroot%_datadir/%name
# Cleanup
rm -rf -- %buildroot%_datadir/%name/scripts
rm -f -- %buildroot%_datadir/%name/*.md
rm -f -- %buildroot%_datadir/%name/vendor/phantomjs/phantomjs

# Install config files
install -p -D -m 640 conf/sample.ini %buildroot%_sysconfdir/%name/%name.ini
# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 755 %buildroot%_sharedstatedir/%name
# Install pid directory
install -d -m 775 %buildroot%_runtimedir/%name
# Install sysconfig
install -p -D -m 644 %SOURCE100 %buildroot%_sysconfdir/sysconfig/%name-server
# Install logrotate
#install -p -D -m 644 %%SOURCE101 %buildroot%_logrotatedir/%name
# Install sysv init scripts
install -p -D -m 755 %SOURCE102 %buildroot%_initdir/%name-server
# Install systemd unit services
install -p -D -m 644 %SOURCE103 %buildroot%_unitdir/%name-server.service
install -p -D -m 644 %SOURCE104 %buildroot%_tmpfilesdir/%name.conf

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name  -c 'Grafana Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name-server

%preun
%preun_service %name-server

%files
%doc CHANGELOG.md LICENSE.md README.md
%_bindir/%name-cli
%_bindir/%name-server
%config(noreplace) %_sysconfdir/sysconfig/%name-server
%_initdir/%name-server
%_unitdir/%name-server.service
%_tmpfilesdir/%name.conf
%dir %attr(0750, root, %name) %_sysconfdir/%name
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.ini
#%config(noreplace) %_logrotatedir/%name
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0775, root, %name) %_runtimedir/%name
%dir %attr(0755, %name, %name) %_sharedstatedir/%name
%_datadir/%name

%changelog
* Mon Dec 04 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.2-alt1%ubt
- 4.6.2

* Mon Oct 30 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.0-alt1%ubt
- 4.6.0

* Fri Oct 13 2017 Alexey Shabalin <shaba@altlinux.ru> 4.5.2-alt1%ubt
- 4.5.2

* Mon Aug 28 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt2%ubt
- fix start options for systemd and sysvinit

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt1%ubt
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
