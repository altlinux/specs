%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define qtsys_intver 5.4.0

Name: qt5-qtsystems
Version: 5.4.0_git20230712.81e08ee
Release: alt1

Summary: Qt 5 Systems
License: GFDL-1.3 and GPL-2.0 and LGPL-3.0 and GPL-3.0
Group: System/Libraries
Url: https://github.com/qt/qtsystems

Source: %name-%version.tar

# sync with version 5.0~git20230712.81e08ee+dfsg-3 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(Qt5Qml)

%if_with check
BuildRequires: dbus
BuildRequires: /proc
BuildRequires: dbus-test-runner
%endif

%description
Qt is a cross-platform C++ application framework. Qt's primary feature
is its rich set of widgets that provide standard GUI functionality.

%package -n libqt5-qtsystems
Summary: Qt 5 Systems (shared libraries)
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description -n libqt5-qtsystems
Qt is a cross-platform C++ application framework. Qt's primary feature
is its rich set of widgets that provide standard GUI functionality.

This package contains shared libraries.

%package -n qt5-qtsystems-devel
Summary: Qt 5 Systems (development files)
Group: Development/KDE and QT
Requires: libqt5-qtsystems = %{version}-%{release}

%description -n qt5-qtsystems-devel
Qt is a cross-platform C++ application framework. Qt's primary feature
is its rich set of widgets that provide standard GUI functionality.

This package contains the header development files and examples used for
building Qt 5 applications using Qt Systems libraries.

%package -n qt5-qtsystems-private-devel
Summary: Qt 5 Systems (development files)
Group: Development/KDE and QT
Requires: libqt5-qtsystems = %{version}-%{release}

%description -n qt5-qtsystems-private-devel
Qt is a cross-platform C++ application framework. Qt's primary feature
is its rich set of widgets that provide standard GUI functionality.

This package contains the private header development files used for
building Qt 5 applications using Qt Systems libraries.

%prep
%setup
%patch -p1

syncqt.pl-qt5 -version %{version}
cd src/systeminfo/ && syncqt.pl-qt5 -copy -module QtSystemInfo -version %qtsys_intver -outdir ../../build -builddir ./ ./
cd ../
cd publishsubscribe/ && syncqt.pl-qt5 -copy -module QtPublishSubscribe -version %qtsys_intver -outdir ../../build -builddir ./ ./
cd ../
cd serviceframework/ && syncqt.pl-qt5 -copy -module QtServiceFramework -version %qtsys_intver -outdir ../../build -builddir ./ ./
cd ../../

%qmake_qt5 ./qtsystems.pro \
           PREFIX=%_prefix \
%if_with check
           CONFIG+="tests ofono upower udisks git_build" \
           QT_BUILD_PARTS+=tests
%else
           CONFIG+="ofono upower udisks git_build"
%endif

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%makeinstall_std INSTALL_ROOT=%{buildroot}

mv -v %{buildroot}%{_datadir}/qt5/bin/servicefw %{buildroot}%{_bindir}/
mv -v %{buildroot}%{_datadir}/qt5/bin/sfwlisten %{buildroot}%{_bindir}/

%check
%make -j1 check

%files
%doc LICENSE.FDL LICENSE.GPL2 LICENSE.GPL3 LICENSE.GPL3-EXCEPT LICENSE.LGPL3
%_bindir/servicefw
%_bindir/sfwlisten

%files -n libqt5-qtsystems
%_libdir/lib*.so.*
%_libdir/qt5/qml/*

%files -n qt5-qtsystems-devel
%doc examples/examples.pro
# prevent direct file conflict with qt5-base-doc package
%exclude %_qt5_examplesdir/examples.pro
%dir %_qt5_examplesdir/systeminfo
%_qt5_examplesdir/systeminfo/*

%exclude %_includedir/qt5/QtPublishSubscribe/%qtsys_intver
%dir %_includedir/qt5/QtPublishSubscribe
%_includedir/qt5/QtPublishSubscribe/*

%exclude %_includedir/qt5/QtServiceFramework/%qtsys_intver
%dir %_includedir/qt5/QtServiceFramework
%_includedir/qt5/QtServiceFramework/*

%exclude %_includedir/qt5/QtSystemInfo/%qtsys_intver
%dir %_includedir/qt5/QtSystemInfo
%_includedir/qt5/QtSystemInfo/*

%dir %_libdir/cmake/Qt5PublishSubscribe
%_libdir/cmake/Qt5PublishSubscribe/*
%dir %_libdir/cmake/Qt5ServiceFramework
%_libdir/cmake/Qt5ServiceFramework/*
%dir %_libdir/cmake/Qt5SystemInfo
%_libdir/cmake/Qt5SystemInfo/*
%_libdir/lib*.so
%_libdir/lib*.prl
%_libdir/pkgconfig/*
%_libdir/qt5/mkspecs/modules/qt_lib_publishsubscribe.pri
%_libdir/qt5/mkspecs/modules/qt_lib_serviceframework.pri
%_libdir/qt5/mkspecs/modules/qt_lib_systeminfo.pri

%files -n qt5-qtsystems-private-devel
%dir %_includedir/qt5/QtPublishSubscribe/%qtsys_intver
%_includedir/qt5/QtPublishSubscribe/%qtsys_intver/*

%dir %_includedir/qt5/QtServiceFramework/%qtsys_intver
%_includedir/qt5/QtServiceFramework/%qtsys_intver/*

%dir %_includedir/qt5/QtSystemInfo/%qtsys_intver
%_includedir/qt5/QtSystemInfo/%qtsys_intver/*

%_libdir/qt5/mkspecs/modules/*_private.pri

%changelog
* Sun Jul 13 2025 Nikolay Strelkov <snk@altlinux.org> 5.4.0_git20230712.81e08ee-alt1
- Initial build for Sisyphus
