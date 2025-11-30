%define _unpackaged_files_terminate_build 1

%define pypi_name pympress

%def_without check

Name: python3-module-%pypi_name
Version: 1.8.6
Release: alt1

Summary: simple and powerful dual-screen PDF reader
License: GPL-2.0-or-later
Group: Office
URL: https://github.com/Cimbali/pympress

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

Requires: libpoppler-gir
Requires: libgstreamer1.0-gir

BuildArch: noarch

Source: %pypi_name-%version.tar

Patch: %name-%version-%release.patch

%description
Pympress is a little PDF reader written in Python using Poppler for PDF
rendering and GTK+ for the GUI.

It is designed to be a dual-screen reader used for presentations and public
talks, with two displays: the *Content window* for a projector, and the
*Presenter window* for your laptop.

It comes with many great features:

* supports embedded videos
* text annotations displayed in the presenter window
* natively supports beamer's *notes on second screen*!

%prep
%setup -n %pypi_name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE.txt README.md
%_bindir/pympress
%_desktopdir/io.github.pympress.desktop
%_pixmapsdir/pympress.png
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Nov 30 2025 Nikolay Strelkov <snk@altlinux.org> 1.8.6-alt1
- Initial build for Sisyphus
