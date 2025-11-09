%define _unpackaged_files_terminate_build 1

%def_without check

Name: quickbib
Version: 0.3.2
Release: alt1

Summary: Cross platform DOI/arXiv to BibTeX desktop utility
License: GPL-3.0-or-later
Group: Publishing
URL: https://github.com/archisman-panigrahi/QuickBib

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: meson

%filter_from_requires /python3(usr.src.tmp.quickbib-buildroot.usr.share.quickbib.quickbib.app_info)/d
%filter_from_requires /python3(usr.src.tmp.quickbib-buildroot.usr.share.quickbib.quickbib.main_window)/d

BuildArch: noarch

Source: %name-%version.tar

%description
This is a cross platform app that enables you to get the bibtex
entry from a DOI number.

It uses doi2bib3 as its backend.

%prep
%setup
sed -i "s|Categories=.*|Categories=Office;Publishing;|" quickbib.desktop
sed -i "s|assets/screenshots/||" README.md
sed -i "s|assets/icon/scalable/|%_iconsdir/hicolor/scalable/apps/|" README.md

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc LICENSE README.md
%doc assets/screenshots/quickbib_arxiv.png
%_bindir/quickbib
%_desktopdir/quickbib.desktop
%exclude %_datadir/doc/quickbib/README.md
%_iconsdir/hicolor/128x128/apps/io.github.archisman_panigrahi.quickbib.png
%_iconsdir/hicolor/scalable/apps/io.github.archisman_panigrahi.quickbib.svg
%exclude %_datadir/quickbib/LICENSE
%dir %_datadir/quickbib
%dir %_datadir/quickbib/quickbib
%_datadir/quickbib/quickbib/*.py

%changelog
* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus
