%global import_path github.com/canonical/lxd
%global _unpackaged_files_terminate_build 1

%define lxdgroup lxd
%define lxduser lxd

Name:		lxd
Version:	5.21.1
Release:	alt1
Summary:	LXD -- REST API, command line tool and OpenStack integration plugin for LXC.

Group:		Development/Other
License:	Apache-2.0
URL:		https://%import_path

Source0:	%name-%version.tar
Patch:		%name-%version-%release.patch
Source3:	lxd.default
Source4:	lxd.dnsmasq

# services
Source11:	lxd.service
Source12:	lxd.socket
Source13:	lxd-startup.service


ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
# For test/deps/import-busybox
BuildRequires(pre): rpm-build-python3

Requires:	shadow-submap
Requires:	lxc-runtime >= 4.0.0
Requires:	lxcfs
Requires:	btrfs-progs
Requires:	lvm2
Requires:	squashfs-tools
Requires:	rsync
Requires:	iptables
Requires:	ebtables
Requires:	dnsmasq
Requires:	attr

BuildRequires: golang >= 1.18
BuildRequires: libcap-devel
BuildRequires: libuv-devel

BuildRequires: libsqlite3-devel
BuildRequires: libdqlite-devel
BuildRequires: libraft-devel
BuildRequires: libudev-devel
BuildRequires: help2man
# Needed for manpages generation. Accessing to '/proc/self/...'
BuildRequires: /proc

BuildRequires:	liblxc-devel >= 4.0.0
BuildRequires:	libacl-devel

%description
REST API, command line tool and OpenStack integration plugin for LXC.

%prep
%setup -q
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

pushd .build/src/%import_path

#export TAGS="libsqlite3"
#go install -v -tags "libsqlite3" ./...
export CGO_LDFLAGS_ALLOW="(-Wl,-wrap,pthread_create)|(-Wl,-z,now)"
TAGS="libsqlite3" %golang_build lxc fuidshift lxd-benchmark lxc-to-lxd lxd/db lxd
CGO_ENABLED=0 TAGS="netgo" %golang_build lxd-migrate
CGO_ENABLED=0 TAGS="agent,netgo" %golang_build lxd-agent

#%golang_build lxd lxc fuidshift lxd-benchmark lxd-p2c lxc-to-lxd lxd/db
popd

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
mkdir -p -- %buildroot%_libexecdir/lxd

# configuration
install -D %SOURCE3 %buildroot%_sysconfdir/sysconfig/lxd
# configuration for dnsmasq called in lxd-bridge
install -D %SOURCE4 %buildroot%_sysconfdir/lxd/dnsmasq.conf

#services
# systemd
mkdir -p %buildroot%_unitdir
cp -av %SOURCE11 %buildroot%_unitdir/
cp -av %SOURCE12 %buildroot%_unitdir/
cp -av %SOURCE13 %buildroot%_unitdir/

# install bash completion
mkdir -p %buildroot%_datadir/bash-completion/completions/
cp -av scripts/bash/lxd-client %buildroot%_datadir/bash-completion/completions/

# /var/{lib,log}/lxd
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name

# Install the manpages
mkdir -p %buildroot%_man1dir
help2man %buildroot%_bindir/fuidshift -n "uid/gid shifter" --no-info --no-discard-stderr > %buildroot%_man1dir/fuidshift.1
help2man %buildroot%_bindir/lxc-to-lxd -n "Convert LXC containers to LXD" --no-info --version-string=%version --no-discard-stderr > %buildroot%_man1dir/lxc-to-lxd.1
help2man %buildroot%_bindir/lxd-benchmark -n "The container lightervisor - benchmark" --no-info --no-discard-stderr > %buildroot%_man1dir/lxd-benchmark.1
%buildroot%_bindir/lxd manpage %buildroot%_man1dir/
%buildroot%_bindir/lxc manpage %buildroot%_man1dir/

# cleanup
rm -rf -- %buildroot%go_path

%pre
%_sbindir/groupadd -r -f %lxdgroup 2>/dev/null || :
%_sbindir/useradd  -r -g %lxdgroup -c "LXD daemon" \
   -s /dev/null -d /dev/null %lxduser 2>/dev/null || :

%post
if [ $1 = 1 ]; then
    if ! grep -qs '^root:' /etc/subuid \
       && ! grep -qs '^root:' /etc/subgid \
       && ! grep -qs '^lxd:' /etc/subuid \
       && ! grep -qs '^lxd:' /etc/subgid
    then
        %_sbindir/usermod --add-subgids 100000-165535 root ||:
        %_sbindir/usermod --add-subgids 100000-165535 lxd ||:
        %_sbindir/usermod --add-subuids 100000-165535 root ||:
        %_sbindir/usermod --add-subuids 100000-165535 lxd ||:
   fi
fi

%post_service %name

%preun
%preun_service %name

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

%config(noreplace) %_sysconfdir/sysconfig/*
%dir %_sysconfdir/lxd
%config(noreplace) %_sysconfdir/lxd/dnsmasq.conf

%_man1dir/*

%changelog
* Tue May 07 2024 Nadezhda Fedorova <fedor@altlinux.org> 5.21.1-alt1
- new version 5.21.1
- change upstream

* Mon Aug 21 2023 Alexey Shabalin <shaba@altlinux.org> 5.16-alt2
- Drop devel package.

* Thu Aug 03 2023 Alexey Shabalin <shaba@altlinux.org> 5.16-alt1
- 5.16

* Wed Jan 26 2022 Alexey Shabalin <shaba@altlinux.org> 4.22-alt1
- new version 4.22.

* Wed Jan 12 2022 Mikhail Gordeev <obirvalger@altlinux.org> 4.21-alt2
- Add requires to attr.

* Wed Dec 22 2021 Alexey Shabalin <shaba@altlinux.org> 4.21-alt1
- new version 4.21.

* Wed Dec 08 2021 Alexey Shabalin <shaba@altlinux.org> 4.20-alt1
- new version 4.20.

* Thu Nov 25 2021 Nikolay A. Fetisov <naf@altlinux.org> 4.17-alt0.61bb78a49.2
- fix build with Go 1.17.1

* Thu Aug 12 2021 Mikhail Gordeev <obirvalger@altlinux.org> 4.17-alt0.61bb78a49.1
- new version 4.17 (Closes: #40674)

* Sat Jul 24 2021 Mikhail Gordeev <obirvalger@altlinux.org> 4.16-alt1
- new version 4.16
- Add subuids and subgids if not added previously

* Thu May 20 2021 Slava Aseev <ptrnine@altlinux.org> 4.10-alt2
- Fix FTBFS due to python3.{prov,req}

* Sat Jan 16 2021 Alexey Shabalin <shaba@altlinux.org> 4.10-alt1
- New version.

* Sun May 17 2020 Alexey Shabalin <shaba@altlinux.org> 4.0.1-alt1
- New LTS version.

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 4.0.0-alt1
- New version.

* Tue Nov 12 2019 Denis Pynkin <dans@altlinux.org> 3.18-alt1
- New version
- Have to checkout module with:
  go get github.com/spf13/cobra@77e4d5aecc4d34e58f72e5a1c4a5a13ef55e6f44
- Fix help2man call
- Added new build requirements to libraft and libco

* Mon Sep 30 2019 Denis Pynkin <dans@altlinux.org> 3.17-alt1
- New version

* Sun Jun 02 2019 Mikhail Gordeev <obirvalger@altlinux.org> 3.10-alt3
- Add rsync, iptables and dnsmasq to requires

* Wed Mar 13 2019 Mikhail Gordeev <obirvalger@altlinux.org> 3.10-alt2
- Fix build by vendorizing build dependencies

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
