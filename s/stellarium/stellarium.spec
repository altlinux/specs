# Floating point tests fails on %%ix86 arches
%ifarch %qt6_qtwebengine_arches
%def_with       check
%endif

# Extra documentation deps
%def_with       doxygen
%def_with       graphviz

# System libraries
%def_with       system_zlib
%def_with       system_qtcompress

%ifarch %qt6_qtwebengine_arches
%def_with       qtwebengine
%endif

# text2speech nessasary only when media enabled
%def_with       media
%def_with       text2speech

# exiv2 nessasary only when lensdistortion enabled
%def_with       lensdistortion
%def_with       exiv2

# libgps nessasary only when gps enabled
%def_with       gps
%def_with       libgps

%def_with       showmysky
%def_with       xlsx
%def_with       translation

# requires libindi API incompatible with codebase
%def_with    telescopecontrol

Name: stellarium
Version: 26.1
Release: alt1

Summary: Astronomical Sky Simulator

License: GPLv2
Group: Education
Url: http://www.stellarium.org

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt6-webengine

%add_python3_req_skip astropy astropy.coordinates astroquery.vizier percache

BuildRequires: cmake gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-charts-devel
BuildRequires: qt6-positioning-devel
BuildRequires: qt6-svg-devel
# Seems, that documentation is strictly nessesary=)
BuildRequires: libmd4c-devel
BuildRequires: perl-podlators
# For python3 scripts
BuildRequires: rpm-build-python3

%{?_with_check:BuildRequires: ctest xvfb-run}

%{?_with_doxygen:BuildRequires: doxygen}
%{?_with_graphviz:BuildRequires: graphviz}

%{?_with_system_zlib:BuildRequires: zlib-devel}
%{?_with_qtwebengine:BuildRequires: qt6-webengine-devel}

%{?_with_media:BuildRequires: qt6-multimedia-devel}
%{?_with_text2speech:BuildRequires: qt6-speech-devel}
%{?_with_text2speech:Requires: speech-dispatcher}

%{?_with_lensdistortion:BuildRequires: libnlopt-devel}
%{?_with_exiv2:BuildRequires: libexiv2-devel}

%{?_with_gps:BuildRequires: qt6-serialport-devel}
%{?_with_libgps:BuildRequires: libgps-devel}

%{?_with_translation:BuildRequires: qt6-tools-devel}
%{?_with_showmysky:BuildRequires: libCalcMySky-devel}
%{?_with_xlsx:BuildRequires: libQXlsx-devel}
%{?_with_telescopecontrol:BuildRequires: libindi-devel}

# Disabled beacause of problems with translation encoding
ExcludeArch: %ix86

# Large chunk of arch-independent data is better not duplicated
Requires: %name-data = %EVR

%description
Stellarium is a free software available for Windows, Linux/Unix and MacOSX.
It renders 3D photo-realistic skies in real time. With stellarium, you
really see what you can see with your eyes, binoculars or a small
telescope.

%package data
Summary: Data files for %name
License: GPLv2
Group: Education
BuildArch: noarch

%description data
Stellarium is a free software available for Windows, Linux/Unix and MacOSX.
It renders 3D photo-realistic skies in real time. With stellarium, you
really see what you can see with your eyes, binoculars or a small
telescope.

This package contains shared data files for Stellarium.

%prep
%setup

%ifarch %e2k
%define _optlevel s
# lcc doesn't ignore unicode bom
find -type f -print0 | xargs -r0 -- sed -i '1s/^\xEF\xBB\xBF//'
%endif

%{?_with_system_zlib:rm -rv src/external/zlib}
%{?_with_system_qtcompress:rm -rv src/external/qtcompress}

%build
# Complaining on:
# Detected locale "C" with character encoding "ANSI_X3.4-1968", which is not UTF-8.
# Qt depends on a UTF-8 locale, and has switched to "C.UTF-8" instead.
# If this causes problems, reconfigure your locale. See the locale(1) manual
# for more information.
export LANG="en_US.UTF-8"

%cmake \
    -DUSE_BUNDLED_QTCOMPRESS=%{without system_qtcompress} \
    -DENABLE_GPS=%{with gps} \
    -DENABLE_MEDIA=%{with media} \
    -DENABLE_SHOWMYSKY=%{with showmysky} \
    -DENABLE_XLSX=%{with xlsx} \
    -DENABLE_NLS=%{with translation} \
    -DUSE_PLUGIN_LENSDISTORTIONESTIMATOR=%{with lensdistortion} \
    -DUSE_PLUGIN_TELESCOPECONTROL=%{with telescopecontrol} \
    -DUSE_PLUGIN_MOSAICCAMERA=1 \
    -DENABLE_TESTING=%{with check} \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DQT_NO_PRIVATE_MODULE_WARNING=ON
%cmake_build

%install
%cmake_install

# See ALT 25353
find %buildroot -name 'DejaVuSans*.ttf' -delete -print

%check
# FIXME: Watch the upstream issue #2591.
# Broken test excluded from suite.
export LANG=en_US.UTF-8
xvfb-run %ctest -E testCalendars

%files
%doc ChangeLog README*
%_bindir/%name
%_mandir/man1/%name.1.xz
%_datadir/applications/*.desktop
%_datadir/metainfo/*.appdata.xml
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/mime/packages/stellarium.xml

%files data
%_datadir/%name

%changelog
* Sat Apr 11 2026 Grigory Ustinov <grenka@altlinux.org> 26.1-alt1
- Build new version.

* Fri Feb 20 2026 Grigory Ustinov <grenka@altlinux.org> 25.4-alt2
- Added rt dependency on speech-dispatcher to fix speech output support.

* Thu Feb 19 2026 Grigory Ustinov <grenka@altlinux.org> 25.4-alt1
- Built new version (Closes: #57521).
- Improved documetation building.
- Built with gps support.
- Built with speech output support.
- Enabled Telescope Control plugin.
- Enabled Mosaic Camera plugin.
- Detached data in separate package.

* Wed Oct 15 2025 Grigory Ustinov <grenka@altlinux.org> 25.3-alt1
- Build new version.

* Sun Jul 06 2025 Grigory Ustinov <grenka@altlinux.org> 25.2-alt1
- Build new version (Closes: #53705, #54997).

* Mon Jan 06 2025 Grigory Ustinov <grenka@altlinux.org> 24.4-alt1
- Automatically updated to 24.4 (Closes: #52591).

* Thu Nov 07 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 24.3-alt1
- NMU: Build new version.

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 0.21.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Apr 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.21.0-alt1
- Build new version.

* Thu Jan 14 2021 Grigory Ustinov <grenka@altlinux.org> 0.20.4-alt1
- Build new version.

* Mon Sep 28 2020 Grigory Ustinov <grenka@altlinux.org> 0.20.3-alt1
- Build new version.

* Thu Jun 25 2020 Grigory Ustinov <grenka@altlinux.org> 0.20.2-alt1
- Build new version.

* Mon Apr 27 2020 Grigory Ustinov <grenka@altlinux.org> 0.20.1-alt1
- Build new version.

* Mon Mar 30 2020 Grigory Ustinov <grenka@altlinux.org> 0.20.0-alt1
- Build new version.

* Tue Dec 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.19.3-alt1
- Build new version.

* Mon Sep 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.19.2-alt1
- Build new version.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 0.19.1-alt1
- Build new version.

* Fri Feb 01 2019 Michael Shigorin <mike@altlinux.org> 0.18.3-alt2
- E2K: drop Unicode BoM symbols from source files
- Minor spec cleanup

* Mon Dec 24 2018 Grigory Ustinov <grenka@altlinux.org> 0.18.3-alt1
- Build new version.

* Thu Aug 16 2018 Grigory Ustinov <grenka@altlinux.org> 0.18.2-alt1
- Build new version.

* Mon Jul 16 2018 Grigory Ustinov <grenka@altlinux.org> 0.18.1-alt1
- Build new version.

* Fri Jun 01 2018 Grigory Ustinov <grenka@altlinux.org> 0.18-alt1
- Build new version (Closes: #34976).
- Remove fonts, packaged in fonts-ttf-dejavu (Closes: #25353).

* Tue Oct 10 2017 Anton Farygin <rider@altlinux.ru> 0.16.1-alt1.S1
- new version

* Sun Feb 21 2016 Mikhail E. Rudachenko (ali) <ali@altlinux.org> 0.14.2-alt1
- new version

* Sun Oct 25 2015 Alexei Takaseev <taf@altlinux.org> 0.14.0-alt1
- 0.14.0

* Fri Feb 20 2015 Mikhail E. Rudachenko (ali) <ali@altlinux.org> 0.13.2-alt1
- new version
- specfile cleanup
- removed patch for desktop file fix

* Fri Jan 09 2015 Mikhail E. Rudachenko (ali) <ali@altlinux.org> 0.13.1-alt1
- new version
- specfile cleanup
- removed .png and .desktop files
- added patch for desktop file fix (Fedora)

* Wed Jun 24 2009 Alex Karpov <karpov@altlinux.ru> 0.10.2-alt1
- new version

* Sat Feb 07 2009 Alex Karpov <karpov@altlinux.ru> 0.10.1-alt1
- new version

* Mon Dec 15 2008 Alex Karpov <karpov@altlinux.ru> 0.10.0-alt0.2
- added .desktop file (#18212)
    + removed obsoleted macros

* Tue Sep 30 2008 Alex Karpov <karpov@altlinux.ru> 0.10.0-alt0.1
- 0.10.0

* Thu Jul 31 2008 Alex Karpov <karpov@altlinux.ru> 0.9.1-alt1.1
- added patch (thanks Turkov Oleg) for blank screen on start fix (#16473)

* Tue Jan 22 2008 Alex Karpov <karpov@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Tue Sep 11 2007 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt2.2
- first build of 0.9.0 for Sisyphus

* Tue Jun 26 2007 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt2.1
- first build of 0.9.0 for Daedalus

* Fri Jun 15 2007 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt2
- spec cleanup
- updated build requirements

* Thu Jun 14 2007 Alex Karpov <karpov@altlinux.ru> 0.9.0-alt1
- new version

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt1
- new version

* Thu Jan 27 2005 Sergey V Turchin <zerg at altlinux dot org> 0.6.2-alt1
- new version

* Tue Aug 17 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6.0-alt1
- new version
- fix menu section

* Wed Oct 01 2003 Sergey V Turchin <zerg at altlinux dot org> 0.5.2-alt1
- new version
- fix build requires

* Fri Jan 17 2003 Sergey V Turchin <zerg@altlinux.ru> 0.5.0-alt1
- new version

* Mon Oct 14 2002 Sergey V Turchin <zerg@altlinux.ru> 0.4.9-alt1
- new version
- build with gcc3.2

* Tue Aug 13 2002 Sergey V Turchin <zerg@altlinux.ru> 0.4.7-alt1
- initial spec

