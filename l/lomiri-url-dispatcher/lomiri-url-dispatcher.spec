%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define _libexecdir %_prefix/libexec

Name: lomiri-url-dispatcher
Version: 0.1.5
Release: alt1

Summary: Lomiri Operating Environment service for requesting URLs to be opened
License: LGPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-url-dispatcher

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ayatana-cmake-modules
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(dbustest-1)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libapparmor)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gtest)

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /usr/bin/dbus-test-runner
BuildRequires: /usr/bin/xvfb-run
BuildRequires: pkgconfig(dbustest-1)
BuildRequires: python3(dbusmock)
BuildRequires: python3(testtools)
%endif

Requires: qt5-declarative-devel

# qt5/qml/Lomiri/Components/ListItems/qmldir, qt5/qml/Lomiri/Components/Pickers/qmldir, qt5/qml/Lomiri/Components/Popups/qmldir, qt5/qml/Lomiri/Components/Styles/qmldir, qt5/qml/Lomiri/Components/qmldir, qt5/qml/Lomiri/Components/Labs/qmldir
Requires: lomiri-ui-toolkit

%description
Allows applications to request a URL to be opened and handled by another
process without seeing the list of other applications on the system or
starting them inside its own Application Confinement.

%package -n lib%{name}
Summary: Library for sending requests to the Lomiri URL Dispatcher
Group: System/Libraries

%description -n lib%{name}
Allows applications to request a URL to be opened and handled by another
process without seeing the list of other applications on the system or
starting them inside its own Application Confinement.

This package contains shared libraries to be used by applications.

%package -n %{name}-devel
Summary: Development files for consumers of the Lomiri URL Dispatcher
Group: Development/Other
Requires: lib%{name} = %{version}-%{release}

%description -n %{name}-devel
Allows applications to request a URL to be opened and handled by another
process without seeing the list of other applications on the system or
starting them inside its own Application Confinement.

This package contains files that are needed to build applications.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCMAKE_BUILD_TYPE=debug \
       -Denable_mirclient=OFF
%cmake_build

%install
%cmake_install

rm -rfv %buildroot%python3_sitelibdir_noarch/lomiri_url_dispatcher_testability || true
rm -rfv %buildroot/lomiri_url_dispatcher_testability || true

%find_lang %name

%post
%systemd_user_post lomiri-url-dispatcher-update-system-dir.service
%systemd_user_post lomiri-url-dispatcher-update-user-dir.service
%systemd_user_post lomiri-url-dispatcher.service

%preun
%systemd_user_preun lomiri-url-dispatcher-update-system-dir.service
%systemd_user_preun lomiri-url-dispatcher-update-user-dir.service
%systemd_user_preun lomiri-url-dispatcher.service

%postun
%systemd_user_postun lomiri-url-dispatcher-update-system-dir.service
%systemd_user_postun lomiri-url-dispatcher-update-user-dir.service
%systemd_user_postun lomiri-url-dispatcher.service

%check
export URL_DISPATCHER_DISABLE_RECOVERABLE_ERROR=1
export G_MESSAGES_DEBUG=all
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING MERGE-REVIEW NEWS README.md
%_bindir/lomiri-url-*
%dir %_libexecdir/lomiri-app-launch/bad-url
%_libexecdir/lomiri-app-launch/bad-url/exec-tool
%dir %_libexecdir/lomiri-app-launch/url-overlay
%_libexecdir/lomiri-app-launch/url-overlay/exec-tool
%dir %_libexecdir/lomiri-url-dispatcher
%_libexecdir/lomiri-url-dispatcher/lomiri-*
%_desktopdir/lomiri-url-dispatcher-gui.desktop
%_datadir/dbus-1/services/*.service
%dir %_datadir/lomiri-url-dispatcher
%_datadir/lomiri-url-dispatcher/*.qml
%dir %_datadir/lomiri-url-dispatcher/gui
%_datadir/lomiri-url-dispatcher/gui/*.qml
%_datadir/lomiri-url-dispatcher/gui/*.svg
%_userunitdir/*.path
%_userunitdir/lomiri-url-dispatcher-update-system-dir.service
%_userunitdir/lomiri-url-dispatcher-update-user-dir.service
%_userunitdir/lomiri-url-dispatcher.service

%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-url-dispatcher.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-url-dispatcher.mo

%files -n lib%{name}
%_libdir/lib%{name}.so.0*

%files -n %{name}-devel
%_libdir/liblomiri-url-dispatcher.so
%_libdir/pkgconfig/*.pc
%dir %_includedir/liblomiri-url-dispatcher
%_includedir/liblomiri-url-dispatcher/*.h
%_datadir/dbus-1/interfaces/*.xml

%changelog
* Wed Jul 01 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.5-alt1
- New version 0.1.5.

* Tue Jul 15 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus
