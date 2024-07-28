# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define  srcname svglib

%def_with check

Name:    python3-module-%srcname
Version: 1.5.1
Release: alt1.1

Summary: Read SVG files and convert them to other formats
License: LGPL-3.0-or-later
Group:   Development/Python3
URL:     https://github.com/deeplook/svglib

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-Reportlab
BuildRequires: python3-module-cssselect2
BuildRequires: python3-module-lxml
BuildRequires: python3-module-chardet
%endif

BuildArch: noarch

# Source-url: https://github.com/deeplook/svglib/archive/refs/tags/v%version.tar.gz
Source: %srcname-%version.tar

Patch: remove-test-required-internet.patch

%description
Svglib is a pure-Python library for reading SVG files and converting
them (to a reasonable degree) to other formats using the ReportLab
Open Source toolkit.

Used as a package you can read existing SVG files and convert them
into ReportLab Drawing objects that can be used in a variety of
contexts, e.g. as ReportLab Platypus Flowable objects or in RML.
As a command-line tool it converts SVG files into PDF ones (but
adding other output formats like bitmap or EPS is really easy
and will be better supported, soon).

Tests include a huge W3C SVG test suite plus ca. 200 flags from
Wikipedia and some selected symbols from Wikipedia (with
increasingly less pointing to missing features).

%package -n svg2pdf
Summary: Convert svg to pdf
Group: File tools
BuildArch: noarch

%description -n svg2pdf
Convert svg to pdf.
This part %name.

%prep
%setup -n %srcname-%version
%autopatch -p1

%build
%pyproject_build

%check
%tox_check_pyproject

%install
%pyproject_install

%files
%python3_sitelibdir/%srcname
%python3_sitelibdir/%srcname-%version.dist-info
%doc *.rst *.txt

%files -n svg2pdf
%_bindir/svg2pdf
%_man1dir/*.1.*

%changelog
* Sun Jul 28 2024 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1.1
- NMU: Fixed FTBFS.

* Mon May 29 2023 Anton Midyukov <antohami@altlinux.org> 1.5.1-alt1
- new version (1.5.1) with rpmgs script

* Fri Jul 30 2021 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
