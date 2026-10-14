Name: scantailor
Version: 1.2.1
Release: alt1

Summary: Scan processing software
License: GPLv3
Group: Graphics
Url: https://github.com/ScanTailor-Advanced/scantailor-advanced

# Source-url: https://github.com/ScanTailor-Advanced/scantailor-advanced/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
# fix translations lookup after the 1.2.0 binary rename
Patch: scantailor-advanced-1.2.1-translations-filter.patch
Patch1: scantailor-advanced-1.2.1-tests-zero-tolerance.patch

BuildRequires: rpm-build-cmake ctest gcc-c++
BuildRequires: boost-devel-headers boost-intrusive-devel boost-devel
BuildRequires: zlib-devel libjpeg-devel libtiff-devel libpng-devel
BuildRequires: qt6-base-devel qt6-tools-devel qt6-svg-devel

%description
scantailor-advanced is a book scan processing software.
ScanTailor Advanced is the version that merges the features
of the ScanTailor Featured and ScanTailor Enhanced versions,
brings new ones and fixes.
It splits scanned pages, aligns, and converts to b/w from
grayscale. It has GUI interface. Analogs of this
program are ScanKromsator (written by kamerade bolega,
currently discontinued), BookRestorer.

%description -l ru_RU.UTF-8
Scantailor - программа для обработки отсканированных
книг. Эта программа может разделять развороты, выравнивать
страницы и переводить в ч/б из градаций серого. Имеет
GUI интерфейс. Наиболее известными аналогами
программы является ScanKromsator (написан камрадом bolega,
сейчас не развивается) и BookRestorer.

%prep
%setup
%patch -p1
%patch1 -p1
# keep settings and translations under the old application name
subst 's|set(APPLICATION_NAME "${target_name}")|set(APPLICATION_NAME "%name")|' CMakeLists.txt
# remove project's options
subst "s|.*add_compile_options.*||" CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
# compatibility with the old binary name
ln -s scantailor-advanced %buildroot%_bindir/%name

%check
export QT_QPA_PLATFORM=offscreen
%ctest -E imageproc_tests
# compares scaleToGray() with QImage::scaled(), whose smoothing differs in Qt6
%_cmake__builddir/imageproc_tests --run_test='!ScaleTestSuite/test_random_image'

%files
%_bindir/scantailor-advanced
%_bindir/%name
%dir %_datadir/%name/
%_datadir/%name/translations/
%_desktopdir/scantailor-advanced.desktop
%_datadir/mime/packages/scantailor-project.xml
%_iconsdir/hicolor/scalable/apps/scantailor-advanced.svg

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1
- switch upstream to https://github.com/ScanTailor-Advanced/scantailor-advanced
- build with Qt6, use rpm-build-cmake
- install upstream scantailor-advanced binary and desktop file
- keep scantailor as a compatibility symlink to scantailor-advanced
- fix translations lookup after the binary rename
- enable unit tests in %%check
- fix unit tests comparing with zero (absolute tolerance, fails on aarch64 and i586)

* Tue Mar 18 2025 Vitaly Lipatov <lav@altlinux.ru> 1.0.19-alt1
- new version 1.0.19 (with rpmrb script)

* Thu Jul 07 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt1
- switch to https://github.com/vigri/scantailor-advanced upstream
- use Qt5 now
- obsolete scantailer-advanced package

* Thu Jul 15 2021 Andrey Cherepanov <cas@altlinux.org> 0.9.12.2-alt1.1
- FTBFS: build without phonon-devel

* Sun Dec 23 2018 Andrey Bergman <vkni@altlinux.org> 0.9.12.2-alt1
- Update to upstream version 0.9.12.2

* Sat Jan 23 2016 Andrey Bergman <vkni@altlinux.org> 0.9.11.1git-alt1
- Update to commit bd9ba..., Dec 5 2015, branch enhanced-working.

* Tue Sep 04 2012 Andrey Bergman <vkni@altlinux.org> 0.9.11.1-alt2
- Adjusted BuildRequires.

* Sat Mar 17 2012 Andrey Bergman <vkni@altlinux.org> 0.9.11.1-alt1
- update to version 0.9.11.1

* Sun Feb 05 2012 Andrey Bergman <vkni@altlinux.org> 0.9.11-alt1
- update to version 0.9.11

* Thu Aug 04 2011 Andrey Bergman <vkni@altlinux.org> 0.9.10-alt1
- update to version 0.9.10

* Wed Dec 08 2010 Andrey Bergman <vkni@altlinux.org> 0.9.9.2-alt2
- corrected desktop entry.

* Mon Oct 25 2010 Andrey Bergman <vkni@altlinux.org> 0.9.9.2-alt1
- update to version 0.9.9.2

* Mon Jul 12 2010 Andrey Bergman <vkni@altlinux.org> 0.9.9.1-alt2
- update to version 0.9.9.1

* Sat May 01 2010 Andrey Bergman <vkni@altlinux.org> 0.9.8.1-alt2
- added priority selection patch

* Mon Apr 26 2010 Andrey Bergman <vkni@altlinux.org> 0.9.8.1-alt1
- update to version 0.9.8.1

* Fri Apr 16 2010 Andrey Bergman <vkni@altlinux.org> 0.9.8-alt2
- added priority selection patch

* Sun Apr 04 2010 Andrey Bergman <vkni@altlinux.org> 0.9.8-alt1
- update to version 0.9.8

* Tue Dec 01 2009 Andrey Bergman <vkni@altlinux.org> 0.9.7.2-alt1
- update to a new version (bugfix and minor improvements)

* Sun Nov 15 2009 Andrey Bergman <vkni@altlinux.org> 0.9.7.1-alt1
- update to a new version (bugfix and minor improvements)

* Wed Nov 11 2009 Andrey Bergman <vkni@altlinux.org> 0.9.7-alt1.2
- Corrected desktop entry.

* Mon Nov 09 2009 Andrey Bergman <vkni@altlinux.org> 0.9.7-alt1.1
- Updated build requirements.

* Mon Nov 09 2009 Andrey Bergman <vkni@altlinux.org> 0.9.7-alt1
- update to a new version

* Sat Sep 05 2009 Andrey Bergman <vkni@altlinux.org> 0.9.6-alt1
- Added menu entry, icon and russian translation.

* Sun Aug 02 2009 Andrey Bergman <vkni@altlinux.org> 0.9.6-alt0.1
- update to a new version

* Thu May 21 2009 Andrey Bergman <vkni@altlinux.org> 0.9.5-alt0.4
- source update

* Mon May 04 2009 Andrey Bergman <vkni@altlinux.org> 0.9.5-alt0.1
- update to a new version (crash fix)

* Sun Apr 26 2009 Andrey Bergman <vkni@altlinux.org> 0.9.4-alt0.1
- new version

* Wed Feb 18 2009 Andrey Bergman <vkni@altlinux.org> 0.9.3-alt0.1
- update to a new version due to crash fix

* Tue Feb 17 2009 Andrey Bergman <vkni@altlinux.org> 0.9.2-alt0.1
- new version

* Sat Dec 20 2008 Andrey Bergman <vkni@altlinux.org> 0.9.1-alt0.2
- Update to version 0.9.1

* Thu Dec 11 2008 Andrey Bergman <vkni@altlinux.org> 0.9.0-alt0.1
- Initial release

