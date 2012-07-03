
Name: phonon-xine
Version: 4.4.4
Release: alt3

Group: System/Libraries
Summary: Xine phonon backend
License: LGPLv2+
Url: http://phonon.kde.org/

Provides: phonon-backend = %{get_version phonon-devel}
Provides: phonon-backend-xine = %version

Source: %name-%version.tar

# Automatically added by buildreq on Tue Feb 01 2011 (-bi)
#BuildRequires: automoc cmake gcc-c++ glibc-devel-static libXScrnSaver-devel libXcomposite-devel libXdamage-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libqt3-devel libqt4-devel libxine-devel libxkbfile-devel rpm-build-ruby
BuildRequires(pre): phonon-devel
BuildRequires: automoc cmake gcc-c++ glibc-devel libqt4-devel libxine-devel kde-common-devel

%description
Xine phonon backend

%prep
%setup -q

%build
%K4cmake \
    -DINCLUDE_INSTALL_DIR=%_K4includedir \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt4dir
%K4make

%install
%K4install


%files
%_qt4dir/plugins/phonon_backend/phonon_xine.so
%_K4srv/phononbackends/xine.desktop
%_iconsdir/hicolor/*/apps/phonon-xine.*

%changelog
* Fri Jan 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt3
- update from master branch

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt2
- fix build requires

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- initial build
