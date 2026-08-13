%global import_path go.etcd.io/bbolt
%global _unpackaged_files_terminate_build 1

Name: bbolt
Version: 1.5.0
Release: alt1
Summary: Bolt is a pure Go key/value store

Group: Development/Databases
License: MIT
Url: https://go.etcd.io/bbolt
Vcs: https://github.com/etcd-io/bbolt.git
Source: %name-%version.tar
Source1: vendor.tar
Patch0: fix-print-version.patch

ExcludeArch: %ix86

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.25
BuildRequires: /proc

%description
%summary.
The goal of the project is to provide a simple, fast, and reliable database
for projects that don't require a full database server such as Postgres or MySQL.

%prep
%setup -a 1
%patch0 -p1
# Replace default version with current
sed -i 's/Version = "[^"]*"/Version = "%version"/' version/version.go

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w -s -buildid="
export GOFLAGS="-trimpath"

%golang_prepare
%golang_build cmd/bbolt

%install
export IGNORE_SOURCES=1
export BUILDDIR="$PWD/.build"
%golang_install

%check
export GOTOOLCHAIN=local
%make test

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Thu Aug 13 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.5.0-alt1
- 1.5.0.
- Enable tests.

* Mon Aug 11 2025 Alexey Shabalin <shaba@altlinux.org> 1.4.2-alt1
- 1.4.2.

* Tue Nov 21 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.3.8-alt1
- Initial build for ALT.
