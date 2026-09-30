%define _lto_cflags %nil

%define foam_major 14
%define foam_patch 20260724
%define foam_dir OpenFOAM-%foam_major
%define foam_root %_libdir/openfoam
%define foam_platform linux64GccDPInt32Opt
%define foam_platform_dir %foam_root/%foam_dir/platforms/%foam_platform
%define foam_libdir %foam_platform_dir/lib

%define foam_optflags -pipe -frecord-gcc-switches -Wall -g -O2

# OpenFOAM uses a private library tree and intentionally links many modules
# with --no-as-needed.
%set_verify_elf_method unresolved=relaxed

%add_findprov_lib_path %foam_libdir
%add_findprov_lib_path %foam_libdir/openmpi-system

# lib.req treats OpenFOAM's intentional overlinking as a fatal error.
# External runtime dependencies for these ELF files are therefore declared
# explicitly below.
%add_findreq_skiplist %foam_platform_dir/bin/*
%add_findreq_skiplist %foam_libdir/*.so*
%add_findreq_skiplist %foam_libdir/openmpi-system/*.so*

%def_with check

Name: openfoam
Version: 20260724
Release: alt1

Summary: Open source computational fluid dynamics (CFD) toolbox
License: GPL-3.0-or-later
Group: Sciences/Physics
URL: https://openfoam.org/
VCS: https://github.com/OpenFOAM/OpenFOAM-14.git

Source: %name-%version.tar
Patch0: openfoam-14-wmakeLnInclude-no-dev-fd.patch
Patch1: openfoam-14-fix-bash-completion-detection.patch

# Initial ALT build is validated on x86_64.  aarch64 needs a separate
# foam_platform value and should be enabled after an independent build test.
ExclusiveArch: x86_64

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake
BuildRequires: flex
BuildRequires: binutils-devel
BuildRequires: libreadline-devel
BuildRequires: zlib-devel
BuildRequires: libXt-devel
BuildRequires: openmpi-devel
BuildRequires: patchelf

Requires: %name-solvers = %EVR
Requires: %name-libs-core = %EVR
Requires: %name-libs-models = %EVR
Requires: %name-libs-extra = %EVR
Requires: gnuplot

%description
OpenFOAM is a free, open source computational fluid dynamics (CFD)
software package. It provides solvers and utilities for fluid flow,
heat transfer, turbulence, multiphase flows, reacting flows, mesh
generation, pre-processing and post-processing.

This package contains OpenFOAM version 14 built against the system
OpenMPI implementation. The initial ALT Linux package disables Scotch,
Zoltan, METIS/ParMETIS and ParaView reader modules.


%package libs-core
Summary: Core shared libraries for OpenFOAM
Group: System/Libraries
Requires: openmpi
Requires: zlib
Requires: libstdc++6

%description libs-core
Core shared libraries used by OpenFOAM applications and solvers.


%package libs-models
Summary: Physical modelling libraries for OpenFOAM
Group: System/Libraries
Requires: %name-libs-core = %EVR

%description libs-models
Physical, thermophysical, multiphase and Lagrangian modelling
libraries for OpenFOAM.


%package libs-extra
Summary: Additional shared libraries for OpenFOAM
Group: System/Libraries
Requires: %name-libs-core = %EVR
Requires: %name-libs-models = %EVR

%description libs-extra
Additional OpenFOAM shared libraries and solver support modules.


%package solvers
Summary: OpenFOAM solvers and utilities
Group: Engineering
Requires: %name-libs-core = %EVR
Requires: %name-libs-models = %EVR
Requires: %name-libs-extra = %EVR

%description solvers
Compiled OpenFOAM solvers and command-line utilities.


%package devel
Summary: Development files for OpenFOAM
Group: Development/C++
Requires: %name = %EVR
Requires: gcc-c++
Requires: make

%description devel
OpenFOAM sources, headers, tests and wmake infrastructure required
to build custom OpenFOAM applications and libraries.


%package tutorials
Summary: Tutorial cases for OpenFOAM
Group: Engineering
Requires: %name = %EVR

%description tutorials
Tutorial cases supplied with OpenFOAM.


%package doc
Summary: Documentation for OpenFOAM
Group: Documentation

%description doc
Documentation supplied with OpenFOAM.


%prep
%setup -T -c -n %foam_dir
tar -xf %SOURCE0 --strip-components=1

%autopatch -p1

# ALT Linux build defaults.  Keep downstream configuration in prefs.sh
# rather than modifying upstream etc/bashrc.
cat > etc/prefs.sh <<'EOF'
# ALT Linux defaults
export SCOTCH_TYPE=none
export METIS_TYPE=none
export PARMETIS_TYPE=none
export ZOLTAN_TYPE=none
export ParaView_TYPE=none

# System OpenMPI
export PATH=%_libdir/openmpi/bin:$PATH
EOF

# Do not inherit ALT LTO flags into OpenFOAM's wmake optimisation rules.
find wmake/rules -type f -path '*Gcc*' -name cOpt \
    -exec sed -i 's|^cOPT[[:space:]]*=.*|cOPT = %foam_optflags|' {} +

find wmake/rules -type f -path '*Gcc*' -name 'c++Opt' \
    -exec sed -i 's|^c++OPT[[:space:]]*=.*|c++OPT = %foam_optflags|' {} +


%build
. ./etc/bashrc

export WM_NCOMPPROCS="${NPROCS:-14}"
./Allwmake -q -j"$WM_NCOMPPROCS"


%install
dest=%buildroot%foam_root/%foam_dir
install -d "$dest"

# Install architecture-independent OpenFOAM tree.  The generated platform
# directory is handled separately below.  VCS metadata and files installed
# through %%doc/%%license are intentionally not copied here.
find . -mindepth 1 -maxdepth 1 \
    ! -name platforms \
    ! -name .gitattributes \
    ! -name COPYING \
    ! -name README.org \
    -exec cp -a -t "$dest" -- {} +

# Install only final platform binaries and libraries.  Do not package
# wmake object/dependency trees.
install -d "$dest/platforms"

for platform in platforms/*; do
    [ -d "$platform" ] || continue

    install -d "$dest/$platform"

    [ ! -d "$platform/bin" ] || \
        cp -a "$platform/bin" "$dest/$platform/"

    [ ! -d "$platform/lib" ] || \
        cp -a "$platform/lib" "$dest/$platform/"
done

foam_platform_dir="$dest/platforms/%foam_platform"

# OpenFOAM executables use private libraries.
find "$foam_platform_dir/bin" -type f \
    -exec patchelf --set-rpath \
    '$ORIGIN/../lib:$ORIGIN/../lib/openmpi-system' {} \;

# Main OpenFOAM libraries.
find "$foam_platform_dir/lib" -maxdepth 1 \
    -type f -name '*.so*' \
    -exec patchelf --set-rpath \
    '$ORIGIN:$ORIGIN/openmpi-system' {} \;

# MPI-specific OpenFOAM libraries also need the system OpenMPI library path.
if [ -d "$foam_platform_dir/lib/openmpi-system" ]; then
    find "$foam_platform_dir/lib/openmpi-system" \
        -type f -name '*.so*' \
        -exec patchelf --set-rpath \
        '$ORIGIN/..:$ORIGIN:%_libdir/openmpi/lib' {} \;
fi

install -d %buildroot%_bindir

cat > %buildroot%_bindir/openfoam14 <<'EOF'
#!/bin/bash
. %foam_root/%foam_dir/etc/bashrc

if [ "$#" -eq 0 ]; then
    exec /bin/bash --noprofile --norc -i
fi

exec "$@"
EOF

chmod 0755 %buildroot%_bindir/openfoam14


%check
# Test the installed tree, including the RUNPATHs written in %%install.
. %buildroot%foam_root/%foam_dir/etc/bashrc

test -x "$FOAM_APPBIN/foamRun"
test -x "$FOAM_APPBIN/blockMesh"
test -f "$FOAM_LIBBIN/libOpenFOAM.so"

"$FOAM_APPBIN/foamRun" -help >/dev/null
"$FOAM_APPBIN/blockMesh" -help >/dev/null


%files
%_bindir/openfoam14

%dir %foam_root
%dir %foam_root/%foam_dir
%dir %foam_root/%foam_dir/platforms
%dir %foam_platform_dir

%foam_root/%foam_dir/bin
%foam_root/%foam_dir/etc
%doc README.org COPYING


%files libs-core
%dir %foam_root
%dir %foam_root/%foam_dir
%dir %foam_root/%foam_dir/platforms
%dir %foam_platform_dir
%dir %foam_libdir

%foam_libdir/libOpenFOAM.so
%foam_libdir/libfiniteVolume.so
%foam_libdir/libmeshTools.so
%foam_libdir/libpolyTopoChange.so
%foam_libdir/libsurfMesh.so
%foam_libdir/libfvModels.so
%foam_libdir/libfvConstraints.so
%foam_libdir/libfvMotionSolvers.so
%foam_libdir/libsampling.so
%foam_libdir/libsnappyHexMesh.so
%foam_libdir/libpointMeshMovers.so
%foam_libdir/libmeshToMeshTopoChanger.so

%foam_libdir/openmpi-system
%foam_libdir/dummy


%files libs-models
%dir %foam_root
%dir %foam_root/%foam_dir
%dir %foam_root/%foam_dir/platforms
%dir %foam_platform_dir
%dir %foam_libdir

%foam_libdir/libphaseSystem.so
%foam_libdir/libfieldFunctionObjects.so
%foam_libdir/liblagrangianParcel.so
%foam_libdir/libLagrangianCloud.so
%foam_libdir/libLagrangian.so
%foam_libdir/libLagrangianThermo.so
%foam_libdir/libLagrangianCloudFunctionObjects.so

%foam_libdir/libmulticomponentThermophysicalModels.so
%foam_libdir/libfluidThermophysicalModels.so
%foam_libdir/libthermophysicalProperties.so
%foam_libdir/libsolidThermo.so
%foam_libdir/libchemistryModel.so
%foam_libdir/libreactionModels.so
%foam_libdir/libradiationModels.so

%foam_libdir/libmomentumTransportModels.so
%foam_libdir/libincompressibleMomentumTransportModels.so
%foam_libdir/libphaseCompressibleMomentumTransportModels.so
%foam_libdir/libphaseIncompressibleMomentumTransportModels.so

%foam_libdir/libmultiphaseEulerFvModels.so
%foam_libdir/libmultiphaseEulerMomentumTransportModels.so
%foam_libdir/libpopulationBalance.so
%foam_libdir/libXiFluidSolver.so

%foam_libdir/libwaves.so
%foam_libdir/libatmosphericModels.so


%files libs-extra
%dir %foam_root
%dir %foam_root/%foam_dir
%dir %foam_root/%foam_dir/platforms
%dir %foam_platform_dir
%dir %foam_libdir

%exclude %foam_libdir/libOpenFOAM.so
%exclude %foam_libdir/libfiniteVolume.so
%exclude %foam_libdir/libmeshTools.so
%exclude %foam_libdir/libpolyTopoChange.so
%exclude %foam_libdir/libsurfMesh.so
%exclude %foam_libdir/libfvModels.so
%exclude %foam_libdir/libfvConstraints.so
%exclude %foam_libdir/libfvMotionSolvers.so
%exclude %foam_libdir/libsampling.so
%exclude %foam_libdir/libsnappyHexMesh.so
%exclude %foam_libdir/libpointMeshMovers.so
%exclude %foam_libdir/libmeshToMeshTopoChanger.so

%exclude %foam_libdir/libphaseSystem.so
%exclude %foam_libdir/libfieldFunctionObjects.so
%exclude %foam_libdir/liblagrangianParcel.so
%exclude %foam_libdir/libLagrangianCloud.so
%exclude %foam_libdir/libLagrangian.so
%exclude %foam_libdir/libLagrangianThermo.so
%exclude %foam_libdir/libLagrangianCloudFunctionObjects.so

%exclude %foam_libdir/libmulticomponentThermophysicalModels.so
%exclude %foam_libdir/libfluidThermophysicalModels.so
%exclude %foam_libdir/libthermophysicalProperties.so
%exclude %foam_libdir/libsolidThermo.so
%exclude %foam_libdir/libchemistryModel.so
%exclude %foam_libdir/libreactionModels.so
%exclude %foam_libdir/libradiationModels.so

%exclude %foam_libdir/libmomentumTransportModels.so
%exclude %foam_libdir/libincompressibleMomentumTransportModels.so
%exclude %foam_libdir/libphaseCompressibleMomentumTransportModels.so
%exclude %foam_libdir/libphaseIncompressibleMomentumTransportModels.so

%exclude %foam_libdir/libmultiphaseEulerFvModels.so
%exclude %foam_libdir/libmultiphaseEulerMomentumTransportModels.so
%exclude %foam_libdir/libpopulationBalance.so
%exclude %foam_libdir/libXiFluidSolver.so

%exclude %foam_libdir/libwaves.so
%exclude %foam_libdir/libatmosphericModels.so

%foam_libdir/*.so*


%files solvers
%dir %foam_root
%dir %foam_root/%foam_dir
%dir %foam_root/%foam_dir/platforms
%dir %foam_platform_dir
%foam_platform_dir/bin


%files devel
%dir %foam_root
%dir %foam_root/%foam_dir
%foam_root/%foam_dir/Allwmake
%foam_root/%foam_dir/applications
%foam_root/%foam_dir/src
%foam_root/%foam_dir/test
%foam_root/%foam_dir/wmake


%files tutorials
%dir %foam_root
%dir %foam_root/%foam_dir
%foam_root/%foam_dir/tutorials


%files doc
%dir %foam_root
%dir %foam_root/%foam_dir
%foam_root/%foam_dir/doc


%changelog
* Tue Sep 29 2026 Timofei Fedotov <sovtouch@altlinux.org> 20260724-alt1
- Initial build for ALT Sisyphus. (Closes: #30575)
