%define _unpackaged_files_terminate_build 1

%def_without check

Name: quickbib
Version: 0.9.4
Release: alt1

Summary: Get BibTeX from a DOI - fast
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
QuickBib helps you quickly generate BibTeX bibliographic entries from
identifiers such as DOIs, arXiv IDs, article URLs and their titles.

Enter an identifier and QuickBib will fetch the metadata and produce a
ready-to-use BibTeX entry which you can copy to your clipboard and use
in your LaTeX documents.

%prep
%setup
sed -i "s|Categories=.*|Categories=Office;Publishing;|" io.github.archisman_panigrahi.QuickBib.desktop
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
%_desktopdir/*.desktop
%exclude %_datadir/doc/quickbib/README.md
%_iconsdir/hicolor/128x128/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%exclude %_datadir/quickbib/LICENSE
%dir %_datadir/quickbib
%dir %_datadir/quickbib/quickbib
%dir %_datadir/quickbib/quickbib/po
%_datadir/quickbib/quickbib/po/*
%_datadir/quickbib/quickbib/*.py
%_datadir/metainfo/*.metainfo.xml

%changelog
* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 0.9.4-alt1
- New version 0.9.4.

* Sat Jun 06 2026 Nikolay Strelkov <snk@altlinux.org> 0.9.3-alt1
- New version 0.9.3.

* Sat May 30 2026 Nikolay Strelkov <snk@altlinux.org> 0.9.1-alt1
- New version 0.9.1.

* Sat May 23 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.3-alt1
- New version 0.8.3.

* Thu May 21 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.2-alt1
- New version 0.8.2.

* Fri May 01 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.2-alt1
- New version 0.7.2.

* Wed Mar 04 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.1-alt1
- New version 0.7.1.

* Wed Feb 25 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 0.6.1-alt1
- New version 0.6.1.

* Sun Feb 08 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.91-alt1
- New version 0.5.91.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.3-alt1
- New version 0.5.3.

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.2-alt1
- New version 0.5.2.

* Fri Dec 19 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.1-alt1
- New version 0.5.1.

* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.1-alt1
- New version 0.4.1.

* Tue Nov 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus
