%define gitrev          b9627fff

Name:    wal-g
Version: 3.0.8
Release: alt1

Summary: WAL-G is an archival restoration tool for PostgreSQL.
License: Apache-2.0
Group:   Databases
URL:     https://github.com/wal-g/wal-g

BuildRequires(pre): rpm-build-golang
BuildRequires: golang /proc
BuildRequires: libbrotli-devel liblzo2-devel libsodium-devel
ExclusiveArch: %go_arches

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

%description
WAL-G is the successor of WAL-E with a number of key differences. WAL-G uses LZ4,
LZMA, ZSTD, or Brotli compression, multiple processors, and non-exclusive base
backups for Postgres.

%prep
%setup
%patch0 -p1

# Build with debuginfo
sed -i 's/-s -w//g' Makefile

%build
export WALG_VERSION=%version
export GIT_REVISION=%gitrev

export USE_BROTLI=1
export USE_LIBSODIUM=1
export USE_LZO=1
export GOEXPERIMENT=jsonv2

%make_build pg_build

%install
install -p -m 755 -D main/pg/wal-g %buildroot%_bindir/wal-g

%files
%doc LICENSE.md docs
%_bindir/*

%changelog
* Wed Jun 24 2026 Alexei Takaseev <taf@altlinux.org> 3.0.8-alt1
- Initial build for c10f1
