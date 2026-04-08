%define _unpackaged_files_terminate_build 1
%global import_path github.com/seaweedfs/seaweedfs

Name: seaweedfs
Version: 4.19
Release: alt1

Summary: Enterprise-Grade Distributed Storage with Self-Healing
License: Apache-2.0
Group: System/Servers
Url: https://seaweedfs.com/
Vcs: https://github.com/seaweedfs/seaweedfs.git

ExclusiveArch: %go_arches
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %name-%version-rust-vendor.tar
Source3: %name.sysconfig
Source4: %name.service

BuildRequires(pre): rpm-build-rust
BuildRequires(pre): rpm-build-golang
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: libssl-devel
BuildRequires: protobuf-compiler

%description
SeaweedFS is a fast distributed storage system for blobs, objects, files,
and data lake, for billions of files! Blob store has O(1) disk seek,
cloud tiering. Filer supports Cloud Drive, xDC replication, Kubernetes,
POSIX FUSE mount, S3 API, S3 Gateway, Hadoop, WebDAV, encryption,
Erasure Coding. Enterprise version is at seaweedfs.com.

%package volume-rust
Summary: Rust-based Volume Server for SeaweedFS
Group: System/Servers
Requires: %name = %version-%release

%description volume-rust
Drop-in replacement for the Go volume server, written in Rust.
Binary compatible with Go server.
Same HTTP and gRPC protocols, seamless migration from Go volume server.

%prep
%setup -a1 -a2
%autopatch -p1

mkdir -p seaweed-volume/.cargo
cat > seaweed-volume/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
export TOPSRCDIR="$PWD"
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd $BUILDDIR/src/%import_path
export LDFLAGS="-X %import_path/weed/util.COMMIT=%version-%release"
%golang_build weed

# Rust volume server
cd $TOPSRCDIR/seaweed-volume
unset LDFLAGS
export RUSTFLAGS="${RUSTFLAGS} -g"
export CARGO_PROFILE_RELEASE_STRIP='none'
%rust_build

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

# Rust volume server
install -D -p -m 0755 $PWD/seaweed-volume/target/release/weed-volume \
%buildroot%_bindir/weed-volume

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

%files volume-rust
%doc seaweed-volume/README.md
%_bindir/weed-volume

%changelog
* Wed Apr 08 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.19-alt1
- Updated from 4.17 to 4.19.
- Added rust-based volume server as subpackage.

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
