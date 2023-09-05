# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qtilitools
Version: 0.1.1
Release: alt2.20230810

Summary: Scripts/commands used in the Qtilities organization
License: BSD-3-Clause
Group: Development/Other

Url: https://github.com/qtilities/qtilitools
Source: %name-%version.tar
Patch: qtilitools-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/qtls-translate
%_datadir/cmake/%name
%doc COPYING README.md

%changelog
* Tue Sep 05 2023 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt2.20230810
- Fix Url
- Fix qtls-translate for ALT Linux (Closes: 47467)

* Sun Aug 20 2023 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt1.20230810
- initial build
