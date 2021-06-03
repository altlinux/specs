%define _unpackaged_files_terminate_build 1

Name: parameterserializer
Version: 0
Release: alt1.git.3b40b7f
Summary: An open-source library for serialization and deserialization of Insight Segmentation and Registration Toolkit (ITK) classes
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/Slicer/ParameterSerializer

ExcludeArch: %arm

# https://github.com/Slicer/ParameterSerializer.git
Source: %name-%version.tar

Patch1: parameterserializer-alt-build.patch

BuildRequires: gcc-c++ cmake
BuildRequires: libitk-devel
BuildRequires: jsoncpp-devel

%description
Serialization is an important technique when exploring
an analysis parameter solution space and performing reproducible research.

This is a set of classes to perform serialization and deserialization
of the parameters of ITK classes, i.e., classes that inherit from itk::LightObject.
Serialization does not require code instrumentation of the target classes.
The parameters of the target class are serialized with an archiver;
the only currently implemented archiver writes and reads JSON files
with the JsonCpp library.

The project is currently used by TubeTK and the SlicerExecutionModel.

The development of this project is supported by TubeTK.

%package -n lib%name
Summary: An open-source library for serialization and deserialization of Insight Segmentation and Registration Toolkit (ITK) classes
Group: System/Libraries

%description -n lib%name
Serialization is an important technique when exploring
an analysis parameter solution space and performing reproducible research.

This is a set of classes to perform serialization and deserialization
of the parameters of ITK classes, i.e., classes that inherit from itk::LightObject.
Serialization does not require code instrumentation of the target classes.
The parameters of the target class are serialized with an archiver;
the only currently implemented archiver writes and reads JSON files
with the JsonCpp library.

The project is currently used by TubeTK and the SlicerExecutionModel.

The development of this project is supported by TubeTK.

This package contains ParameterSerializer shared libraries.

%package devel
Summary: An open-source library for serialization and deserialization of Insight Segmentation and Registration Toolkit (ITK) classes
Group: Development/C++
Requires: lib%name = %EVR

%description devel
Serialization is an important technique when exploring
an analysis parameter solution space and performing reproducible research.

This is a set of classes to perform serialization and deserialization
of the parameters of ITK classes, i.e., classes that inherit from itk::LightObject.
Serialization does not require code instrumentation of the target classes.
The parameters of the target class are serialized with an archiver;
the only currently implemented archiver writes and reads JSON files
with the JsonCpp library.

The project is currently used by TubeTK and the SlicerExecutionModel.

The development of this project is supported by TubeTK.

This package contains development files for ParameterSerializer.

%prep
%setup
%patch1 -p1

%build
%cmake \
	-DBUILD_TESTING:BOOL=OFF \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files -n lib%name
%doc LICENSE
%doc README.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*

%changelog
* Fri May 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0-alt1.git.3b40b7f
- Initial build for ALT.
