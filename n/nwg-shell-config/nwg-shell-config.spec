%define _unpackaged_files_terminate_build 1

Name: nwg-shell-config
Version: 0.5.64
Release: alt1

Summary: nwg-shell configuration utility
License: MIT
Group: Graphical desktop/Other
URL: https://github.com/nwg-piotr/nwg-shell-config

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

#Requires: /usr/bin/nwg-screenshot-cli
Requires: typelib(AyatanaAppIndicator3)
Requires: python3(requests)
Requires: playerctl
Requires: gtklock
Requires: wlsunset

# Path /usr/share/i18n/locales/ is needed by /usr/bin/nwg-shell-translate
Requires: glibc-i18ndata

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Nwg-shell-config utility provides a graphical user interface for
configuring sway and Hyprland Wayland compositors in nwg-shell.

%prep
%setup -n %name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

# installing additional files
install -Dm 644 %{name}.desktop %buildroot/%_desktopdir/%{name}.desktop
install -Dm 644 *.svg -t %buildroot/%_pixmapsdir/

%files
%doc LICENSE README.md
%python3_sitelibdir/nwg_shell_config/
%python3_sitelibdir/%{pyproject_distinfo nwg_shell_config}
%_bindir/*
%_desktopdir/%{name}.desktop
%_pixmapsdir/*

%changelog
* Wed Apr 22 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.64-alt1
- New version 0.5.64.

* Fri Apr 03 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.63-alt1
- New version 0.5.63.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.62-alt1
- New version 0.5.62.

* Sat Jun 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.60-alt1
- New version 0.5.60.

* Sat Jun 14 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.59-alt1
- New version 0.5.59.

* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.58-alt1
- Initial build for Sisyphus with support of Ayatana Indicator
