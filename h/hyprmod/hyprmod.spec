%global _unpackaged_files_terminate_build 1
%global namespace io.github.bluemancz
%def_with check

Name: hyprmod
Version: 0.4.0
Release: alt1
Summary: A native GTK4/libadwaita settings app for Hyprland
License:  GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/BlueManCZ/hyprmod
VCS: https://github.com/BlueManCZ/hyprmod

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: /usr/bin/glib-compile-schemas

%if_with check
BuildRequires: libadwaita-gir
BuildRequires: libappstream-glib
BuildRequires: lua5.4
BuildRequires: python3-module-hyprland-config
BuildRequires: python3-module-hyprland-monitors
BuildRequires: python3-module-hyprland-schema
BuildRequires: python3-module-hyprland-socket
BuildRequires: python3-module-hyprland-state
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-pytest
BuildRequires: xvfb-run
%endif

%description
A native GTK4/libadwaita settings app for Hyprland - 
tweak any option, see it change live, save when you're happy.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
install -Dm 0644 data/applications/%namespace.%name.desktop \
                 %buildroot%_desktopdir/%namespace.%name.desktop
install -Dm 0644 data/metainfo/%namespace.%name.metainfo.xml \
                 %buildroot%_datadir/metainfo/%namespace.%name.metainfo.xml
install -Dm 0644 data/icons/hicolor/scalable/apps/%namespace.%name.svg \
                 %buildroot%_iconsdir/hicolor/scalable/apps/%namespace.%name.svg

%check
xvfb-run -a python3 -m pyproject_installer run -- python3 -m pytest -k "not test_environment_block_present"
desktop-file-validate %buildroot%_desktopdir/%namespace.%name.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%namespace.%name.metainfo.xml

%files
%_bindir/%name
%_desktopdir/%namespace.%name.desktop
%_datadir/metainfo/%namespace.%name.metainfo.xml
%_iconsdir/hicolor/scalable/apps/%namespace.%name.svg
%python3_sitelibdir/%name
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Sun Jul 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.0-alt1
- Updated to version 0.4.0.

* Sun May 31 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.0-alt1
- Updated to version 0.3.0.

* Sun May 10 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.0-alt1
- Updated to version 0.2.0.

* Sat May 09 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.0-alt1
- Initial build for ALT.
