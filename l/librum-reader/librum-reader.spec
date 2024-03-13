Name: librum-reader
Version: 0.11.0
Release: alt2
Summary: Librum is an application designed to make reading enjoyable and straightforward for everyone.

Source:  %name-%version.tar
Source1: %name-%version-libs-di.tar
Source2: %name-%version-libs-mupdf-thirdparty-extract.tar
Source3: %name-%version-libs-mupdf-thirdparty-mujs.tar
Source4: %name-%version-libs-mupdf.tar
Source5: %name-%version-libs-rapidfuzz-cpp.tar

Patch0: alt-fix_version_number.patch
# patch mupdf python script to build mupdf as static lib and link it with mupdfcpp
Patch1: alt-force_static_mupdf_build.patch
Patch2: alt-force_python_to_link_statically_mupdf_with_mupdfcpp.patch
# add version and soversion to shared libs
Patch3: alt-add_soversion_for_adapters.patch
Patch4: alt-add_soversion_for_domain.patch
Patch5: alt-add_soversion_for_infrastructure.patch
Patch6: alt-add_soversion_for_presentation.patch


Group: Office 
Url: https://github.com/Librum-Reader/Librum
License: GPLv3
#forked version with OPDS servers support from
# Url: https://github.com/3036662/librum-reader_OPDS

BuildRequires: make cmake gcc-c++ qt6-base-devel qt6-declarative-devel qt6-declarative qt6-tools-devel
BuildRequires: zlib-devel clang16.0-devel  clang16.0-libs
BuildRequires: python3-module-clang >= 16
BuildRequires: rpm-macros-qt6 python3-module-setuptools
#dependecies to use system libraries instead of submodules 
BuildRequires: zlib-devel libjbig2dec-devel libfreetype-devel
BuildRequires: libharfbuzz-devel libfreeglut-devel libcurl-devel
BuildRequires: libleptonica-devel tesseract-devel
BuildRequires: gdcm-devel libopenjpeg2.0-devel libgumbo-devel liblcms2-devel
BuildRequires: libtinyxml2-devel boost-devel-headers libwebp-devel libzip-devel libzip-utils

%description
Librum is an application designed to make reading enjoyable and straightforward for everyone.
It's not just an e-book reader. With Librum, you can manage your own online library and access it from any device anytime, anywhere. It has features like note-taking, bookmarking, and highlighting, while offering customization to make it as personal as you want!

%package lib
Summary: shared libs for librum package
Group: Office
%description lib
shared libraries for librum
Requires: qt6-declarative qt6-svg qt6-svg-common  qt6-qtbase libleptonica tesseract libharfbuzz libcurl libfreeglut libfreetype jbig2dec zlib libgumbo2
Requires: libqt6-concurrent libqt6-labsanimation libqt6-labsfolderlistmodel libqt6-labsqmlmodels libqt6-labssettings libqt6-labssharedimage
Requires: libqt6-labswavefrontmesh libqt6-openglwidgets libqt6-printsupport libqt6-qmlcompiler libqt6-qmlcore
Requires: libqt6-qmllocalstorage libqt6-qmlworkerscript libqt6-qmlxmllistmodel libqt6-quickdialogs2 libqt6-quickdialogs2quickimpl
Requires: libqt6-quickdialogs2utils libqt6-quicklayouts libqt6-quickparticles  libqt6-quickshapes libqt6-quicktest libqt6-quickwidgets
Requires: libqt6-sql libqt6-svg libqt6-test libqt6-xml 
Requires: gdcm libopenjpeg2.0 liblcms2 
Requires: libwebp libzip-utils

%package client
Summary: executable file for package
Group: Office
Requires: qt6-svg qt6-declarative  qt6-svg-common  qt6-qtbase libqt6-svg
Requires: %name-lib
%description client
executable for librum package

%prep
%setup -a1 -a2 -a3 -a4 -a5 
%patch0 
%patch1 
%patch2
%patch3 
%patch4
%patch5
%patch6 

%build
# patch correct library dest
for file in $(find . -name CMakeLists.txt )
do
  sed -i "s/DESTINATION lib/DESTINATION %_lib/g" $file 
done
%cmake  -DBUILD_TEST=Off -DNO_VENV=On -DCMAKE_PREFIX_PATH=%_qt6_bindir
%cmake_build

%install
%cmake_install

%files lib
%_libdir/libadapters.so.0
%_libdir/libadapters.so.0.11
%_libdir/libdomain.so.0
%_libdir/libdomain.so.0.11
%_libdir/libinfrastructure.so.0
%_libdir/libinfrastructure.so.0.11
%_libdir/libpresentation.so.0
%_libdir/libpresentation.so.0.11
%_libdir/libapplication.so.0
%_libdir/libapplication.so.0.11
%_libdir/libreadermupdfcpp.so.1
%ghost %_libdir/libadapters.so
%ghost %_libdir/libapplication.so
%ghost %_libdir/libdomain.so
%ghost %_libdir/libinfrastructure.so
%ghost %_libdir/libpresentation.so

%files client
%_bindir/librum
%_datadir/applications/librum.desktop
%_datadir/pixmaps/librum.svg

%changelog
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
