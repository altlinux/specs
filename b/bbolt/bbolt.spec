%global import_path go.etcd.io/bbolt
%global _unpackaged_files_terminate_build 1

Name: bbolt
Version: 1.4.2
Release: alt1
Summary: Bolt is a pure Go key/value store

Group: Development/Databases
License: MIT
Url: https://%import_path
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.23
BuildRequires: /proc

%description
%summary.
The goal of the project is to provide a simple, fast, and reliable database
for projects that don't require a full database server such as Postgres or MySQL.

%prep
%setup -q
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export CGO_ENABLED=0

%golang_prepare
%golang_build cmd/bbolt

%install
export IGNORE_SOURCES=1
export BUILDDIR="$PWD/.gopath"
%golang_install

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Mon Aug 11 2025 Alexey Shabalin <shaba@altlinux.org> 1.4.2-alt1
- 1.4.2.

* Tue Nov 21 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.3.8-alt1
- Initial build for ALT.

