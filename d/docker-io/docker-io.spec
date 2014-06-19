Name: docker-io
Version: 1.0.0
Release: alt2
Summary: Automates deployment of containerized applications
License: ASL 2.0
Group: System/Configuration/Other

Url: http://www.docker.io
# only x86_64 for now: https://github.com/dotcloud/docker/issues/136
ExclusiveArch: x86_64
Conflicts: docker

# https://github.com/crosbymichael/docker
Source0: %name-%version.tar

BuildRequires: /proc gcc golang systemd-devel libdevmapper-devel-static libsqlite3-devel-static libbtrfs-devel
BuildRequires: python-module-sphinx-devel python-module-sphinxcontrib-httpdomain pandoc
BuildRequires: golang(github.com/gorilla/mux) golang(github.com/kr/pty) golang(code.google.com/p/go.net/websocket) golang(code.google.com/p/gosqlite/sqlite3) golang(github.com/syndtr/gocapability/capability) golang(github.com/godbus/dbus) golang(github.com/coreos/go-systemd/activation)

BuildRequires: golang-github-gorilla-mux-devel >= 0-alt3
BuildRequires: golang-github-kr-pty-devel >= 0-alt3
BuildRequires: golang-github-coreos-go-systemd-devel >= 2-alt1.gitf743bc1
Requires: tar lxc xz
Provides: lxc-docker

%define commit 63fe64c471e7d76be96a625350468dfc65c06c31
%define shortcommit %(c=%commit; echo ${c:0:7})

%define gopath %_datadir/gocode

# do not strip
%brp_strip_none %_bindir/docker /usr/libexec/docker/dockerinit

# do not extract debuginfo
%define __find_debuginfo_files %nil

# do not run debugedit for them
%add_debuginfo_skiplist /usr/bin/docker
%add_debuginfo_skiplist /usr/libexec/docker/dockerinit

%description
Docker is an open-source engine that automates the deployment of any
application as a lightweight, portable, self-sufficient container that will
run virtually anywhere.

Docker containers can encapsulate any payload, and will run consistently on
and between virtually any server. The same container that a developer builds
and tests on a laptop will run at scale, in production*, on VMs, bare-metal
servers, OpenStack clusters, public instances, or combinations of the above.

%prep
%setup
find vendor/src/ -mindepth 3 -maxdepth 3 -type d | \
	egrep -v '(code.google.com/p/go)' | xargs echo rm -rf

%build
mkdir _build

pushd _build
  mkdir -p src/github.com/dotcloud
  ln -s $(dirs +1 -l) src/github.com/dotcloud/docker
popd

export DOCKER_GITCOMMIT="%shortcommit/%version"
#export DOCKER_BUILDTAGS='selinux'
export GOPATH=$(pwd)/_build:%gopath

hack/make.sh dynbinary
contrib/man/md/md2man-all.sh
cp contrib/syntax/vim/LICENSE LICENSE-vim-syntax
cp contrib/syntax/vim/README.md README-vim-syntax.md

%install
# install binary
install -d %buildroot%_bindir
install -p -m 755 bundles/%version/dynbinary/docker-%version %buildroot%_bindir/docker
# install dockerinit
install -d %buildroot/usr/libexec/docker
install -p -m 755 bundles/%version/dynbinary/dockerinit-%version %buildroot/usr/libexec/docker/dockerinit
# install manpage
install -d %buildroot%_man1dir
install -p -m 644 contrib/man/man1/docker*.1 %buildroot%_man1dir
# install bash completion
install -d %buildroot%_sysconfdir/bash_completion.d
install -p -m 644 contrib/completion/bash/docker %buildroot%_sysconfdir/bash_completion.d/docker.bash
# install zsh completion
install -d %buildroot%_datadir/zsh/site-functions
install -p -m 644 contrib/completion/zsh/_docker %buildroot%_datadir/zsh/site-functions
# install vim syntax highlighting
install -d %buildroot%_datadir/vim/vimfiles/{doc,ftdetect,syntax}
install -p -m 644 contrib/syntax/vim/doc/dockerfile.txt %buildroot%_datadir/vim/vimfiles/doc
install -p -m 644 contrib/syntax/vim/ftdetect/dockerfile.vim %buildroot%_datadir/vim/vimfiles/ftdetect
install -p -m 644 contrib/syntax/vim/syntax/dockerfile.vim %buildroot%_datadir/vim/vimfiles/syntax
# install udev rules
install -d %buildroot%_sysconfdir/udev/rules.d
install -p -m 755 contrib/udev/80-docker.rules %buildroot%_sysconfdir/udev/rules.d
# install storage dir
install -d -m 700 %buildroot%_sharedstatedir/docker
# install systemd/init scripts
install -d %buildroot%_unitdir
install -p -m 644 contrib/init/systemd/docker.service %buildroot%_unitdir
#install -p -m 644 %%SOURCE1 %%buildroot%%_unitdir
%if 0
install -d %buildroot%_initddir
install -p -m 755 contrib/init/sysvinit-debian/docker %buildroot%_initddir/docker
%endif
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
%doc LICENSE-vim-syntax README-vim-syntax.md
%_sysctldir/docker.conf
%_man1dir/docker*.1.*
%_bindir/docker
%dir /usr/libexec/docker
/usr/libexec/docker/dockerinit
%_unitdir/docker.service
%if 0
%_initddir/docker
%endif
%config(noreplace) %_sysconfdir/sysconfig/docker
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/docker.bash
%_datadir/zsh/site-functions/_docker
%dir %_sharedstatedir/docker
%_sysconfdir/udev/rules.d/80-docker.rules
%_datadir/vim/vimfiles/doc/dockerfile.txt
%_datadir/vim/vimfiles/ftdetect/dockerfile.vim
%_datadir/vim/vimfiles/syntax/dockerfile.vim

%changelog
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
