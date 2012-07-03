
Name: automoc
Version: 0.9.88
Release: alt1

Group: Development/KDE and QT
Summary: %name for KDE4
Url: http://websvn.kde.org/trunk/kdesupport/automoc
License: GPLv2+

Provides: automoc4 = %version-%release

Source0: automoc4-%version.tar.bz2
Patch0: automoc-fix-libdir.patch

BuildRequires: cmake gcc-c++ libqt4-devel >= 4.4 kde-common-devel >= 4

%description
%name for KDE4


%prep
%setup -q  -n automoc4-%version
#%patch0 -p0


%build
%K4build


%install
%K4install


%files
%_K4bindir/automoc4
%_K4libdir/automoc4

%changelog
* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 0.9.88-alt1
- new version

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 0.9.87-alt1
- new version

* Wed Jul 30 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9.84-alt1
- new version

* Wed May 28 2008 Sergey V Turchin <zerg at altlinux dot org> 0.0.805344-alt0.1
- initial build
