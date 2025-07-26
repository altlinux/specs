%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define qtpim_intver 5.4.0

Name: qt5-pim
Version: 5.15
Release: alt1

Summary: Qt 5 PIM module
License: LGPL-2.1 and GFDL-1.3 and GPL-3.0
Group: Graphical desktop/KDE
Url: https://invent.kde.org/qt/qt/qtpim

Source: %name-%version.tar

# sync with 5.0~git20201102.f9a8f0fc+dfsg1 + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-qt5

BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)

%if_with check
BuildRequires: /proc
BuildRequires: /usr/bin/xauth
BuildRequires: /usr/bin/xvfb-run
%endif

%description
Qt is a cross-platform C++ application framework. Qt's primary feature
is its rich set of widgets that provide standard GUI functionality.

This package contains Qt 5 PIM module.

%package -n libqt5-pim
Summary: Qt 5 PIM module (shared libraries)
Group: System/Libraries

%description -n libqt5-pim
Qt is a cross-platform C++ application framework. Qt's primary feature
is its rich set of widgets that provide standard GUI functionality.

This package contains shared libraries for Qt 5 PIM module.

%package -n libqt5-pim-devel
Summary: Qt 5 PIM module (development files)
Group: Development/KDE and QT
Requires: libqt5-pim = %{version}-%{release}

%description -n libqt5-pim-devel
Qt is a cross-platform C++ application framework. Qt's primary feature
is its rich set of widgets that provide standard GUI functionality.

This package contains the header development files and examples used for
building Qt 5 applications using Qt 5 PIM module.

%package -n libqt5-pim-doc
Summary: Qt 5 PIM module (development files)
Group: Documentation
BuildArch: noarch

%description -n libqt5-pim-doc
Qt is a cross-platform C++ application framework. Qt's primary feature
is its rich set of widgets that provide standard GUI functionality.

This package contains the documentation for building Qt 5 applications
using Qt 5 PIM module.

%prep
%setup
%patch -p1
sed -i "s/^MODULE_VERSION.*/MODULE_VERSION = 5.0.0/g" .qmake.conf

%build
# Build headers manually
cd src/contacts/ && syncqt.pl-qt5 -copy -module QtContacts -version %{qtpim_intver} -outdir ../../build -builddir ./ ./
cd ../
cd organizer/ && syncqt.pl-qt5 -copy -module QtOrganizer -version %{qtpim_intver} -outdir ../../build -builddir ./ ./
cd ../
cd versit/ && syncqt.pl-qt5 -copy -module QtVersit -version %{qtpim_intver} -outdir ../../build -builddir ./ ./
cd ../
cd versitorganizer/ && syncqt.pl-qt5 -copy -module QtVersitOrganizer -version %{qtpim_intver} -outdir ../../build -builddir ./ ./
cd ../../

# For building
cd ./build/include/QtContacts
ln -s %{qtpim_intver}/QtContacts/private
cd ../QtOrganizer
ln -s %{qtpim_intver}/QtOrganizer/private
cd ../QtVersit
ln -s %{qtpim_intver}/QtVersit/private
cd ../QtVersitOrganizer
ln -s %{qtpim_intver}/QtVersitOrganizer/private
cd ../../../

cd ./build
%qmake_qt5 \
          ../qtpim.pro \
          CONFIG+=nostrip \
%if_with check
          QT_BUILD_PARTS+=tests \
%endif
          QMAKE_CXXFLAGS="%optflags"

%make_build
%make_build docs

sed -i "s/Qt5 = 5/Qt5/g" lib/pkgconfig/*.pc

%install
%makeinstall_std -C build INSTALL_ROOT=%buildroot
%makeinstall_std -C build INSTALL_ROOT=%buildroot install_docs

# copying all missed includes manually
cp -arv ./build/include/* %buildroot/%_includedir/qt5/

# fix strange 5.0.0 = 5.0.0 in cmake files
sed -i "s/5.0.0 = 5.0.0/5.0.0/g" %buildroot%_libdir/cmake/Qt5Contacts/Qt5ContactsConfig.cmake

# do not install the skeleton plugin
find %buildroot -name Qt5Organizer_QSkeletonOrganizerPlugin.cmake -delete -print

%check
xvfb-run -a %make -C build -j1 check -- LC_ALL=en_US.UTF-8  QML2_IMPORT_PATH=%buildroot%_qt5_qmldir QT_PLUGIN_PATH=%buildroot%_qt5_plugindir

%files -n libqt5-pim
%doc header.LGPL21 LICENSE.GPL2 LICENSE.GPL3 LICENSE.GPL3-EXCEPT
%_libdir/lib*.so.*
%_libdir/qt5/qml/*
%dir %_libdir/qt5/plugins/contacts
%_libdir/qt5/plugins/contacts/*
%dir %_libdir/qt5/plugins/organizer
%_libdir/qt5/plugins/organizer/*
%dir %_libdir/qt5/plugins/versit
%_libdir/qt5/plugins/versit/*

%files -n libqt5-pim-devel
%dir %_qt5_examplesdir/contacts
%_qt5_examplesdir/contacts/contacts.pro
%exclude %_includedir/qt5/QtContacts/%qtpim_intver
%exclude %_includedir/qt5/QtContacts/headers.pri
%exclude %_includedir/qt5/QtContacts/private
%dir %_includedir/qt5/QtContacts
%_includedir/qt5/QtContacts/*

%dir %_qt5_examplesdir/organizer
%_qt5_examplesdir/organizer/*
%exclude %_includedir/qt5/QtOrganizer/%qtpim_intver
%exclude %_includedir/qt5/QtOrganizer/headers.pri
%exclude %_includedir/qt5/QtOrganizer/private
%dir %_includedir/qt5/QtOrganizer
%_includedir/qt5/QtOrganizer/*

%exclude %_includedir/qt5/QtVersitOrganizer/%qtpim_intver
%exclude %_includedir/qt5/QtVersitOrganizer/headers.pri
%exclude %_includedir/qt5/QtVersitOrganizer/private
%dir %_includedir/qt5/QtVersitOrganizer
%_includedir/qt5/QtVersitOrganizer/*

%exclude %_includedir/qt5/QtVersit/%qtpim_intver
%exclude %_includedir/qt5/QtVersit/headers.pri
%exclude %_includedir/qt5/QtVersit/private
%dir %_includedir/qt5/QtVersit
%_includedir/qt5/QtVersit/*

%dir %_libdir/cmake/Qt5Contacts
%_libdir/cmake/Qt5Contacts/Qt5ContactsConfig.cmake
%_libdir/cmake/Qt5Contacts/Qt5ContactsConfigVersion.cmake
%_libdir/cmake/Qt5Contacts/Qt5Contacts_QMemoryContactsPlugin.cmake

%dir %_libdir/cmake/Qt5Organizer
%_libdir/cmake/Qt5Organizer/Qt5OrganizerConfig.cmake
%_libdir/cmake/Qt5Organizer/Qt5OrganizerConfigVersion.cmake
%_libdir/cmake/Qt5Organizer/Qt5Organizer_QMemoryOrganizerPlugin.cmake

%dir %_libdir/cmake/Qt5VersitOrganizer
%_libdir/cmake/Qt5VersitOrganizer/Qt5VersitOrganizerConfig.cmake
%_libdir/cmake/Qt5VersitOrganizer/Qt5VersitOrganizerConfigVersion.cmake

%dir %_libdir/cmake/Qt5Versit
%_libdir/cmake/Qt5Versit/Qt5VersitConfig.cmake
%_libdir/cmake/Qt5Versit/Qt5VersitConfigVersion.cmake
%_libdir/cmake/Qt5Versit/Qt5Versit_QBackupHandlerVersitPlugin.cmake
%_libdir/cmake/Qt5Versit/Qt5Versit_QVCardPreserverVersitPlugin.cmake

%_libdir/lib*.so
%_libdir/lib*.prl
%_libdir/pkgconfig/*
%_libdir/qt5/mkspecs/modules/qt_lib_contacts.pri
%_libdir/qt5/mkspecs/modules/qt_lib_organizer.pri
%_libdir/qt5/mkspecs/modules/qt_lib_versitorganizer.pri
%_libdir/qt5/mkspecs/modules/qt_lib_versit.pri
%exclude %_libdir/qt5/mkspecs/modules/*_private.pri

%files -n libqt5-pim-doc
%doc LICENSE.FDL
%_qt5_docdir/*.qch
%dir %_qt5_docdir/qtcontacts
%_qt5_docdir/qtcontacts/*
%dir %_qt5_docdir/qtorganizer
%_qt5_docdir/qtorganizer/*
%dir %_qt5_docdir/qtversit
%_qt5_docdir/qtversit/*

%changelog
* Sun Jul 13 2025 Nikolay Strelkov <snk@altlinux.org> 5.15-alt1
- Initial build for Sisyphus
