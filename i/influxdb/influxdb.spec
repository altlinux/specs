%global import_path github.com/influxdata/influxdb
%global commit 5887e92e8950435ac7e496ff8dada784051284b7

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name:		influxdb
Version:	1.3.1
Release:	alt1
Summary:	Distributed time-series database

Group:		Development/Other
License:	MIT
URL:		https://github.com/influxdata/influxdb

Source0:	%name-%version.tar

Source101: influxdb.logrotate
Source102: influxdb.init
Source103: influxdb.service
Source104: influxdb.tmpfiles

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: xmlto asciidoc

%description
InfluxDB is an open source time series database with
no external dependencies. It's useful for recording metrics,
events, and performing analytics.

%prep
%setup -q

%build
# Important!!!
# The %builddir/.gopath created by the hands. It contains the dependencies required for your project.
# This is necessary because the gdm cannot work with the vendor directory and always tries to update
# all dependencies from the external servers. So, we can't use Makefile to compile.
#
# $ export GOPATH="$PWD/.gopath"
# $ git rm -rf -- "$GOPATH"
# $ make
# $ find $GOPATH -type d -name .git |xargs rm -rf --
# $ git add "$GOPATH"

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./...

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install

rm -rf -- %buildroot%_datadir
rm -f %buildroot%_bindir/{gdm,stress_test_server,test_client}

# Install config files
install -p -D -m 640 etc/config.sample.toml %buildroot%_sysconfdir/%name/%name.conf
# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 755 %buildroot%_sharedstatedir/%name
# Install pid directory
install -d -m 775 %buildroot%_runtimedir/%name
# Install logrotate
install -p -D -m 644 %SOURCE101 %buildroot%_logrotatedir/%name
# Install sysv init scripts
install -p -D -m 755 %SOURCE102 %buildroot%_initdir/%name
# Install systemd unit services
install -p -D -m 644 %SOURCE103 %buildroot%_unitdir/%name.service
install -p -D -m 644 %SOURCE104 %buildroot%_tmpfilesdir/%name.conf
# Install man files
%make_install DESTDIR=%buildroot%_prefix -C man install

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name  -c 'InfluxDB Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/influx
%_bindir/influx_inspect
%_bindir/influx_stress
%_bindir/influx_tsm
%_bindir/influxd
%_man1dir/influx*.1.*
%_initdir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%dir %attr(0750, root, influxdb) %_sysconfdir/%name
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.conf
%config(noreplace) %_logrotatedir/%name
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0775, root, %name) %_runtimedir/%name
%dir %attr(0755, %name, %name) %_sharedstatedir/%name

%changelog
* Mon Jul 24 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- First build for ALTLinux.

