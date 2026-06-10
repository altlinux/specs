%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module dqtimageformats

%def_enable fmt_mng
# Debian abandon libjasper
%def_disable fmt_jp2

Name: dqt6-imageformats
Version: 6.10.3
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt6 - QtImageFormats component
Url: http://qt.io/
License: LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

Requires: %name-common = %EVR
Requires: dqt6-svg

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-dqt6 dqt6-tools
BuildRequires(pre): libdqt6-gui libdqt6-qml libdqt6-help
BuildRequires(pre): clang-devel
BuildRequires: cmake glibc-devel libtiff-devel libwebp-devel dqt6-base-devel
%{?_enable_fmt_jp2:BuildRequires: libjasper-devel}
%{?_enable_fmt_mng:BuildRequires: libmng-devel}

%description
The core Qt Gui library by default supports reading and writing image
files of the most common file formats: PNG, JPEG, BMP, GIF and a few more,
ref. Reading and Writing Image Files. The Qt Image Formats add-on module
provides optional support for other image file formats, including:
MNG, TGA, TIFF, WBMP.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: dqt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: dqt6-base-devel
%description devel
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt6 %qt_module

%prep
%setup -qn %qt_module-everywhere-src-%version
%if_disabled fmt_jp2
rm -rf config.tests/jasper
%endif
%if_disabled fmt_mng
rm -rf  config.tests/libmng
%endif

%build
%DQ6build \
    -DQT_GENERATE_SBOM:BOOL=OFF \
    #
%if %qdoc_found
%DQ6make --target docs
%endif

%install
%DQ6install_qt
%if %qdoc_found
#%make -C BUILD DESTDIR=%buildroot install_docs ||:
mkdir -p %buildroot/%_docdir/dqt6/
cp -ar BUILD/share/doc/dqt6/* %buildroot/%_docdir/dqt6/
%endif

# relax depends on plugins files
for f in %buildroot/%_dqt6_libdir/cmake/Qt?*/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files common
%doc LICENSES/*

%files
%_dqt6_plugindir/imageformats/*.so

%files devel
%_dqt6_libdir/cmake/Qt?Gui/Qt?Q*Plugin*.cmake
%_dqt6_libdir/cmake/Qt6/Find*.cmake

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%endif

%changelog
* Mon Jun 08 2026 Leontiy Volodin <lvol@altlinux.org> 6.10.3-alt0.dde.1
- merge with new version

* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt1
- new version

* Wed Feb 25 2026 Leontiy Volodin <lvol@altlinux.org> 6.10.2-alt0.dde.1
- merge with new version

* Thu Feb 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.2-alt1
- new version

* Tue Jan 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.1-alt1
- new version

* Fri Nov 21 2025 Leontiy Volodin <lvol@altlinux.org> 6.9.3-alt0.dde.1
- merge with new version

* Thu Nov 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.3-alt1
- new version

* Tue Aug 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.2-alt1
- new version

* Thu Jun 19 2025 Leontiy Volodin <lvol@altlinux.org> 6.9.1-alt0.dde.1
- merge with new version

* Tue Jun 03 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.1-alt1
- new version

* Tue Feb 25 2025 Leontiy Volodin <lvol@altlinux.org> 6.8.2-alt0.dde.1
- merge with new version

* Thu Feb 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.8.2-alt1
- new version

* Wed Oct 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.7.2-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Thu Jun 02 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
