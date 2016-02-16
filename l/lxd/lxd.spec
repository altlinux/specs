%global import_path github.com/lxc/lxd

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/* %go_root/bin/* %go_tooldir/*

%define lxdgroup lxd
%define lxduser lxd

Name:		lxd
Version:	2.0.0
Release:	alt0.beta4
Summary:	LXD -- REST API, command line tool and OpenStack integration plugin for LXC.

Group:		Development/Other
License:	Apache v.2
URL:		https://%import_path

Packager:	Denis Pynkin <dans@altlinux.ru>

Source0:	%name-%version.tar
Source2:	lxd-image-update.cron
Source3:	lxd.default

# services
Source11:	lxd.service
Source12:	lxd.socket
Source13:	lxd-startup.service


ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

Requires:	python3
Requires:	lxc-libs
Requires:	lxcfs
Requires:	btrfs-progs
Requires:	lvm2


# lxc
BuildRequires:	golang(gopkg.in/flosch/pongo2.v3)
BuildRequires:	golang(github.com/gorilla/websocket)
BuildRequires:	golang(github.com/olekukonko/tablewriter)
BuildRequires:	golang(github.com/gosexy/gettext)
BuildRequires:	golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:	golang(gopkg.in/inconshreveable/log15.v2)
BuildRequires:	golang(gopkg.in/yaml.v2)

# lxd
BuildRequires:	lxc-devel
BuildRequires:	golang(github.com/coreos/go-systemd/activation)
BuildRequires:	golang(github.com/dustinkirkland/golang-petname)
BuildRequires:	golang(github.com/golang/protobuf/proto)
BuildRequires:	golang(github.com/gorilla/mux)
BuildRequires:	golang(github.com/mattn/go-sqlite3)
BuildRequires:	golang(github.com/pborman/uuid)
BuildRequires:	golang(github.com/syndtr/gocapability/capability)
BuildRequires:	golang(gopkg.in/lxc/go-lxc.v2)
BuildRequires:	golang(gopkg.in/tomb.v2)

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

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"

%golang_prepare

cd .build/src/%import_path

for pkg in lxc lxd fuidshift lxd-bridge/lxd-bridge-proxy
do
    %golang_build $pkg
done

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
mv %buildroot/%_bindir/lxd-bridge-proxy %buildroot/%_libexecdir/lxd/
cp -av lxd-bridge/lxd-bridge %buildroot/%_libexecdir/lxd/
what="$(relative %_libexecdir/lxd/lxd-bridge-proxy %go_root/bin/lxd-bridge-proxy)"
ln -fs -- "$what" %buildroot/%go_root/bin/lxd-bridge-proxy

# Crontab entry for images update
%__install -D %SOURCE2 %buildroot/%_sysconfdir/cron.hourly/lxd-image-update

# configuration
%__install -D %SOURCE3 %buildroot/%_sysconfdir/sysconfig/lxd

#services
# systemd
mkdir -p %buildroot/%_unitdir
cp -av %SOURCE11 %buildroot/%_unitdir/
cp -av %SOURCE12 %buildroot/%_unitdir/
cp -av %SOURCE13 %buildroot/%_unitdir/

# install bash completion
mkdir -p %buildroot/%_datadir/bash-completion/completions/
cp -av config/bash/lxd-client %buildroot/%_datadir/bash-completion/completions/

# /var/{lib,log}/lxd
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name
# /var/lib/lxd/lxd-bridge
mkdir -p %buildroot%_localstatedir/%name/lxd-bridge

mkdir -p %buildroot/%_bindir/
cp -av scripts/lx* %buildroot/%_bindir/


%pre
%_sbindir/groupadd -r -f %lxdgroup 2>/dev/null || :
%_sbindir/useradd  -r -g %lxdgroup -c "LXD daemon" \
   -s /dev/null -d /dev/null %lxduser 2>/dev/null || :

%files
%doc AUTHORS COPYING
%_bindir/*
%go_root/bin/*
%attr(0750,%lxduser,%lxdgroup) %dir %_localstatedir/%name
%attr(0750,%lxduser,%lxdgroup) %dir %_localstatedir/%name/lxd-bridge
%attr(0750,%lxduser,%lxdgroup) %dir %_logdir/%name
%dir %_libexecdir/lxd
%_libexecdir/lxd/*

%_unitdir/*

%_datadir/bash-completion/completions/*

%_sysconfdir/cron.hourly/*

%_sysconfdir/sysconfig/*


%files devel
%go_path/src/*

%changelog
* Thu Feb 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.beta4
- Version update

* Thu Feb 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.beta3
- Version update

* Mon Feb 15 2016 Denis Pynkin <dans@altlinux.ru> 2.0.0-alt0.beta2
- Initial version
- Taken init scripts from Ubuntu
