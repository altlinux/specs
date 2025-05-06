%define _unpackaged_files_terminate_build 1
%define import_path github.com/pingcap/tidb

Name: tidb
Version: 7.5.6
Release: alt1

Summary: Is an open-source, cloud-native, distributed SQL database
License: Apache-2.0
Group: Development/Databases
Url: https://www.pingcap.com
Vcs: https://github.com/pingcap/tidb

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %name-%version-dist.tar

# Opened issue Link:  https://github.com/pingcap/tidb/issues/60959
ExcludeArch: i586

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
TiDB is an open-source, distributed
SQL database written in Go, designed to deliver
horizontal scalability, high availability, and real-time
analytical processing (HTAP) while maintaining
full compatibility with the MySQL protocol.
Built for modern cloud-native architectures, TiDB combines the familiarity of
MySQL with the resilience of distributed systems,
enabling seamless scaling for high-traffic applications.

%prep
%setup -a1 -a2

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd $BUILDDIR/src/%import_path
%golang_build cmd/%name-server

%install
export BUILDDIR="$PWD/.build"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1

install -Dm644 dist/tidb.service %buildroot/%_unitdir/tidb.service
install -Dm644 dist/tidb-sysusers.conf %buildroot/%_sysusersdir/tidb.conf
install -Dm644 dist/tidb-tmpfiles.conf %buildroot/%_tmpfilesdir/tidb.conf
install -Dm644 dist/tidb.toml %buildroot/%_sysconfdir/tidb/tidb.toml

%golang_install

%files
%doc LICENSE README.md SECURITY.md
%_bindir/tidb-server
%_sysconfdir/tidb/tidb.toml
%_unitdir/tidb.service
%_sysusersdir/tidb.conf
%_tmpfilesdir/tidb.conf

%changelog
* Wed Apr 3 2025 Ivan Khanas <xeno@altlinux.org> 7.5.6-alt1
- Initial build for ALT Sisyphus.
