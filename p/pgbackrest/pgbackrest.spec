Name:    pgbackrest
Version: 2.57.0
Release: alt1

Summary: Reliable PostgreSQL Backup & Restore
License: MIT
Group:   Other

Url:     https://github.com/pgbackrest/pgbackrest
Source: %name-%version.tar

BuildRequires(pre): meson

BuildRequires: libpq-devel
BuildRequires: libssl-devel
BuildRequires: libxml2-devel
BuildRequires: libyaml-devel
BuildRequires: zlib-devel
BuildRequires: bzlib-devel
BuildRequires: liblz4-devel
BuildRequires: libzstd-devel
BuildRequires: libssh2-devel

%description
pgBackRest aims to be a reliable, easy-to-use backup and restore \
solution that can seamlessly scale up to the largest databases and \
workloads by utilizing algorithms that are optimized for \
database-specific requirements.

The following features are available:
- Parallel backup & restore
- Local or remote operation
- Full, incremental, differential backups
- Backup rotation & archive expiration
- Backup integrity
- Page checksums
- Backup resume
- Streaming compression & checksums
- Delta restore
- Parallel, asynchronous WAL push & get
- Tablespace & link support
- Amazon S3 support
- Encryption
- Compatibility with PostgreSQL >= 8.3

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/*

%changelog
* Wed Oct 22 2025 Alexei Takaseev <taf@altlinux.org> 2.57.0-alt1
- 2.57.0
- Add support PostgreSQL 18
- Use meson for build

* Thu Oct 02 2025 Alexei Takaseev <taf@altlinux.org> 2.54.2-alt2
- Change BR: libpq5-devel -> libpq-devel

* Thu Apr 10 2025 Kirill Izmestev <felixz@altlinux.org> 2.54.2-alt1
- new version 2.54.2

* Fri Apr 07 2023 Nikolay Burykin <bne@altlinux.org> 2.45-alt1
- Initial build for Sisyphus
