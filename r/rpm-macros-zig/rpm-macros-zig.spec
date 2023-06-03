# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: rpm-macros-zig
Version: 1
Release: alt1
Summary: RPM macros for Zig
License: GPL-2.0-only
Group: Development/Other
BuildArch: noarch

Source: zig.macros

%description
%summary.

%install
install -pDm644 %SOURCE0 %buildroot%_rpmmacrosdir/zig

%files
%_rpmmacrosdir/zig

%changelog
* Sat Jun 03 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- First version.
