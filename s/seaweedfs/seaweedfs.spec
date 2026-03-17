%define _unpackaged_files_terminate_build 1
%global import_path github.com/seaweedfs/seaweedfs

Name: seaweedfs
Version: 4.17
Release: alt1

Summary: Enterprise-Grade Distributed Storage with Self-Healing
License: Apache-2.0
Group: System/Servers
Url: https://seaweedfs.com/
Vcs: https://github.com/seaweedfs/seaweedfs.git

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source3: %name.sysconfig
Source4: %name.service

BuildRequires(pre): rpm-build-golang

%description
SeaweedFS is a fast distributed storage system for blobs, objects, files,
and data lake, for billions of files! Blob store has O(1) disk seek,
cloud tiering. Filer supports Cloud Drive, xDC replication, Kubernetes,
POSIX FUSE mount, S3 API, S3 Gateway, Hadoop, WebDAV, encryption,
Erasure Coding. Enterprise version is at seaweedfs.com.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd $BUILDDIR/src/%import_path
export LDFLAGS="-X %import_path/weed/util.COMMIT=%release"
%golang_build weed

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

# install systemd services
install -D -p -m 0644 %SOURCE4 %buildroot%_unitdir/%name.service
install -D -p -m 0640 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -d -m 0750 %buildroot%_localstatedir/%name
install -d -m 0750 %buildroot%_logdir/%name

%pre
%_sbindir/groupadd -r -f _%name ||:
%_sbindir/useradd -r -g _%name -d %_localstatedir/%name -s /dev/null -c "SeaweedFS daemon" _%name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE
%_bindir/weed
%_unitdir/%name.service
%config(noreplace) %attr(640,root,_%name) %_sysconfdir/sysconfig/%name
%dir %attr(750,_%name,_%name) %_localstatedir/%name
%dir %attr(750,_%name,_%name) %_logdir/%name

%changelog
* Tue Mar 17 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.17-alt1
- Updated from 4.16 to 4.17.

* Tue Mar 10 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.16-alt1
- Updated from 4.15 to 4.16.

* Fri Mar 06 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.15-alt1
- Updated from 4.13 to 4.15.

* Sat Feb 21 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 4.13-alt1
- Updated from 4.09 to 4.13.

* Wed Feb 04 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 4.09-alt1
- Initial build for ALT.
