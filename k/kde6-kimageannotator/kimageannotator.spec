%define rname kimageannotator

%define sover 0.6
%define libkimageannotator libkimageannotator%sover

Name: kde6-%rname
Version: 0.7.1
Release: alt1
%K6init

Group: System/Libraries
Summary: Library and a tool for annotating images
Url: https://github.com/ksnip/kImageAnnotator
License: LGPL-3.0

Source: %rname-%version.tar
Patch1: alt-void-return.patch
Patch2: alt-sover.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake
BuildRequires: qt6-svg-devel qt6-tools-devel qt6-wayland-devel
BuildRequires: kde6-kcolorpicker-devel

%description
%summary

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkimageannotator
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Conflicts: kde5-kimageannotator-devel
%description -n %libkimageannotator
%name library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1


%build
%K6build \
    -DBUILD_WITH_QT6=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    #

%install
%K6install
mkdir %buildroot/%_libdir/cmake/kImageAnnotator/
for f in %buildroot/%_libdir/cmake/kImageAnnotator-Qt?/* ; do
    ln -sr $f %buildroot/%_libdir/cmake/kImageAnnotator/
done
for f in %buildroot/%_libdir/cmake/kImageAnnotator/* ; do
    echo "$f" | grep -q '\-Qt[[:digit:]]' \
	&& ln -sr $f `echo "$f" | sed 's|\-Qt[[:digit:]]||'` \
	||:
done
%find_lang %name --all-name --with-qt

%files common -f %name.lang
%doc LICENSE* CHANGELOG.md README.md
%dir %_datadir/kImageAnnotator/
%dir %_datadir/kImageAnnotator/translations/

%files devel
%_includedir//kImageAnnotator-Qt?/
%_libdir/cmake//kImageAnnotator/
%_libdir/cmake//kImageAnnotator-Qt?/
%_K6link/lib*.so

%files -n %libkimageannotator
%_K6lib/libkImageAnnotator.so.%sover
%_K6lib/libkImageAnnotator.so.*

%changelog
* Tue Oct 01 2024 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt1
- initial build
