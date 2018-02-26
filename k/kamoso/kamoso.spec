Name:           kamoso
Version:        2.0.2
Release:        alt2
Summary:        Application for taking pictures and videos from a webcam

Group:          Video
License:        GPLv2+
URL:            https://projects.kde.org/projects/extragear/multimedia/kamoso/
Source0:        ftp://ftp.kde.org/pub/kde/stable/kamoso/%{version}/src/%{name}-%{version}.tar.bz2

BuildRequires(pre): kde4libs-devel >= 4.6.0
BuildRequires:  gcc-c++ 
BuildRequires:  libkipi4-devel 
BuildRequires:  qt-gstreamer-devel
BuildRequires:  libsoprano-devel
BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano

%description
Kamoso is an application to take pictures and videos out of your webcam.

%prep
%setup -q

%build
%K4build

%install
%K4install
%K4find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING TODO
%_K4bindir/%name
%_K4bindir/kamosoPluginTester
%_K4lib/kipiplugin_youtube.so
%_desktopdir/kde4/%name.desktop
%_K4srv/kipiplugin_youtube.desktop
%_K4srvtyp/kamosoplugin.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_iconsdir/hicolor/*/actions/youtube.*

%changelog
* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt2
- fix build requires

* Fri Apr 27 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt0.M60P.2
- rebuild

* Fri Feb 24 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt0.M60P.1
- Backport to p6 branch

* Tue Feb 21 2012 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus
