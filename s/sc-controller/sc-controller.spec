Name: sc-controller
Version: 0.4.8.11
Release: alt1
Summary: User-mode driver and GTK3-based GUI for the Steam Controller
License: GPL-2.0-only
Group: System/Libraries
Url: https://github.com/Ryochan7/sc-controller
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
BuildRequires(Pre): rpm-macros-python3
BuildRequires: desktop-file-utils
BuildRequires: fdupes
BuildRequires: gobject-introspection
BuildRequires: hicolor-icon-theme
BuildRequires: pkg-config
BuildRequires: python3-module-setuptools 
BuildRequires: shared-mime-info
BuildRequires: zlib-devel
BuildRequires: python3-dev
BuildRequires: libudev-devel
Requires: python3-module-evdev
Requires: python3-module-pygobject3
Requires: python3-module-pycairo
Requires: python3-module-libacl
Requires: python3-module-setuptools
Requires: python3-module-vdf
Requires: librsvg-gir

%description
Application allowing to setup, configure and use the Steam Controller
without using the Steam client.

%prep
%setup

%build
python3 setup.py build

%install
python3 setup.py install --root=%buildroot --optimize=1
install -Dpm0644 scripts/69-sc-controller.rules %buildroot%_udevrulesdir/69-sc-controller.rules

fdupes %buildroot%prefix

%files
%doc LICENSE
%doc README.md ADDITIONAL-LICENSES TODO.md
%_bindir/*
%python3_sitelibdir/*
%_desktopdir/*
%_pixmapsdir/*
%_datadir/scc/
%_datadir/mime/packages/*
%_iconsdir/hicolor/*
%_udevrulesdir/69-sc-controller.rules

%changelog
* Sun Jul 02 2023 Artyom Bystrov <arbars@altlinux.org> 0.4.8.11-alt1
- initial build for ALT Sisyphus
