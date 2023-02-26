%define _unpackaged_files_terminate_build 1

%def_with ClangCodeModel
%define llvm_version 13.0
%define qt_version 6.2.0

%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%add_findreq_skiplist  %_datadir/qtcreator/*
%add_findprov_skiplist %_datadir/qtcreator/*

Name:    qt-creator
Version: 9.0.2
Release: alt1

Summary: Cross-platform IDE for Qt
License: GPL-3.0 with Qt-GPL-exception-1.0 and MIT and LGPL-2.0 and LGPL-2.1 and LGPL-3.0 and BSD-3-Clause and BSL-1.0 and ALT-Public-Domain
Group:   Development/Tools

URL: http://qt-project.org/wiki/Category:Tools::QtCreator
VCS: git://code.qt.io/qt-creator/qt-creator.git
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: submodules.tar

Patch0: %name-%version-%release.patch

Provides: qtcreator = %EVR
Obsoletes: qtcreator-clangcodemodel
Provides: qtcreator-clangcodemodel = %EVR

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): qt6-base-devel >= %qt_version
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: gcc-c++
BuildRequires: qt6-designer >= %qt_version
BuildRequires: qt6-declarative-devel >= %qt_version
BuildRequires: qt6-tools-devel >= %qt_version
BuildRequires: qt6-serialport-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel >= %qt_version
%endif
BuildRequires: qt6-svg-devel >= %qt_version
BuildRequires: qt6-5compat-devel >= %qt_version
BuildRequires: qt6-shadertools-devel >= %qt_version
BuildRequires: qt6-quicktimeline-devel >= %qt_version
BuildRequires: kf5-syntax-highlighting-devel
%if_with ClangCodeModel
BuildRequires: clang%llvm_version
BuildRequires: clang%llvm_version-devel
BuildRequires: clang%llvm_version-tools
BuildRequires: clangd%llvm_version
BuildRequires: lld%llvm_version
BuildRequires: llvm%llvm_version-devel
BuildRequires: llvm%llvm_version-tools
%endif
BuildRequires: libsystemd-devel
BuildRequires: elfutils-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel
BuildRequires: libxml2-devel
# Qbs documentation
#BuildRequires: python3-module-lxml
#BuildRequires: python3-module-bs4
# Missing build requirements
#BuildRequires: litehtml-devel

Requires: %name-core = %EVR
# Add Qt5 build environment to build Qt project
Requires: qt6-base-devel
Requires: qt6-tools

%ifarch %e2k
# error: cpio archive too big - 4446M
%global __find_debuginfo_files %nil
%endif

%add_python3_req_skip dmgbuild

%description
Qt Creator (previously known as Project Greenhouse) is a new, lightweight,
cross-platform integrated  development environment (IDE) designed to make
development with the Qt application framework even faster and easier.

This package contains IDE and Qt5 build environment.

%package core
Summary: Cross-platform IDE for Qt
Group:   Development/Tools
Requires: %name-data = %EVR
Provides: qbs = 1.14.0
Obsoletes: qbs < 1.14.0
Requires: qt6-translations

%description core
Qt Creator (previously known as Project Greenhouse) is a new, lightweight,
cross-platform integrated  development environment (IDE) designed to make
development with the Qt application framework even faster and easier.

This is core part of IDE without Qt5 build environment.

%package doc
Summary: %name docs
Group: Documentation
%if_enabled qtwebengine
Requires: %name
%endif
Requires: qt6-base-doc
Requires: qt6-tools

%description doc
Documentation for %name

%package data
Summary: Data files for %name
Group: Development/Tools
%if_enabled qtwebengine
Requires: %name-core
%endif

%description data
Data files for %name

%prep
%setup
# Unpack submodules content
tar xf %SOURCE1
#sed -i 's,tools\/qdoc3,bin,' doc/doc.pri
#subst 's,share\/doc\/qtcreator,share\/qtcreator\/doc,' doc/doc.pri src/plugins/help/helpplugin.cpp
%patch0 -p1
%ifarch %e2k
# strip UTF-8 BOM, lcc 1.23 won't ignore it yet
find src -type f -print0 -name '*.cpp' -o -name '*.h' |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif
# Use Python3 for Python scripts
subst 's@#!.*python[23]\?@#!%__python3@' `find . -name \*.py` \
	src/shared/qbs/src/3rdparty/python/bin/dmgbuild \
	src/libs/qt-breakpad/qtbreakpadsymbols

%build
%global optflags_lto %optflags_lto -ffat-lto-objects
export QTDIR=%_qt6_prefix
export PATH="%{_qt6_bindir}:$PATH"
export ALTWRAP_LLVM_VERSION="%llvm_version"
%ifarch %e2k
# fool sqlite into building with lcc
sed -i 's,^QMAKE_CFLAGS_WARN_ON.*$,& -D__INTEL_COMPILER,' src/libs/3rdparty/sqlite/sqlite.pri
%endif
%if_with ClangCodeModel
export LLVM_INSTALL_DIR="%_prefix"
%remove_optflags -frecord-gcc-switches
%endif

%cmake -GNinja \
    -Wno-dev \
    -DWITH_DOCS=ON \
    -DBUILD_QBS=ON \
    -Djournald=ON \
    -DBUILD_DEVELOPER_DOCS=OFF \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS -Wl,-rpath,%_libdir/qtcreator -Wl,-rpath,%_libdir/qtcreator/plugins" \
    -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS -Wl,-rpath,%_libdir/qtcreator -Wl,-rpath,%_libdir/qtcreator/plugins"

%ninja_build -C "%_cmake__builddir"
%ninja_build -C "%_cmake__builddir" qch_docs

%install
%ninja_install -C "%_cmake__builddir"
# Unable to install documentstion using ninja-build
#%%ninja_install -C "%_cmake__builddir" qch_docs
install -Dpm0644 %_cmake__builddir/share/doc/qtcreator/qtcreator.qch %buildroot%_defaultdocdir/qtcreator/qtcreator.qch

# Remove Windows cdb debugger support to prevent unmet python2.7(cdbext)
rm -f %buildroot%_datadir/qtcreator/debugger/cdbbridge.py

%files

%files core
%doc README* LICENSE*
%_bindir/*
%_libdir/qtcreator
%_prefix/libexec/qtcreator
%_iconsdir/hicolor/*/apps/QtProject-qtcreator.png
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml

%files doc
%_defaultdocdir/qtcreator

%files data
%dir %_datadir/qtcreator
%_datadir/qtcreator/*

%changelog
* Sat Feb 25 2023 Andrey Cherepanov <cas@altlinux.org> 9.0.2-alt1
- New version.

* Mon Dec 26 2022 Andrey Cherepanov <cas@altlinux.org> 9.0.1-alt1
- New version.

* Mon Nov 28 2022 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- New version.

* Thu Nov 24 2022 Sergey V Turchin <zerg@altlinux.org> 8.0.2-alt2
- allow to build without QtWebEngine

* Sat Oct 29 2022 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt1
- New version.
- Used LLVM 13.0.

* Mon Aug 15 2022 Andrey Cherepanov <cas@altlinux.org> 8.0.1-alt1
- New version.

* Mon Jul 25 2022 Andrey Cherepanov <cas@altlinux.org> 8.0.0-alt1
- New version.

* Thu Jun 09 2022 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt2
- Correctly include KSyntaxHighlighting headers (patch from OpenSUSE) (ALT #42956).

* Wed May 25 2022 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt1
- New version.

* Thu Apr 28 2022 Andrey Cherepanov <cas@altlinux.org> 7.0.1-alt1
- New version.

* Fri Mar 25 2022 Andrey Cherepanov <cas@altlinux.org> 7.0.0-alt1
- New version.

* Fri Feb 18 2022 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt3
- using not_qt5_qtwebengine_arches macro

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 6.0.2-alt2
- fix requires

* Tue Feb 01 2022 Andrey Cherepanov <cas@altlinux.org> 6.0.2-alt1
- New version.

* Mon Jan 31 2022 Sergey V Turchin <zerg@altlinux.org> 6.0.1-alt2
- build according qtwebengine arches

* Tue Dec 21 2021 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- New version.

* Mon Dec 06 2021 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version.

* Fri Nov 05 2021 Andrey Cherepanov <cas@altlinux.org> 5.0.3-alt1
- New version.

* Sun Oct 03 2021 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1
- New version.

* Thu Sep 16 2021 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version.

* Mon Aug 30 2021 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt2
- Set ALTWRAP_LLVM_VERSION to select correct LLVM version.

* Fri Aug 27 2021 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version (ALT #40822).
- Build using ninja-build.

* Wed Jul 14 2021 Andrey Cherepanov <cas@altlinux.org> 4.15.2-alt1
- New version.

* Tue Jun 15 2021 Andrey Cherepanov <cas@altlinux.org> 4.15.1-alt2
- Package core part separately as qt-creator-core (ALT #40219).

* Thu Jun 10 2021 Andrey Cherepanov <cas@altlinux.org> 4.15.1-alt1
- New version.
- Build by LLVM 12.0.

* Thu May 06 2021 Andrey Cherepanov <cas@altlinux.org> 4.15.0-alt1
- New version.

* Mon Mar 22 2021 Andrey Cherepanov <cas@altlinux.org> 4.14.2-alt1
- New version.

* Thu Feb 25 2021 Andrey Cherepanov <cas@altlinux.org> 4.14.1-alt1
- New version.

* Mon Dec 21 2020 Andrey Cherepanov <cas@altlinux.org> 4.14.0-alt1
- New version.
- Add qt5-base-doc to qt-creator-doc requirements.

* Fri Nov 20 2020 Andrey Cherepanov <cas@altlinux.org> 4.13.3-alt1
- New version.

* Sun Oct 04 2020 Andrey Cherepanov <cas@altlinux.org> 4.13.2-alt1
- New version.

* Thu Sep 17 2020 Andrey Cherepanov <cas@altlinux.org> 4.13.1-alt1
- New version.

* Mon Sep 14 2020 Andrey Cherepanov <cas@altlinux.org> 4.13.0-alt3
- Update Russian translations from upstream.

* Tue Sep 08 2020 Andrey Cherepanov <cas@altlinux.org> 4.13.0-alt2
- Add changelog entry from p9 branch.

* Thu Sep 03 2020 Andrey Cherepanov <cas@altlinux.org> 4.13.0-alt1
- New version.
- Enable journald support.

* Thu Jul 09 2020 Andrey Cherepanov <cas@altlinux.org> 4.12.4-alt0.1.p9
- Backport new version to p9 branch.

* Thu Jul 09 2020 Andrey Cherepanov <cas@altlinux.org> 4.12.4-alt1
- New version.

* Thu Jun 18 2020 Andrey Cherepanov <cas@altlinux.org> 4.12.3-alt1
- New version.

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 4.12.2-alt1
- New version.

* Thu May 28 2020 Andrey Cherepanov <cas@altlinux.org> 4.12.1-alt2
- Build with LLVM 10.0.

* Wed May 20 2020 Andrey Cherepanov <cas@altlinux.org> 4.12.1-alt1
- New version.

* Tue Apr 28 2020 Andrey Cherepanov <cas@altlinux.org> 4.12.0-alt1
- New stable version.

* Mon Apr 13 2020 Andrey Cherepanov <cas@altlinux.org> 4.12.0-alt0.1.rc1
- New version (RC1).

* Sat Apr 04 2020 Andrey Cherepanov <cas@altlinux.org> 4.11.2-alt1
- New version.
- Build with ClangCodeModel plugin.

* Wed Feb 12 2020 Andrey Cherepanov <cas@altlinux.org> 4.11.1-alt2
- Add Russian localization to desktop file (ALT #36851).

* Fri Feb 07 2020 Andrey Cherepanov <cas@altlinux.org> 4.11.1-alt1
- New version.

* Mon Dec 16 2019 Andrey Cherepanov <cas@altlinux.org> 4.11.0-alt1
- New version.
- Build without ClangCodeModel due to the lack of LLVM 8.x in repository.
- Fix license.
- Set python3 as interpreter of Python scripts.

* Fri Nov 08 2019 Andrey Cherepanov <cas@altlinux.org> 4.9.2-alt4
- Add to requirements qt5-tran slations and qt5-tools.

* Fri Nov 01 2019 Andrey Cherepanov <cas@altlinux.org> 4.9.2-alt3
- Add Qt5 build environment to build Qt project (ALT #37403).

* Wed Oct 02 2019 Michael Shigorin <mike@altlinux.org> 4.9.2-alt2
- E2K:
  + fix build with dummy-qt5-webkit-devel dropped
  + fix BOM oneliner according to Secure Packaging Policy
- Added explicit BR: qt5-declarative-devel.
- Minor spec cleanup.

* Mon Jul 01 2019 Andrey Cherepanov <cas@altlinux.org> 4.9.2-alt1
- New version.

* Tue Jun 18 2019 Andrey Cherepanov <cas@altlinux.org> 4.9.1-alt2
- Build qbsprojectmanager plugin with bundled qbs (ALT #36917).
- Use ALT-specific Qt5 utilities names.
- Build perfparser from submodule.

* Thu May 30 2019 Andrey Cherepanov <cas@altlinux.org> 4.9.1-alt1
- New version.

* Sun May 05 2019 Michael Shigorin <mike@altlinux.org> 4.9.0-alt2.1
- E2K: fix build (and disable overly large debuginfo subpackage)

* Mon Apr 22 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.9.0-alt2
- Updated build dependencies: libbotan is no longer required.

* Tue Apr 16 2019 Andrey Cherepanov <cas@altlinux.org> 4.9.0-alt1
- New version (ALT #36600).

* Wed Mar 06 2019 Andrey Cherepanov <cas@altlinux.org> 4.8.2-alt1
- New version.

* Thu Jan 17 2019 Andrey Cherepanov <cas@altlinux.org> 4.8.1-alt1
- New version.

* Fri Dec 07 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt1
- New version.

* Wed Oct 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.7.2-alt1
- New version.

* Fri Sep 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.1-alt1
- Updated to upstream version 4.7.1.
- Updated runtime dependencies.

* Tue Sep 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.0-alt1
- Updated to upstream version 4.7.0.
- Applied patch from upstream for supporting libbotan-2.
- Removed clangcodemodel subpackage.
- Spec cleanup.

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt1
- New version.

* Thu May 03 2018 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt1
- New version.

* Tue Apr 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.0-alt1
- Updated to upstream version 4.6.0.
- Added debuginfo (Closes: #34153).
- Enabled parallel build.

* Sat Oct 14 2017 Andrey Cherepanov <cas@altlinux.org> 4.4.1-alt2
- Package ClangCodeModel (ALT #33943)

* Fri Oct 06 2017 Andrey Cherepanov <cas@altlinux.org> 4.4.1-alt1
- New version
- Add optional build ClangCodeModel plugin (disabled by default)

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 4.4.0-alt1
- New version

* Sat Jul 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version

* Thu May 25 2017 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version

* Sun Apr 23 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- New version

* Tue Jan 24 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.1-alt1
- new version 4.2.1

* Sat Dec 17 2016 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- new version 4.2.0
- provides qtcreator
- remove Windows cdb debugger support to prevent unmet python2.7(cdbext)

* Fri Aug 26 2016 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- new version 4.1.0

* Sun Jun 19 2016 Andrey Cherepanov <cas@altlinux.org> 4.0.2-alt1
- new version 4.0.2

* Fri Jun 10 2016 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- new version 4.0.1

* Fri May 13 2016 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version

* Tue Mar 29 2016 Sergey V Turchin <zerg@altlinux.org> 3.6.0-alt1.1
- NMU: Rebuild with new Qt5

* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version
- Build with Qt5 (closes #31175)

* Fri Feb 07 2014 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.1-alt1
- update to newest version with multiple improvements

* Sun Feb 02 2014 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.1-alt1
- update to new version (closes #29569)

* Thu Apr 11 2013 Anatoly Lyutin <vostok@altlinux.org> 2.7.0-alt1
- new version (closes #28740)

* Tue Dec 18 2012 Anatoly Lyutin <vostok@altlinux.org> 2.6.0-alt2
- true 2.6.0 (closes #28152)

* Mon Nov 26 2012 Anatoly Lyutin <vostok@altlinux.org> 2.6.0-alt1
- new version (closes #27938)

* Fri May 11 2012 Anatoly Lyutin <vostok@altlinux.org> 2.5.0-alt1
- new version

* Mon Jan 09 2012 Anatoly Lyutin <vostok@altlinux.org> 2.4.0-alt1
- new version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.0-alt1.1
- Rebuild with Python-2.7

* Thu Sep 22 2011 Anatoly Lyutin <vostok@altlinux.org> 2.3.0-alt1
- new version (closes #26219)

* Fri Aug 05 2011 Anatoly Lyutin <vostok@altlinux.org> 2.2.1-alt1
- new version

* Mon Jun 06 2011 Anatoly Lyutin <vostok@altlinux.org> 2.2.0-alt1
- update to 2.2.0

* Fri Mar 04 2011 Anatoly Lyutin <vostok@altlinux.org> 2.1.0-alt1
- update to 2.1.0

* Wed Jul 28 2010 Anatoly Lyutin <vostok@altlinux.org> 2.0.0-alt1
- update to 2.0.0

* Mon Mar 01 2010 Boris Savelev <boris@altlinux.org> 1.3.1-alt1
- new version

* Tue Dec 15 2009 Boris Savelev <boris@altlinux.org> 1.3.0-alt1
- new version (closes: #22547)

* Sun Aug 30 2009 Boris Savelev <boris@altlinux.org> 1.2.1-alt3.g26a3a3e
- build from upstream git

* Wed Aug 05 2009 Boris Savelev <boris@altlinux.org> 1.2.1-alt2.g0dbe82f
- new version

* Thu Jul 16 2009 Boris Savelev <boris@altlinux.org> 1.2.1-alt1.gba2a5a6
- new version

* Tue Jun 30 2009 Boris Savelev <boris@altlinux.org> 1.2.0-alt2.g6315f14
- build from upstream git
- add translations (closes:#20605)

* Fri Jun 26 2009 Boris Savelev <boris@altlinux.org> 1.2.0-alt1.g934ee44
- version up

* Mon May 25 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt6.gcf7cd73
- add %_bindir/qtcreator_process_stub (fix #20171)

* Mon May 11 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt5.gcf7cd73
- build from upstream git

* Sun May 03 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt4.ga1dc8f5
- build from upstream git

* Tue Apr 28 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt3.git.124.g092d8ca
- build from upstream git

* Tue Apr 28 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt2
- build doc (fix #19799)

* Thu Apr 23 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt1
- initial build for Sisyphus from Fedora
