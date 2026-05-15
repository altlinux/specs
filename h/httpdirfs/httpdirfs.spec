# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: httpdirfs
Version: 1.2.9
Release: alt1
Summary: FUSE mount for HTTP
License: GPL-3.0-or-later
Group: Networking/File transfer
Url: https://github.com/fangfufu/httpdirfs/
Requires: /usr/bin/fusermount3

Source: %name-%version.tar
BuildRequires(pre): rpm-macros-meson
BuildRequires: help2man
BuildRequires: libcurl-devel
BuildRequires: libexpat-devel
BuildRequires: libfuse3-devel
BuildRequires: libgumbo-devel
BuildRequires: libssl-devel
BuildRequires: libuuid-devel
BuildRequires: meson

%description
Filesystem client for HTTP directory listings httpdirfs is program that
can be used to mount HTTP directory listings (generated using an Apache
DirectoryIndex, for example) as a virtual filesystem through the FUSE
interface. It supports HTTP basic authentication.

%prep
%setup
# warning: "_FORTIFY_SOURCE" redefined
sed -i /_FORTIFY_SOURCE/d meson.build

%build
%meson
%meson_build

%install
%meson_install

%check
%buildroot%_bindir/httpdirfs --version

%files
%define _customdocdir %_docdir/%name
%doc CHANGELOG.md LICENSE README.md USAGE.md
%_bindir/httpdirfs
%_man1dir/httpdirfs.1*

%changelog
* Fri May 15 2026 Vitaly Chikunov <vt@altlinux.org> 1.2.9-alt1
- Update to 1.2.9 (2026-05-13).

* Sun May 10 2026 Vitaly Chikunov <vt@altlinux.org> 1.2.8-alt1
- Update to 1.2.8 (2026-05-10).

* Wed Jan 07 2026 Vitaly Chikunov <vt@altlinux.org> 1.2.7-alt1
- First import 1.2.7-41-g2ebd190 (2025-12-13).
