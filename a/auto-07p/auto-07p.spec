%define _unpackaged_files_terminate_build 1
%define auto_dir %_prefix/lib/auto-07p
%def_with openmpi
%def_without coin3d

Summary: software for continuation and bifurcation problems in ODE
Name: auto-07p
Version: 0.9.3

Release: alt0.4
Packager: Igor Vlasenko <viy@altlinux.org>
License: GPLv2+
Group: Sciences/Mathematics
Url: https://www.macs.hw.ac.uk/~gabriel/auto07/auto.html
VCS: https://github.com/auto-07p/auto-07p.git
Source: %{name}-%{version}.tar
Source1: auto16.png
Source2: auto32.png
Source3: auto48.png
#https://packages.debian.org/ru/sid/auto-07p
# debian man page
Source4: %{name}.1

Patch0: auto-07p-0.93-alt-cleanup.patch

# debian patches for 0.92: we do not need them
#Patch01: 01_auto.patch replaced by auto-07p-0.93-alt-cleanup.patch
#Patch02: 02_env.patch - no need; env should br sourced, not run
#Patch03: 03_drop_tek.patch # not applicable to 0.93
#Patch04: 04_fix_bashisms.patch # applied in upstream
#Patch05: 05_python3.patch # not general enough; see sed in %%prep

# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ gcc-fortran imake libICE-devel libSM-devel libX11-devel libXt-devel xorg-cf-files
# END SourceDeps(oneline)

# doc
BuildRequires: texlive-dist transfig

# ModuleNotFoundError: No module named 'tkSimpleDialog'
# main script is cross python2/python3. it use try - catch to define python2 names like
# import tkSimpleDialog as tkinter.simpledialog.
# however, subscripts will have name dependencies on python2's Tkinter
AutoReqProv: yes,nopython,nopython3
%add_python3_lib_path %auto_dir/python
BuildRequires: rpm-build-python3 python3-modules-tkinter python3-module-matplotlib
Requires: python3-modules-tkinter python3-module-matplotlib

%if_with coin3d
BuildRequires: pkgconfig(Coin)
# missing -lSoXt (libsoxt-devel) in alt
BuildRequires: libsoxt-devel libopenmotif-devel
BuildRequires: libsoqt-devel pkgconfig(Qt5Core) pkgconfig(Qt5Gui) pkgconfig(Qt5OpenGL)
%else
# hide: conflicts with Coin 3d
BuildRequires: libInventor-devel libInventorXt-devel
%endif
%if 0
# just for buildreq-src to ignore Qt4
BuildRequires: pkgconfig(QtCore) pkgconfig(QtGui) pkgconfig(QtOpenGL)
%endif
%if_with openmpi
BuildRequires: openmpi-devel
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: openmpi
%endif


%description
AUTO can do a limited bifurcation analysis of algebraic systems
of the form
  f(u,p) = 0,  f,u in Rn
and of systems of ordinary differential equations of the form
  u'(t) = f(u(t),p),  f,u in Rn
subject to initial conditions, boundary conditions, and integral
constraints. Here p denotes one or more parameters. AUTO can also
do certain continuation and evolution computations for parabolic
PDEs.  It also includes the software HOMCONT for the bifurcation
analysis of homoclinic orbits. AUTO is quite fast and can benefit
from multiple processors; therefore it is applicable to rather
large systems of differential equations.

%package devel
Summary: development files for the software package AUTO
Group: Development/C++

%description devel
development files for the software package AUTO

%package auto97
Summary: auto97 GUI to the software package AUTO
Group: Sciences/Mathematics

%description auto97
This is auto97 GUI to the software package AUTO.

%package plaut04
Summary: plaut04 data visualizer to the software package AUTO
Group: Sciences/Mathematics

%description plaut04
This is plaut04 data visualizer to the software package AUTO.

%package doc
Summary: documentation to the software package AUTO
Group: Documentation
BuildArch: noarch

%description doc
Title: AUTO-07P: CONTINUATION AND BIFURCATION SOFTWARE
 FOR ORDINARY DIFFERENTIAL EQUATIONS
Author: Eusebius J. Doedel and Bart E. Oldeman
 Concordia University, Montreal, Canada
Abstract: This is a guide to the software package AUTO for
 continuation and bifurcation problems in ordinary
 differential equations.

%package demos
Summary: demos to the software package AUTO
Group: Documentation
AutoReqProv: yes,nopython,nopython3
BuildArch: noarch

%description demos
Those are demo files to the software package AUTO.

%package tests
Summary: tests  to the software package AUTO
Group: Documentation
AutoReqProv: yes,nopython,nopython3
BuildArch: noarch

%description tests
This is test suite to the software package AUTO.
Note that the test results should be checked manually.

%prep
%setup -q
%patch0 -p1

sed -i -e 's,@AUTO_DIR@,%auto_dir,g' bin/auto bin/autox

%if_with python2
sed -i -e 's,^#! */usr/bin/env *python,#!/usr/bin/env python2,' `grep -rl '^#! */usr/bin/env *python$'`
%else
sed -i -e 's,^#! */usr/bin/env *python,#!/usr/bin/env python3,' `grep -rl '^#! */usr/bin/env *python$'`
%endif

# we rename auto -> %name
sed -i -e 's,^#! */usr/bin/env *auto,#!/usr/bin/env %{name},' `grep -rl '^#! */usr/bin/env *auto$'`

%add_optflags %optflags_shared
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%{?optflags_lto:%add_optflags %optflags_lto}
%build
%if_with openmpi
. %_libdir/openmpi/bin/mpivars.sh
%endif
#export DEB_CFLAGS_MAINT_APPEND = -fPIC
#export DEB_FFLAGS_MAINT_APPEND = -fPIC -std=legacy
export FFLAGS="$FFLAGS -std=legacy"
echo FFLAGS="<$FFLAGS>"
%configure \
    --enable-plaut \
    --enable-plaut04 \
    --enable-plaut04-qt \
    --enable-gui \
%if_with openmpi
    --with-mpi \
    --with-mpi-lib=%_libdir/openmpi/lib/ \
    --with-mpi-include=%_libdir/openmpi/include/ \
%endif
    --with-optimization-flags="$FFLAGS"

%make_build

# compile manual
make -C doc auto.pdf ../plaut04/doc/userguide.pdf
# compile tutorial.ps
pushd doc
./\@tut || echo no ghostscript -- so be it
popd

%install
install -m 644 -D bin/auto %buildroot%_bindir/auto-07p
install -m 644 -D bin/autox %buildroot%_bindir/autox

mkdir -p %buildroot%_includedir
install -m 644 -D include/auto*.h %buildroot%_includedir
install -m 644 -D include/config.h \
	%buildroot%_includedir/auto-07p_config.h
sed -i 's/"config\.h"/<auto-07p_config.h>/' %buildroot%_includedir/auto_f2c.h

mkdir -p %buildroot%auto_dir/python/auto/graphics/
install -m 644 -D python/auto/*.py \
	%buildroot%auto_dir/python/auto/
install -m 644 -D python/auto/graphics/*.py \
	%buildroot%auto_dir/python/auto/graphics/

chmod +x %buildroot%auto_dir/python/auto/interactiveBindings.py
cp -av cmds %buildroot%auto_dir/
rm -f %buildroot%auto_dir/cmds/*.in
cp -av lib %buildroot%auto_dir/

# do we need to install .autorc ?
install -m 644 autorc .autorc %buildroot%auto_dir/

# /bin ->
#### wrappers: to /usr/bin
# auto
# autox
#### gui
# auto97
# plaut04
#### plaut: to AUTO_DIR/bin
# plaut
#### utils: to AUTO_DIR/bin
# autlab
# deletelp
# double
# keepbp
# keeplp
# keepsp
# keepuz
# listlabels
# reduce
# relabel
# triple
cp -av bin %buildroot%auto_dir/
rm -f %buildroot%auto_dir/bin/auto{,x}

cp -av gui %buildroot%auto_dir/
rm -f %buildroot%auto_dir/gui/*.in
rm -f %buildroot%auto_dir/gui/*.c

install -m 644 -D plaut04/doc/userguide.pdf %buildroot%auto_dir/plaut04/doc/userguide.pdf
cp -av plaut04/includes plaut04/widgets plaut04/plaut04.rc %buildroot%auto_dir/plaut04/


cp -av demos %buildroot%auto_dir/
cp -av test %buildroot%auto_dir/

sed -i 's,$HOME/auto/07p,%auto_dir,g' %buildroot%auto_dir/cmds/auto.env*

%if_disabled plaut
rm -f %buildroot%auto_dir/python/auto/graphics/pyplaut.py
%endif
%if_disabled tek
rm -f %buildroot%auto_dir/cmds/@ps %buildroot%auto_dir/cmds/@eps
%endif

# installing debian man pages
install -D -m644 %{SOURCE4} %buildroot%_man1dir/%name.1

# install pixmaps
install -D -m644 %{SOURCE1} %buildroot%_miconsdir/%name.png
install -D -m644 %{SOURCE2} %buildroot%_niconsdir/%name.png
install -D -m644 %{SOURCE3} %buildroot%_liconsdir/%name.png

# install desktop
mkdir -p %buildroot%_desktopdir/

# autox ?
for cmd in auto97 plaut04; do
    cat > %buildroot%_bindir/%{name}-${cmd}.sh <<EOF
#!/bin/sh
. %auto_dir/cmds/auto.env.sh
exec %auto_dir/bin/${cmd}
EOF
    cat > %buildroot%_desktopdir/%name-${cmd}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%name - $cmd
Comment=AUTO -- software for continuation and bifurcation problems in ODE
Comment[ru]=Инструмент для решения уравнений высшей математики.
Comment[uk]=Інструмент для розв'язку рівнянь вищої математики.
Icon=%name
Exec=%{name}-${cmd}.sh
Terminal=false
Categories=Science;Math;
EOF
done

#exit 1

%files
%doc README CHANGELOG
%_bindir/%name
%_bindir/autox
%dir %auto_dir
%auto_dir/python
%auto_dir/cmds
%auto_dir/lib
%dir %auto_dir/bin
%auto_dir/bin/plaut
%auto_dir/bin/autlab
%auto_dir/bin/deletelp
%auto_dir/bin/double
%auto_dir/bin/keepbp
%auto_dir/bin/keeplp
%auto_dir/bin/keepsp
%auto_dir/bin/keepuz
%auto_dir/bin/listlabels
%auto_dir/bin/reduce
%auto_dir/bin/relabel
%auto_dir/bin/triple
%auto_dir/autorc
%auto_dir/.autorc
%_man1dir/auto-07p.1*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
#exclude %auto_dir/demos
#exclude %auto_dir/test
#exclude %auto_dir/gui
#%exclude %auto_dir/bin/auto97
#exclude %auto_dir/plaut04
#exclude %auto_dir/bin/plaut04
#auto_dir/bin/auto97
#auto_dir/bin/plaut04
%if 0
%files devel
%endif
%_includedir/auto*.h

%files auto97
%_bindir/%name-auto97.sh
%_desktopdir/%{name}-auto97.desktop
%auto_dir/gui
%auto_dir/bin/auto97

%files plaut04
%_bindir/%name-plaut04.sh
%_desktopdir/%{name}-plaut04.desktop
%auto_dir/plaut04
%auto_dir/bin/plaut04

%files doc
%doc doc/auto.pdf
%doc doc/tutorial.ps
%doc plaut/plaut.ps

%files demos
%auto_dir/demos

%files tests
%auto_dir/test


%changelog
* Thu Nov 02 2023 Igor Vlasenko <viy@altlinux.org> 0.9.3-alt0.4
- Sisyphus pre-release
- built with libInventorXt/Motif interface

* Wed Nov 01 2023 Igor Vlasenko <viy@altlinux.org> 0.9.3-alt0.1
- initial build

