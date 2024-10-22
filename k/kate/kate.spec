%define rname kate

%define sover 6
%define libkateprivate libkateprivate%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Editors
Summary: Advanced text editor
Url: http://www.kde.org
License:  GPL-3.0-or-later

Requires: %name-common
#Requires: %name-core
Requires: kf6-syntax-highlighting

Provides: kde5-kate = %EVR
Obsoletes: kde5-kate < %EVR

Source: %rname-%version.tar
Patch1: alt-soname.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel 
BuildRequires: libgit2-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel kf6-kpackage-devel
BuildRequires: kf6-kparts-devel kf6-kservice-devel kf6-ktexteditor-devel kf6-ktextwidgets-devel kf6-kwallet-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel 
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-threadweaver-devel kf6-syntax-highlighting-devel
BuildRequires: plasma6-activities-devel

%description
A fast and advanced text editor with nice plugins

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-kate-common = %EVR
Obsoletes: kde5-kate-common < %EVR
%description common
%name common package

%package core
Summary: Core files needed for %rname
Group: Graphical desktop/KDE
Requires: %name-common
%description core
Core files needed for %rname

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n kwrite
Group: Editors
Summary: Text editor for KDE
Requires: %name-common
#Requires: %name-core
Provides: kde5-kwrite = %EVR
Obsoletes: kde5-kwrite < %EVR
%description -n kwrite
Text editor for KDE

%package -n %libkateprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
Obsoletes: libkateprivate5 < %EVR
%description -n %libkateprivate
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

# clean mime-type
sed -i 's|inode/directory;||' apps/kate/data/org.kde.kate.desktop

%build
%K6build

%install
%K6install
%K6install_move data kateproject katexmltools kconf_update
%find_lang %name --with-kde --all-name

kde6_add_text_mimes() {
desktop-file-install --mode=0755 --dir %buildroot/%_K6xdgapp \
	--add-mime-type=text/css \
	--add-mime-type=text/csv \
	--add-mime-type=text/english \
	--add-mime-type=text/plain \
	--add-mime-type=text/x-adasrc \
	--add-mime-type=text/x-bibtex \
	--add-mime-type=text/x-c++ \
	--add-mime-type=text/x-chdr \
	--add-mime-type=text/x-c++hdr \
	--add-mime-type=text/x-csharp \
	--add-mime-type=text/x-csrc \
	--add-mime-type=text/x-c++src \
	--add-mime-type=text/x-dsrc \
	--add-mime-type=text/x-fortran \
	--add-mime-type=text/x-gle \
	--add-mime-type=text/x-java \
	--add-mime-type=text/x-javascript \
	--add-mime-type=text/x-log \
	--add-mime-type=text/x-makefile \
	--add-mime-type=text/x-objcsrc \
	--add-mime-type=text/x-pascal \
	--add-mime-type=text/x-patch \
	--add-mime-type=text/x-perl \
	--add-mime-type=text/x-php \
	--add-mime-type=text/x-python \
	--add-mime-type=text/x-sh \
	--add-mime-type=text/x-sql \
	--add-mime-type=text/x-tcl \
	--add-mime-type=text/x-tex \
	--add-mime-type=text/x-rpm-spec \
	$1
}

kde6_add_text_mimes %buildroot/%_K6xdgapp/org.kde.kate.desktop
kde6_add_text_mimes %buildroot/%_K6xdgapp/org.kde.kwrite.desktop

%files common -f %name.lang
%doc LICENSES/*
%_K6icon/hicolor/*/apps/kate.*

#%files core

%files
%_K6bin/kate
%_K6plug/kf6/ktexteditor/
%_K6xdgapp/org.kde.kate.desktop
%_K6data/kateproject/
%_K6data/katexmltools/
#%_K6conf_up/*kate*
%_datadir/metainfo/*kate*.xml

%files -n kwrite
%_K6bin/kwrite
%_K6xdgapp/org.kde.kwrite.desktop
%_K6icon/hicolor/*/apps/kwrite.*
%_datadir/metainfo/*kwrite*.xml

%files -n %libkateprivate
%_K6lib/libkateprivate.so.%sover
%_K6lib/libkateprivate.so.*

#%files devel
#%_K6inc/kate/
#%_K6inc/kate_*.h
#%_K6link/lib*.so


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

