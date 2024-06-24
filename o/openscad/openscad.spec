# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: openscad
Version: 2021.01
Release: alt5

Summary: The Programmers Solid 3D CAD Modeller

# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License: GPLv2 with exceptions and CC0
Group: Engineering
Url: https://openscad.org/

# Source0-url: https://github.com/%name/%name/releases/download/%name-%version/%name-%version.src.tar.gz
Source0: %name-%version.tar
# https://github.com/openscad/openscad/blob/0f54c3e98d2a4638951b9ea5a32336a9a7839130/locale/ru.po
Source1: ru.po
Patch: openscad-polyclipping.patch
# fix build with cgal >= 5.3
Patch1: cc49ad8dac24309f5452d5dea9abd406615a52d9.patch
# https://github.com/openscad/openscad/commit/9b79576c1ee9d57d0f4a5de5c1365bb87c548f36
Patch2: %name-2021.01-fix-overloaded-join.patch
# https://github.com/openscad/openscad/commit/770e3234cbfe66edbc0333f796b46d36a74aa652
Patch3: CVE-2022-0496.patch
# https://github.com/openscad/openscad/commit/84addf3c1efbd51d8ff424b7da276400bbfa1a4b
Patch4: CVE-2022-0497.patch
Patch5: openscad-2021.01-alt-fix-for-boost-1.85.0.patch
# fix build with cgal >= 5.4
Patch6: openscad-2021.01-cgal-build-fix.patch

# needed cgal-devel on armh
ExcludeArch: armh

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: cmake
BuildRequires: cgal-devel
BuildRequires: ImageMagick-tools
BuildRequires: xorg-xvfb xvfb-run
BuildRequires: boost-asio-devel boost-context-devel boost-devel boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-signals-devel boost-wave-devel
BuildRequires: desktop-file-utils
BuildRequires: eigen3
BuildRequires: libfreetype-devel >= 2.4
BuildRequires: fontconfig-devel >= 2.10
BuildRequires: libGLEW-devel >= 1.6
BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: libgmp-devel libgmpxx-devel
BuildRequires: libharfbuzz-devel libharfbuzz-utils
BuildRequires: libxml2-devel
BuildRequires: libdouble-conversion-devel
BuildRequires: libzip-devel
BuildRequires: libmpfr-devel >= 3.0.0
BuildRequires: opencsg-devel >= 1.3.2
BuildRequires: libpolyclipping-devel >= 6.1.3
BuildRequires: procps sysvinit-utils
BuildRequires: qt5-base-devel qt5-designer
BuildRequires: qt5-multimedia-devel
BuildRequires: flex
BuildRequires: libqscintilla2-qt5-devel
BuildRequires: libcairo-devel
%ifnarch %e2k
# act -> go
BuildRequires: lib3mf-devel
BuildRequires: boost-coroutine-devel
%endif

Requires: %name-MCAD = %EVR
%add_python3_path %_datadir/%name/libraries/MCAD

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

###############################################
%package MCAD
Group: Engineering
Summary: OpenSCAD Parametric CAD Library
License: LGPLv2+ and LGPLv2 and LGPLv3+ and (GPLv3 or LGPLv2) and (GPLv3+ or LGPLv2) and (CC-BY-SA or LGPLv2+) and (CC-BY-SA or LGPLv2) and CC-BY and BSD and MIT and Public Domain
Url: https://www.github.com/openscad/MCAD
Requires: %name = %EVR
#BuildArch: noarch

%description MCAD
This library contains components commonly used in designing and moching up
mechanical designs. It is currently unfinished and you can expect some API
changes, however many things are already working.

%prep
%setup
%autopatch -p1

%ifarch %e2k
# mcst#8018
sed -i "s/c++14/c++17/" c++std.pri
# lcc 1.25 didn't grok that (1.26 does)
cc -v 2>&1 | grep -q 'lcc:1\.25' && {
sed -i 's/std::array<uint8_t,.*data()/"\\x89\\x50\\x4e\\x47\\x0d\\x0a\\x1a\\x0a"/' src/surface.cc
}
%endif

cp -f %SOURCE1 locale/ru.po

# Unbundle polyclipping
rm src/ext/polyclipping -rf

# Remove unwanted things from MCAD, such as nonworking Python tests
pushd libraries/MCAD
for FILE in *.py; do
  rm -r $FILE
done
mv bitmap/README bitmap-README
popd

# Tests cmake check for MCAD by probing libraries/MCAD/__init__.py
# But we've just removed it
sed -i 's@MCAD/__init__.py@MCAD/gears.scad@' tests/CMakeLists.txt

%build
%qmake_qt5 \
	PREFIX=%prefix \
	VERSION=%version \
%ifnarch %e2k
	CONFIG-=debug \
%endif
	%nil
%make_build

# tests
pushd tests
cmake -DPYTHON_EXECUTABLE:STRING=%__python3
%make_build
popd

%install
%makeinstall_std INSTALL_ROOT=%buildroot
rm -r %buildroot%_datadir/%name/fonts
%find_lang %name

for FILE in lgpl-2.1.txt README.markdown TODO bitmap-README; do
  rm %buildroot%_datadir/%name/libraries/MCAD/$FILE
done

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop

# tests
pushd tests
ctest || : # let the tests fail, as they probably won't work in hasher
popd

%files -f %name.lang
%doc README.md
%doc RELEASE_NOTES.md
%attr(755,root,root) %_bindir/%name
%_datadir/metainfo/*.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/mime/packages/%name.xml
%dir %_datadir/%name
%_datadir/%name/examples
%_datadir/%name/color-schemes
%_datadir/%name/locale
%dir %_datadir/%name/libraries
%_datadir/%name/templates
%_man1dir/*

%files MCAD
%doc libraries/MCAD/README.markdown
%doc libraries/MCAD/TODO
%doc libraries/MCAD/bitmap-README
%_datadir/%name/libraries/MCAD

%changelog
* Sun Jun 23 2024 Anton Midyukov <antohami@altlinux.org> 2021.01-alt5
- Fix build with CGAL >= 5.4

* Fri May 17 2024 Ivan A. Melnikov <iv@altlinux.org> 2021.01-alt4.2
- NMU: Fix building with boost 1.85.0.

* Tue Apr 25 2023 Michael Shigorin <mike@altlinux.org> 2021.01-alt4.1
- E2K (thx ilyakurdyukov@):
  + avoid BR: lib3mf for now (BR chain boils down to go)
  + avoid BR: boost-coroutine-devel (missing so far)
  + get *-debuginfo back
  + explicit -std=c++17 (mcst#8018)
  + lcc 1.25 ftbfs workaround

* Mon Jun 20 2022 Anton Midyukov <antohami@altlinux.org> 2021.01-alt4
- Fixes:
  + CVE-2022-0496 Out-of-bounds memory access in DXF loader (path
    identification)
  + CVE-2022-0497 Out-of-bounds memory access in comment parser
  + Fix build issue with overloaded join().
- cleanup spec

* Thu May 05 2022 Anton Midyukov <antohami@altlinux.org> 2021.01-alt3
- update russian translation from upstream

* Fri Aug 13 2021 Vitaly Lipatov <lav@altlinux.ru> 2021.01-alt2
- NMU: fix build with cgal >= 5.3
- NMU: fix URL
- NMU: drop BR: boost-python-devel (see # 40722)

* Thu May 13 2021 Anton Midyukov <antohami@altlinux.org> 2021.01-alt1
- New version 2021.01
- ExcludeArch: armh

* Tue Dec 01 2020 Anton Midyukov <antohami@altlinux.org> 2019.05-alt7
- Not required fonts (Closes: 39356)

* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2019.05-alt6
- Rebuilt with boost-1.74.0.

* Thu Jun 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2019.05-alt5
- Rebuilt with boost-1.73.0.

* Wed Apr 15 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2019.05-alt4
- Rebuilt with cgal 5.0.2.

* Fri Apr 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2019.05-alt3
- Rebuilt with boost-1.72.0.

* Mon Dec 23 2019 Anton Midyukov <antohami@altlinux.org> 2019.05-alt2
- Update russian translation (thanks Alexander Kurachenko)

* Wed Nov 27 2019 Anton Midyukov <antohami@altlinux.org> 2019.05-alt1
- New version 2019.05
- switch to gear

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2015.03.3-alt2_12.1
- NMU: rebuilt with boost-1.67.0

* Thu Apr 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2015.03.3-alt2_12
- Rebuilt with new boost.

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 2015.03.3-alt1_12
- new version

* Wed Oct 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2015.03.2-alt3_4
- Rebuilt with qscintilla2 2.10.1.

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2015.03.2-alt2_4
- Rebuilt with CGAL 4.10
- Enabled tests

* Fri Feb 26 2016 Igor Vlasenko <viy@altlinux.ru> 2015.03.2-alt1_4
- new version
- TODO: disabled tests - need fixes for x86_64
        'No rule to make target /usr/lib/libCGAL.so'

* Mon Apr 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.03-alt2.2
- Rebuilt with CGAL 4.6

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2014.03-alt2.1
- rebuild with boost 1.57.0

* Wed Dec 24 2014 Dmitry Derjavin <dd@altlinux.org> 2014.03-alt2
- Revision up

* Thu May 08 2014 Igor Vlasenko <viy@altlinux.ru> 2014.03-alt1_1
- converted for ALT Linux by srpmconvert tools
- TODO: fixes for No rule to make target /usr/lib/libCGAL.so
