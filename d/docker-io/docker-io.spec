Name: docker-io
Version: 0.7
Release: alt2.rc3
Summary: Automates deployment of containerized applications
License: ASL 2.0
Group: System/Configuration/Other

Patch0: docker-0.7-remove-dotcloud-tar.patch
Url: http://www.docker.io
# only x86_64 for now: https://github.com/dotcloud/docker/issues/136
ExclusiveArch: x86_64

Source0: %name-%version.tar
Source1: docker.service
Source2: docker.init

BuildRequires: gcc golang golang-docs golang-godoc systemd-devel libdevmapper-devel-static libsqlite3-devel-static
BuildRequires: python-module-sphinx-devel python-module-sphinxcontrib-httpdomain
BuildRequires: golang("github.com/gorilla/mux") golang("github.com/kr/pty") golang("code.google.com/p/go.net/websocket") golang("code.google.com/p/gosqlite/sqlite3")

Requires: tar lxc
Provides: lxc-docker

%global gopath          %_datadir/gocode


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
%patch0 -p1 -b docker-0.7-remove-dotcloud-tar.patch

%build
mkdir _build
pushd _build

mkdir -p src/github.com/dotcloud
ln -s $(dirs +1 -l) src/github.com/dotcloud/docker
export GOPATH=$(pwd):%gopath

go build -v github.com/dotcloud/docker/docker
#Fix https://github.com/dotcloud/docker/issues/2203
export LDFLAGS='-X main.GITCOMMIT "'%version-%release'" -X main.VERSION "'%version'" -w -linkmode external -extldflags "-lpthread -ldl -static -Wl,--unresolved-symbols=ignore-in-shared-libs"'
export BUILDFLAGS='-tags netgo '
go build -v -ldflags "$LDFLAGS" $BUILDFLAGS github.com/dotcloud/docker/docker-init

popd

make -C docs/ man

%install
install -d %buildroot%_bindir
install -d -m 700 %buildroot%_sharedstatedir/docker
install -p -m 755 _build/docker %buildroot%_bindir
install -p -m 755 _build/docker-init %buildroot%_bindir
install -d %buildroot%_mandir/man1
install -p -m 644 docs/_build/man/docker.1 %buildroot%_man1dir/
install -d %buildroot%_sysconfdir/bash_completion.d
install -p -m 644 contrib/docker.bash %buildroot%_sysconfdir/bash_completion.d/
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
# -D=false: Debug mode
# -H=[unix:///var/run/docker.sock]: tcp://host:port to bind/connect to or unix://path/to/socket to use
# -api-enable-cors=false: Enable CORS requests in the remote api.
# -b="": Attach containers to a pre-existing network bridge. Use 'none' to disable container networking
# -dns="": Set custom dns servers
# -ip="0.0.0.0": Default ip address to use when binding a containers ports
# -iptables=true: Disable iptables within docker
# -r=true: Restart previously running containers

# Example
#OPTIONS='-b="breth0" -dns="8.8.8.8"'

OPTIONS=''

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
%_unitdir/docker.service
%_sysctldir/docker.conf
%_man1dir/docker.1*
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/docker.bash
%dir %_sharedstatedir/docker

%changelog
* Fri Oct 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt2.rc3
- Update up to upstream/v0.7-rc3 branch
- Add ExclusiveArch: x86_64
- Build docker-init statically

* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt1.rc3
- Build for ALT
