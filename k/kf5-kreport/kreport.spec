Name:    kf5-kreport
Summary: Framework for creation and generation of reports
Group: Development/KDE and QT
Version: 3.0.2
Release: alt1

License: LGPLv2+

Url:     https://community.kde.org/KReport
# git://anongit.kde.org/kreport.git
Source: %name-%version.tar
Patch1: %name-%version-fedora-pkgconfig.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel qt5-declarative-devel qt5-webkit-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kguiaddons-devel kf5-kwidgetsaddons-devel kde5-marble-devel
BuildRequires: kf5-kproperty-devel
BuildRequires: python cmake pkgconfig

%description
A framework for creation and generation of reports in multiple formats.

%package devel
Summary: Developer files for %name
Group: Development/KDE and QT
%description devel
%{summary}.

%prep
%setup
%patch1 -p1

%build
%K5build \
	-DINCLUDE_INSTALL_DIR:PATH=%_K5inc

%install
%K5install

%files
%doc COPYING.LIB
%_K5lib/libKReport3.so.3*
%dir %_K5plug/kreport3/
# TODO: consider splitting some into subpkgs (maps/marble in particular)
%_K5plug/kreport3/org.kde.kreport.barcode.so
%_K5plug/kreport3/org.kde.kreport.maps.so
%_K5plug/kreport3/org.kde.kreport.web.so
%_datadir/kservicetypes5/kreport_elementplugin.desktop
# .rcc icon resources
%_datadir/kreport3/

%files devel
%_K5inc/KReport3/
%_K5link/libKReport3.so
%_K5lib/cmake/KReport3/
%_K5lib/pkgconfig/KReport3.pc
%_K5archdata/mkspecs/modules/qt_KReport3.pri


%changelog
* Thu Aug 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2-alt1
- Initial build for ALT.

* Fri Aug 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-4
- move rcc icon resource to main/runtime pkg, runtime complains if missing

* Sat Aug 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-3
- add/tighten dep on kproperty

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-2
- fix/sanitize pkgconfig deps

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-1
- 3.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-0.1
- first try
