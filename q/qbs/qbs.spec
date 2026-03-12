%define _untracked_files_terminate_build 1

%define _libexecdir %_usr/libexec

%define abiversion 3

%def_with check

Name:    qbs
Version: 3.1.2
Release: alt2

Summary: Modern build tool for software projects
License: LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) AND (LGPL-2.1-only OR LGPL-3.0-only WITH Qt-LGPL-exception-1.1) AND GPL-3.0-only WITH Qt-GPL-exception-1.0
Group:   Development/Tools 
Url:  	 https://qbs.io
Vcs:     https://github.com/qbs/qbs.git

Source: %name-%version.tar

BuildRequires(pre): cmake rpm-macros-qt6
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-tools-devel

BuildRequires: python3-module-lxml
BuildRequires: python3-module-beautifulsoup4

%if_with check
BuildRequires: ctest
%endif

Provides: %name-common = %EVR
Obsoletes: %name-common < %EVR

%description
Qbs is a tool that helps simplify the build process for developing projects
across multiple platforms. Qbs can be used for any software project, regardless
of programming language, toolkit, or libraries used.

Qbs is an all-in-one tool that generates a build graph from a high-level
project description (like qmake or CMake) and additionally undertakes the task
of executing the commands in the low-level build graph (like make).

%package devel
Summary: Development files for %name
Group: Development/Tools
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package examples
Summary: Example projects using %name
Requires: %name = %EVR
BuildArch: noarch
Group: Development/Tools

%description examples
The %name-examples package contains example files for using %name.

%prep
%setup

%build
export PATH="%{_qt6_bindir}:$PATH";
export QTDIR=%_qt6_prefix; 
	
%cmake \
    -GNinja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DINSTALL_ARCHDATADIR=%_qt6_archdatadir \
	-DINSTALL_BINDIR=%_qt6_bindir \
	-DINSTALL_DATADIR=%_qt6_datadir \
	-DINSTALL_DOCDIR=%_qt6_docdir \
	-DINSTALL_EXAMPLESDIR=%_qt6_examplesdir \
	-DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON \
	-DINSTALL_INCLUDEDIR=%_qt6_headerdir \
	-DINSTALL_QMLDIR=%_qt6_qmldir \
	-DINSTALL_LIBDIR=%_qt6_libdir \
	-DINSTALL_LIBEXECDIR=%_qt6_libexecdir \
	-DINSTALL_PLUGINSDIR=%_qt6_plugindir \
	-DINSTALL_SYSCONFDIR=%_qt6_sysconfdir \
	-DINSTALL_TRANSLATIONSDIR=%_qt6_translationdir \
	-DINSTALL_MKSPECSDIR=%_qt6_mkspecsdir \
	-DQT_DISABLE_RPATH:BOOL=TRUE \
  -DWITH_TESTS=OFF \
  -DQBS_LIB_INSTALL_DIR=%_libdir \
  -DQBS_PLUGINS_INSTALL_BASE=%_lib \
  -DWITH_UNIT_TESTS=ON \
  -DQBS_ENABLE_RPATH=OFF \
  -DQBS_INSTALL_QCH_DOCS=ON \
  -DQBS_DOC_INSTALL_DIR=%_qt6_docdir

%cmake_build

%install
%cmake_install
install -Dpm 0644 doc/man/%name.1 %buildroot%_man1dir/%name.1

#Remove python dmgbuild directory, macOS specific utilites.
rm -rfv %buildroot%_datadir/%name/python

%if_with check
%check
%ctest || :
%endif

%files
%doc *.md LICENSE.LGPLv21 LICENSE.LGPLv3 LICENSE.GPL3-EXCEPT LGPL_EXCEPTION.txt
%_bindir/%{name}*
%_libdir/%name
%_libdir/lib%{name}*.so.%{abiversion}*
%_datadir/%name
%_libexecdir/%name
%_man1dir/%name.1*
%exclude %_datadir/%name/examples

%files devel 
%_includedir/%name
%_libdir/lib%{name}*.so

%files examples
%_datadir/%name/examples

%changelog
* Wed Mar 11 2026 Nikita Shmatko <nash@altlinux.org> 3.1.2-alt2
- Added ABI versioning.
- Minor specfile fixes.

* Thu Dec 18 2025 Nikita Shmatko <nash@altlinux.org> 3.1.2-alt1
- New version 3.1.2.
- Removed obsolete i586 compatibility patch.

* Wed Sep 24 2025 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt2
- Fixed update from qbs-1.23.

* Mon Sep 01 2025 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version 3.0.1 (thanks nash@).

* Thu Jul 28 2022 Nazarov Denis <nenderus@altlinux.org> 1.23.0-alt1
- Version 1.23.0

* Wed Jan 12 2022 Nazarov Denis <nenderus@altlinux.org> 1.21.0-alt1
- Version 1.21.0

* Sun Nov 14 2021 Nazarov Denis <nenderus@altlinux.org> 1.20.1-alt2
- Add conflicts to qt-creator-core
- Separate shared library and common files

* Sat Nov 13 2021 Nazarov Denis <nenderus@altlinux.org> 1.20.1-alt1
- Version 1.20.1

* Tue Jun 18 2019 Andrey Cherepanov <cas@altlinux.org> 1.13.1-alt1
- New version.

* Tue Jul 12 2016 Nazarov Denis <nenderus@altlinux.org> 1.5.2-alt1
- Version 1.5.2

* Sat Jan 16 2016 Nazarov Denis <nenderus@altlinux.org> 1.4.4-alt1
- Version 1.4.4

* Mon Nov 09 2015 Nazarov Denis <nenderus@altlinux.org> 1.4.3-alt1
- Version 1.4.3

* Wed Jul 29 2015 Nazarov Denis <nenderus@altlinux.org> 1.4.1-alt1
- Version 1.4.1

* Tue Jun 23 2015 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Wed Oct 15 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.2-alt1
- Version 1.3.2

* Thu Sep 18 2014 Nazarov Denis <nenderus@altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Sun Jun 01 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt0.M70T.1
- Build for branch t7

* Fri May 30 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Thu May 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt0.M70T.1
- Build for branch t7

* Wed May 07 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Sun Feb 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.2-alt0.M70T.1
- Build for branch t7

* Fri Feb 14 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Thu Jan 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.1-alt1.M70T.1
- Build for branch t7

* Thu Jan 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.1-alt2
- Fix arch for examples subpackage

* Thu Jan 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.1.1-alt1
- Initial release for ALT Linux
