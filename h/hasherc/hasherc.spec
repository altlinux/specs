%define _unpackaged_files_terminate_build 1

%define shortname hshc
%define commonname hasherc_common

Name: hasherc
Version: 0.3.0
Release: alt1

Summary: A tool for building packages for ALT operating systems in containers
License: GPL-3.0-or-later
Group: Development/Tools
Url: https://altlinux.space/alt-gnome/hasherc
Vcs: https://altlinux.space/alt-gnome/hasherc.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: podman

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-python3
BuildRequires: meson

%description
%summary.

NOT FULL REPLACEMENT FOR HASHER

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
%_bindir/gear-%shortname
%_bindir/%shortname-*
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/%commonname/

%changelog
* Sat Jun 14 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.3.0-alt1
- New version: 0.3.0

* Fri May 30 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.2.1-alt1
- New version: 0.2.1

* Thu May 29 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.2.0-alt1
- New version: 0.2.0

* Wed May 28 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.1.4-alt1
- Initial build.
