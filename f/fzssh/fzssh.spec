%define _unpackaged_files_terminate_build 1
%define sover 11.0.0

Name: fzssh
Version: 1.2.0
Release: alt1
Summary: FileZilla SSH client library
Group: System/Libraries
License: AGPL-3.0-or-later
Url: https://fzssh.filezilla-project.org/
Source: fzssh-%version.tar
Source999: watch

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: libfilezilla-devel >= 0.55.3
BuildRequires: libnettle-devel >= 3.10
BuildRequires: libgmp-devel >= 6.2
BuildRequires: libargon2-devel

%description
fzssh is an SSH/SFTP client library based on libfilezilla. It is comprised
of libfzssh, libfzssh-crypt and libfzssh-client shared libraries and is
used by FileZilla and related projects.

%package -n libfzssh%sover
Summary: FileZilla SSH client shared libraries
Group: System/Libraries

%description -n libfzssh%sover
fzssh is an SSH/SFTP client library based on libfilezilla.

This package contains shared libraries needed to run applications
that use fzssh.

%package -n libfzssh-devel
Summary: Development files for fzssh
Group: Development/C++
Requires: libfzssh%sover = %EVR
Requires: libfilezilla-devel

%description -n libfzssh-devel
fzssh is an SSH/SFTP client library based on libfilezilla.

This package contains headers, development symlinks and pkg-config
files needed to build applications against fzssh.

%prep
%setup

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files -n libfzssh%sover
%_libdir/libfzssh.so.%sover
%_libdir/libfzssh-crypt.so.%sover
%_libdir/libfzssh-client.so.%sover

%files -n libfzssh-devel
%doc README NEWS
%_libdir/libfzssh.so
%_libdir/libfzssh-crypt.so
%_libdir/libfzssh-client.so
%_includedir/fzssh/
%_pkgconfigdir/libfzssh-client.pc

%changelog
* Thu Apr 23 2026 Anton Farygin <rider@altlinux.org> 1.2.0-alt1
- initial build for ALT Linux
