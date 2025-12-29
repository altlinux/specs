%define _unpackaged_files_terminate_build 1

Name: librum-reader
Version: 0.12.2
Release: alt5
Summary: Librum is an application designed to make reading enjoyable

Source:  %name-%version.tar
Source1: %name-%version-libs-mupdf.tar
Source2: %name-%version-libs-mupdf-thirdparty-lcms2.tar
Source3: %name-%version-libs-mupdf-thirdparty-extract.tar
Source4: %name-%version-libs-mupdf-thirdparty-mujs.tar
Source5: %name-%version-libs-di.tar

Patch0: python_mupdf_build.patch
Patch1: cmake_build.patch
Patch2: mupdf_disable_strip.patch

Group: Office
License: GPL-3.0-only
Url: https://github.com/Librum-Reader/Librum
VCS: https://github.com/Librum-Reader/Librum.git

BuildRequires: make cmake gcc-c++ qt6-base-devel qt6-declarative-devel 
BuildRequires: qt6-declarative qt6-tools-devel
BuildRequires: zlib-devel clang17.0-devel
BuildRequires: python3-module-clang >= 17
BuildRequires: rpm-macros-qt6 python3-module-setuptools
#dependecies to use system libraries instead of submodules
BuildRequires: zlib-devel libjbig2dec-devel libfreetype-devel
BuildRequires: libharfbuzz-devel libfreeglut-devel libcurl-devel
BuildRequires: libleptonica-devel tesseract-devel
BuildRequires: gdcm-devel libgumbo-devel liblcms2-devel
BuildRequires: rapidfuzz-cpp-devel libopenjpeg2.0-devel 
BuildRequires: bzlib-devel libopenjpeg2.0-devel

%description
Librum is an application designed to make reading enjoyable 
and straightforward for everyone. It's not just an e-book reader. 
With Librum, you can manage your own online library and access it from any 
device anytime, anywhere. It has features like note-taking, bookmarking,
and highlighting, while offering customization 
to make it as personal as you want!

%package lib
Summary: Shared libs for the Librum-Reader package
Group: Office
Requires: qt6-declarative qt6-svg qt6-svg-common  qt6-qtbase
Requires: libqt6-concurrent libqt6-labsanimation libqt6-labsfolderlistmodel
Requires: libqt6-labsqmlmodels libqt6-labssettings libqt6-labssharedimage
Requires: libqt6-labswavefrontmesh libqt6-openglwidgets libqt6-printsupport
Requires: libqt6-qmlcompiler libqt6-qmlcore libqt6-qmllocalstorage
Requires: libqt6-qmlworkerscript libqt6-qmlxmllistmodel libqt6-quickdialogs2 
Requires: libqt6-quickdialogs2quickimpl libqt6-quickdialogs2utils
Requires: libqt6-quicklayouts libqt6-quickparticles libqt6-xml
Requires: libqt6-quickshapes libqt6-quicktest libqt6-quickwidgets
Requires: libqt6-sql libqt6-svg libqt6-test 

%description lib
Shared libraries for the Librum-Reader package.

%package client
Summary: Executable file the Librum-Reader package
Group: Office
Requires: qt6-svg qt6-declarative  qt6-svg-common  qt6-qtbase libqt6-svg
Requires: %name-lib = %EVR

%description client
Executable for the Librum-Reader package.

%prep
%setup -a0 -a1 -a2 -a3 -a4 -a5
%patch0
%patch1
%patch2

%build
# patch correct library dest
for file in $(find . -name CMakeLists.txt )
do
  sed -i "s/DESTINATION lib/DESTINATION %_lib/g" $file
done

%cmake -DNO_VENV=On -DCMAKE_PREFIX_PATH=%_qt6_bindir
%cmake_build

%install

%cmake_install

# Remove unversioned shared libraries.
rm -f %buildroot/%_libdir/lib*.so
rm -f %buildroot/%_libdir/mutool

%files lib
%_libdir/libadapters.so.0
%_libdir/libadapters.so.0.12
%_libdir/libdomain.so.0
%_libdir/libdomain.so.0.12
%_libdir/libinfrastructure.so.0
%_libdir/libinfrastructure.so.0.12
%_libdir/libpresentation.so.0
%_libdir/libpresentation.so.0.12
%_libdir/libapplication.so.0
%_libdir/libapplication.so.0.12
%_libdir/libreadermupdfcpp.so.1

%files client
%_bindir/librum
%_datadir/applications/librum.desktop
%_datadir/pixmaps/librum.svg

%changelog
* Mon Dec 29 2025 Oleg Proskurin <proskur@altlinux.org> 0.12.2-alt5
- Fix major mistakes in the .spec file.

* Tue Jul 01 2025 Oleg Proskurin <proskur@altlinux.org> 0.12.2-alt4
- Fix QML for Qt 6.9.1 (Closes #54983)

* Thu Jan 09 2025 Oleg Proskurin <proskur@altlinux.org> 0.12.2-alt3
- Fix requires (Closes: #52643)

* Thu Dec 12 2024 Oleg Proskurin <proskur@altlinux.org> 0.12.2-alt2
- Remove redundant mupdf dependency

* Thu May 02 2024 Oleg Proskurin <proskur@altlinux.org> 0.12.2-alt1
- New version

* Mon Mar 11 2024 Oleg Proskurin <proskur@altlinux.org> 0.11.0-alt2
- Add setuptools dependency

* Wed Dec 20 2023 Oleg Proskurin <proskur@altlinux.org> 0.11.0-alt1
- New version

* Mon Dec 04 2023 Oleg Proskurin <proskur@altlinux.org> 0.10.2-alt1
- New version

* Tue Nov 07 2023 Oleg Proskurin <proskur@altlinux.org> 0.10.1-alt1
- New version

* Tue Oct 24 2023 Oleg Proskurin <proskur@altlinux.org> 0.10.0-alt1
- New version

* Mon Oct 09 2023 Oleg Proskurin <proskur@altlinux.org> 0.9.2-alt1
- Initial Build

