%define _unpackaged_files_terminate_build 1

%def_with check

Name: gitfourchette
Version: 1.9.0
Release: alt1

Summary: Comfortable Git UI for Linux
License: GPL-3.0-only
Group: Development/Tools
URL: https://gitfourchette.org
VCS: https://github.com/jorio/gitfourchette

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3(pygit2)
BuildRequires: python3(pytest)
BuildRequires: python3(pytestqt)
%endif

Requires: git
Requires: python3(PyQt6)
Requires: fuse

# this command is only for Mac, so may be skipped
%filter_from_requires /^.usr.bin.opendiff/d

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

The comfortable Git UI for Linux. Features:

* A comfortable way to explore and understand your Git repositories.
* Powerful tools to stage code, create commits, and manage branches.
* Snappy and intuitive Qt UI designed to fit in snugly with KDE Plasma.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# install icon and desktop file manually
install -Dm644 pkg/appimage/gitfourchette.png %buildroot%_iconsdir/hicolor/256x256/apps/gitfourchette.png
install -Dm644 pkg/appimage/gitfourchette.desktop %buildroot%_desktopdir/gitfourchette.desktop

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md
%_bindir/gitfourchette
%_bindir/gitfourchette-askpass
%_bindir/gitfourchette-mount
%_desktopdir/gitfourchette.desktop
%_iconsdir/hicolor/256x256/apps/gitfourchette.png
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Fri Jul 03 2026 Nikolay Strelkov <snk@altlinux.org> 1.9.0-alt1
- New version 1.9.0.

* Thu May 21 2026 Nikolay Strelkov <snk@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 1.7.1-alt1
- New version 1.7.1.

* Sat Apr 11 2026 Nikolay Strelkov <snk@altlinux.org> 1.7.0-alt1
- New version 1.7.0.

* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 1.6.0-alt1
- New version 1.6.0.

* Sat Jan 17 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus
