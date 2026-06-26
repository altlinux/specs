Name:    go-tpc
Version: 1.0.12
Release: alt1

Summary: A toolbox to benchmark workloads in TPC
License: Apache-2.0
Group:   Databases
URL:     https://github.com/pingcap/go-tpc

BuildRequires(pre): rpm-build-golang
BuildRequires: golang /proc
ExclusiveArch: %go_arches

Source: %name-%version.tar
Patch0: Makefile.patch

%description
A toolbox to benchmark workloads in TPC for TiDB and almost MySQL
compatible databases, and PostgreSQL compatible database, such as
PostgreSQL / CockroachDB / AlloyDB / Yugabyte.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
install -p -m 755 -D bin/go-tpc %buildroot%_bindir/go-tpc

%files
%doc README.md LICENSE docs
%_bindir/*

%changelog
* Thu Jun 18 2026 Alexei Takaseev <taf@altlinux.org> 1.0.12-alt1
- Initial build for c10f1
