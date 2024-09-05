%define qdoc_found %{expand:%%(if [ -e %_dqt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module dqtimageformats

%def_enable fmt_mng
# Debian abandon libjasper
%def_disable fmt_jp2

Name: dqt5-imageformats
Version: 5.15.13
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt5 - QtImageFormats component
Url: http://qt.io/
License: LGPLv2 / GPLv3

Requires: %name-common = %EVR
Requires: dqt5-svg

Source: %qt_module-everywhere-src-%version.tar

# Automatically added by buildreq on Tue Jun 03 2014 (-bi)
# optimized out: elfutils libGL-devel libcloog-isl4 libjpeg-devel libdqt5-clucene libdqt5-core libdqt5-gui libdqt5-help libdqt5-network libdqt5-sql libdqt5-widgets libdqt5-xml libstdc++-devel python-base dqt5-base-devel dqt5-declarative-devel dqt5-tools ruby ruby-stdlibs zlib-devel
#BuildRequires: gcc-c++ glibc-devel-static libjasper-devel libmng-devel libtiff-devel libwebp-devel python-module-protobuf dqt5-script-devel dqt5-tools-devel dqt5-webkit-devel dqt5-xmlpatterns-devel rpm-build-ruby
BuildRequires(pre): rpm-macros-dqt5 dqt5-tools
BuildRequires: gcc-c++ glibc-devel libtiff-devel libwebp-devel dqt5-base-devel
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
Requires: dqt5-base-common
%description common
Common package for %name

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%prep
%setup -qn %qt_module-everywhere-src-%version
syncqt.pl-dqt5 -version %version

%if_disabled fmt_jp2
rm -rf config.tests/jasper
%endif
%if_disabled fmt_mng
rm -rf  config.tests/libmng
%endif


%build
%qmake_dqt5
%make_build
%if %qdoc_found
export QT_HASH_SEED=0
%make docs
%endif

%install
%install_dqt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files
%doc LICENSE*EXCEPT*
%_dqt5_plugindir/imageformats/*.so
%_dqt5_libdir/cmake/Qt5Gui/Qt5Gui_*Plugin.cmake

%files doc
%if %qdoc_found
%_dqt5_docdir/*
%endif

%changelog
* Tue May 21 2024 Leontiy Volodin <lvol@altlinux.org> 5.15.13-alt0.dde.1
- fork qt5 for separate deepin buildings (ALT #48138)

* Thu Apr 04 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.13-alt1
- new version

* Wed Jan 10 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.12-alt1
- new version

* Wed Nov 22 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.11-alt1
- new version

* Mon Jul 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.10-alt1
- new version

* Wed Apr 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.9-alt1
- new version

* Wed Jan 18 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.8-alt1
- new version

* Tue Nov 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt1
- new version

* Fri Oct 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.6-alt1
- new version

* Mon Jul 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt3
- merge M90P changes

* Tue Oct 06 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt2
- build without libjasper

* Tue Oct 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.12.9-alt1.M90P.1
- Fixed build with new libjasper.

* Thu Sep 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt1
- new version

* Fri Jul 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Mon Jun 22 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt1
- new version

* Thu Apr 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Thu Mar 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1
- new version

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1
- new version

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1
- new version

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1
- new version

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1
- new version

* Fri May 12 2017 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt2
- rebuild with new libmng

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Thu Oct 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1.M80P.1
- build for M80P

* Thu Oct 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt2
- build with mng and jasper

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Mon Jan 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- rebuild with new libwebp

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Tue Jul 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Tue Jun 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Tue Feb 18 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Thu Dec 12 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt0.M70P.1
- built for M70P

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
