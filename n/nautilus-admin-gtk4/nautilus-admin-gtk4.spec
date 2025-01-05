%define nameU nautilus-admin

Name: nautilus-admin-gtk4
Version: 1.2.0
Release: alt3

Summary: Extension for Nautilus to do administrative operations
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://github.com/MacTavishAO/nautilus-admin-gtk4

Vcs: https://github.com/MacTavishAO/nautilus-admin-gtk4

Source0: %name-%version.tar

Patch: nautilus-admin-1.2.0-alt1-fixes.patch

Requires: nautilus-python
%add_python3_path %_datadir/nautilus-python/extensions

BuildRequires(pre): rpm-macros-cmake rpm-build-python3 rpm-build-gir
BuildRequires: cmake

BuildArch: noarch

%description
Nautilus Admin is a simple Python extension for the Nautilus file
manager that adds some administrative actions to the right-click menu:
- Open as Administrator: opens a folder in a new Nautilus window running
  with administrator (root) privileges.
- Edit as Administrator: opens a file in a Gedit window running with
  administrator (root) privileges.

%prep
%setup

%patch -p0

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang --with-gnome %nameU

%files -f %nameU.lang
%doc *.md
%_datadir/nautilus-python/extensions/%nameU.py
%_datadir/nautilus-python/extensions/__pycache__/*

%changelog
* Sun Jan 05 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.2.0-alt3
- drop ru.po
- fix for translated locales

* Fri Dec 20 2024 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt2
- use rpm-build-{python3,gir} to find runtime dependencies
- spec cleanup

* Thu Dec 19 2024 Aleksandr Shamaraev <shad@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
