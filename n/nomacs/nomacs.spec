%global github_owner    nomacs
# https://github.com/nomacs/nomacs/issues/530
%global git_build    224

Name: nomacs
Version: 3.17.2287
Release: alt2

License: GPLv3+ and CC-BY
Group: Graphics
Summary: A fast and small image viewer
Url: http://www.nomacs.org

#Source: https://github.com/%name/%name/archive/%name-%version.tar.gz
#Source0:	https://github.com/%{github_owner}/%{name}/archive/%{version}.%{build}.tar.gz/%{name}-%{version}.%{git_build}.tar.gz
Source0:	%name-%version.tar.xz
Source1:	https://github.com/%{github_owner}/%{name}-plugins/archive/%{version}.tar.gz/%{name}-plugins-3.16.tar.gz
# desktop entries rename (https://github.com/nomacs/nomacs/issues/528)
Patch0:		%{name}-3.16.%{git_build}-desktop.diff
# plugins search path (https://github.com/nomacs/nomacs/issues/531)
Patch1:		%{name}-3.16.%{git_build}-pluginspath.diff
# plugins install path (https://github.com/nomacs/nomacs-plugins/issues/34)
Patch2:		%{name}-plugins-3.16-instpath.diff
Patch3:         quazip1_cmake_remove_after_new_version.diff
Patch5:		nomacs-not-update-version.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libexiv2-devel libgomp-devel
BuildRequires: libtiff-devel libopencv-devel-static libraw-devel libgomp-devel
BuildRequires: zlib-devel libwebp-devel libtbb-devel libtiffxx-devel
BuildRequires: qt5-linguist cmake qt5-base-devel qt5-svg-devel qt5-tools-devel libopencv-devel
BuildRequires: libqtsingleapplication-qt5-devel  libqtermwidget-devel
BuildRequires: qt5-declarative-devel  qt5-networkauth-devel

Obsoletes: %name-plugins
#BuildRequires:	cmake(Qt5Gui)
# qt5-qtsvg-devel
#BuildRequires:	cmake(Qt5Svg)
# exiv2-devel
BuildRequires:	pkgconfig(exiv2) >= 0.20
# opencv-devel
#BuildRequires:	pkgconfig(opencv) >= 2.1.0
# LibRaw-devel
BuildRequires:	pkgconfig(libraw) >= 0.12.0
# libtiff-devel
BuildRequires:	pkgconfig(libtiff-4)
# libwebp-devel >= 0.3.1
BuildRequires:	pkgconfig(libwebp)
# quazip-qt5-devel >= 0.7
BuildRequires:	quazip-qt5-devel
# libheif-devel (rpmfusion-free)
# BuildRequires:	pkgconfig(libheif)
BuildRequires:	lcov

#BuildRequires: libqpsd-devel

%description
nomacs is a free image viewer small, fast and able to handle the most common
image formats including RAW images. Additionally it is possible to synchronize
multiple viewers. A synchronization of viewers running on the same computer
or via LAN is possible. It allows to compare images and spot the differences
(e.g. schemes of architects to show the progress).

#package	plugins
#Summary:	Plugins for nomacs image viewer.
#Requires:	%{name} = %{version}-%{release}
#Group: Graphics

#%description	plugins
#Some usefull plugins for nomacs:
#- Affine transformations
#- RGB image from greyscales
#- Fake miniature filter
#- Page extractions
#- Painting



%prep
#setup -n %{name}-%{version}.%{git_build}
%setup -q
#patch0
#patch1
%patch5 -p1
#setup -T -D -a 1 -n %{name}-3.16.%{git_build}
# plug them in
#mv nomacs-plugins-%{version}/* ImageLounge/plugins/
#patch2
#patch3 -p1

# Be sure
#rmdir {3rd-party/*,3rd-party}
# wrong lang code (https://github.com/nomacs/nomacs/issues/529)
rm -fv ImageLounge/translations/nomacs_als.ts


%build
%cmake ImageLounge \
  -DCMAKE_BUILD_TYPE=Release\
  -DENABLE_RAW=1 \
  -DUSE_SYSTEM_WEBP=ON \
  -DUSE_SYSTEM_QUAZIP=ON \
  -DENABLE_TRANSLATIONS=ON

%cmake_build

%install
%cmakeinstall_std

%find_lang --with-qt %name
# workaround errors wrt to spaces
sed -i -e 's|Image Lounge|Image?Lounge|g' %{name}.lang


%files -f %name.lang
%doc README.md
%_bindir/%name
%_libdir/libnomacsCore.so*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/Image?Lounge/themes/
%dir %{_datadir}/%{name}/Image?Lounge/
%dir %{_datadir}/%{name}/Image?Lounge/translations/
%_datadir/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%_man1dir/*

#files	plugins
#_libdir/nomacs-plugins/


%changelog
* Fri Nov 17 2023 Ilya Mashkin <oddity@altlinux.ru> 3.17.2287-alt2
- rebuild with new libexiv2

* Fri Nov 17 2023 Ilya Mashkin <oddity@altlinux.ru> 3.17.2287-alt1
- 3.17.2287
- skip plugins

* Sun Jan 30 2022 Ilya Mashkin <oddity@altlinux.ru> 3.16-alt1
- 3.16
- Sync spec with FC
- Update License tag

* Fri Sep 14 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.6-alt7
- rebuilt against libraw.so.19

* Tue Jun 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.6-alt6
- Rebuilt with libopencv-3.4.

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.6-alt5
- Fixed build.

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.6-alt4
- Updated build dependencies

* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.6-alt3
- rebuilt against libraw.so.16

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.6-alt2
- rebuilt against libwebp.so.6

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.6-alt1
- 2.4.6

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt2
- rebuilt against libraw.so.15

* Wed Jul 01 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.3-alt2.1.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Mar 13 2014 Dmitry Derjavin <dd@altlinux.org> 1.6.3-alt2.1
- NMU: rebuild with libopencv-2.4.8.1;

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt2
- rebuilt against libraw.so.10

* Sat Jan 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3
- built against libexiv2.so.13

* Fri Apr 05 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux
