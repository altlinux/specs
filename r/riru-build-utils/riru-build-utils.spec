%define _unpackaged_files_terminate_build 1

%define shortname rbu
%define snakename riru_build_utils

Name: riru-build-utils
Version: 0.10.5
Release: alt1

Summary: Build utilities for Average Rirusha Project
License: GPL-3.0-or-later and BSD-2-Clause
Group: Development/Tools
Url: https://altlinux.space/rirusha/riru-build-utils
Vcs: https://altlinux.space/rirusha/riru-build-utils.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: rpm-utils
Requires: openssh-clients
Requires: gear-remotes-utils
Requires: git
Requires: hasherc
Requires: meson

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: python3-module-paramiko
BuildRequires: python3-module-lxml
BuildRequires: python3-module-requests

%description
%summary.

Contains update, test and create commands.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_bindir/%shortname
%_bindir/%shortname-*
%python3_sitelibdir_noarch/%snakename/
%_datadir/%name/

%changelog
* Thu May 29 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.10.5-alt1
- New version: 0.10.5

* Wed May 28 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.10.2-alt1
- New version: 0.10.2
- Change upstream URL/VCS

* Mon Feb 17 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.8.6-alt1
- Initial build.
