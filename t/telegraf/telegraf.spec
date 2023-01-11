%global import_path github.com/influxdata/telegraf

%global _unpackaged_files_terminate_build 1

Name:		telegraf
Version:	1.25.0
Release:	alt1
Summary:	The plugin-driven server agent for collecting and reporting metrics

Group:		Development/Other
License:	MIT
URL:		https://github.com/influxdata/telegraf

Source0:	%name-%version.tar

Source101: telegraf.logrotate
Source102: telegraf.init
Source103: telegraf.service
Source104: telegraf.tmpfiles

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.19

%description
Telegraf is an agent written in Go for collecting, processing, aggregating, and writing metrics.

Design goals are to have a minimal memory footprint with a plugin system so that developers
in the community can easily add support for collecting metrics from well known services
(like Hadoop, Postgres, or Redis) and third party APIs (like Mailchimp, AWS CloudWatch,
or Google Analytics).

%prep
# $ git rm -rf vendor
# $ go mod vendor -v
# $ git add -f vendor
# $ git commit -m "update go pkgs by go mod vendor"

%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

cd .gopath/src/%import_path
export INTERNAL_PKG=github.com/influxdata/telegraf/internal
export VERSION=%version
export COMMIT=%release
export BRANCH=altlinux

CGO_ENABLED=0 GOGC=off go install -ldflags " \
    -X $INTERNAL_PKG.Version=$VERSION \
    -X $INTERNAL_PKG.Commit=$COMMIT \
    -X $INTERNAL_PKG.Branch=$BRANCH \
    " -a ./cmd/telegraf

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"
%golang_install

# cleanup
rm -rf -- %buildroot%_datadir

# Install config files
install -p -D -m 640 etc/telegraf.conf %buildroot%_sysconfdir/%name/%name.conf
install -d -m 750 %buildroot%_sysconfdir/%name/%name.d
# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 750 %buildroot%_sharedstatedir/%name
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
%_sbindir/useradd -r -g %name -G %name  -c 'Telegraf Agent Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:
%_sbindir/usermod -a -G proc telegraf ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc docs/*
%_bindir/%name
%_initdir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%dir %attr(0750, root, %name) %_sysconfdir/%name
%dir %attr(0750, root, %name) %_sysconfdir/%name/%name.d
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.conf
%config(noreplace) %_logrotatedir/%name
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0775, root, %name) %_runtimedir/%name
%dir %attr(0750, %name, %name) %_sharedstatedir/%name

%changelog
* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 1.25.0-alt1
- 1.25.0

* Thu Oct 13 2022 Alexey Shabalin <shaba@altlinux.org> 1.24.2-alt1
- 1.24.2
- /var/run -> /run in init script and tmpfiles

* Mon Apr 25 2022 Alexey Shabalin <shaba@altlinux.org> 1.22.2-alt1
- 1.22.2

* Thu Mar 24 2022 Alexey Shabalin <shaba@altlinux.org> 1.22.0-alt1
- 1.22.0

* Wed Jan 26 2022 Alexey Shabalin <shaba@altlinux.org> 1.21.2-alt1
- 1.21.2

* Wed Nov 17 2021 Alexey Shabalin <shaba@altlinux.org> 1.20.3-alt1
- 1.20.3

* Fri Jul 30 2021 Alexey Shabalin <shaba@altlinux.org> 1.19.2-alt1
- 1.19.2

* Fri Feb 19 2021 Alexey Shabalin <shaba@altlinux.org> 1.17.3-alt1
- 1.17.3

* Thu Nov 12 2020 Alexey Shabalin <shaba@altlinux.org> 1.16.1-alt1
- 1.16.1

* Sun Oct 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.16.0-alt1
- 1.16.0

* Sat Sep 19 2020 Alexey Shabalin <shaba@altlinux.org> 1.15.3-alt1
- 1.15.3

* Wed Aug 05 2020 Alexey Shabalin <shaba@altlinux.org> 1.15.2-alt1
- 1.15.2

* Fri May 29 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.3-alt1
- 1.14.3

* Tue Apr 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.1-alt1
- 1.14.1

* Sat Apr 11 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.0-alt1
- 1.14.0

* Sun Dec 22 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.0-alt1
- 1.13.0

* Wed Sep 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.1-alt1
- 1.12.1

* Tue Aug 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.4-alt1
- 1.11.4

* Thu Jul 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.2-alt1
- 1.11.2

* Thu Mar 28 2019 Alexey Shabalin <shaba@altlinux.org> 1.10.1-alt1
- 1.10.1
- add user telegraf to proc group (fixed ALT#35130)

* Wed Feb 27 2019 Alexey Shabalin <shaba@altlinux.org> 1.9.5-alt1
- 1.9.5

* Tue Feb 26 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.9.2-alt2
- Added support parked ("P") state of processes.

* Mon Jan 21 2019 Alexey Shabalin <shaba@altlinux.org> 1.9.2-alt1
- 1.9.2

* Thu Oct 11 2018 Alexey Shabalin <shaba@altlinux.org> 1.8.1-alt1
- 1.8.1

* Sat Apr 28 2018 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Feb 14 2018 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt2
- fix "commit"

* Thu Feb 01 2018 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Mon Oct 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Thu Oct 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt1
- rebuild with Universal Branch Tag
- fix run with sysv init script

* Thu Jul 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt1
- 1.3.5
- upadte init script
- add user home dir to files

* Mon Jul 24 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt2
- add sysv init, systemd unit, logrotate config, tmpfiles

* Sun Jul 23 2017 Alexey Gladkov <legion@altlinux.ru> 1.3.4-alt1
- First build for ALTLinux.
