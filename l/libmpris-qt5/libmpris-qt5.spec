%define repo qtmpris

Name: libmpris-qt5
Summary: Qt and QML MPRIS interface and adaptor
Version: 1.0.6
Release: alt1
License: LGPL-2.1+
Group: System/Libraries
Url: https://git.merproject.org/mer-core/%repo
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: https://git.merproject.org/mer-core/%repo/-/archive/%version/%repo-%version.tar.bz2
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: make

%description
%summary.

%package -n mpris-qt5-devel
Summary: Development package for %name
Group: Development/Other

%description -n mpris-qt5-devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version

%build
%qmake_qt5 CONFIG+=nostrip
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc COPYING README.md
%_libdir/lib*.so.1*

%files -n mpris-qt5-devel
%dir %_qt5_headerdir/MprisQt/
%_qt5_headerdir/MprisQt/Mpris
# %_qt5_headerdir/MprisQt/MprisQt
%_qt5_headerdir/MprisQt/MprisPlayer
%_qt5_headerdir/MprisQt/MprisController
%_qt5_headerdir/MprisQt/MprisManager
%_qt5_headerdir/MprisQt/mpris.h
%_qt5_headerdir/MprisQt/mprisqt.h
%_qt5_headerdir/MprisQt/mprisplayer.h
%_qt5_headerdir/MprisQt/mpriscontroller.h
%_qt5_headerdir/MprisQt/mprismanager.h
%dir %_qt5_qmldir/org/nemomobile/
%dir %_qt5_qmldir/org/nemomobile/mpris/
%_qt5_qmldir/org/nemomobile/mpris/%name-qml-plugin.so
%_qt5_qmldir/org/nemomobile/mpris/plugins.qmltypes
%_qt5_qmldir/org/nemomobile/mpris/qmldir
%_qt5_archdatadir/mkspecs/features/*.prf
%_pkgconfigdir/*.pc
%_libdir/lib*.so

%changelog
* Wed Apr 14 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.6-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
