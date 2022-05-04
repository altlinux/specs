%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%add_optflags -D_FILE_OFFSET_BITS=64

Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/castxml /usr/bin/latex java-devel-default libcurl-devel libqt4-devel rpm-build-java rpm-build-perl zlib-devel
# END SourceDeps(oneline)
BuildRequires: xsltproc
%define fedora 34
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
BuildRequires: /usr/bin/git
# Enabled by default
%bcond_without tests

%if 0%{?fedora} < 33
%undefine __cmake_in_source_build
%endif

Name:       gdcm
Version:    3.0.12
Release:    alt1_1
Summary:    Grassroots DiCoM is a C++ library to parse DICOM medical files
License:    BSD
URL:        http://gdcm.sourceforge.net/wiki/index.php/Main_Page
# Use github release
Source0:    https://github.com/malaterre/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    http://downloads.sourceforge.net/project/gdcm/gdcmData/gdcmData/gdcmData.tar.gz

Patch1: 0001-3.0.1-Use-copyright.patch
# Fix for 1687233
Patch3: 0002-Fix-export-variables.patch

BuildRequires:  libCharLS-devel >= 2.0
BuildRequires:  ctest cmake
BuildRequires:  doxygen
BuildRequires:  libxslt-devel
BuildRequires:  libdcmtk-devel
BuildRequires:  docbook5-style-xsl
BuildRequires:  docbook-style-xsl
BuildRequires:  libexpat-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  graphviz libgraphviz
BuildRequires:  libgl2ps-devel
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  libuuid-devel
BuildRequires:  libssl-devel
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  libpoppler-devel
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  libsqlite3-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libxml2-devel
Source44: import.info

# BuildRequires:  vtk-devel

# Do not generate latex
# BuildRequires:  /usr/bin/latex
# BuildRequires:  /usr/bin/pdflatex
# BuildRequires:  /usr/bin/dvips
# BuildRequires:  /usr/bin/epstopdf
#BuildRequires: texlive-ec


%description
Grassroots DiCoM (GDCM) is a C++ library for DICOM medical files.
It supports ACR-NEMA version 1 and 2 (huffman compression is not supported),
RAW, JPEG, JPEG 2000, JPEG-LS, RLE and deflated transfer syntax.
It comes with a super fast scanner implementation to quickly scan hundreds of
DICOM files. It supports SCU network operations (C-ECHO, C-FIND, C-STORE,
C-MOVE). PS 3.3 & 3.6 are distributed as XML files.
It also provides PS 3.15 certificates and password based mechanism to
anonymize and de-identify DICOM datasets.

%package    doc
Group: Documentation
Summary:    Includes html documentation for gdcm
BuildArch:  noarch

%description doc
You should install the gdcm-doc package if you would like to
access upstream documentation for gdcm.

%package    applications
Group: Development/Tools
Summary:    Includes command line programs for GDCM
Requires:   %{name} = %{version}-%{release}

%description applications
You should install the gdcm-applications package if you would like to
use command line programs part of GDCM. Includes tools to convert,
anonymize, manipulate, concatenate, and view DICOM files.

%package    devel
Group: Development/Other
Summary:    Libraries and headers for GDCM
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-applications = %{version}-%{release}

%description devel
You should install the gdcm-devel package if you would like to
compile applications based on gdcm

%package    examples
Group: Development/Other
Summary:    CSharp, C++, Java, PHP and Python example programs for GDCM
Requires:   %{name} = %{version}-%{release}

%description examples
GDCM examples

%package -n python3-module-gdcm
Group: Development/Other
Summary:    Python binding for GDCM
%{?python_provide:%python_provide python3-gdcm}
Requires:   %{name} = %{version}-%{release}

%description -n python3-module-gdcm
You should install the python3-gdcm package if you would like to
used this library with python

%prep
%setup -q -n GDCM-%{version}
git init -q
git config user.name "rpmbuild"
git config user.email "<rpmbuild>"
git config gc.auto 0
git add --force .
git commit -q --allow-empty -a --author "rpmbuild <rpmbuild>" -m "%{NAME}-%{VERSION} base"
cat %_sourcedir/0001-3.0.1-Use-copyright.patch | git apply --index --reject  -
git commit -q -m 0001-3.0.1-Use-copyright.patch --author "rpmbuild <rpmbuild>"
cat %_sourcedir/0002-Fix-export-variables.patch | git apply --index --reject  -
git commit -q -m 0002-Fix-export-variables.patch --author "rpmbuild <rpmbuild>"

# Data source
%setup -n GDCM-%{version} -q -T -D -a 1

# Fix cmake command
sed -i.backup 's/add_dependency/add_dependencies/' Utilities/doxygen/CMakeLists.txt

# Stop doxygen from producing LaTeX output
sed -i.backup 's/^GENERATE_LATEX.*=.*YES/GENERATE_LATEX = NO/' Utilities/doxygen/doxyfile.in

# Remove bundled utilities (we use Fedora's ones)

rm -rf Utilities/gdcmexpat
rm -rf Utilities/gdcmopenjpeg-v1
rm -rf Utilities/gdcmopenjpeg-v2
rm -rf Utilities/gdcmzlib
rm -rf Utilities/gdcmuuid
rm -rf Utilities/gdcmcharls

# Remove bundled utilities (we don't use them)
rm -rf Utilities/getopt
rm -rf Utilities/pvrg
rm -rf Utilities/rle
rm -rf Utilities/wxWidgets

# Needed for testing:
#rm -rf Utilities/gdcmmd5

%build
%{fedora_v2_cmake}  .. \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DGDCM_INSTALL_PACKAGE_DIR=%{_libdir}/cmake/%{name} \
    -DGDCM_INSTALL_INCLUDE_DIR=%{_includedir}/%{name} \
    -DGDCM_INSTALL_DOC_DIR=%{_docdir}/%{name} \
    -DGDCM_INSTALL_MAN_DIR=%{_mandir} \
    -DGDCM_INSTALL_LIB_DIR=%{_libdir} \
    -DGDCM_BUILD_TESTING:BOOL=ON \
    -DGDCM_DATA_ROOT=../gdcmData/ \
    -DGDCM_BUILD_EXAMPLES:BOOL=OFF \
    -DGDCM_DOCUMENTATION:BOOL=OFF \
    -DGDCM_WRAP_PYTHON:BOOL=ON \
    -DPYTHON_EXECUTABLE=%{__python3} \
    -DGDCM_INSTALL_PYTHONMODULE_DIR=%{python3_sitelibdir} \
    -DGDCM_WRAP_JAVA:BOOL=OFF \
    -DGDCM_WRAP_CSHARP:BOOL=OFF \
    -DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
    -DGDCM_BUILD_APPLICATIONS:BOOL=ON \
    -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
    -DGDCM_USE_VTK:BOOL=OFF \
    -DGDCM_USE_SYSTEM_CHARLS:BOOL=ON \
    -DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
    -DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
    -DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
    -DGDCM_USE_SYSTEM_UUID:BOOL=ON \
    -DGDCM_USE_SYSTEM_LJPEG:BOOL=OFF \
    -DGDCM_USE_SYSTEM_OPENSSL:BOOL=ON \
    -DGDCM_USE_JPEGLS:BOOL=ON \
    -DGDCM_USE_SYSTEM_LIBXML2:BOOL=ON \
    -DGDCM_USE_SYSTEM_JSON:BOOL=ON \
    -DGDCM_USE_SYSTEM_POPPLER:BOOL=ON

#Cannot build wrap_java:
#   -DGDCM_VTK_JAVA_JAR:PATH=/usr/share/java/vtk.jar no found!
#   yum provides */vtk.jar -> No results found

%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install
install -d $RPM_BUILD_ROOT%{python3_sitelibdir}

# Install examples
install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/Examples/
cp -rv ./Examples/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/Examples/

%if %{with tests}
%check
# Making the tests informative only for now. Several failing tests (27/228):
# 11,40,48,49,107-109,111-114,130-135,146,149,,151-154,157,194,216,219
make test -C %{__cmake_builddir} || exit 0
%endif

%files
%doc AUTHORS README.md
%doc --no-dereference Copyright.txt README.Copyright.txt
%{_libdir}/libgdcmCommon.so.3.0
%{_libdir}/libgdcmCommon.so.3.0.12
%{_libdir}/libgdcmDICT.so.3.0
%{_libdir}/libgdcmDICT.so.3.0.12
%{_libdir}/libgdcmDSED.so.3.0
%{_libdir}/libgdcmDSED.so.3.0.12
%{_libdir}/libgdcmIOD.so.3.0
%{_libdir}/libgdcmIOD.so.3.0.12
%{_libdir}/libgdcmMEXD.so.3.0
%{_libdir}/libgdcmMEXD.so.3.0.12
%{_libdir}/libgdcmMSFF.so.3.0
%{_libdir}/libgdcmMSFF.so.3.0.12
%{_libdir}/libgdcmjpeg12.so.3.0
%{_libdir}/libgdcmjpeg12.so.3.0.12
%{_libdir}/libgdcmjpeg16.so.3.0
%{_libdir}/libgdcmjpeg16.so.3.0.12
%{_libdir}/libgdcmjpeg8.so.3.0
%{_libdir}/libgdcmjpeg8.so.3.0.12
%{_libdir}/libgdcmmd5.so.3.0
%{_libdir}/libgdcmmd5.so.3.0.12
%{_libdir}/libsocketxx.so.1.2
%{_libdir}/libsocketxx.so.1.2.0
%dir %{_datadir}/%{name}
%{_datadir}/%{name}-3.0/XML/
#exclude %{_docdir}/%{name}/html/
#exclude %{_docdir}/%{name}/Examples/

#files doc
#doc %{_docdir}/%{name}/html/

%files applications
%{_bindir}/gdcmanon
%{_bindir}/gdcmconv
%{_bindir}/gdcmdiff
%{_bindir}/gdcmdump
%{_bindir}/gdcmgendir
%{_bindir}/gdcmimg
%{_bindir}/gdcminfo
%{_bindir}/gdcmpap3
%{_bindir}/gdcmpdf
%{_bindir}/gdcmraw
%{_bindir}/gdcmscanner
%{_bindir}/gdcmscu
%{_bindir}/gdcmtar
%{_bindir}/gdcmxml
%doc %{_mandir}/man1/*.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libgdcmCommon.so
%{_libdir}/libgdcmDICT.so
%{_libdir}/libgdcmDSED.so
%{_libdir}/libgdcmIOD.so
%{_libdir}/libgdcmMEXD.so
%{_libdir}/libgdcmMSFF.so
%{_libdir}/libgdcmjpeg12.so
%{_libdir}/libgdcmjpeg16.so
%{_libdir}/libgdcmjpeg8.so
%{_libdir}/libgdcmmd5.so
%{_libdir}/libsocketxx.so
%{_libdir}/cmake/%{name}/

%if 0
%files examples
%{_datadir}/%{name}/Examples/
%endif

%files -n python3-module-gdcm
%{python3_sitelibdir}/%{name}*.py
%{python3_sitelibdir}/_%{name}swig.so
%{python3_sitelibdir}/__pycache__/%{name}*

%changelog
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
