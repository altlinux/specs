# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate ImageMagick-tools gcc-c++ libGL-devel libGLU-devel python-devel rpm-build-python
# END SourceDeps(oneline)
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: boost-filesystem-devel boost-program_options-devel cmake
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           openscad
Version:        2015.03.3
%global upversion 2015.03-3
Release:        alt1_12
Summary:        The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License:        GPLv2 with exceptions and CC0
Group:          Engineering
URL:            http://www.%{name}.org/
Source0:        http://files.%{name}.org/%{name}-%{upversion}.src.tar.gz
Patch0:         %{name}-polyclipping.patch
BuildRequires:  cgal libcgal-devel libcgal-qt5-devel
BuildRequires:  ImageMagick
BuildRequires:  xorg-xvfb xvfb-run
BuildRequires:  bison >= 2.4
BuildRequires:  boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3
BuildRequires:  flex >= 2.5.35
BuildRequires:  libfreetype-devel >= 2.4
BuildRequires:  fontconfig-devel >= 2.10
BuildRequires:  gettext gettext-tools
BuildRequires:  libGLEW-devel >= 1.6
BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  libgmp-devel libgmpxx-devel
BuildRequires:  libharfbuzz-devel libharfbuzz-utils
BuildRequires:  xorg-dri-nouveau xorg-dri-radeon
BuildRequires:  libmpfr-devel >= 3.0.0
BuildRequires:  opencsg-devel >= 1.3.2
BuildRequires:  libpolyclipping-devel >= 6.1.3
BuildRequires:  procps sysvinit-utils
BuildRequires:  python
BuildRequires:  libqt4-declarative libqt4-devel qt4-designer
BuildRequires:  libqscintilla2-qt4-devel
Requires:       font(liberationmono)
Requires:       font(liberationsans)
Requires:       font(liberationserif)
Requires:     %{name}-MCAD = %{version}-%{release}
Source44: import.info
Patch33: openscad-2015.03.2-alt-qscintilla.patch

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
Requires:       %{name} = %{version}-%{release}
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
%patch33 -p2

%build
%{qmake_qt4} PREFIX=%{_prefix}
%make_build

# tests
cd tests
cmake .
%make_build
cd -

%install
make install INSTALL_ROOT=%{buildroot}
rm -rf %{buildroot}%{_datadir}/%{name}/fonts
%find_lang %{name}

rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/lgpl-2.1.txt
rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/README.markdown
rm %{buildroot}%{_datadir}/%{name}/libraries/MCAD/TODO

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# tests
cd tests
ctest %{?_smp_mflags} || : # let the tests fail, as they probably won't work in Koji
cd -

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

