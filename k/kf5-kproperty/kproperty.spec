Name:    kf5-kproperty
Summary: Property editing framework with editor widget
Group: Development/KDE and QT
Version: 3.0.2
Release: alt1

License: LGPLv2+
Url:     https://community.kde.org/KProperty
# git://anongit.kde.org/kproperty.git
Source: %name-%version.tar
Patch1: %name-%version-fedora-pkgconfig.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kguiaddons-devel kf5-kwidgetsaddons-devel
BuildRequires: cmake pkgconfig

%description
A property editing framework with editor widget similar to what is
known from Qt Designer.

%package devel
Summary: Developer files for %name
Group: Development/KDE and QT
Requires: %name = %EVR
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
%_K5lib/libKPropertyCore3.so.3*
%_K5lib/libKPropertyWidgets3.so.3*
# .rcc icon resources
# not sure if this is needed at runtime for sure or not, but it's relatively
# small currently, so can't hurt -- rex
%_datadir/kpropertywidgets3/

%files devel
%_K5inc/KPropertyCore3/
%_K5link/libKPropertyCore3.so
%_K5lib/cmake/KPropertyCore3/
%_K5lib/pkgconfig/KPropertyCore3.pc
%_K5inc/KPropertyWidgets3/
%_K5link/libKPropertyWidgets3.so
%_K5lib/cmake/KPropertyWidgets3/
%_K5lib/pkgconfig/KPropertyWidgets3.pc

%changelog
* Thu Aug 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2-alt1
- Initial build for ALT.

* Fri Aug 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-4
- move rcc icon resources to main/runtime pkg

* Sat Aug 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-3
- fix pkgconfig harder

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-2
- fix/sanitize pkgconfig deps

* Fri Aug 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.2-1
- 3.0.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Rex Dieter <rdieter@fedoraproject.org> -  3.0.1-1
- first try
