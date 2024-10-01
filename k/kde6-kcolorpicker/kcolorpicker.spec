%define rname kcolorpicker

%define sover 0.6
%define libkcolorpicker libkcolorpicker%sover

Name: kde6-%rname
Version: 0.3.1
Release: alt1
%K6init

Group: System/Libraries
Summary: QToolButton with color popup menu with lets you select a color
Url: https://github.com/ksnip/kcolorpicker
License: LGPL-3.0

Source: %rname-%version.tar
Patch1: alt-sover.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake qt6-svg-devel qt6-wayland-devel

%description
%summary

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: kde5-kcolorpicker-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkcolorpicker
Group: System/Libraries
Summary: %name library
%description -n %libkcolorpicker
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DBUILD_WITH_QT6=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    #

%install
%K6install
mkdir %buildroot/%_libdir/cmake/kColorPicker/
for f in %buildroot/%_libdir/cmake/kColorPicker-Qt?/* ; do
    ln -sr $f %buildroot/%_libdir/cmake/kColorPicker/
done
for f in %buildroot/%_libdir/cmake/kColorPicker/* ; do
    echo "$f" | grep -q '\-Qt[[:digit:]]' \
	&& ln -sr $f `echo "$f" | sed 's|\-Qt[[:digit:]]||'` \
	||:
done
#find_lang %name --with-kde --all-name

%files devel
%_includedir/kColorPicker-Qt?/
%_libdir/cmake/kColorPicker/
%_libdir/cmake/kColorPicker-Qt?/
%_K6link/lib*.so

%files -n %libkcolorpicker
%doc LICENSE* README.md
%_K6lib/libkColorPicker.so.%sover
%_K6lib/libkColorPicker.so.*

%changelog
* Mon Sep 30 2024 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- initial build
