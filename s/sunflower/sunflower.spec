%define oname Sunflower
Name:    sunflower
Version: 0.5.63
Release: alt1

Summary: Small and highly customizable twin-panel file manager for Linux with support for plugins
License: GPL-3.0
Group:   Graphical desktop/GNOME
URL:     https://github.com/MeanEYE/Sunflower

Packager: Alexander Burmatov <thatman@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-chardet
BuildRequires: python3-modules-sqlite3
BuildRequires: libgtk+3-gir-devel
BuildRequires: libnotify-gir
BuildRequires: libvte3-gir-devel

BuildArch: noarch

Source:  %name-%version.tar

Patch1:  update-path-for-icon.patch

%description
Sunflower is a small and highly customizable twin-panel file manager for Linux
with support for plugins. It is intended to be an easy-to-use and powerful
file manager that seamlessly integrates into the GNOME desktop environment
(but not limited to). Fully compatible and native to Wayland compositors.

%prep
%setup
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%oname-%version.dist-info
%_datadir/%name
%_datadir/applications/%oname.desktop

%changelog
* Fri Mar 10 2023 Alexander Burmatov <thatman@altlinux.org> 0.5.63-alt1
- Initial build for Sisyphus
- New file manager (ALT #45433)
