Name: mount-archive
Version: 1.26
Release: alt1

Summary: FUSE file system for archives and compressed files (ZIP, RAR, 7Z, ISO, TGZ, XZ...)

License: Apache-2.0
Group: System/Kernel and hardware
Url: https://github.com/fdegros/mount-archive

# Source-url: https://github.com/fdegros/mount-archive/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# libfuse3 runs fusermount3 to mount and unmount as a regular user
Requires: /usr/bin/fusermount3

BuildRequires: gcc-c++ make pkg-config
BuildRequires: libfuse3-devel libarchive-devel boost-devel-headers
BuildRequires: libgtest-devel

%description
mount-archive (formerly fuse-archive) serves one or several archives or
compressed files (e.g. foo.tar, foo.tar.gz, foo.xz, foo.zip, foo.7z, foo.rar,
foo.iso) as a read-only FUSE file system. It uses libarchive to read
archives and FUSE 3 to provide the file system.

The program is installed as fuse-archive.

%prep
%setup
# keep the shipped man page, do not regenerate it with pandoc
touch fuse-archive.1

%build
%make_build CXXFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%_prefix

%check
# tests/test.py mounts archives and needs /dev/fuse; run the unit tests only
%make_build CXXFLAGS="%optflags" unit_tests

%files
%doc LICENSE README.md AUTHORS
%_bindir/fuse-archive
%_man1dir/fuse-archive.1*

%changelog
* Wed Nov 04 2026 Vitaly Lipatov <lav@altlinux.ru> 1.26-alt1
- initial build for ALT Sisyphus

