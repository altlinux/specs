%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: martchus-qtutilities
Version: 6.21.1
Release: alt1

Summary: Common Qt related C++ classes and routines used by my applications such as dialogs, widgets and models
License: GPL-2.0-or-later
Group: Development/C++
Url: https://github.com/Martchus/qtutilities

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(martchus-c++utilities)

%description
%summary

%package -n libmartchus-qtutilities6
Summary: common Qt related functionality used by Martchus' applications
Group: System/Libraries

%description -n libmartchus-qtutilities6
Martchus-qtutilities contains Qt-related C++ classes and routines for such
things as the dialogs, widgets, and models used in Martchus' applications.

%package -n libmartchus-qtutilities-devel
Summary: common Qt related functionality used by Martchus' applications (headers)
Group: Development/C++

%description -n libmartchus-qtutilities-devel
Martchus-qtutilities contains Qt-related C++ classes and routines for such
things as the dialogs, widgets, and models used in Martchus' applications.

This is the development version of the library. You will need this only if
you intend to compile programs that use this library.

%prep
%setup

%build
%cmake \
       -DBUILD_SHARED_LIBS=ON \
       -DNAMESPACE=martchus \
       -DPACKAGE_NAMESPACE=martchus \
       -DQT_PACKAGE_PREFIX=Qt6
%cmake_build

%install
%cmake_install

%find_lang %name --with-qt

%files -n libmartchus-qtutilities6
%doc LICENSE README.md
%_libdir/libmartchus-qtutilities.so.6*

%files -n libmartchus-qtutilities-devel -f %{name}.lang
%dir %_includedir/martchus-qtutilities
%dir %_includedir/martchus-qtutilities/qtutilities
%dir %_includedir/martchus-qtutilities/qtutilities/aboutdialog
%_includedir/martchus-qtutilities/qtutilities/aboutdialog/aboutdialog.h
%dir %_includedir/martchus-qtutilities/qtutilities/enterpassworddialog
%_includedir/martchus-qtutilities/qtutilities/enterpassworddialog/enterpassworddialog.h
%_includedir/martchus-qtutilities/qtutilities/global.h
%dir %_includedir/martchus-qtutilities/qtutilities/misc
%_includedir/martchus-qtutilities/qtutilities/misc/adoptlocker.h
%_includedir/martchus-qtutilities/qtutilities/misc/compat.h
%_includedir/martchus-qtutilities/qtutilities/misc/conversion.h
%_includedir/martchus-qtutilities/qtutilities/misc/dbusnotification.h
%_includedir/martchus-qtutilities/qtutilities/misc/desktoputils.h
%_includedir/martchus-qtutilities/qtutilities/misc/dialogutils.h
%_includedir/martchus-qtutilities/qtutilities/misc/disablewarningsmoc.h
%_includedir/martchus-qtutilities/qtutilities/misc/recentmenumanager.h
%_includedir/martchus-qtutilities/qtutilities/misc/trylocker.h
%_includedir/martchus-qtutilities/qtutilities/misc/undefxmlparsermacros.h
%_includedir/martchus-qtutilities/qtutilities/misc/xmlparsermacros.h
%dir %_includedir/martchus-qtutilities/qtutilities/models
%_includedir/martchus-qtutilities/qtutilities/models/checklistmodel.h
%dir %_includedir/martchus-qtutilities/qtutilities/paletteeditor
%_includedir/martchus-qtutilities/qtutilities/paletteeditor/colorbutton.h
%_includedir/martchus-qtutilities/qtutilities/paletteeditor/paletteeditor.h
%_includedir/martchus-qtutilities/qtutilities/qtutilities-definitions.h
%dir %_includedir/martchus-qtutilities/qtutilities/resources
%_includedir/martchus-qtutilities/qtutilities/resources/importplugin.h
%_includedir/martchus-qtutilities/qtutilities/resources/qtconfigarguments.h
%_includedir/martchus-qtutilities/qtutilities/resources/resources.h
%dir %_includedir/martchus-qtutilities/qtutilities/settingsdialog
%_includedir/martchus-qtutilities/qtutilities/settingsdialog/optioncategory.h
%_includedir/martchus-qtutilities/qtutilities/settingsdialog/optioncategoryfiltermodel.h
%_includedir/martchus-qtutilities/qtutilities/settingsdialog/optioncategorymodel.h
%_includedir/martchus-qtutilities/qtutilities/settingsdialog/optionpage.h
%_includedir/martchus-qtutilities/qtutilities/settingsdialog/qtsettings.h
%_includedir/martchus-qtutilities/qtutilities/settingsdialog/settingsdialog.h
%dir %_includedir/martchus-qtutilities/qtutilities/setup
%_includedir/martchus-qtutilities/qtutilities/setup/updater.h
%_includedir/martchus-qtutilities/qtutilities/version.h
%dir %_includedir/martchus-qtutilities/qtutilities/widgets
%_includedir/martchus-qtutilities/qtutilities/widgets/buttonoverlay.h
%_includedir/martchus-qtutilities/qtutilities/widgets/clearcombobox.h
%_includedir/martchus-qtutilities/qtutilities/widgets/clearlineedit.h
%_includedir/martchus-qtutilities/qtutilities/widgets/clearplaintextedit.h
%_includedir/martchus-qtutilities/qtutilities/widgets/clearspinbox.h
%_includedir/martchus-qtutilities/qtutilities/widgets/iconbutton.h
%_includedir/martchus-qtutilities/qtutilities/widgets/pathselection.h
%_libdir/libmartchus-qtutilities.so
%_pkgconfigdir/martchus-qtutilities.pc
%dir %_datadir/martchus-qtutilities
%dir %_datadir/martchus-qtutilities/cmake
%_datadir/martchus-qtutilities/cmake/martchus-qtutilitiesConfig.cmake
%_datadir/martchus-qtutilities/cmake/martchus-qtutilitiesConfigVersion.cmake
%_datadir/martchus-qtutilities/cmake/martchus-qtutilitiesTargets-*.cmake
%_datadir/martchus-qtutilities/cmake/martchus-qtutilitiesTargets.cmake
%dir %_datadir/martchus-qtutilities/cmake/modules
%_datadir/martchus-qtutilities/cmake/modules/QtConfig.cmake
%_datadir/martchus-qtutilities/cmake/modules/QtGuiConfig.cmake
%_datadir/martchus-qtutilities/cmake/modules/QtJsProviderConfig.cmake
%_datadir/martchus-qtutilities/cmake/modules/QtLinkage.cmake
%_datadir/martchus-qtutilities/cmake/modules/QtWebViewProviderConfig.cmake
%dir %_datadir/martchus-qtutilities/cmake/templates
%_datadir/martchus-qtutilities/cmake/templates/jsdefs.h.in
%_datadir/martchus-qtutilities/cmake/templates/jsincludes.h.in
%_datadir/martchus-qtutilities/cmake/templates/qtconfig.h.in
%_datadir/martchus-qtutilities/cmake/templates/webviewdefs.h.in
%_datadir/martchus-qtutilities/cmake/templates/webviewincludes.h.in
%dir %_datadir/martchus-qtutilities/translations

%changelog
* Fri May 15 2026 Nikolay Strelkov <snk@altlinux.org> 6.21.1-alt1
- New version 6.21.1.

* Wed Apr 08 2026 Nikolay Strelkov <snk@altlinux.org> 6.21.0-alt1
- New version 6.21.0.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 6.20.0-alt1
- New version 6.20.0.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 6.19.1-alt1
- New version 6.19.1.

* Wed Jan 07 2026 Nikolay Strelkov <snk@altlinux.org> 6.19.0-alt1
- New version 6.19.0.

* Thu Dec 04 2025 Nikolay Strelkov <snk@altlinux.org> 6.18.4-alt1
- New version 6.18.4.

* Sat Nov 22 2025 Nikolay Strelkov <snk@altlinux.org> 6.18.3-alt1
- Initial build for Sisyphus
