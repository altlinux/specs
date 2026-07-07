%define _unpackaged_files_terminate_build 1

Name: fooyin
Version: 0.11.1
Release: alt1

Summary: Music player built around customisation
License: GPL-3.0
Group: Sound
Url: https://www.fooyin.org/
Vcs: https://github.com/fooyin/fooyin.git

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Patch: %name-%version-alt-change-libdir.patch

Requires: icon-theme-hicolor

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-sql-interbase
BuildRequires: qt6-sql-mysql
BuildRequires: qt6-sql-postgresql
BuildRequires: qt6-sql-odbc
#
BuildRequires: libpostproc-devel
BuildRequires: qcoro6-devel
BuildRequires: /proc
#
BuildRequires: taglib-devel
BuildRequires: libalsa-devel
BuildRequires: libsndfile-devel
BuildRequires: libavcodec-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libavdevice-devel
BuildRequires: libavfilter-devel
BuildRequires: libswscale-devel
BuildRequires: libswresample-devel
BuildRequires: libkdsingleapplication-qt6-devel
#
BuildRequires: libgtest-devel
BuildRequires: ctest

%description
Fooyin is a music player built around customisation. It offers a growing list of
widgets to manage and play your local music collection. It's extendable through
the use of plugins and many widgets make use of FooScript to offer an even
deeper level of control.

%package devel
Summary: Support for developing fooyin plugins
Group: Development/C++
Requires: %name = %EVR

%description devel
This package provides development files used to create plugins for fooyin.

%prep
%setup
%autopatch -p1

%build
%ifarch %ix86
 %add_optflags -msse2
%endif
%cmake \
-DBUILD_LIBVGM=OFF \
-DBUILD_TESTING=ON \
-DINSTALL_HEADERS=ON
%cmake_build

%install
%cmake_install
%find_lang %name --with-qt
echo '%%lang(zh) %_datadir/%name/translations/fooyin_zh_Hant.qm' >> %name.lang

%check
%ctest --test-dir %_target_platform/tests/

%files -f %name.lang
%dir %_docdir/%name
%doc %_docdir/%name/*
%_bindir/%name
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_datadir/applications/*.desktop
%_datadir/metainfo/*.xml
%_datadir/icons/hicolor/*/apps/org.fooyin.fooyin.*
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/fyplugin_*.so
%_libdir/libfooyin_*.so.*

%files devel
%_includedir/%name/
%_libdir/libfooyin_*.so
%_libdir/cmake/%name/

%changelog
* Tue Jul 07 2026 Anton Kurachenko <srebrov@altlinux.org> 0.11.1-alt1
- New version 0.11.1.
- Added tests and devel package.
- Dropped i586 build.

* Sun May 10 2026 Anton Kurachenko <srebrov@altlinux.org> 0.10.5-alt1
- New version 0.10.5.

* Fri Mar 13 2026 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt4
- NMU: fix build requires

* Mon Mar 09 2026 Andrew A. Vasilyev <andy@altlinux.org> 0.9.2-alt3
- NMU: fix FTBFS
- update to upstream/master

* Sat Dec 27 2025 Anton Kurachenko <srebrov@altlinux.org> 0.9.2-alt2
- Fixed FTBFS with ffmpeg-8.

* Tue Sep 23 2025 Anton Kurachenko <srebrov@altlinux.org> 0.9.2-alt1
- New version 0.9.2.

* Sat Aug 23 2025 Anton Kurachenko <srebrov@altlinux.org> 0.9.1-alt1
- New version 0.9.1.

* Sun Aug 17 2025 Anton Kurachenko <srebrov@altlinux.org> 0.9.0-alt1
- New version 0.9.0.

* Wed Jun 11 2025 Anton Kurachenko <srebrov@altlinux.org> 0.8.1-alt3
- Fixed FTBFS with Qt-6.9.

* Sat Nov 23 2024 Anton Kurachenko <srebrov@altlinux.org> 0.8.1-alt2
- Updated Url and Vcs links.

* Wed Oct 30 2024 Anton Kurachenko <srebrov@altlinux.org> 0.8.1-alt1
- New version 0.8.1.

* Tue Oct 15 2024 Anton Kurachenko <srebrov@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Fri Oct 04 2024 Anton Kurachenko <srebrov@altlinux.org> 0.7.3-alt1
- New version 0.7.3.

* Fri Sep 27 2024 Anton Kurachenko <srebrov@altlinux.org> 0.7.2-alt1
- New version 0.7.2.

* Sun Sep 22 2024 Anton Kurachenko <srebrov@altlinux.org> 0.7.1-alt1
- New version 0.7.1.

* Mon Sep 02 2024 Anton Kurachenko <srebrov@altlinux.org> 0.6.2-alt1
- New version 0.6.2.

* Tue Jul 09 2024 Anton Kurachenko <srebrov@altlinux.org> 0.5.3-alt1
- New version 0.5.3.

* Sat Jun 29 2024 Anton Kurachenko <srebrov@altlinux.org> 0.5.0-alt1
- New version 0.5.0.

* Mon Jun 17 2024 Anton Kurachenko <srebrov@altlinux.org> 0.4.5-alt1
- New version 0.4.5.

* Tue Jun 04 2024 Anton Kurachenko <srebrov@altlinux.org> 0.4.4-alt1
- New version 0.4.4.

* Mon May 27 2024 Anton Kurachenko <srebrov@altlinux.org> 0.4.2-alt1
- Initial build for ALT.
