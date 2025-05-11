%define _unpackaged_files_terminate_build 1

Name: typobuster
Version: 1.0.0
Release: alt1

Summary: Lightweight editor with text transformations and auto-correction.
License: GPL-3.0
Group: Graphical desktop/Other
URL: https://github.com/nwg-piotr/typobuster

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: typelib(Gspell)

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
Typobuster is a simplified text editor with a wide selection of
transformations and automatic correction of common typos.

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
%doc README.md typobuster.svg
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_bindir/*
%_desktopdir/%{name}.desktop
%_pixmapsdir/*

%changelog
* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
