%define _unpackaged_files_terminate_build 1

Name: nwg-clipman
Version: 0.2.8
Release: alt1

Summary: nwg-shell clipboard manager - a GTK3-based GUI for cliphist
License: MIT
Group: Graphical desktop/Other
URL: https://github.com/nwg-piotr/nwg-clipman

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: cliphist
Requires: wl-clipboard
Requires: typelib(GtkLayerShell)

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
%summary

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
%doc LICENSE README.md nwg-clipman.svg
%python3_sitelibdir/nwg_clipman/
%python3_sitelibdir/%{pyproject_distinfo nwg_clipman}/*
%_bindir/*
%_desktopdir/%{name}.desktop
%_pixmapsdir/*

%changelog
* Sun Nov 30 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.8-alt1
- New version 0.2.8.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.7-alt1
- New version 0.2.7.

* Sat Jun 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.6-alt1
- New version 0.2.6.

* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus
