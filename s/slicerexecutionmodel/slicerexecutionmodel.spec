%define _unpackaged_files_terminate_build 1

Name: slicerexecutionmodel
Version: 2.0.0
Release: alt2.git.f19d6e8
Summary: An open-source CMake-based project that provides macros and associated tools for the easy building of 3D Slicer command line interface (CLI) modules
License: BSD-style
Group: Development/Tools
Url: https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel

ExcludeArch: %arm

# https://github.com/Slicer/SlicerExecutionModel.git
Source: %name-%version.tar

Patch1: slicerexecutionmodel-alt-install.patch

BuildRequires: gcc-c++ cmake
BuildRequires: libitk-devel
BuildRequires: jsoncpp-devel
BuildRequires: parameterserializer-devel
BuildRequires: libtclap-devel

%description
The SlicerExecutionModel is a CMake-based project providing macros
and associated tools allowing to easily build Slicer CLI (Command line module).

It is designed to improve the acceptance and productivity of Slicer application developers.
The Execution Model provides a simple mechanism for incorporating
command line programs as Slicer modules.
These command line modules are self-describing, emitting an XML description
of its command line arguments. Slicer uses this XML description
to construct a GUI for the module.

SlicerExecutionModel is documented here:

https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel.

%package -n lib%name
Summary: An open-source CMake-based project that provides macros and associated tools for the easy building of 3D Slicer command line interface (CLI) modules
Group: System/Libraries

%description -n lib%name
The SlicerExecutionModel is a CMake-based project providing macros
and associated tools allowing to easily build Slicer CLI (Command line module).

It is designed to improve the acceptance and productivity of Slicer application developers.
The Execution Model provides a simple mechanism for incorporating
command line programs as Slicer modules.
These command line modules are self-describing, emitting an XML description
of its command line arguments. Slicer uses this XML description
to construct a GUI for the module.

SlicerExecutionModel is documented here:

https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel.

This package contains SlicerExecutionModel shared libraries.

%package devel
Summary: An open-source CMake-based project that provides macros and associated tools for the easy building of 3D Slicer command line interface (CLI) modules
Group: Development/C++
Requires: lib%name = %EVR
Requires: parameterserializer-devel
Requires: libtclap-devel

%description devel
The SlicerExecutionModel is a CMake-based project providing macros
and associated tools allowing to easily build Slicer CLI (Command line module).

It is designed to improve the acceptance and productivity of Slicer application developers.
The Execution Model provides a simple mechanism for incorporating
command line programs as Slicer modules.
These command line modules are self-describing, emitting an XML description
of its command line arguments. Slicer uses this XML description
to construct a GUI for the module.

SlicerExecutionModel is documented here:

https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel.

This package contains development files for SlicerExecutionModel.

%prep
%setup
%patch1 -p1

# ensure bundled tclap is not used
rm -rf tclap

%build
%cmake \
	-DSlicerExecutionModel_USE_UTF8:BOOL=ON \
	-DSlicerExecutionModel_USE_JSONCPP:BOOL=ON \
	-DSlicerExecutionModel_USE_SERIALIZER:BOOL=ON \
	-DSlicerExecutionModel_INSTALL_LIB_DIR:STRING=%_lib \
	-DSlicerExecutionModel_INSTALL_NO_DEVELOPMENT:BOOL=OFF \
	-DGenerateCLP_USE_JSONCPP:BOOL=ON \
	-DGenerateCLP_USE_SERIALIZER:BOOL=ON \
	-DGenerateCLP_INSTALL_NO_DEVELOPMENT:BOOL=OFF \
	-DModuleDescriptionParser_USE_SERIALIZER:BOOL=ON \
	-DModuleDescriptionParser_INSTALL_NO_DEVELOPMENT:BOOL=OFF \
	-DModuleDescriptionParser_LIBRARY_PROPERTIES='VERSION;0;SOVERSION;0' \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files -n lib%name
%doc License.txt NOTICE
%doc README.md
%_libdir/*.so.*

%files devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*

%changelog
* Mon Jun 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt2.git.f19d6e8
- Rebuilt with system tclap.

* Fri May 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1.git.f19d6e8
- Initial build for ALT.
