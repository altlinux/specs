%global provider        github
%global provider_tld    com
%global project         docker
%global repo            %project

%global import_path %provider.%provider_tld/%project/%repo
%global commit      fa7b24f2c3948d1eb52453c609417a6bc7eba5dd
%global shortcommit fa7b24f

Name: docker-io
Version: 1.2.0
Release: alt1
Summary: Automates deployment of containerized applications
License: ASL 2.0
Group: System/Configuration/Other

Url: http://www.docker.io
# only x86_64 for now: https://github.com/docker/docker/issues/136
ExclusiveArch: x86_64
Conflicts: docker

# https://github.com/crosbymichael/docker
Source0: %name-%version.tar

BuildRequires: /proc gcc golang >= 1.3 systemd-devel libdevmapper-devel-static libsqlite3-devel-static libbtrfs-devel
BuildRequires: python-module-sphinx-devel python-module-sphinxcontrib-httpdomain pandoc
BuildRequires: golang(github.com/gorilla/mux) golang(github.com/kr/pty) golang(code.google.com/p/go.net/websocket) golang(code.google.com/p/gosqlite/sqlite3) golang(github.com/syndtr/gocapability/capability) golang(github.com/godbus/dbus) golang(github.com/coreos/go-systemd/activation)

BuildRequires: golang-github-gorilla-mux-devel >= 0-alt3
BuildRequires: golang-github-kr-pty-devel >= 0-alt3
BuildRequires: golang-github-coreos-go-systemd-devel >= 2-alt1.gitf743bc1
Requires: tar lxc xz
Provides: lxc-docker

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

%package devel
Group: Development/Other
Requires: golang
Requires: docker-io-pkg-devel
Summary: A golang registry for global request variables (source libraries)
Provides: golang(%import_path) = %version-%release
Provides: golang(%import_path/api) = %version-%release
Provides: golang(%import_path/api/client) = %version-%release
Provides: golang(%import_path/api/server) = %version-%release
Provides: golang(%import_path/archive) = %version-%release
Provides: golang(%import_path/builtins) = %version-%release
Provides: golang(%import_path/contrib) = %version-%release
Provides: golang(%import_path/contrib/docker-device-tool) = %version-%release
Provides: golang(%import_path/contrib/host-integration) = %version-%release
Provides: golang(%import_path/daemon) = %version-%release
Provides: golang(%import_path/daemon/execdriver) = %version-%release
Provides: golang(%import_path/daemon/execdriver/execdrivers) = %version-%release
Provides: golang(%import_path/daemon/execdriver/lxc) = %version-%release
Provides: golang(%import_path/daemon/execdriver/native) = %version-%release
Provides: golang(%import_path/daemon/execdriver/native/configuration) = %version-%release
Provides: golang(%import_path/daemon/execdriver/native/template) = %version-%release
Provides: golang(%import_path/daemon/graphdriver) = %version-%release
Provides: golang(%import_path/daemon/graphdriver/aufs) = %version-%release
Provides: golang(%import_path/daemon/graphdriver/btrfs) = %version-%release
Provides: golang(%import_path/daemon/graphdriver/devmapper) = %version-%release
Provides: golang(%import_path/daemon/graphdriver/graphtest) = %version-%release
Provides: golang(%import_path/daemon/graphdriver/vfs) = %version-%release
Provides: golang(%import_path/daemon/networkdriver) = %version-%release
Provides: golang(%import_path/daemon/networkdriver/bridge) = %version-%release
Provides: golang(%import_path/daemon/networkdriver/ipallocator) = %version-%release
Provides: golang(%import_path/daemon/networkdriver/portallocator) = %version-%release
Provides: golang(%import_path/daemon/networkdriver/portmapper) = %version-%release
Provides: golang(%import_path/dockerversion) = %version-%release
Provides: golang(%import_path/engine) = %version-%release
Provides: golang(%import_path/graph) = %version-%release
Provides: golang(%import_path/image) = %version-%release
Provides: golang(%import_path/integration) = %version-%release
Provides: golang(%import_path/integration-cli) = %version-%release
Provides: golang(%import_path/links) = %version-%release
Provides: golang(%import_path/nat) = %version-%release
Provides: golang(%import_path/opts) = %version-%release
Provides: golang(%import_path/registry) = %version-%release
Provides: golang(%import_path/runconfig) = %version-%release
Provides: golang(%import_path/utils) = %version-%release
Provides: golang(%import_path/utils/broadcastwriter) = %version-%release

%description devel
This is the source libraries for docker.

%package pkg-devel
Group: Development/Other
Requires: golang
Summary: A golang registry for global request variables (source libraries)
Provides: golang(%import_path/pkg/graphdb) = %version-%release
Provides: golang(%import_path/pkg/iptables) = %version-%release
Provides: golang(%import_path/pkg/listenbuffer) = %version-%release
Provides: golang(%import_path/pkg/mflag) = %version-%release
Provides: golang(%import_path/pkg/mflag/example) = %version-%release
Provides: golang(%import_path/pkg/mount) = %version-%release
Provides: golang(%import_path/pkg/namesgenerator) = %version-%release
Provides: golang(%import_path/pkg/networkfs/etchosts) = %version-%release
Provides: golang(%import_path/pkg/networkfs/resolvconf) = %version-%release
Provides: golang(%import_path/pkg/proxy) = %version-%release
Provides: golang(%import_path/pkg/signal) = %version-%release
Provides: golang(%import_path/pkg/symlink) = %version-%release
Provides: golang(%import_path/pkg/sysinfo) = %version-%release
Provides: golang(%import_path/pkg/system) = %version-%release
Provides: golang(%import_path/pkg/systemd) = %version-%release
Provides: golang(%import_path/pkg/tailfile) = %version-%release
Provides: golang(%import_path/pkg/term) = %version-%release
Provides: golang(%import_path/pkg/testutils) = %version-%release
Provides: golang(%import_path/pkg/truncindex) = %version-%release
Provides: golang(%import_path/pkg/units) = %version-%release
Provides: golang(%import_path/pkg/user) = %version-%release
Provides: golang(%import_path/pkg/version) = %version-%release

%description pkg-devel
These source librariees are provided by docker, but are independent of
docker specific logic. The import paths of %import_path/pkg/...

%prep
%setup
sed -i 's/go-md2man -in "$FILE" -out/pandoc -s -t man "$FILE" -o/g' docs/man/md2man-all.sh

%build
mkdir _build

pushd _build
  mkdir -p src/github.com/docker
  ln -s $(realpath ..) src/github.com/docker/docker
popd

export DOCKER_GITCOMMIT="%shortcommit/%version"
#export DOCKER_BUILDTAGS='selinux'
export GOPATH=$(pwd)/_build:%gopath:$(pwd)/vendor

hack/make.sh dynbinary
docs/man/md2man-all.sh
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
install -d %buildroot%_mandir/man1
install -p -m 644 docs/man/man1/docker*.1 %buildroot%_mandir/man1
install -d %buildroot%_mandir/man5
install -p -m 644 docs/man/man5/Dockerfile.5 %buildroot%_mandir/man5
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
install -p -m 644 contrib/init/systemd/docker.socket %buildroot%_unitdir
%if 0
install -d %buildroot%_initddir
install -p -m 755 contrib/init/sysvinit-debian/docker %buildroot%_initddir/docker
%endif

# sources
install -d -p %buildroot/%gopath/src/%import_path

for dir in api archive builtins daemon dockerversion engine graph \
           image links nat opts pkg registry runconfig utils
do
	cp -rpav $dir %buildroot/%gopath/src/%import_path/
done

cat > %buildroot%_unitdir/docker.service <<EOF
[Unit]
Description=Docker Application Container Engine
Documentation=http://docs.docker.com
After=network.target docker.socket
Requires=docker.socket

[Service]
Type=notify
EnvironmentFile=-/etc/sysconfig/docker
EnvironmentFile=-/etc/sysconfig/docker-storage
ExecStart=/usr/bin/docker -d -H fd:// $OPTIONS $DOCKER_STORAGE_OPTIONS
LimitNOFILE=1048576
LimitNPROC=1048576

[Install]
Also=docker.socket
EOF

install -d %buildroot%_sysconfdir/sysconfig
cat > %buildroot%_sysconfdir/sysconfig/docker <<EOF
OPTIONS=

EOF

cat > %buildroot%_sysconfdir/sysconfig/docker-storage <<EOF
# This file may be automatically generated by an installation program.

# By default, Docker uses a loopback-mounted sparse file in
# /var/lib/docker.  The loopback makes it slower, and there are some
# restrictive defaults, such as 100GB max storage.

# If your installation did not set a custom storage for Docker, you
# may do it below.

# Example: Use a custom pair of raw logical volumes (one for metadata,
# one for data).
# DOCKER_STORAGE_OPTIONS = --storage-opt dm.metadatadev=/dev/mylogvol/my-docker-metadata --storage-opt dm.datadev=/dev/mylogvol/my-docker-data

DOCKER_STORAGE_OPTIONS=

EOF

%pre
getent group docker > /dev/null || %_sbindir/groupadd -r docker
exit 0

%post
%post_service docker

%preun
%preun_service docker
%files
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md LICENSE MAINTAINERS NOTICE README.md
%doc LICENSE-vim-syntax README-vim-syntax.md
%config(noreplace) %_sysconfdir/sysconfig/docker
%config(noreplace) %_sysconfdir/sysconfig/docker-storage
%_mandir/man1/docker*.1*
%_mandir/man5/Dockerfile.5*
%_bindir/docker
%dir /usr/libexec/docker
/usr/libexec/docker/dockerinit
%_unitdir/docker.service
%_unitdir/docker.socket
%_sysconfdir/bash_completion.d/docker.bash
%_datadir/zsh/site-functions/_docker
%dir %_sharedstatedir/docker
%_sysconfdir/udev/rules.d/80-docker.rules
%_datadir/vim/vimfiles/doc/dockerfile.txt
%_datadir/vim/vimfiles/ftdetect/dockerfile.vim
%_datadir/vim/vimfiles/syntax/dockerfile.vim

%files devel
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md LICENSE MAINTAINERS NOTICE README.md
%dir %gopath/src/%provider.%provider_tld/%project
%dir %gopath/src/%import_path
%dir %gopath/src/%import_path/api
%gopath/src/%import_path/api/MAINTAINERS
%gopath/src/%import_path/api/README.md
%gopath/src/%import_path/api/*.go
%dir %gopath/src/%import_path/api/client
%gopath/src/%import_path/api/client/*.go
%dir %gopath/src/%import_path/api/server
%gopath/src/%import_path/api/server/MAINTAINERS
%gopath/src/%import_path/api/server/*.go
%dir %gopath/src/%import_path/archive
%gopath/src/%import_path/archive/MAINTAINERS
%gopath/src/%import_path/archive/README.md
%gopath/src/%import_path/archive/*.go
%dir %gopath/src/%import_path/archive/testdata
%gopath/src/%import_path/archive/testdata/broken.tar
%dir %gopath/src/%import_path/builtins
%gopath/src/%import_path/builtins/*.go
%dir %gopath/src/%import_path/daemon
%gopath/src/%import_path/daemon/*.go
%gopath/src/%import_path/daemon/MAINTAINERS
%gopath/src/%import_path/daemon/README.md
%dir %gopath/src/%import_path/daemon/execdriver
%gopath/src/%import_path/daemon/execdriver/*.go
%gopath/src/%import_path/daemon/execdriver/MAINTAINERS
%dir %gopath/src/%import_path/daemon/execdriver/execdrivers
%gopath/src/%import_path/daemon/execdriver/execdrivers/*.go
%dir %gopath/src/%import_path/daemon/execdriver/lxc
%gopath/src/%import_path/daemon/execdriver/lxc/MAINTAINERS
%gopath/src/%import_path/daemon/execdriver/lxc/*.go
%dir %gopath/src/%import_path/daemon/execdriver/native
%gopath/src/%import_path/daemon/execdriver/native/*.go
%dir %gopath/src/%import_path/daemon/execdriver/native/configuration
%gopath/src/%import_path/daemon/execdriver/native/configuration/*.go
%dir %gopath/src/%import_path/daemon/execdriver/native/template
%gopath/src/%import_path/daemon/execdriver/native/template/*.go
%dir %gopath/src/%import_path/daemon/graphdriver
%gopath/src/%import_path/daemon/graphdriver/*.go
%dir %gopath/src/%import_path/daemon/graphdriver/aufs
%gopath/src/%import_path/daemon/graphdriver/aufs/*.go
%dir %gopath/src/%import_path/daemon/graphdriver/btrfs
%gopath/src/%import_path/daemon/graphdriver/btrfs/*.go
%gopath/src/%import_path/daemon/graphdriver/btrfs/MAINTAINERS
%dir %gopath/src/%import_path/daemon/graphdriver/devmapper
%gopath/src/%import_path/daemon/graphdriver/devmapper/*.go
%gopath/src/%import_path/daemon/graphdriver/devmapper/MAINTAINERS
%gopath/src/%import_path/daemon/graphdriver/devmapper/README.md
%dir %gopath/src/%import_path/daemon/graphdriver/graphtest
%gopath/src/%import_path/daemon/graphdriver/graphtest/*.go
%dir %gopath/src/%import_path/daemon/graphdriver/vfs
%gopath/src/%import_path/daemon/graphdriver/vfs/*.go
%dir %gopath/src/%import_path/daemon/networkdriver
%dir %gopath/src/%import_path/daemon/networkdriver/bridge
%gopath/src/%import_path/daemon/networkdriver/bridge/*.go
%dir %gopath/src/%import_path/daemon/networkdriver/ipallocator
%gopath/src/%import_path/daemon/networkdriver/ipallocator/*.go
%gopath/src/%import_path/daemon/networkdriver/*.go
%dir %gopath/src/%import_path/daemon/networkdriver/portallocator
%gopath/src/%import_path/daemon/networkdriver/portallocator/*.go
%dir %gopath/src/%import_path/daemon/networkdriver/portmapper
%gopath/src/%import_path/daemon/networkdriver/portmapper/*.go
%dir %gopath/src/%import_path/dockerversion
%gopath/src/%import_path/dockerversion/*.go
%dir %gopath/src/%import_path/engine
%gopath/src/%import_path/engine/MAINTAINERS
%gopath/src/%import_path/engine/*.go
%dir %gopath/src/%import_path/graph
%gopath/src/%import_path/graph/MAINTAINERS
%gopath/src/%import_path/graph/*.go
%dir %gopath/src/%import_path/image
%gopath/src/%import_path/image/*.go
%dir %gopath/src/%import_path/links
%gopath/src/%import_path/links/*.go
%dir %gopath/src/%import_path/nat
%gopath/src/%import_path/nat/*.go
%dir %gopath/src/%import_path/opts
%gopath/src/%import_path/opts/*.go
%dir %gopath/src/%import_path/registry
%gopath/src/%import_path/registry/MAINTAINERS
%gopath/src/%import_path/registry/*.go
%dir %gopath/src/%import_path/runconfig
%gopath/src/%import_path/runconfig/*.go
%dir %gopath/src/%import_path/utils
%gopath/src/%import_path/utils/*.go

%files pkg-devel
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md LICENSE MAINTAINERS NOTICE README.md
%dir %gopath/src/%provider.%provider_tld/%project
%dir %gopath/src/%import_path
%dir %gopath/src/%import_path/pkg
%gopath/src/%import_path/pkg/README.md
%dir %gopath/src/%import_path/pkg/broadcastwriter
%gopath/src/%import_path/pkg/broadcastwriter/*.go
%dir %gopath/src/%import_path/pkg/graphdb
%gopath/src/%import_path/pkg/graphdb/MAINTAINERS
%gopath/src/%import_path/pkg/graphdb/*.go
%dir %gopath/src/%import_path/pkg/httputils
%gopath/src/%import_path/pkg/httputils/MAINTAINERS
%gopath/src/%import_path/pkg/httputils/*.go
%dir %gopath/src/%import_path/pkg/iptables
%gopath/src/%import_path/pkg/iptables/MAINTAINERS
%gopath/src/%import_path/pkg/iptables/*.go
%dir %gopath/src/%import_path/pkg/jsonlog
%gopath/src/%import_path/pkg/jsonlog/*.go
%dir %gopath/src/%import_path/pkg/listenbuffer
%gopath/src/%import_path/pkg/listenbuffer/*.go
%dir %gopath/src/%import_path/pkg/log
%gopath/src/%import_path/pkg/log/*.go
%dir %gopath/src/%import_path/pkg/mflag
%gopath/src/%import_path/pkg/mflag/LICENSE
%gopath/src/%import_path/pkg/mflag/MAINTAINERS
%gopath/src/%import_path/pkg/mflag/README.md
%dir %gopath/src/%import_path/pkg/mflag/example
%gopath/src/%import_path/pkg/mflag/example/example.go
%gopath/src/%import_path/pkg/mflag/*.go
%dir %gopath/src/%import_path/pkg/mount
%gopath/src/%import_path/pkg/mount/MAINTAINERS
%gopath/src/%import_path/pkg/mount/*.go
%dir %gopath/src/%import_path/pkg/namesgenerator
%gopath/src/%import_path/pkg/namesgenerator/*.go
%dir %gopath/src/%import_path/pkg/networkfs
%gopath/src/%import_path/pkg/networkfs/MAINTAINERS
%dir %gopath/src/%import_path/pkg/networkfs/etchosts
%gopath/src/%import_path/pkg/networkfs/etchosts/*.go
%dir %gopath/src/%import_path/pkg/networkfs/resolvconf
%gopath/src/%import_path/pkg/networkfs/resolvconf/*.go
%dir %gopath/src/%import_path/pkg/parsers
%gopath/src/%import_path/pkg/parsers/MAINTAINERS
%gopath/src/%import_path/pkg/parsers/*.go
%dir %gopath/src/%import_path/pkg/parsers/filters
%gopath/src/%import_path/pkg/parsers/filters/*.go
%dir %gopath/src/%import_path/pkg/parsers/kernel
%gopath/src/%import_path/pkg/parsers/kernel/*.go
%dir %gopath/src/%import_path/pkg/parsers/operatingsystem
%gopath/src/%import_path/pkg/parsers/operatingsystem/*.go
%dir %gopath/src/%import_path/pkg/proxy
%gopath/src/%import_path/pkg/proxy/MAINTAINERS
%gopath/src/%import_path/pkg/proxy/*.go
%dir %gopath/src/%import_path/pkg/signal
%gopath/src/%import_path/pkg/signal/*.go
%dir %gopath/src/%import_path/pkg/symlink
%gopath/src/%import_path/pkg/symlink/MAINTAINERS
%gopath/src/%import_path/pkg/symlink/*.go
%dir %gopath/src/%import_path/pkg/sysinfo
%gopath/src/%import_path/pkg/sysinfo/MAINTAINERS
%gopath/src/%import_path/pkg/sysinfo/*.go
%dir %gopath/src/%import_path/pkg/system
%gopath/src/%import_path/pkg/system/MAINTAINERS
%gopath/src/%import_path/pkg/system/*.go
%dir %gopath/src/%import_path/pkg/systemd
%gopath/src/%import_path/pkg/systemd/MAINTAINERS
%gopath/src/%import_path/pkg/systemd/*.go
%dir %gopath/src/%import_path/pkg/tailfile
%gopath/src/%import_path/pkg/tailfile/*.go
%dir %gopath/src/%import_path/pkg/tarsum
%gopath/src/%import_path/pkg/tarsum/*.go
%dir %gopath/src/%import_path/pkg/tarsum/testdata
%dir %gopath/src/%import_path/pkg/tarsum/testdata/46af0962ab5afeb5ce6740d4d91652e69206fc991fd5328c1a94d364ad00e457
%gopath/src/%import_path/pkg/tarsum/testdata/46af0962ab5afeb5ce6740d4d91652e69206fc991fd5328c1a94d364ad00e457/json
%gopath/src/%import_path/pkg/tarsum/testdata/46af0962ab5afeb5ce6740d4d91652e69206fc991fd5328c1a94d364ad00e457/layer.tar
%dir %gopath/src/%import_path/pkg/tarsum/testdata/511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158
%gopath/src/%import_path/pkg/tarsum/testdata/511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158/json
%gopath/src/%import_path/pkg/tarsum/testdata/511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158/layer.tar
%dir %gopath/src/%import_path/pkg/truncindex
%gopath/src/%import_path/pkg/truncindex/MAINTAINERS
%gopath/src/%import_path/pkg/truncindex/*.go
%dir %gopath/src/%import_path/pkg/term
%gopath/src/%import_path/pkg/term/MAINTAINERS
%gopath/src/%import_path/pkg/term/*.go
%dir %gopath/src/%import_path/pkg/testutils
%gopath/src/%import_path/pkg/testutils/MAINTAINERS
%gopath/src/%import_path/pkg/testutils/README.md
%gopath/src/%import_path/pkg/testutils/utils.go
%dir %gopath/src/%import_path/pkg/units
%gopath/src/%import_path/pkg/units/MAINTAINERS
%gopath/src/%import_path/pkg/units/*.go
%dir %gopath/src/%import_path/pkg/version
%gopath/src/%import_path/pkg/version/*.go

%changelog
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
