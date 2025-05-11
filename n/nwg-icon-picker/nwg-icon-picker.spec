%define _unpackaged_files_terminate_build 1

Name: nwg-icon-picker
Version: 0.1.1
Release: alt1

Summary: GTK icon chooser with a text search option
License: MIT
Group: Graphical desktop/Other
URL: https://github.com/nwg-piotr/nwg-icon-picker

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
This program is intended to work as the icon picker for nwg-panel, but 
it may be used standalone. It displays a window to choose an icon with a
textual search entry, and returns the icon name. You can also open a file
from the search result in GIMP or Inkscape - if installed.

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
%doc LICENSE README.md nwg-icon-picker.svg
%python3_sitelibdir/nwg_icon_picker/
%python3_sitelibdir/%{pyproject_distinfo nwg_icon_picker}
%_bindir/*
%_desktopdir/%{name}.desktop
%_pixmapsdir/*

%changelog
* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus
