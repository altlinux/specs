
%define libsover 5
%define liblibkmldonkey liblibkmldonkey%libsover

%define rname kmldonkey
Name: kde4-%rname
Version: 2.0.2
Release: alt3

Summary: MLdonkey KDE frontend
License: GPL
Group: Networking/File transfer
Url: http://www.kmldonkey.org/
Source: %rname-%version.tar.bz2

Requires: kde4libs >= %{get_version kde4libs}
Conflicts: kmldonkey <= 0.10.1-alt3

BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++

%description
KMLDonkey is a project that aims to fully integrate the mldonkey P2P software
into the KDE desktop.


%package devel
Summary: Development part of KDE MLdonkey client
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description devel
This package contains development part of %name

%package -n %liblibkmldonkey
Summary: %name library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %liblibkmldonkey
%name library

%package common
Summary: %name common empty package
Group: System/Configuration/Other
%description common
%name common empty package


%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install
%K4find_lang --with-kde %rname


%files common

%files -f %rname.lang
%doc AUTHORS ChangeLog

%_K4bindir/*
%_K4iconsdir/hicolor/*/apps/*.*
%_K4xdg_apps/kmldonkey.desktop

%_K4lib/plasma_*_kmldonkey.so
%_K4apps/%rname
%_K4srv/plasma-*-kmldonkey.desktop

%files -n %liblibkmldonkey
%_K4libdir/liblibkmldonkey.so.%libsover
%_K4libdir/liblibkmldonkey.so.%libsover.*

%files devel
%_K4includedir/%rname
%_K4link/lib*.so


%changelog
* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt3
- move to standart place

* Mon Nov 29 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt2
- fix to build

* Tue Sep 15 2009 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- initial specfile
