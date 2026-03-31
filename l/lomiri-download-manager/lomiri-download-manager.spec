%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: lomiri-download-manager
Version: 0.3.1
Release: alt1

Summary: Lomiri Upload/Download Manager
License: LGPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-download-manager

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: boost-devel
BuildRequires: boost-log-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: libglog-devel
BuildRequires: libgflags-devel
BuildRequires: libunwind-devel
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(libapparmor)
BuildRequires: pkgconfig(systemd)
BuildRequires: doxygen
BuildRequires: /usr/bin/dot

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /usr/bin/dbus-test-runner
BuildRequires: /usr/bin/xvfb-run
BuildRequires: ayatana-cmake-modules
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gmock)
%endif

Requires: unzip

%description
%summary

%package -n lib%{name}
Summary: Lomiri Upload/Download Manager - shared libraries (Qt5)
Group: System/Libraries

%description -n lib%{name}
Lomiri Upload/Download Manager performs uploads and downloads from a
centralized location.

This package includes the Qt5 shared libraries for %{name}.

%package -n %{name}-devel
Summary: QT 5 library for Lomiri Download Manager (development files)
Group: Development/Other
Requires: lib%{name} = %{version}-%{release}

%description -n %{name}-devel
Lomiri Upload/Download Manager performs uploads and downloads from a
centralized location.

This package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary: QT 5 library for Lomiri Download Manager - documentation files
Group: Documentation
BuildArch: noarch

%description doc
Lomiri Upload/Download Manager performs uploads and downloads from a
centralized location.

This package contains the documentation of the Lomiri DownloadManager.

%prep
%setup
%patch -p1

sed -i "s|add_dependencies(\${TARGET} GMock)|# add_dependencies(\${TARGET} GMock)|" tests/common/CMakeLists.txt

%build
%cmake \
       -W no-dev \
       -DENABLE_WERROR=OFF \
       -DENABLE_QT6=OFF \
%if_with check
       -DBUILD_TESTING=ON \
%else
       -DBUILD_TESTING=OFF \
%endif
       -DENABLE_DOC=ON \
       -DENABLE_UBUNTU_COMPAT=ON \
       -DCMAKE_INSTALL_LIBEXECDIR=%_libdir \
       -DQDOC_EXECUTABLE=%_qt5_bindir/qdoc
%cmake_build

%install
%cmake_install

%find_lang %name

%post
%systemd_user_post lomiri-download-manager-systemd.service
%systemd_user_post lomiri-upload-manager-systemd.service

%preun
%systemd_user_preun lomiri-download-manager-systemd.servi
%systemd_user_preun lomiri-upload-manager-systemd.service

%postun
%systemd_user_postun lomiri-download-manager-systemd.servi
%systemd_user_postun lomiri-upload-manager-systemd.service

%check
%ctest -j1 -V

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING HACKING NEWS
%_bindir/lomiri-download-manager
%_bindir/lomiri-upload-manager
%_man1dir/lomiri-download-manager.1.*
%_man1dir/lomiri-upload-manager.1.*
%_sysconfdir/dbus-1/system.d/com.lomiri.applications.Downloader.conf
%_sysconfdir/dbus-1/system.d/com.lomiri.applications.Uploader.conf
%_userunitdir/lomiri-download-manager-systemd.service
%_userunitdir/lomiri-upload-manager-systemd.service
%dir %_qt5_qmldir/Ubuntu/DownloadManager
%_qt5_qmldir/Ubuntu/DownloadManager/*
%dir %_qt5_qmldir/Lomiri/DownloadManager
%_qt5_qmldir/Lomiri/DownloadManager/*
%_datadir/dbus-1/services/lomiri-download-manager.service
%_datadir/dbus-1/services/lomiri-upload-manager.service
%_datadir/dbus-1/system-services/com.lomiri.applications.Downloader.service
%_datadir/dbus-1/system-services/com.lomiri.applications.Uploader.service
%dir %_libdir/%name
%_libdir/%name/ldm-extractor
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-download-manager.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-download-manager.mo

%files -n lib%{name}
%_libdir/lib%{name}-common.so.0*
%_libdir/liblomiri-upload-manager-common.so.0*
%_libdir/lib%{name}-client*.so.0*
%_libdir/libldm*.so.0*

%files -n %{name}-devel
%_libdir/libldm-common.so
%_libdir/libldm-priv-common.so
%_libdir/lib%{name}-client.so
%_libdir/lib%{name}-common.so
%_libdir/liblomiri-upload-manager-common.so
%_pkgconfigdir/ldm-common.pc
%_pkgconfigdir/lomiri-download-manager-client.pc
%_pkgconfigdir/lomiri-download-manager-common.pc
%_pkgconfigdir/lomiri-upload-manager-common.pc
%dir %_includedir/qt5/lomiri/download_manager
%_includedir/qt5/lomiri/download_manager/*
%dir %_includedir/qt5/lomiri/transfers
%_includedir/qt5/lomiri/transfers/*
%dir %_includedir/qt5/lomiri/upload_manager
%_includedir/qt5/lomiri/upload_manager/*

%files doc
%dir %_docdir/%name
%_docdir/%name/*

%changelog
* Tue Mar 31 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.1-alt1
- New version 0.3.1.

* Sun Feb 15 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt2
- Fixed FTBFS.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.2-alt1
- New version 0.2.2.

* Tue Jul 15 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus
