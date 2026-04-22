%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define abiversion 3.2
%define socketxxsoname 1.2

%define libgdcm_common libgdcmcommon%abiversion
%define libgdcm_dict libgdcmdict%abiversion
%define libgdcm_dsed libgdcmdsed%abiversion
%define libgdcm_iod libgdcmiod%abiversion
%define libgdcm_jpeg8 libgdcmjpeg8_%abiversion
%define libgdcm_jpeg12 libgdcmjpeg12_%abiversion
%define libgdcm_jpeg16 libgdcmjpeg16_%abiversion
%define libgdcm_md5 libgdcmmd5_%abiversion
%define libgdcm_mexd libgdcmmexd%abiversion
%define libgdcm_msff libgdcmmsff%abiversion
%define libgdcm_socketxx libgdcmsocketxx%socketxxsoname
%define libgdcm_vtk libgdcmvtk%{vtk_version}_%vtk_soname

Name: gdcm
Version: 3.2.5
Release: alt2

Summary: Cross-platform DICOM implementation
License: BSD-3-Clause
Group: System/Libraries
Url: https://sourceforge.net/projects/gdcm/
VCS: https://git.code.sf.net/p/gdcm/gdcm.git

Source0: %name-%version.tar
Source1: gdcmData.tar
Patch0: gdcm-3.0.1-unknown-use-copyright.patch
Patch1: %name-%version-%release.patch
Patch3: gdcm-3.0.24-alt-export-variables.patch

BuildRequires(pre): rpm-build-java
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-vtk
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: docbook5-style-xsl
BuildRequires: doxygen
BuildRequires: /usr/bin/latex
BuildRequires: fontconfig-devel
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: libCharLS-devel
BuildRequires: libdcmtk-devel
BuildRequires: libexpat-devel
BuildRequires: libgl2ps-devel
BuildRequires: libgraphviz
BuildRequires: libjson-c-devel
BuildRequires: libogg-devel
BuildRequires: libopenjpeg2.0-devel
BuildRequires: libpoppler-devel
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel
BuildRequires: libtheora-devel
BuildRequires: libuuid-devel
BuildRequires: libvtk-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: python3-devel
BuildRequires: swig
BuildRequires: xsltproc

Requires: %libgdcm_common
Requires: %libgdcm_dict
Requires: %libgdcm_dsed
Requires: %libgdcm_iod
Requires: %libgdcm_jpeg8
Requires: %libgdcm_jpeg12
Requires: %libgdcm_jpeg16
Requires: %libgdcm_md5
Requires: %libgdcm_mexd
Requires: %libgdcm_msff
Requires: %libgdcm_socketxx

%description
Grassroots DiCoM is a C++ library for DICOM medical files. It is
accessible from Python, C#, Java and PHP. It supports RAW, JPEG, JPEG
2000, JPEG-LS, RLE and deflated transfer syntax.
It comes with a super fast scanner implementation to quickly
scan hundreds of DICOM files.
It supports SCU network operations (C-ECHO, C-FIND, C-STORE, C-MOVE).
PS 3.3 & 3.6 are distributed as XML files.
It also provides PS 3.15 certificates and password based mecanism
to anonymize and de-identify DICOM datasets.

%package -n %libgdcm_common
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_common
%summary.

%package -n %libgdcm_dict
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_dict
%summary.

%package -n %libgdcm_dsed
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_dsed
%summary.

%package -n %libgdcm_iod
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_iod
%summary.

%package -n %libgdcm_jpeg8
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_jpeg8
%summary.

%package -n %libgdcm_jpeg12
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_jpeg12
%summary.

%package -n %libgdcm_jpeg16
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_jpeg16
%summary.

%package -n %libgdcm_md5
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_md5
%summary.

%package -n %libgdcm_mexd
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_mexd
%summary.

%package -n %libgdcm_msff
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_msff
%summary.

%package -n %libgdcm_socketxx
Summary: %summary
Group: System/Libraries

Conflicts: gdcm < 3.0.22

%description -n %libgdcm_socketxx
%summary.

%package -n %libgdcm_vtk
Summary: %summary
Group: System/Libraries

%description -n %libgdcm_vtk
%summary.

%package doc
Summary: Documentation for gdcm
Group: Documentation
BuildArch: noarch

%description doc
You should install the gdcm-doc package if you would like to
access upstream documentation for gdcm.

%package applications
Summary: Includes command line programs for GDCM
Group: Development/Tools

%description applications
You should install the gdcm-applications package if you would like to
use command line programs part of GDCM. Includes tools to convert,
anonymize, manipulate, concatenate, and view DICOM files.

%package devel
Summary: Libraries and headers for GDCM
Group: Development/Other

Requires: gdcm-applications

%description devel
You should install the gdcm-devel package if you would like to
compile applications based on gdcm.

%package examples
Summary: CSharp, C++, Java, PHP and Python example programs for GDCM
Group: Development/Other
BuildArch: noarch

%description examples
GDCM examples

%package -n python3-module-gdcm
Summary: Python binding for GDCM
Group: Development/Other

%description -n python3-module-gdcm
You should install the python3-gdcm package if you would like to
used this library with python.

%prep
%setup -a1
%autopatch -p1

sed -i \
  's/^GENERATE_LATEX.*=.*YES/GENERATE_LATEX = NO/' \
  Utilities/doxygen/doxyfile.in

rm -rf \
  Utilities/gdcmcharls \
  Utilities/gdcmexpat \
  Utilities/gdcmopenjpeg \
  Utilities/gdcmutfcpp \
  Utilities/gdcmuuid \
  Utilities/gdcmzlib \
  #

%build
%ifarch %ix86
%add_optflags -D_FILE_OFFSET_BITS=64
%endif
# vtk module require using relative path from prefix
%cmake -Wno-dev -Wno-unused-variable \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DCMAKE_CXX_STANDARD=20 \
  -DCMAKE_INSTALL_PREFIX:PATH=%prefix \
  -DCMAKE_SKIP_RPATH:BOOL=ON \
  -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
  -DEXPAT_LIBRARY:FILEPATH=%_libdir/libexpat.so \
  -DGDCM_BUILD_APPLICATIONS:BOOL=ON \
  -DGDCM_BUILD_DOCBOOK_MANPAGES:BOOL=ON \
  -DGDCM_BUILD_EXAMPLES:BOOL=OFF \
  -DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
  -DGDCM_BUILD_TESTING:BOOL=ON \
  -DGDCM_DATA_ROOT:PATH=$PWD/gdcmData \
  -DGDCM_DOCUMENTATION:BOOL=ON \
  -DGDCM_DOXYGEN_NO_FOOTER:BOOL=ON \
  -DGDCM_INSTALL_DOC_DIR:PATH=%_docdir/gdcm \
  -DGDCM_INSTALL_INCLUDE_DIR:PATH=include/gdcm \
  -DGDCM_INSTALL_LIB_DIR:PATH=%_lib \
  -DGDCM_INSTALL_MAN_DIR:PATH=%_mandir \
  -DGDCM_INSTALL_PACKAGE_DIR:PATH=%_lib/cmake/gdcm \
  -DGDCM_INSTALL_PYTHONMODULE_DIR:STRING=%_lib/python3/site-packages \
  -DGDCM_NO_PYTHON_LIBS_LINKING:BOOL=ON \
  -DGDCM_PDF_DOCUMENTATION:BOOL=OFF \
  -DGDCM_USE_JPEGLS:BOOL=ON \
  -DGDCM_USE_PARAVIEW:BOOL=OFF \
  -DGDCM_USE_PVRG:BOOL=OFF \
  -DGDCM_USE_SYSTEM_CHARLS:BOOL=ON \
  -DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
  -DGDCM_USE_SYSTEM_JSON:BOOL=ON \
  -DGDCM_USE_SYSTEM_LIBXML2:BOOL=ON \
  -DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
  -DGDCM_USE_SYSTEM_OPENSSL:BOOL=ON \
  -DGDCM_USE_SYSTEM_POPPLER:BOOL=ON \
  -DGDCM_USE_SYSTEM_UUID:BOOL=ON \
  -DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
  -DGDCM_USE_VTK:BOOL=ON \
  -DGDCM_VTK_DOCUMENTATION:BOOL=OFF \
  -DGDCM_WRAP_CSHARP:BOOL=OFF \
  -DGDCM_WRAP_JAVA:BOOL=OFF \
  -DGDCM_WRAP_PHP:BOOL=OFF \
  -DGDCM_WRAP_PYTHON:BOOL=ON \
  -DPYTHON_EXECUTABLE:PATH=%_bindir/python3 \
  -DPYTHON_VERSION_MAJOR=3 \
  -DVTKGDCM_WRAP_JAVA:BOOL=OFF \
  -DVTKGDCM_WRAP_PYTHON:BOOL=ON \
  #

%cmake_build

%install
%cmake_install
install -d \
  %buildroot%python3_sitelibdir \
  %buildroot%_datadir/%name/Examples \
  %buildroot%_includedir/%name \
  #
install -Dm 644 Utilities/gdcm_zlib.h \
  -t %buildroot%_includedir

cp -rv Examples/* %buildroot%_datadir/%name/Examples

%check
export LD_LIBRARY_PATH="%buildroot%_libdir:$PWD/%_arch-alt-linux/bin"
export PYTHONPATH="%buildroot%python3_sitelibdir"
%ctest ||:

%files
%nil

%files -n %libgdcm_common
%doc AUTHORS README.md
%_libdir/libgdcmCommon.so.%{abiversion}*

%files -n %libgdcm_dsed
%_libdir/libgdcmDSED.so.%{abiversion}*

%files -n %libgdcm_dict
%_libdir/libgdcmDICT.so.%{abiversion}*

%files -n %libgdcm_iod
%_libdir/libgdcmIOD.so.%{abiversion}*

%files -n %libgdcm_jpeg8
%_libdir/libgdcmjpeg8.so.%{abiversion}*

%files -n %libgdcm_jpeg12
%_libdir/libgdcmjpeg12.so.%{abiversion}*

%files -n %libgdcm_jpeg16
%_libdir/libgdcmjpeg16.so.%{abiversion}*

%files -n %libgdcm_md5
%_libdir/libgdcmmd5.so.%{abiversion}*

%files -n %libgdcm_mexd
%_libdir/libgdcmMEXD.so.%{abiversion}*

%files -n %libgdcm_msff
%_libdir/libgdcmMSFF.so.%{abiversion}*

%files -n %libgdcm_socketxx
%_libdir/libsocketxx.so.%{socketxxsoname}*

%files -n %libgdcm_vtk
%_libdir/libvtkgdcm-%vtk_version.so.*

%files doc
%_docdir/gdcm/html

%files applications
%_bindir/gdcm*
%_man1dir/gdcm*

%files devel
%_datadir/gdcm-*/XML/
%_includedir/gdcm/
%_includedir/gdcm_zlib.h
%_includedir/vtkgdcmpython.h
%_libdir/cmake/gdcm/
%_libdir/lib*.so
%_libdir/vtk-%vtk_version/hierarchy/vtkgdcm/vtkgdcm-hierarchy.txt

%files examples
%_datadir/gdcm/Examples

%files -n python3-module-gdcm
%python3_sitelibdir/gdcm.py
%python3_sitelibdir/gdcmswig.py
%python3_sitelibdir/_gdcmswig.so
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/vtkgdcm/

%changelog
* Wed Apr 22 2026 Anton Farygin <rider@altlinux.org> 3.2.5-alt2
- disabled PVRG JPEG codec: unbuildable with gcc-15 (C23 default),
  upstream is abandoned and declares it broken; IJG codec covers
  the standard cases.

* Fri Apr 03 2026 Anton Farygin <rider@altlinux.org> 3.2.5-alt1
- 3.2.2 -> 3.2.5

* Wed Feb 04 2026 Anton Farygin <rider@altlinux.org> 3.2.2-alt2
- Fixed build with vtk 9.5.

* Mon Oct 13 2025 Constantin Sunzow <protvin@altlinux.org> 3.2.2-alt1
- New version.

* Mon Jul 21 2025 Constantin Sunzow <protvin@altlinux.org> 3.0.26-alt1
- New version.

* Fri Mar 07 2025 Constantin Sunzow <protvin@altlinux.org> 3.0.25-alt1
- Rebuild with vtk macros.
- New version.

* Mon Feb 17 2025 Constantin Sunzow <protvin@altlinux.org> 3.0.24-alt4
- Rebuild against vtk 9.4.

* Wed Jan 29 2025 Constantin Sunzow <protvin@altlinux.org> 3.0.24-alt3
- Stub package for old name.

* Thu Jan 23 2025 Constantin Sunzow <protvin@altlinux.org> 3.0.24-alt2
- Build against system CharLS.

* Thu Jan 23 2025 Constantin Sunzow <protvin@altlinux.org> 3.0.24-alt1.p11.1
- Apply export include directory from prefix.
- Compliance with Shared Libs Policy.
- Remove bundled libraries.
- Clean lost files.

* Thu Dec 26 2024 Constantin Sunzow <protvin@altlinux.org> 3.0.24-alt1
- Purge archive extracted source code.
- Build from git tag.
- New version.

* Thu Jul 20 2023 Sergey V Turchin <zerg@altlinux.org> 3.0.21-alt1
- new version
- don't build with Qt4
- fix compile with gcc-10

* Fri Apr 14 2023 Michael Shigorin <mike@altlinux.org> 3.0.12-alt3
- E2K: fix build (ilyakurdyukov@)

* Mon May 23 2022 Slava Aseev <ptrnine@altlinux.org> 3.0.12-alt2
- do not pack manuals for non-existent executables (closes: #42141)
- remove import.info

* Wed May 04 2022 Slava Aseev <ptrnine@altlinux.org> 3.0.12-alt1_1
- new version

* Thu Oct 14 2021 Igor Vlasenko <viy@altlinux.org> 3.0.9-alt1_3
- new version

* Tue Oct 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.5-alt1_0.1
- Fixed build with gcc-11.

* Mon May 11 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.5-alt1_0
- new version

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_0
- new version
- build w/o python: not to lock python38 update.

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.8.4-alt4_11
- fixed build, disabled python. stub for python38 update.

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.8.4-alt3_11
- fixed build

* Wed Jan 09 2019 Igor Vlasenko <viy@altlinux.ru> 2.8.4-alt2_11
- fixed build

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.8.4-alt2_8.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Aug 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.4-alt2_8
- Fixed build.

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.8.4-alt1_8
- applied repocop patch
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.8.4-alt1_7
- update to new release by fcimport

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.5-alt1_19.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Jan 30 2018 Igor Vlasenko <viy@altlinux.ru> 2.6.5-alt1_19
- new version

* Thu Nov 21 2013 Sergey V Turchin <zerg@altlinux.org> 2.2.3-alt2.M70P.1
- Rebuild for poppler

* Tue Apr 23 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.3-alt2
- Rebuild for poppler

* Tue Apr 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.3-alt1
- 2.2.3

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt2
- rebuilt for perl-5.16

* Sat Jun 23 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Nov 07 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.18-alt1
- first build for ALT Linux
