%define _unpackaged_files_terminate_build 1

%global provider        github
%global provider_tld    com
%global project         docker
%global repo            docker
%global servicename     docker

%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit      d7573ab8672555762688f4c7ab8cc69ae8ec1a47
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    docker-engine
Version: 23.0.0
Release: alt3
Summary: The open-source application container engine
License: Apache-2.0
Group: System/Configuration/Other

Url: https://github.com/moby/moby
ExclusiveArch: %go_arches
Conflicts: docker

Source0: %name-%version.tar
Source1: %servicename.service
Source2: %servicename.init
Source3: %servicename.sysconf
Source4: %servicename-storage.sysconf
Source5: daemon.json

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc gcc golang >= 1.3 systemd-devel libdevmapper-devel libbtrfs-devel libseccomp-devel
Requires: tar xz
Provides: docker-io = %version-%release
Provides: docker-ce = %version-%release
Obsoletes: docker-io <= 17.05.0
Obsoletes: docker-io-devel <= 17.05.0
Obsoletes: docker-ce < 20.10.0
Requires: /usr/bin/docker-proxy
Requires: docker-containerd >= 1.0.2-alt1
Requires: docker-runc >= 1.0.0-alt4.rc5
Requires: docker-init >= 0.17.0-alt1
Requires: docker-cli >= 20.10.0-alt1.rc2
Requires: iptables

# do not extract debuginfo
%define __find_debuginfo_files %nil

%description
Docker Engine is an open source containerization technology for building and
containerizing your applications. Docker Engine acts as a client-server application with:

* A server with a long-running daemon process dockerd.
* APIs which specify interfaces that programs can use to talk to and instruct the Docker daemon.
* A command line interface (CLI) client docker

%package rootless
Summary: Use docker rootless
Group: System/Configuration/Other
Requires: rootlesskit %name slirp4netns

%description rootless
%summary

%package -n docker-proxy
Summary: docker-proxy util
Group: Development/Other

%description -n docker-proxy
This package provides docker-proxy util.

%prep
%setup

%build
# Temporary workaround to build with golang 1.16. Waiting for upstream to
# add go modules support.
export GO111MODULE=off
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"

%golang_prepare

export DOCKER_GITCOMMIT=%{shortcommit}
export DOCKER_BUILDTAGS='selinux journald pkcs11 seccomp'
export VERSION=%{version}
hack/make.sh dynbinary

%install
# install binary
install -d %{buildroot}%{_bindir}
install -p -m 755 bundles/dynbinary-daemon/dockerd %{buildroot}%{_bindir}/dockerd
install -p -m 755 bundles/dynbinary-daemon/docker-proxy %{buildroot}%{_bindir}/docker-proxy

# install udev rules
install -d %{buildroot}%{_sysconfdir}/udev/rules.d
install -m 644 -p contrib/udev/80-docker.rules %{buildroot}%{_sysconfdir}/udev/rules.d

# install storage dir
install -d %{buildroot}%{_sharedstatedir}/%{servicename}

# install systemd/init scripts
install -p -D -m 644 altlinux/%{servicename}.service %{buildroot}%{_unitdir}/%{servicename}.service
install -p -m 644 contrib/init/systemd/docker.socket %{buildroot}%{_unitdir}/
install -p -D -m 755 altlinux/%{servicename}.init %{buildroot}%{_initddir}/%{servicename}

install -d %buildroot%_sysconfdir/sysconfig
install -p -m 644 altlinux/docker.sysconf %buildroot%_sysconfdir/sysconfig/docker
install -p -m 644 altlinux/docker-storage.sysconf %buildroot%_sysconfdir/sysconfig/docker-storage

install -d %buildroot%_sysconfdir/docker
install -p -m 644 altlinux/daemon.json %buildroot%_sysconfdir/docker/daemon.json

# install rootless scripts
install -p -D -m 755 contrib/dockerd-rootless-setuptool.sh %{buildroot}%{_bindir}/dockerd-rootless-setuptool.sh
install -p -D -m 755 contrib/dockerd-rootless.sh %{buildroot}%{_bindir}/dockerd-rootless.sh

%pre
getent group docker > /dev/null || %{_sbindir}/groupadd -r docker
exit 0

%post
%post_service docker

%preun
%preun_service docker

%files rootless
%_bindir/dockerd-rootless-setuptool.sh
%_bindir/dockerd-rootless.sh

%files -n docker-proxy
%_bindir/docker-proxy

%files
%doc AUTHORS LICENSE
%doc MAINTAINERS NOTICE
%doc CONTRIBUTING.md README.md
%config(noreplace) %{_sysconfdir}/sysconfig/docker
%config(noreplace) %{_sysconfdir}/sysconfig/docker-storage
%config(noreplace) %{_sysconfdir}/docker/daemon.json
%{_bindir}/dockerd
%{_unitdir}/docker.service
%{_unitdir}/docker.socket
%_initdir/docker
%dir %{_sharedstatedir}/docker
%{_sysconfdir}/udev/rules.d/80-docker.rules

%changelog
* Thu Feb 2 2023 Vladimir Didenko <cow@altlinux.org> 23.0.0-alt3
- 23.0.0 release

* Sat Jan 21 2023 Vladimir Didenko <cow@altlinux.org> 23.0.0-alt2.rc3
- 23.0.0-rc3

* Fri Jan 20 2023 Vladimir Didenko <cow@altlinux.org> 23.0.0-alt1.rc2
- 23.0.0-rc2

* Fri Jan 20 2023 Vladimir Didenko <cow@altlinux.org> 20.10.23-alt1
- 20.10.23

* Mon Dec 19 2022 Vladimir Didenko <cow@altlinux.org> 20.10.22-alt1
- 20.10.22

* Fri Oct 28 2022 Vladimir Didenko <cow@altlinux.org> 20.10.21-alt1
- 20.10.21

* Thu Oct 20 2022 Vladimir Didenko <cow@altlinux.org> 20.10.20-alt1
- 20.10.20 (Fixes: CVE-2022-39253)

* Fri Oct 14 2022 Vladimir Didenko <cow@altlinux.org> 20.10.19-alt1
- 20.10.19

* Mon Sep 12 2022 Vladimir Didenko <cow@altlinux.org> 20.10.18-alt1
- 20.10.18 (Fixes: CVE-2022-36109)

* Wed Jun 8 2022 Vladimir Didenko <cow@altlinux.org> 20.10.17-alt1
- 20.10.17

* Tue May 17 2022 Vladimir Didenko <cow@altlinux.org> 20.10.16-alt1
- 20.10.16

* Thu May 12 2022 Vladimir Didenko <cow@altlinux.org> 20.10.15-alt1
- 20.10.15

* Mon Mar 28 2022 Vladimir Didenko <cow@altlinux.org> 20.10.14-alt1
- 20.10.14 (Fixes: CVE-2022-24769)

* Wed Mar 23 2022 Mikhail Gordeev <obirvalger@altlinux.org> 20.10.13-alt2
- add rootless subpackage

* Fri Mar 11 2022 Vladimir Didenko <cow@altlinux.org> 20.10.13-alt1
- 20.10.13

* Wed Dec 1 2021 Vladimir Didenko <cow@altlinux.org> 20.10.11-alt1
- 20.10.11

* Mon Oct 25 2021 Vladimir Didenko <cow@altlinux.org> 20.10.10-alt1
- 20.10.10

* Wed Oct 6 2021 Vladimir Didenko <cow@altlinux.org> 20.10.9-alt1
- 20.10.9 (Fixes: CVE-2021-39293)

* Thu Aug 5 2021 Vladimir Didenko <cow@altlinux.org> 20.10.8-alt1
- 20.10.8

* Fri Jun 18 2021 Vladimir Didenko <cow@altlinux.org> 20.10.7-alt1
- 20.10.7

* Fri Apr 30 2021 Vladimir Didenko <cow@altlinux.org> 20.10.6-alt1
- 20.10.6

* Thu Mar 11 2021 Vladimir Didenko <cow@altlinux.org> 20.10.5-alt1
- 20.10.5

* Sat Feb 20 2021 Vladimir Didenko <cow@altlinux.org> 20.10.3-alt2
- fix build with golang 1.16

* Tue Feb 09 2021 Vladimir Didenko <cow@altlinux.org> 20.10.3-alt1
- 20.10.3

* Tue Jan 12 2021 Vladimir Didenko <cow@altlinux.org> 20.10.2-alt1
- 20.10.2

* Wed Dec 23 2020 Vladimir Didenko <cow@altlinux.org> 20.10.1-alt1
- 20.10.1

* Wed Dec 9 2020 Vladimir Didenko <cow@altlinux.org> 20.10.0-alt2
- 20.10.0 release

* Fri Dec 4 2020 Vladimir Didenko <cow@altlinux.org> 20.10.0-alt1.rc2
- rename package to docker-engine because of new upstream repo
- 20.10.0-rc2

* Sat Oct 24 2020 Alexey Shabalin <shaba@altlinux.org> 19.03.13-alt2
- fix docker and dockerd --version
- update default docker daemon config (daemon.json)
- update systemd service unit and install docker.socket

* Wed Sep 30 2020 Vladimir Didenko <cow@altlinux.org> 19.03.13-alt1
- 19.03.13

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 19.03.12-alt1
- 19.03.12

* Fri Jun 5 2020 Vladimir Didenko <cow@altlinux.org> 19.03.11-alt1
- 19.03.11 (fixes: CVE-2020-13401)

* Fri May 29 2020 Vladimir Didenko <cow@altlinux.org> 19.03.10-alt1
- 19.03.10

* Thu Mar 12 2020 Vladimir Didenko <cow@altlinux.org> 19.03.8-alt1
- 19.03.8 (better mitigation for CVE-2019-14271)

* Tue Feb 18 2020 Vladimir Didenko <cow@altlinux.org> 19.03.6-alt1
- 19.03.6
- Fix license name

* Fri Nov 15 2019 Vladimir Didenko <cow@altlinux.org> 19.03.5-alt1
- 19.03.5

* Thu Oct 10 2019 Vladimir Didenko <cow@altlinux.org> 19.03.3-alt1
- 19.03.3

* Thu Sep 12 2019 Vladimir Didenko <cow@altlinux.org> 19.03.2-alt1
- 19.03.2

* Thu Sep 05 2019 Mikhail Gordeev <obirvalger@altlinux.org> 19.03.1-alt2
- Make udev rules not executable

* Wed Aug 7 2019 Vladimir Didenko <cow@altlinux.org> 19.03.1-alt1
- 19.03.1 (fixes CVE-2019-14271)

* Thu Jul 25 2019 Vladimir Didenko <cow@altlinux.org> 19.03.0-alt1
- 19.03.0

* Wed Jul 24 2019 Mikhail Gordeev <obirvalger@altlinux.org> 18.09.8-alt1
- 18.09.8

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 18.09.7-alt2
- fix spec file

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 18.09.7-alt1
- 18.09.7

* Wed May 8 2019 Vladimir Didenko <cow@altlinux.org> 18.09.6-alt1
- 18.09.6

* Wed Apr 17 2019 Vladimir Didenko <cow@altlinux.org> 18.09.5-alt1
- 18.09.5

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.org> 18.09.4-alt1
- 18.09.4

* Fri Mar 22 2019 Alexey Shabalin <shaba@altlinux.org> 18.09.3-alt1
- 18.09.3
- build with seccomp support

* Fri Mar 15 2019 Mikhail Gordeev <obirvalger@altlinux.org> 18.09.1-alt2
- Change golang-github-cpuguy83-go-md2man to go-md2man in BuildRequires

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.org> 18.09.1-alt1
- New version

* Thu Jan 17 2019 Mikhail Gordeev <obirvalger@altlinux.org> 18.09.0-alt4
- add iptables to requires

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 18.09.0-alt3
- add completions for zsh and fish

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 18.09.0-alt2
- Use overlay2 storage driver by default

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.org> 18.09.0-alt1
- New version

* Thu Aug 30 2018 Vladimir Didenko <cow@altlinux.org> 18.06.1-alt1
- New version

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.org> 18.06.0-alt1.1
- remove unused build requirements

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.org> 18.06.0-alt1
- New version

* Mon May 14 2018 Alexey Shabalin <shaba@altlinux.ru> 18.03.1-alt2
- define ExclusiveArch as  %%go_arches

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.org> 18.03.1-alt1
- New version

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.org> 18.03.0-alt1
- New version

* Wed Feb 7 2018 Vladimir Didenko <cow@altlinux.org> 18.02.0-alt2.rc2
- Support rename of docker-init to tini

* Wed Feb 7 2018 Vladimir Didenko <cow@altlinux.org> 18.02.0-alt1.rc2
- New version

* Mon Jan 15 2018 Vladimir Didenko <cow@altlinux.org> 18.01.0-alt1
- New version

* Tue Jan 9 2018 Vladimir Didenko <cow@altlinux.org> 17.12.0-alt1
- New version
- Remove devel package (seems useless)

* Tue May 16 2017 Vladimir Didenko <cow@altlinux.org> 17.05.0-alt1
- New version

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.org> 17.04.0-alt1
- New version

* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.org> 17.03.0-alt1
- New version

* Fri Feb 10 2017 Vladimir Didenko <cow@altlinux.org> 1.13.1-alt1
- New version

* Wed Jan 25 2017 Vladimir Didenko <cow@altlinux.org> 1.13.0-alt1
- New version

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.org> 1.12.5-alt1
- New version

* Tue Nov 29 2016 Vladimir Didenko <cow@altlinux.org> 1.12.3-alt1
- New version

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.org> 1.12.2-alt1
- New version

* Tue Sep 20 2016 Alexandr Boltris <alex@altlinux.org> 1.12.1-alt2
- add docker-proxy. fixes #32489

* Fri Aug 19 2016 Vladimir Didenko <cow@altlinux.org> 1.12.1-alt1
- New version

* Tue Aug 2 2016 Vladimir Didenko <cow@altlinux.org> 1.12.0-alt1
- New version

* Thu Jun 2 2016 Vladimir Didenko <cow@altlinux.org> 1.11.2-alt1
- New version

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.org> 1.11.1-alt1
- New version
- Remove manual provides

* Thu May 5 2016 Vladimir Didenko <cow@altlinux.org> 1.11.0-alt1
- New version

* Fri Mar 11 2016 Vladimir Didenko <cow@altlinux.org> 1.10.3-alt1
- New version

* Thu Feb 25 2016 Vladimir Didenko <cow@altlinux.org> 1.10.2-alt1
- New version

* Tue Feb 16 2016 Vladimir Didenko <cow@altlinux.org> 1.10.1-alt1
- New version
- Restore bash completions

* Wed Feb 10 2016 Vladimir Didenko <cow@altlinux.org> 1.10.0-alt1.1
- fix provides

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.org> 1.10.0-alt1
- New version.
- Merge devel and pkg-devel packages
- add init script for sysvinit

* Wed Nov 25 2015 Vladimir Didenko <cow@altlinux.org> 1.9.1-alt1
- New version.

* Fri Nov 6 2015 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- New version.

* Tue Oct 13 2015 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- New version.
- Return CAP_AUDIT_READ since std-def kernel supports it now
- Fix build with golang 1.5

* Mon Aug 24 2015 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- New version.

* Fri May 08 2015 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.1-alt1
- Update to new version with security updates
 + Fix read/write /proc paths (CVE-2015-3630)
 + Prohibit VOLUME /proc and VOLUME / (CVE-2015-3631)
 + Fix opening of file-descriptor 1 (CVE-2015-3627)
 + Fix symlink traversal on container respawn allowing
   local privilege escalation (CVE-2015-3629)
 + Prohibit mount of /sys

* Sat Apr 18 2015 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.0-alt1
- Update to last stable version
- Avoid of using CAP_AUDIT_READ capability for support
  less than 3.16.x kernel versions
- Rename dockerversion to autogen (c40993777f152426ea029)

* Wed Nov 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.1-alt1
- New version.
- Updated spec to Fedora 1.3.1-2.

* Mon Sep 15 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.0-alt1
- New version.

* Wed Aug 13 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.2-alt1
- New version.

* Thu Jun 19 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt2
- Dropped %%_datadir/vim/vimfiles/{doc,ftdetect,syntax}.

* Wed Jun 11 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt1
- New version.

* Mon May 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.11.1-alt1
- New version.

* Wed Apr 23 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10.0-alt2
- %%post: restored creation of docker group.

* Tue Apr 22 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10.0-alt1
- New version.

* Mon Jan 06 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.3-alt1
- New version

* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.2-alt1
- New version

* Tue Nov 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.0-alt1
- Release

* Mon Nov 25 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt3.rc7
- New RC

* Sat Oct 19 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt3.rc4
- New RC

* Fri Oct 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt2.rc3
- Update up to upstream/v0.7-rc3 branch
- Add ExclusiveArch: x86_64
- Build docker-init statically

* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt1.rc3
- Build for ALT
