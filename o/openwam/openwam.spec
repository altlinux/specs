Name:    openwam
Version: 2.2
Release: alt2.git25f46f2

Summary: The Open Source 1D Gas-Dynamic Code 
License: GPL-3.0+
Group: Sciences/Physics
URL: http://openwam.webs.upv.es/docs/ 
# VCS: https://github.com/CMT-UPV/OpenWAM

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: OpenWAM-%version.tar
Patch: upstream-fixes-%version.patch
Patch2000: %name-e2k.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libgomp-devel

ExclusiveArch: %ix86 x86_64 %e2k

%description
OpenWAM is a free open source tool for gas dynamics modelling, mainly developed
for Internal Combustion Engines.

%prep
%setup -n OpenWAM-%version
%patch -p1
%ifarch %e2k
%patch2000 -p1
%endif

%build
%add_optflags -Wno-error=return-type
%cmake \
    -DBUILD_DOCUMENTATION=ON \
    -DBUILD_PARALLEL=ON
%cmake_build

%install
pushd %_cmake__builddir
install -Dpm0755 Source/OpenWAM %buildroot%_bindir/OpenWAM
mkdir -p %buildroot%_defaultdocdir/%name
cp -a doc/html/* %buildroot%_defaultdocdir/%name

%files
%_bindir/OpenWAM
%doc %_defaultdocdir/%name

%changelog
* Wed Jul 28 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.2-alt2.git25f46f2
- Added patch for Elbrus.

* Mon Jun 21 2021 Andrey Cherepanov <cas@altlinux.org> 2.2-alt1.git25f46f2
- Inital build in Sisyphus.
