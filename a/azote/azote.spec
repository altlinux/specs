%define _unpackaged_files_terminate_build 1

Name: azote
Version: 1.16.0
Release: alt2

Summary: Wallpaper manager for wlroots-based compositors and some other WMs
License: GPL-3.0 and BSD-1-Clause
Group: Graphical desktop/Other
URL: https://github.com/nwg-piotr/azote

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%add_python3_req_skip gi.repository.GdkPixbuf
%filter_from_requires /^typelib(AppIndicator3)/d
Requires: typelib(AyatanaAppIndicator3)
Requires: python3(send2trash)
Requires: python3(yaml)
# for x11
Requires: python3(Xlib)
Requires: feh
Requires: maim
Requires: slop
# for sway
Requires: wlr-randr

%ifarch x86_64 aarch64
Requires: grim
Requires: slurp
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Azote is a GTK+3 - based picture browser and background setter, as the
frontend to the swaybg (sway/Wayland) and feh (X windows) commands.
The user interface is being developed with multi-headed setups in mind.
Azote also includes several colour management tools.

The program, written primarily for sway, should work on all wlroots-based
Wayland compositors, as well as on some X11 window managers. GNOME is not
supported.

%prep
%setup -n %name-%version
sed -i 's|^Categories=.*|Categories=GTK;Settings;DesktopSettings;|' dist/azote.desktop

%build
%pyproject_build

%install
%pyproject_install
install -Dm 644 -t %{buildroot}/%{_datadir}/pixmaps dist/%{name}.svg
install -Dm 644 -t %{buildroot}/%{_datadir}/%{name} dist/indicator*.png
install -Dm 644 -t %{buildroot}/%_desktopdir/ dist/%{name}.desktop

%files
%doc CREDITS.md README.md LICENSE LICENSE-COLORTHIEF
%_bindir/%name
%_desktopdir/*.desktop
%_pixmapsdir/%{name}.*
%dir %_datadir/%name/
%_datadir/%name/*
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 1.16.0-alt2
- Applied repocop fix for freedesktop-desktop

* Sat May 10 2025 Nikolay Strelkov <snk@altlinux.org> 1.16.0-alt1
- Initial build for Sisyphus
