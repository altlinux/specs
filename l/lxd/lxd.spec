%global import_path github.com/lxc/lxd

#global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
#add_debuginfo_skiplist %go_root %_bindir

%define lxdgroup lxd
%define lxduser lxd

Name:		lxd
Version:	3.10
Release:	alt1
Summary:	LXD -- REST API, command line tool and OpenStack integration plugin for LXC.

Group:		Development/Other
License:	Apache v.2
URL:		https://%import_path

Packager:	Denis Pynkin <dans@altlinux.ru>

Source0:	%name-%version.tar
Patch:		%name-%version-%release.patch
Source2:	lxd-image-update.cron
Source3:	lxd.default
Source4:	lxd.dnsmasq

# services
Source11:	lxd.service
Source12:	lxd.socket
Source13:	lxd-startup.service


ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

Requires:	shadow-submap
Requires:	lxc-libs
Requires:	lxcfs
Requires:	btrfs-progs
Requires:	lvm2
Requires:	squashfs-tools
Requires:	liblxd_sqlite3

BuildRequires: libcap-devel
BuildRequires: libuv-devel

BuildRequires: liblxd_sqlite3-devel
BuildRequires: libdqlite-devel

BuildRequires: help2man
# Needed for manpages generation. Accessing to '/proc/self/...'
BuildRequires: /proc

# lxc
BuildRequires: golang(gopkg.in/flosch/pongo2.v3)
BuildRequires: golang(github.com/gorilla/websocket)
BuildRequires: golang(github.com/olekukonko/tablewriter)
BuildRequires: golang(github.com/gosexy/gettext)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(gopkg.in/inconshreveable/log15.v2)
BuildRequires: golang(gopkg.in/yaml.v2)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/cobra/doc)
BuildRequires: golang(gopkg.in/juju/environschema.v1/form)
BuildRequires: golang(gopkg.in/macaroon-bakery.v2/httpbakery)
BuildRequires: golang(gopkg.in/macaroon-bakery.v2/httpbakery/form)
BuildRequires: golang(github.com/juju/persistent-cookiejar)
BuildRequires: golang(gopkg.in/errgo.v1)

# fuidshift
BuildRequires:  golang(github.com/spf13/cobra)

# lxd
BuildRequires:	lxc-devel
BuildRequires:	libacl-devel
BuildRequires: golang(github.com/coreos/go-systemd/activation)
BuildRequires: golang(github.com/dustinkirkland/golang-petname)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/gorilla/mux)
BuildRequires: golang(github.com/mattn/go-sqlite3)
BuildRequires: golang(github.com/pborman/uuid)
BuildRequires: golang(github.com/syndtr/gocapability/capability)
BuildRequires: golang(gopkg.in/lxc/go-lxc.v2)
BuildRequires: golang(gopkg.in/tomb.v2)
BuildRequires: golang(github.com/CanonicalLtd/candidclient)
BuildRequires: golang(github.com/CanonicalLtd/go-dqlite)
BuildRequires: golang(github.com/boltdb/bolt)
BuildRequires: golang(github.com/flosch/pongo2)
BuildRequires: golang(github.com/gorilla/websocket)
BuildRequires: golang(github.com/hashicorp/raft)
BuildRequires: golang(github.com/hashicorp/raft-boltdb)
BuildRequires: golang(github.com/miekg/dns)
BuildRequires: golang(github.com/olekukonko/tablewriter)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/cobra/doc)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(gopkg.in/lxc/go-lxc.v2)
BuildRequires: golang(gopkg.in/macaroon-bakery.v2/bakery)
BuildRequires: golang(gopkg.in/macaroon-bakery.v2/bakery/checkers)
BuildRequires: golang(gopkg.in/macaroon-bakery.v2/bakery/identchecker)
BuildRequires: golang(gopkg.in/macaroon-bakery.v2/httpbakery)
BuildRequires: golang(gopkg.in/robfig/cron.v2)
BuildRequires: golang(gopkg.in/yaml.v2)
BuildRequires: golang(github.com/Rican7/retry)
BuildRequires: golang(github.com/armon/go-metrics)
BuildRequires: golang(github.com/gogo/protobuf/proto)
BuildRequires: golang(gopkg.in/CanonicalLtd/candidclient.v1)
BuildRequires: golang(github.com/CanonicalLtd/raft-http)
BuildRequires: golang(github.com/CanonicalLtd/raft-membership)
BuildRequires: golang(github.com/CanonicalLtd/raft-test)
BuildRequires: golang(github.com/hashicorp/go-msgpack/codec)
BuildRequires: golang(github.com/ryanfaerman/fsm)
BuildRequires: golang(github.com/stretchr/testify)
BuildRequires: golang(github.com/juju/gomaasapi)

#lxd-p2c
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/pborman/uuid)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)

#lxc-to-lxd
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/pborman/uuid)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(gopkg.in/lxc/go-lxc.v2)

#lxd-benchmark
BuildRequires:  golang(github.com/spf13/cobra)

%description
REST API, command line tool and OpenStack integration plugin for LXC.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch
Requires: golang

%description devel
%summary
This package contains library source intended for building other packages
which use the supplementary Go tools libraries with %import_path imports.


%prep
%setup -q
%patch0 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"
export CGO_ENABLED=1

%golang_prepare

cd .build/src/%import_path

# Need to use a patched version of libsqlite
export TAGS="libsqlite3"
export CGO_CPPFLAGS="$(pkg-config --cflags lxd_sqlite3)"
export CGO_LDFLAGS="$(pkg-config --libs lxd_sqlite3)"
%golang_build lxd lxc fuidshift lxd-benchmark lxd-p2c lxc-to-lxd lxd/db

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

mkdir -p -- %buildroot/%go_root/bin
for f in %buildroot/%_bindir/*; do
	[ -x "$f" ] || continue
	f="${f##*/}"
	what="$(relative %_bindir/$f %go_root/bin/$f)"
	ln -s -- "$what" %buildroot/%go_root/bin/$f
done

# lxc-bridge
mkdir -p -- %buildroot/%_libexecdir/lxd

# Crontab entry for images update
%__install -D %SOURCE2 %buildroot/%_sysconfdir/cron.hourly/lxd-image-update

# configuration
%__install -D %SOURCE3 %buildroot/%_sysconfdir/sysconfig/lxd
# configuration for dnsmasq called in lxd-bridge
%__install -D %SOURCE4 %buildroot/%_sysconfdir/lxd/dnsmasq.conf

#services
# systemd
mkdir -p %buildroot/%_unitdir
cp -av %SOURCE11 %buildroot/%_unitdir/
cp -av %SOURCE12 %buildroot/%_unitdir/
cp -av %SOURCE13 %buildroot/%_unitdir/

# install bash completion
mkdir -p %buildroot/%_datadir/bash-completion/completions/
cp -av scripts/bash/lxd-client %buildroot/%_datadir/bash-completion/completions/

# /var/{lib,log}/lxd
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name

# Install the manpages
mkdir -p %buildroot/%_man1dir
help2man %buildroot/%_bindir/fuidshift -n "uid/gid shifter" --no-info > %buildroot/%_man1dir/fuidshift.1
help2man %buildroot/%_bindir/lxc-to-lxd -n "Convert LXC containers to LXD" --no-info --version-string=%version > %buildroot/%_man1dir/lxc-to-lxd.1
help2man %buildroot/%_bindir/lxd-benchmark -n "The container lightervisor - benchmark" --no-info --no-discard-stderr > %buildroot/%_man1dir/lxd-benchmark.1
%buildroot/%_bindir/lxd manpage %buildroot/%_man1dir/
%buildroot/%_bindir/lxc manpage %buildroot/%_man1dir/

%pre
%_sbindir/groupadd -r -f %lxdgroup 2>/dev/null || :
%_sbindir/useradd  -r -g %lxdgroup -c "LXD daemon" \
   -s /dev/null -d /dev/null %lxduser 2>/dev/null || :

%files
%doc AUTHORS COPYING
%_bindir/*
%go_root/bin/*
%attr(0751,%lxduser,%lxdgroup) %dir %_localstatedir/%name
%attr(0751,%lxduser,%lxdgroup) %dir %_logdir/%name
#dir %_libexecdir/lxd
#_libexecdir/lxd/*

%_unitdir/*

%_datadir/bash-completion/completions/*

%_sysconfdir/cron.hourly/*

%config(noreplace) %_sysconfdir/sysconfig/*
%dir %_sysconfdir/lxd
%config(noreplace) %_sysconfdir/lxd/dnsmasq.conf

%_man1dir/*

%files devel
%go_path/src/*

%changelog
* Wed Feb 13 2019 Denis Pynkin <dans@altlinux.org> 3.10-alt1
- Update

* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 3.8-alt1
- Update
- Add manpages generation

* Sun Jun 24 2018 Denis Pynkin <dans@altlinux.org> 3.2-alt1
- Update

* Wed May 09 2018 Denis Pynkin <dans@altlinux.org> 3.0.0-alt1
- new version

* Wed Sep 06 2017 Denis Pynkin <dans@altlinux.org> 2.17-alt1
- new version 2.17

* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 2.16-alt1
- new version 2.16

* Fri Jun 30 2017 Denis Pynkin <dans@altlinux.org> 2.15-alt1
- new version 2.15

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.11-alt1
- new version

* Sat Nov 26 2016 Denis Pynkin <dans@altlinux.org> 2.6.2-alt1
- new version 2.6.2

* Sat Nov 26 2016 Denis Pynkin <dans@altlinux.org> 2.6-alt2
- Added cgmanager dependency back
- Patch included

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.6-alt1
- new version 2.6

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 2.4.1-alt1
- Release 2.4

* Sat Oct 01 2016 Denis Pynkin <dans@altlinux.org> 2.3.0-alt1
- Release 2.3
- Removed cgmanager dependency
- Removed lxd-bridge due new network API

* Mon Sep 26 2016 Denis Pynkin <dans@altlinux.org> 2.2.0-alt1
- Release 2.2
- Fixed lxc-to-lxd script

* Wed Aug 24 2016 Denis Pynkin <dans@altlinux.org> 2.1.0-alt3
- configuration fixes for lxd-bridge service

* Wed Aug 24 2016 Denis Pynkin <dans@altlinux.org> 2.1.0-alt2
- Added squashfs-tools in Requires

* Tue Aug 23 2016 Denis Pynkin <dans@altlinux.org> 2.1.0-alt1
- Release 2.1

* Thu Apr 14 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt3
- Release 2.0

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt2.rc2
- Version update

* Thu Mar 03 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt2.rc1
- Added LXD bridge start/stop and configuration
- Version update

* Mon Feb 29 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt1.beta4
- rebuild with new lxc

* Thu Feb 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.beta4
- Version update

* Thu Feb 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.beta3
- Version update

* Mon Feb 15 2016 Denis Pynkin <dans@altlinux.ru> 2.0.0-alt0.beta2
- Initial version
- Taken init scripts from Ubuntu
