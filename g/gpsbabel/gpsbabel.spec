%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict
%ifarch %qt6_qtwebengine_arches
%def_enable gui
%else
%def_disable gui
%endif

Name: gpsbabel
Version: 1.9.0
Release: alt1
Summary: A tool to convert between various formats used by GPS devices
License: GPLv2
Group: Sciences/Geosciences
Url: https://www.gpsbabel.org

VCS: https://github.com/gpsbabel/gpsbabel.git
Source: %name-%version.tar
Source2: gpsbabel.png

Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: libexpat-devel libusb-devel zlib-devel libminizip-devel gcc-c++
BuildRequires: libshape-devel
BuildRequires: cmake
BuildRequires: qt6-base-devel qt6-tools-devel qt6-serialport-devel qt6-5compat-devel
%if_enabled gui
BuildRequires: qt6-webengine-devel
%endif

%description
GPSBabel converts waypoints, tracks, and routes from one format to another,
whether that format is a common mapping format like Delorme, Streets and
Trips, or even a serial upload or download to a GPS unit such as those from
Garmin and Magellan. By flatting the Tower of Babel that the authors of
various programs for manipulating GPS data have imposed upon us, it returns
to us the ability to freely move our own waypoint data between the programs
and hardware we choose to use.

It contains extensive data manipulation abilities making it a
convenient for server-side processing or as the backend for other
tools.

It does not convert, transfer, send, or manipulate maps. We process
data that may (or may not be) placed on a map, such as waypoints,
tracks, and routes.

%if_enabled gui
%package gui
Group: Sciences/Geosciences
Summary: A tool to convert between various formats used by GPS devices

%description gui
This package contains gui for gpsbabel.
%endif

%prep
%setup
%patch1 -p1

rm -rf zlib shapelib

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%cmake -DGPSBABEL_WITH_LIBUSB=pkgconfig \
	-DGPSBABEL_WITH_SHAPELIB=pkgconfig \
	-DGPSBABEL_WITH_ZLIB=pkgconfig \
	%{?!enabled_gui:-DGPSBABEL_MAPPREVIEW=OFF} \
	%nil
%cmake_build

%install
%cmake_install
install -m 0755 -d %buildroot%_bindir/
install -m 0755 -p %_cmake__builddir/gpsbabel %buildroot%_bindir/

%if_enabled gui
install -m 0755 -p %_cmake__builddir/gui/GPSBabelFE/gpsbabelfe %buildroot%_bindir/
install -m 0755 -d %buildroot%_datadir/gpsbabel
install -m 0644 -p gui/gmapbase.html %buildroot%_datadir/gpsbabel
desktop-file-install \
        --dir %buildroot/%_datadir/applications \
        gui/gpsbabel.desktop
install -m 0755 -d            %buildroot%_datadir/icons/hicolor/256x256/apps/
install -m 0644 -p %SOURCE2 %buildroot%_datadir/icons/hicolor/256x256/apps/
%endif

%find_lang %name --with-qt --all-name

%files
%doc AUTHORS README* intdoc
%_bindir/%name

%if_enabled gui
%files gui -f %name.lang
%doc gui/README*
%_bindir/gpsbabelfe
%_datadir/gpsbabel
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%endif

%changelog
* Wed Jul 10 2024 Anton Farygin <rider@altlinux.ru> 1.9.0-alt1
- 1.7.0 -> 1.9.0 (Closes: #42138)

* Mon Nov 27 2023 Ivan A. Melnikov <iv@altlinux.org> 1.7.0-alt2.1
- NMU: Use rpm-macros-qt5-webengine (fixes build on loongarch64)

* Fri Jan 28 2022 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt2
- build with qtwebkit instead of qtwebengione on e2k and ppc64le

* Wed Oct 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.0-alt1
- Updated to upstream version 1.7.0.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt3
- NMU: remove %%ubt from release

* Mon May 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.4-alt2
- Built Qt5 gui.

* Mon May 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.4-alt1
- Updated to upstream version 1.5.4.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.6-alt2.qa1
- NMU: rebuilt for debuginfo.

* Sat Oct 31 2009 Grigory Batalov <bga@altlinux.ru> 1.3.6-alt2
- Rebuilt with texlive.

* Wed Dec 10 2008 Grigory Batalov <bga@altlinux.ru> 1.3.6-alt1
- New upstream release.

* Fri Sep 12 2008 Grigory Batalov <bga@altlinux.ru> 1.3.5-alt1
- New upstream release.

* Sun Nov 18 2007 Grigory Batalov <bga@altlinux.ru> 1.3.4-alt1
- New upstream release.

* Thu Jun 21 2007 Grigory Batalov <bga@altlinux.ru> 1.3.3-alt1
- Build for ALT Linux.

* Wed Apr 16 2007 Roozbeh Pournader <roozbeh@farsiweb.info> - 1.3.3-1
- Make first Fedora spec based on the one provided upstream
