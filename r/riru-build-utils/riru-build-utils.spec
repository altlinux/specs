%define _unpackaged_files_terminate_build 1

%define shortname rbu
%define snakename riru_build_utils

Name: riru-build-utils
Version: 0.8.6
Release: alt1

Summary: Build utilities for Average Rirusha Project
License: GPL-3.0-or-later
Group: Development/Tools
Url: https://github.com/Rirusha/riru-build-utils
Vcs: https://github.com/Rirusha/riru-build-utils.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

Requires: rpm-utils
Requires: gear
Requires: openssh-clients
Requires: gear-remotes-utils
Requires: git

BuildRequires(pre): rpm-macros-meson rpm-build-python3
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
%python3_sitelibdir_noarch/%snakename/
%_datadir/%name/

%changelog
* Mon Feb 17 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.8.6-alt1
- Initial build.

