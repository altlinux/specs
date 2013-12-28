Name: docker-io
Version: 0.7.2
Release: alt1
Summary: Automates deployment of containerized applications
License: ASL 2.0
Group: System/Configuration/Other

Url: http://www.docker.io
# only x86_64 for now: https://github.com/dotcloud/docker/issues/136
ExclusiveArch: x86_64

# https://github.com/crosbymichael/docker
Source0: %name-%version.tar
Source1: docker.service
Source2: docker.init

BuildRequires: /proc gcc golang systemd-devel libdevmapper-devel-static libsqlite3-devel-static
BuildRequires: python-module-sphinx-devel python-module-sphinxcontrib-httpdomain
BuildRequires: golang(github.com/gorilla/mux) golang(github.com/kr/pty) golang(code.google.com/p/go.net/websocket) golang(code.google.com/p/gosqlite/sqlite3) golang(github.com/syndtr/gocapability/capability)

Requires: tar lxc xz
Provides: lxc-docker

%global commit 28b162eeb48002e1824a1b43bbc864e93af8e26b
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global gopath          %_datadir/gocode
%global __find_debuginfo_files /bin/true
%add_verify_elf_skiplist /usr/bin/docker
%add_verify_elf_skiplist %_usr/libexec/docker/dockerinit
%brp_strip_none /usr/bin/*
%brp_strip_none %_usr/libexec/docker/*

%description
Docker is an open-source engine that automates the deployment of any
application as a lightweight, portable, self-sufficient container that will
run virtually anywhere.

Docker containers can encapsulate any payload, and will run consistently on
and between virtually any server. The same container that a developer builds
and tests on a laptop will run at scale, in production*, on VMs, bare-metal
servers, OpenStack clusters, public instances, or combinations of the above.

%prep
%setup -q
rm -rf vendor

%build
mkdir _build
pushd _build

mkdir -p src/github.com/dotcloud
ln -s $(dirs +1 -l) src/github.com/dotcloud/docker
export GOPATH=$(pwd):%gopath

# passing version information build flags BZ #1017186
export LDFLAGS="-X main.GITCOMMIT '%shortcommit/%release' -X main.VERSION '%version' -w"
export BUILDFLAGS='-tags netgo'
# dockerinit still needs to be a static binary, even if docker is dynamic
CGO_ENABLED=0 go build -v -a -ldflags "$LDFLAGS -d" $BUILDFLAGS github.com/dotcloud/docker/dockerinit
# sha1 our new dockerinit to ensure separate docker and dockerinit always run in a perfect pair compiled for one another
export DOCKER_INITSHA1="$(sha1sum dockerinit | cut -d' ' -f1)"
# exported so that "dyntest" can easily access it later without recalculating it
go build -v -a -ldflags "$LDFLAGS -X github.com/dotcloud/docker/utils.INITSHA1 \"$DOCKER_INITSHA1\"" $BUILDFLAGS github.com/dotcloud/docker/docker

popd

make -C docs/ man

%install
install -d -m 700 %buildroot%_sharedstatedir/docker
install -p -D -m 755 _build/docker %buildroot%_bindir/docker
install -p -D -m 755 _build/dockerinit %buildroot%_usr/libexec/docker/dockerinit
install -d %buildroot%_mandir/man1
install -p -m 644 docs/_build/man/docker.1 %buildroot%_man1dir/
install -d %buildroot%_sysconfdir/bash_completion.d
install -p -m 644 contrib/completion/bash/docker %buildroot%_sysconfdir/bash_completion.d/docker.bash
install -d %buildroot%_datadir/zsh/site-functions
install -p -m 644 contrib/completion/zsh/_docker %buildroot%_datadir/zsh/site-functions
install -d %buildroot%_unitdir
install -p -m 644 %SOURCE1 %buildroot%_unitdir
install -d %buildroot%_initdir
install -p -m 755 %SOURCE2 %buildroot%_initdir/docker

install -d %buildroot%_sysctldir
cat > %buildroot%_sysctldir/docker.conf <<EOF
net.ipv4.ip_forward = 1
net.ipv6.conf.all.forwarding = 1
EOF

install -d %buildroot%_sysconfdir/sysconfig
cat > %buildroot%_sysconfdir/sysconfig/docker <<EOF
#Usage of docker:
#  -D=false: Enable debug mode
#  -H=[unix:///var/run/docker.sock]: Multiple tcp://host:port or unix://path/to/socket to bind in daemon mode, single connection otherwise
#  -api-enable-cors=false: Enable CORS headers in the remote API
#  -b="": Attach containers to a pre-existing network bridge; use 'none' to disable container networking
#  -dns="": Force docker to use specific DNS servers
#  -g="/var/lib/docker": Path to use as the root of the docker runtime
#  -icc=true: Enable inter-container communication
#  -ip="0.0.0.0": Default IP address to use when binding container ports
#  -iptables=true: Disable docker's addition of iptables rules
#  -p="/var/run/docker.pid": Path to use for daemon PID file
#  -r=true: Restart previously running containers
#  -s="": Force the docker runtime to use a specific storage driver
#  !!!WARNING!!! In case of a change the driver, data from the old driver will not be available
#  List of drivers used in an order is: aufs, devicemapper, vfs

# Example
#OPTIONS='-r -s=devicemapper -b="breth0" -dns="8.8.8.8"'
OPTIONS='-r -s=devicemapper -b="none"'

EOF

%pre
getent group docker > /dev/null || %_sbindir/groupadd -r docker
exit 0

%post
%post_service docker

%preun
%preun_service docker

%files
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md FIXME LICENSE MAINTAINERS NOTICE README.md
%config(noreplace) %_sysconfdir/sysconfig/docker
%_initdir/*
%_bindir/*
%_usr/libexec/docker
%_unitdir/docker.service
%_sysctldir/docker.conf
%_man1dir/docker.1*
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/docker.bash
%_datadir/zsh/site-functions/_docker
%dir %_sharedstatedir/docker

%changelog
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
