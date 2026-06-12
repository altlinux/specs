Name:    qpdftools
Version: 3.1.3
Release: alt1

Summary: Qpdf Tools is an easy-to-use Qt interface for Ghostscript and QPDF
License: Unlicense
Group:   Text tools
Url:     https://github.com/silash35/qpdftools

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake extra-cmake-modules
BuildRequires: qt6-base-devel qt6-tools-devel

%description
Qpdf Tools is an easy-to-use Qt interface for Ghostscript and QPDF, which
makes it possible for normal users to manage their PDFs.

%prep
%setup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md UNLICENSE
%_bindir/qpdftools
%_desktopdir/br.eng.silas.qpdftools.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/br.eng.silas.qpdftools.svg
%_datadir/metainfo/br.eng.silas.qpdftools.metainfo.xml

%changelog
* Fri Jun 12 2026 Sergey Palcheh <minergenon@altlinux.org> 3.1.3-alt1
- new version 3.1.3

* Sun Jun 01 2025 Sergey Palcheh <minergenon@altlinux.org> 3.1.2-alt1
- new version 3.1.2 (with rpmrb script)

* Wed Feb 26 2025 Sergey Palcheh <minergenon@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
