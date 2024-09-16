%define import_path github.com/lxc/incus
%define _unpackaged_files_terminate_build 1
%define incususer incusadm

Name:		incus
Version:	6.5.0
Release:	alt1
Summary:	Incus is a system container and virtual machine manager

Group:		Development/Other
License:	Apache-2.0
URL:		https://github.com/lxc/incus

Source0:	%name-%version.tar
Patch:          %name-%version.patch
Source11:      %name.socket
Source12:      %name.service
Source13:      %name-startup.service
Source14:      %name-user.socket
Source15:      %name-user.service
# Ensure Incus groups exist
Source16:      %name-sysusers.conf
# Ensure system dnsmasq ignores Incus network bridge
Source17:      %name-dnsmasq.conf
Source18:      %name-tmpfiles.conf
Source19:      %name-sysctl.conf

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.19
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: liblz4-devel
BuildRequires: pkgconfig(lxc) 
BuildRequires: liblxc-devel >= 6.0.0
BuildRequires: libsqlite3-devel
BuildRequires: libraft-devel
BuildRequires: libudev-devel
BuildRequires: libcowsql-devel
BuildRequires: libcap-devel
BuildRequires: help2man
BuildRequires: /proc

Requires:       %name-client = %version-%release
Requires:       attr
Requires:       dnsmasq
Requires:       iptables, ebtables
Requires:       lxcfs >= 6.0.0
Requires:       rsync
Requires:       shadow-utils
Requires:       squashfs-tools
Requires:       tar
Requires:       xdelta
Requires:       xz

%description
Incus is a modern, secure and powerful system
container and virtual machine manager. It provides
a unified experience for running and managing full
Linux systems inside containers or virtual machines.
Incus supports images for a large number of Linux
distributions and is built around a very powerful,
yet pretty simple, REST API.

%package -n %name-client
Summary:        Container hypervisor based on LXC - Client
License:        Apache-2.0
Group:          Development/Other
Requires:       gettext
	
%description -n %name-client
Incus offers a REST API to remotely manage containers over the network,
using an image based work-flow and with support for live migration.
This package contains the command line client.

%package -n %name-tools
Summary:        Container hypervisor based on LXC - Extra Tools
License:        Apache-2.0
Group:          Development/Other	
Requires:       %name = %version-%release
# fuidshift is also shipped with lxd
Conflicts:      lxd-tools
	
%description -n %name-tools
Incus offers a REST API to remotely manage containers over the network,
using an image based work-flow and with support for live migration.
This package contains extra tools provided with Incus.
 - fuidshift - A tool to map/unmap filesystem uids/gids
 - lxc-to-incus - A tool to migrate LXC containers to Incus
 - lxd-to-incus - A tool to migrate an existing LXD environment to Incus
 - incus-benchmark - A Incus benchmark utility
 - incus-migrate - A physical to container migration tool
	
%package -n %name-agent
Summary:        Incus guest agent
License:        Apache-2.0
Group:          Development/Other	
Requires:       %name = %version-%release

%description -n %name-agent
This packages provides an agent to run inside Incus virtual machine guests.
It has to be installed on the Incus host if you want to allow agent
injection capability when creating a virtual machine.
	
%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
pushd $BUILDDIR/src/%import_path
for i in incus fuidshift incus-benchmark lxc-to-incus lxd-to-incus incusd incus-user; do
	CGO_LDFLAGS_ALLOW="(-Wl,-wrap,pthread_create)|(-Wl,-z,now)" TAGS="libsqlite3" %golang_build cmd/$i
done
CGO_ENABLED=0 TAGS="netgo" %golang_build cmd/incus-migrate
CGO_ENABLED=0 TAGS="agent,netgo" %golang_build cmd/incus-agent
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

#configuration
install -p -D %SOURCE16 %buildroot%_sysusersdir/%name.conf
#configuration for dnsmasq called in lxd-bridge
install -p -D %SOURCE17 %buildroot%_sysconfdir/%name/dnsmasq.conf
#configuration for temp files
mkdir -p %buildroot%_tmpfilesdir/
install -p -D %SOURCE18 %buildroot%_tmpfilesdir/%name.conf
install -p -D %SOURCE19 %buildroot%_sysconfdir/sysconfig/incus

#services systemd
mkdir -p %buildroot%_unitdir
cp -av %SOURCE11 %buildroot%_unitdir/
cp -av %SOURCE12 %buildroot%_unitdir/
cp -av %SOURCE13 %buildroot%_unitdir/
cp -av %SOURCE14 %buildroot%_unitdir/
cp -av %SOURCE15 %buildroot%_unitdir/

#install bash completion
mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/incus
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_incus
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/incus.fish

#/var/{lib,log}/lxd
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name

#install the manpages
mkdir -p %buildroot%_man1dir
help2man %buildroot%_bindir/fuidshift -n "uid/gid shifter" --no-info --no-discard-stderr > %buildroot%_man1dir/fuidshift.1
help2man %buildroot%_bindir/lxc-to-incus -n "Convert LXC containers to Incus" --no-info --version-string=%version --no-discard-stderr > %buildroot%_man1dir/lxc-to-incus.1
help2man %buildroot%_bindir/lxd-to-incus -n "Convert LXD containers to Incus" --no-info --version-string=%version --no-discard-stderr > %buildroot%_man1dir/lxd-to-incus.1
help2man %buildroot%_bindir/incus-agent -n "Incus virtual machine guest agent" --no-info --no-discard-stderr > %buildroot%_man1dir/incus-agent.1
help2man %buildroot%_bindir/incus-benchmark -n "Incus benchmark" --no-info --no-discard-stderr > %buildroot%_man1dir/incus-benchmark.1
help2man %buildroot%_bindir/incus-migrate -n "Incus physical to instance migration tool" --no-info --no-discard-stderr > %buildroot%_man1dir/incus-migrate.1
help2man %buildroot%_bindir/incus-simplestreams -n "Maintain an Incus-compatible simplestreams tree" --no-info --no-discard-stderr > %buildroot%_man1dir/incus-simplestreams.1
help2man %buildroot%_bindir/incus-user -n "Incus user project daemon" --no-info --no-discard-stderr > %buildroot%_man1dir/incus-user.1

%buildroot%_bindir/incusd manpage %buildroot%_man1dir/
%buildroot%_bindir/incus manpage %buildroot%_man1dir/

%pre
groupadd -r -f %name-admin 2>/dev/null || :
groupadd -r -f %name 2>/dev/null || :
useradd  -r -g %name-admin -c "Incus daemon" \
   -s /dev/null -d /dev/null %incususer 2>/dev/null || :

%post
usermod --add-subgids 100000-165535 root ||:
usermod --add-subgids 100000-165535 %incususer ||:
usermod --add-subuids 100000-165535 root ||:
usermod --add-subuids 100000-165535 %incususer ||:

%post_service %name

%preun
%preun_service %name

%files
%doc *.md
%_bindir/incusd
%_bindir/%name-user
%config(noreplace) %_tmpfilesdir/%name.conf
%config(noreplace) %_sysconfdir/%name/dnsmasq.conf
%config(noreplace) %_sysusersdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/*
%_unitdir/*
%_man1dir/incusd.*
%_man1dir/%name-user.*
%attr(0751,%incususer,%name-admin) %dir %_localstatedir/%name
%attr(0751,%incususer,%name-admin) %dir %_logdir/%name

%files -n %name-client
%_bindir/%name
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/_*
%_datadir/fish/vendor_completions.d/*.fish
%_man1dir/%name-simplestreams.*
%_man1dir/%name.*

%files -n %name-tools
%_bindir/fuidshift
%_bindir/%name-benchmark
%_bindir/%name-migrate
%_bindir/lxc-to-%name
%_bindir/lxd-to-%name
%_man1dir/fuidshift.*
%_man1dir/%name-benchmark.*
%_man1dir/%name-migrate.*
%_man1dir/lxc-to-%name.*
%_man1dir/lxd-to-%name.*

%files -n %name-agent
%_bindir/%name-agent
%_man1dir/%name-agent.*

%changelog
* Mon Sep 09 2024 Nadezhda Fedorova <fedor@altlinux.org> 6.5.0-alt1
- Updated to 6.5.0.

* Mon Jul 15 2024 Nadezhda Fedorova <fedor@altlinux.org> 6.3.0-alt1
- Updated to 6.3.0.
- Deleted subgid/subuid settings for nobody, it's unusable in alt.

* Fri May 17 2024 Nadezhda Fedorova <fedor@altlinux.org> 6.1.0-alt1
- Initial version.
