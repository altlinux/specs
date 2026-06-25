#
# Upstream provide static library.
# See https://www.altlinux.org/LTO
#
%define optflags_lto %nil

%global spooles_cc gcc -std=c90 -D_DEFAULT_SOURCE %optflags

%global descr SPOOLES is a library for solving sparse real and complex linear systems\
of equations, written in the C language using object oriented design.

Name: spooles
Version: 2.2
Release: alt12

Summary: A sparse matrix library
License: ALT-Public-Domain
Group: System/Libraries
Url: http://www.netlib.org/linalg/spooles/

# http://www.netlib.org/linalg/spooles/spooles.2.2.tgz
Source: %name-%version.tar

%description
%descr

%package -n lib%name-devel-static
Summary: %summary
Group: Development/C

%description -n lib%name-devel-static
%descr

%prep
%setup

%build
%make_build CC="%spooles_cc" lib
%make_build CC="%spooles_cc" -C MT/src

%install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
for f in $(find -name '*.h');
do
	install -Dt "%buildroot%_includedir/$(dirname "$f")" "$f";
done
install -Dpm 0644 spooles.a %buildroot%_libdir/spooles.a
install -Dpm 0644 MT/src/spoolesMT.a %buildroot%_libdir/spoolesMT.a

%files -n lib%name-devel-static
%_includedir/A2.h
%_includedir/A2
%_includedir/BKL.h
%_includedir/BKL
%_includedir/BPG.h
%_includedir/BPG
%_includedir/Chv.h
%_includedir/Chv
%_includedir/ChvList.h
%_includedir/ChvList
%_includedir/ChvManager.h
%_includedir/ChvManager
%_includedir/Coords.h
%_includedir/Coords
%_includedir/DSTree.h
%_includedir/DSTree
%_includedir/DV.h
%_includedir/DV
%_includedir/DenseMtx.h
%_includedir/DenseMtx
%_includedir/Drand.h
%_includedir/Drand
%_includedir/EGraph.h
%_includedir/EGraph
%_includedir/ETree.h
%_includedir/ETree
%_includedir/Eigen
%_includedir/FrontMtx.h
%_includedir/FrontMtx
%_includedir/GPart.h
%_includedir/GPart
%_includedir/Graph.h
%_includedir/Graph
%_includedir/I2Ohash.h
%_includedir/I2Ohash
%_includedir/IIheap.h
%_includedir/IIheap
%_includedir/ILUMtx.h
%_includedir/ILUMtx
%_includedir/IV.h
%_includedir/IV
%_includedir/IVL.h
%_includedir/IVL
%_includedir/Ideq.h
%_includedir/Ideq
%_includedir/InpMtx.h
%_includedir/InpMtx
%_includedir/Iter
%_includedir/LinSol
%_includedir/Lock.h
%_includedir/Lock
%_includedir/MPI.h
%_includedir/MPI
%_includedir/MSMD.h
%_includedir/MSMD
%_includedir/MT.h
%_includedir/MT
%_includedir/Network.h
%_includedir/Network
%_includedir/PatchAndGoInfo.h
%_includedir/PatchAndGoInfo
%_includedir/Pencil.h
%_includedir/Pencil
%_includedir/Perm.h
%_includedir/Perm
%_includedir/SPOOLES.h
%_includedir/SemiImplMtx
%_includedir/SolveMap.h
%_includedir/SolveMap
%_includedir/SubMtx.h
%_includedir/SubMtx
%_includedir/SubMtxList.h
%_includedir/SubMtxList
%_includedir/SubMtxManager.h
%_includedir/SubMtxManager
%_includedir/SymbFac.h
%_includedir/SymbFac
%_includedir/Tree.h
%_includedir/Tree
%_includedir/Utilities.h
%_includedir/Utilities
%_includedir/ZV.h
%_includedir/ZV
%_includedir/cfiles.h
%_includedir/misc.h
%_includedir/misc
%_includedir/timings.h
%_libdir/spooles.a
%_libdir/spoolesMT.a

%changelog
* Thu Jun 04 2026 Ulysses Apokin <ulysses@altlinux.org> 2.2-alt12
- Return the package to Sisyphus for FreeCAD FEM Workbench.
