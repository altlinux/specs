# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison /usr/bin/desktop-file-validate /usr/bin/pkg-config gcc-c++ libGL-devel libGLEW-devel libGLU-devel pkgconfig(fontconfig) pkgconfig(freetype2) pkgconfig(harfbuzz) python-devel python3-devel rpm-build-python3
# END SourceDeps(oneline)
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: boost-filesystem-devel boost-program_options-devel cmake
Name:           openscad
Version:        2015.03.2
%global upversion 2015.03-2
Release:        alt1_4
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License:        GPLv2 with exceptions and CC0
Group:          Engineering
URL:            http://www.%{name}.org/
Source0:        http://files.%{name}.org/%{name}-%{upversion}.src.tar.gz
Patch0:         %{name}-polyclipping.patch
BuildRequires:  libcgal-devel >= 3.6
BuildRequires:  ImageMagick
BuildRequires:  xvfb-run
BuildRequires:  bison >= 2.4
BuildRequires: boost-devel boost-devel-headers boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3
BuildRequires:  flex >= 2.5.35
BuildRequires:  libfreetype-devel >= 2.4
BuildRequires:  fontconfig-devel >= 2.10
BuildRequires:  gettext
BuildRequires:  libglew-devel >= 1.6
BuildRequires:  glib2-devel
BuildRequires: libgmp-devel libgmp_cxx-devel
BuildRequires:  libharfbuzz-devel >= 0.9.19
BuildRequires: xorg-dri-intel xorg-dri-nouveau xorg-dri-radeon xorg-dri-swrast
BuildRequires:  libmpfr-devel >= 3.0.0
BuildRequires:  opencsg-devel >= 1.3.2
BuildRequires:  polyclipping-devel >= 6.1.3
BuildRequires:  procps-ng
BuildRequires:  python
BuildRequires:  qt4-devel >= 4.4
BuildRequires:  libqscintilla2-qt4-devel
Requires:       fonts-ttf-liberation
Requires:       fonts-ttf-liberation
Requires:       fonts-ttf-liberation
Source44: import.info

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.


###############################################
%package        MCAD
Group: Engineering
Summary:        OpenSCAD Parametric CAD Library
License:        LGPLv2+ and LGPLv2 and LGPLv3+ and (GPLv3 or LGPLv2) and (GPLv3+ or LGPLv2) and (CC-BY-SA or LGPLv2+) and (CC-BY-SA or LGPLv2) and CC-BY and BSD and MIT and Public Domain
URL:            https://www.github.com/openscad/MCAD
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    MCAD
This library contains components commonly used in designing and moching up
mechanical designs. It is currently unfinished and you can expect some API
changes, however many things are already working.

### LICENSES:

##  LGPLv2+:
#   2Dshapes.scad
#   3d_triangle.scad
#   fonts.scad
#   gridbeam.scad
#   hardware.scad
#   libtriangles.scad
#   multiply.scad
#   shapes.scad
#   screw.scad

##  LGPLv2:
#   gears.scad
#   involute_gears.scad
#   servos.scad
#   transformations.scad
#   triangles.scad
#   unregular_shapes.scad
#   bitmap/letter_necklace.scad

##  LGPLv3+:
#   teardrop.scad

##  GPLv3 or LGPLv2:
#   motors.scad
#   nuts_and_bolts.scad


##  GPLv3+ or LGPLv2:
#   metric_fastners.scad
#   regular_shapes.scad

##  CC-BY-SA or LGPLv2+:
#   bearing.scad
#   materials.scad
#   stepper.scad
#   utilities.scad

##  CC-BY-SA or LGPLv2:
#   units.scad

##  CC-BY:
#   polyholes.scad
#   bitmap/alphabet_block.scad
#   bitmap/bitmap.scad
#   bitmap/height_map.scad
#   bitmap/name_tag.scad

## BSD
#   boxes.scad

## MIT
#   constants.scad
#   curves.scad
#   math.scad

## Public Domain
#   lego_compatibility.scad
#   trochoids.scad

###############################################

%prep
%setup -qn %{name}-%{upversion}

# Unbundle polyclipping
rm src/polyclipping -rf
%patch0 -p1

%build
%{qmake_qt4} PREFIX=%{_prefix}
make %{?_smp_mflags}

# 'No rule to make target /usr/lib/libCGAL.so' on x86_64
%if 0
# tests
cd tests
cmake .
make %{?_smp_mflags}
cd -
%endif

%install
make install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/%{name}/fonts
%find_lang %{name}

rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/lgpl-2.1.txt
rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/README.markdown
rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/TODO

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0
# tests
cd tests
ctest %{?_smp_mflags} || : # let the tests fail, as they probably won't work in Koji
cd -
%endif

%files -f %{name}.lang
%doc COPYING
%doc README.md RELEASE_NOTES
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/appdata/*.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/color-schemes
%{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/libraries
%{_mandir}/man1/*

%files MCAD
%doc libraries/MCAD/lgpl-2.1.txt
%doc libraries/MCAD/README.markdown libraries/MCAD/TODO
%{_datadir}/%{name}/libraries/MCAD

%changelog
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

