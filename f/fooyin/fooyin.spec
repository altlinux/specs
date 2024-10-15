%define _unpackaged_files_terminate_build 1

Name: fooyin
Version: 0.8.0
Release: alt1

Summary: Music player built around customisation
License: GPL-3.0
Group: Sound
Url: https://github.com/ludouzi/fooyin

Source: %name-%version.tar
Patch: %name-%version-alt-change-libdir.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-svg-devel
BuildRequires: libtag-devel
BuildRequires: libalsa-devel
BuildRequires: libsndfile-devel
BuildRequires: libavcodec-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libavdevice-devel
BuildRequires: libavfilter-devel
BuildRequires: libswscale-devel
BuildRequires: libswresample-devel
BuildRequires: libpostproc-devel
BuildRequires: libkdsingleapplication-qt6-devel

%description
Fooyin is a music player built around customisation. It offers a growing list of
widgets to manage and play your local music collection. It's extendable through
the use of plugins and many widgets make use of FooScript to offer an even
deeper level of control.

%prep
%setup
%autopatch -p1

%build
%cmake \
-DBUILD_LIBVGM=OFF
%cmake_build

%install
%cmake_install
%find_lang %name --with-qt

# Remove development libraries
rm -fv %buildroot%_libdir/libfooyin*.so

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

%changelog
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
