%global import_path github.com/influxdata/kapacitor
%global commit 06a16e51ceb5b7086b3b855969c3f93532da1550

%global _unpackaged_files_terminate_build 1

Name:		kapacitor
Version:	1.5.9
Release:	alt1
Summary:	Open source framework for processing, monitoring, and alerting on time series data

Group:		Development/Other
License:	MIT
URL:		https://github.com/influxdata/kapacitor

Source0:	%name-%version.tar

Source101: %name.logrotate
Source102: %name.init
Source103: %name.service
Source104: %name.tmpfiles

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
Open source framework for processing, monitoring, and alerting on time series data.

%prep
%setup -q

%build

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

%golang_build cmd/*

#go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./...

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install

rm -rf -- %buildroot%_datadir

# Install config files
install -p -D -m 640 etc/kapacitor/kapacitor.conf %buildroot%_sysconfdir/%name/%name.conf
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

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name  -c 'Kapacitor Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/kapacitor
%_bindir/kapacitord
%_initdir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%dir %attr(0750, root, %name) %_sysconfdir/%name
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.conf
%config(noreplace) %_logrotatedir/%name
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0775, root, %name) %_runtimedir/%name
%dir %attr(0755, %name, %name) %_sharedstatedir/%name

%changelog
* Wed Apr 07 2021 Alexey Shabalin <shaba@altlinux.org> 1.5.9-alt1
- 1.5.9

* Thu Jul 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt2
- NMU: remove %ubt from release

* Mon Aug 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1%ubt
- 1.3.3

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1%ubt
- rebuild with Universal Branch Tag
- fix run with sysv init script

* Tue Jul 25 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- First build for ALTLinux.
