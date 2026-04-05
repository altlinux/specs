%define _unpackaged_files_terminate_build 1

%def_with check

Name: krop
Version: 0.7.0
Release: alt1

Summary: Simple graphical tool to crop the pages of PDF files
License: GPL-3.0-or-later
Group: Office
URL: https://github.com/arminstraub/krop

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: python3-module-pymupdf

BuildArch: noarch

Source: %name-%version.tar

%description
krop is a simple graphical tool to crop the pages of PDF files.
It is written in Python and relies on PyQt and PyMuPDF (or a suitable
subset of pypdf/pikepdf/python-poppler-qt) for its functionality.
A unique feature of krop is its ability to automatically split pages
into subpages to fit the limited screen size of devices such as
eReaders. This is particularly useful, if your eReader does not
support convenient scrolling.

%prep
%setup -n %name-%version
sed -i 's|^Categories=.*|Categories=Office;Publishing;|' com.arminstraub.krop.desktop

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc ChangeLog LICENSE README.md TODO
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_bindir/krop
%_desktopdir/com.arminstraub.krop.desktop
%_iconsdir/hicolor/scalable/apps/com.arminstraub.krop.svg
%_man1dir/krop.1.*
%_datadir/metainfo/com.arminstraub.krop.metainfo.xml

%changelog
* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
