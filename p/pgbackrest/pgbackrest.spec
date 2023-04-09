Name:    pgbackrest
Version: 2.45
Release: alt1

Summary: Reliable PostgreSQL Backup & Restore
License: MIT
Group:   Other

Url:     https://github.com/pgbackrest/pgbackrest
Source: %name-%version.tar

#BuildRequires:
BuildRequires: libpq5-devel
BuildRequires: openssl-devel 
BuildRequires: libxml2-devel
BuildRequires: libyaml-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel

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
pushd src
%configure
%make_build
popd

%install
%makeinstall_std -C src

%files
%doc *.md
%_bindir/*

%changelog
* Fri Apr 07 2023 Nikolay Burykin <bne@altlinux.org> 2.45-alt1
- Initial build for Sisyphus
