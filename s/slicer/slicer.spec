%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define slicerver 5.2
Name: slicer
Version: %slicerver.2
Release: alt1
Summary: Multi-platform, free open source software for visualization and image computing
License: BSD-like
Group: Sciences/Medicine
Url: https://www.slicer.org/

# Exlusion source: pythonqt, CTK
ExcludeArch: %arm

# https://github.com/Slicer/Slicer.git
Source: %name-%version.tar

# Downloaded from link specified in SuperBuild.cmake
Source1: %name-%version-jqPlot.tar

# Copied from CTK
Source2: FindPythonQt.cmake

Source3: slicer.desktop

Patch1: %name-alt-build.patch
Patch2: %name-alt-python3-compat.patch
Patch3: %name-upstream-wc-last-change-date-fix.patch
Patch4: %name-alt-itk-compat.patch
Patch5: %name-alt-vtk-9.1-compat.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires: python3-devel
BuildRequires: gcc-c++ cmake
BuildRequires: qt5-base-devel qt5-multimedia-devel qt5-script-devel qt5-svg-devel qt5-tools-devel-static qt5-xmlpatterns-devel qt5-x11extras-devel
BuildRequires: libpcre2-devel libbrotli-devel
%ifarch %qt5_qtwebengine_arches
BuildRequires: qt5-webengine-devel
%endif
BuildRequires: libitk-devel
BuildRequires: libvtk-devel
BuildRequires: CTK-devel
BuildRequires: teem-devel
BuildRequires: vtkaddon-devel
BuildRequires: slicerexecutionmodel-devel
BuildRequires: libcurl-devel
BuildRequires: libqrestapi-devel
BuildRequires: CTKAppLauncherLib-devel
BuildRequires: pythonqt-devel
BuildRequires: rapidjson-devel
BuildRequires: bzip2-devel
BuildRequires: libniftilib-devel liblpsolve-devel
BuildRequires: doxygen /usr/bin/dot

%add_python3_path %_libdir/Slicer-%slicerver

%add_python3_req_skip EditorLib
%add_python3_req_skip SegmentEditorEffects SegmentEditorEffects.AbstractScriptedSegmentEditorEffect SegmentEditorEffects.AbstractScriptedSegmentEditorLabelEffect
%add_python3_req_skip Slicer slicer slicer.ScriptedLoadableModule slicer.util
%add_python3_req_skip SimpleITK __main__ github github.GithubObject
%add_python3_req_skip vtk.util vtk.util.numpy_support

%description
What is 3D Slicer ?

Desktop software to solve advanced image computing challenges
with a focus on clinical and biomedical applications.

Development platform to quickly build and deploy custom solutions
for research and commercial products, using free, open source software.

Community of knowledgeable users and developers working together
to improve medical computing.

%package devel
Summary: Multi-platform, free open source software for visualization and image computing
Group: Development/C++
Requires: %name = %EVR
Requires: %name-qt5-designer-plugin = %EVR

%description devel
What is 3D Slicer ?

Desktop software to solve advanced image computing challenges
with a focus on clinical and biomedical applications.

Development platform to quickly build and deploy custom solutions
for research and commercial products, using free, open source software.

Community of knowledgeable users and developers working together
to improve medical computing.

This package contains development files for Slicer.

%package qt5-designer-plugin
Summary: Multi-platform, free open source software for visualization and image computing
Group: Development/C++

%description qt5-designer-plugin
What is 3D Slicer ?

Desktop software to solve advanced image computing challenges
with a focus on clinical and biomedical applications.

Development platform to quickly build and deploy custom solutions
for research and commercial products, using free, open source software.

Community of knowledgeable users and developers working together
to improve medical computing.

This package contains Slicer plugins for qt5 designer.

%prep
%setup -a1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

install %SOURCE2 ./CMake/

# change python shebangs to python3
find . -name '*.py' | xargs sed -i \
	-e '1s|^#!/usr/bin/env python$|#!/usr/bin/env python3|' \
	-e '1s|^#!/usr/bin/python$|#!/usr/bin/python3|' \
	%nil


%build
%add_optflags -D_FILE_OFFSET_BITS=64

jqplotdir="$(pwd)/jqPlot"

%cmake \
	-DSlicer_DEFAULT_RELEASE_TYPE:STRING=Stable \
	-DSlicer_VERSION:STRING=%slicerver \
	-DSlicer_VERSION_FULL:STRING=%version \
	-DSlicer_VTK_VERSION_MAJOR=9 \
	-DSlicer_SUPERBUILD:BOOL=OFF \
	-DSlicer_BUILD_I18N_SUPPORT:BOOL=ON \
	-DSlicer_INSTALL_DEVELOPMENT:BOOL=ON \
	-DSlicer_INSTALL_NO_DEVELOPMENT:BOOL=OFF \
	-DSlicer_WITH_LIBRARY_VERSION:BOOL=ON \
	-DBUILD_TESTING:BOOL=OFF \
	-DSlicer_USE_PYTHONQT:BOOL=ON \
	-DjqPlot_DIR:PATH="${jqplotdir}" \
	-DSlicer_USE_QtTesting:BOOL=OFF \
	-DSlicer_USE_SYSTEM_DCMTK:BOOL=ON \
	-DSlicer_USE_SYSTEM_CTK:BOOL=ON \
	-DSlicer_USE_SYSTEM_OpenSSL:BOOL=ON \
	-DSlicer_USE_SYSTEM_TBB:BOOL=ON \
	-DSlicer_USE_SYSTEM_python:BOOL=ON \
	-DSlicer_USE_SYSTEM_QT:BOOL=ON \
	-DSlicer_BUILD_WEBENGINE_SUPPORT:BOOL=%{?_qt5_qtwebengine_arches:ON}%{!?_not_qt5_qtwebengine_arches:OFF} \
	-DSlicer_USE_SYSTEM_ITK:BOOL=ON \
	-DSlicer_USE_SYSTEM_LibArchive:BOOL=ON \
	-DSlicerExecutionModel_DEFAULT_CLI_INSTALL_RUNTIME_DESTINATION:PATH=%_libdir/Slicer-%slicerver/cli-modules \
	-DSlicerExecutionModel_DEFAULT_CLI_INSTALL_LIBRARY_DESTINATION:PATH=%_libdir/Slicer-%slicerver/lib/Slicer-%slicerver/cli-modules \
	-DSlicer_STORE_SETTINGS_IN_APPLICATION_HOME_DIR:BOOL=OFF \
	%nil

%cmake_build

%install
%cmakeinstall_std

install -d %buildroot%_bindir
cat > %buildroot%_bindir/Slicer << END
#!/bin/sh
exec %_libdir/Slicer-%slicerver/Slicer "\$@"
END

chmod +x %buildroot%_bindir/Slicer

# install symlinks for library discovery: they are loaded dynamically, but they have dependencies on each other as well
# separate library is used for dynamic loading, symlink in generic directory is used for loading as dependency

install -d %buildroot%_libdir
find %buildroot%_libdir/Slicer-%slicerver -name '*.so*' | while read i ; do
	ln -sr $i %buildroot%_libdir/
done


# install desktop file and icon
install -d %buildroot%_desktopdir
install -m644 %SOURCE3 %buildroot%_desktopdir/

install -d %buildroot%_datadir/%name
install -m644 Resources/3DSlicer-DesktopIcon.png %buildroot%_datadir/%name/

# remove unpackaged files
find %buildroot%_libdir -name '*.a' -delete

# generated cmake files require a lot of fixing before they'd become useable
rm -rf %buildroot%_libdir/cmake
rm -rf %buildroot%_libdir/Slicer-%slicerver/lib/Slicer-%slicerver/cmake

# fix qt designer launch
ln -sr %buildroot%_bindir/designer-qt5 %buildroot%_libdir/Slicer-%slicerver/bin/designer-real

%files
%doc COPYRIGHT.txt License.txt
%doc README.txt CONTRIBUTING.md AUTHORS.md
%_bindir/Slicer
%_libdir/*.so
%_libdir/*.so.*
%dir %_libdir/Slicer-%slicerver
%_libdir/Slicer-%slicerver/Slicer
%_libdir/Slicer-%slicerver/bin
%_libdir/Slicer-%slicerver/cli-modules
%_libdir/Slicer-%slicerver/lib
%_libdir/Slicer-%slicerver/libexec
%_libdir/Slicer-%slicerver/share
%_qt5_plugindir/iconengines/*.so
%_qt5_plugindir/styles/*.so
%_datadir/MRMLCore
%_desktopdir/*.desktop
%dir %_datadir/%name
%_datadir/%name/3DSlicer-DesktopIcon.png

%files devel
%_includedir/*

%files qt5-designer-plugin
%_qt5_plugindir/designer/*.so

%changelog
* Mon May 15 2023 Elizaveta Morozova <morozovaes@altlinux.org> 5.2.2-alt1
- Updated version to 5.2.2.
- Added patch: slicer-alt-itk-compat - removed custom ITK Namespaces (feature requires bundled ITK).
- Added patch: slicer-upstream-wc-last-change-date-fix - fixed undefined WC_LAST_CHANGED error.
- Updated patches: slicer-alt-build, slicer-alt-vtk-9.1-compat, slicer-alt-python3-compat.
- Removed obsolete upstream fixes.

* Wed Feb 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 4.11.20210226-alt4
- Rebuilt with VTK-9.1.

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 4.11.20210226-alt3
- Build with qtwebkit on e2k end ppc64le.

* Tue Oct 05 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.11.20210226-alt2
- Fixed build with gcc-11.
- Fixed launch of qt designer.

* Fri May 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.11.20210226-alt1
- Initial build for ALT.
