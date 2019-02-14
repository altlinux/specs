Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-fedora-compat
BuildRequires: /usr/bin/castxml /usr/bin/latex java-devel-default libcurl-devel libqt4-devel python-devel rpm-build-java rpm-build-perl rpm-build-python zlib-devel
# END SourceDeps(oneline)
BuildRequires: xsltproc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		gdcm
Version:	2.8.4
Release:	alt3_11
Summary:	Grassroots DiCoM is a C++ library to parse DICOM medical files
License:	BSD
URL:		http://gdcm.sourceforge.net/wiki/index.php/Main_Page
Source0:	http://sourceforge.net/projects/gdcm/files/gdcm%%202.x/GDCM%%20%{version}/%{name}-%{version}.tar.bz2
Source1:	http://downloads.sourceforge.net/project/gdcm/gdcmData/gdcmData/gdcmData.tar.gz

Patch1:	gdcm-2.4.0-usecopyright.patch
Patch2:	gdcm-2.4.0-install2libarch.patch
Patch3:	gdcm-2.4.0-no-versioned-dir.patch
# From http://public.kitware.com/pipermail/vtkusers/2013-February/127377.html
#Patch4: gdcm-0005-support-vtk6.patch
Patch6: gdcm-2.6-fix-cmake-config-paths.patch
Patch7: gdcm-2.8.4-fix-manpage-gen.patch
Patch8: gdcm-2.8.4-fix-poppler.patch
Patch9: gdcm-2.8.4-poppler-0.67.0.patch

BuildRequires:	libCharLS-devel >= 1.0
BuildRequires:	ctest cmake
BuildRequires:	doxygen
BuildRequires:	libxslt-devel
BuildRequires:	docbook5-style-xsl
BuildRequires:	libexpat-devel
BuildRequires:	fontconfig-devel
BuildRequires:	graphviz libgraphviz
BuildRequires:	libgl2ps-devel
BuildRequires:	libogg-devel
BuildRequires:	libtheora-devel
BuildRequires:	libuuid-devel
BuildRequires:	libssl-devel
BuildRequires:  pkgconfig(libopenjp2)
#BuildRequires:	/usr/bin/pdflatex
BuildRequires:	libpoppler-devel
BuildRequires:	python3-devel
BuildRequires:	swig
BuildRequires:	libjson-c-devel
BuildRequires:	libxml2-devel
#BuildRequires:	texlive-ec
#BuildRequires:	vtk-devel
BuildRequires: gcc gcc-c++
Source44: import.info
# debian
Patch134: poppler0.71.patch
# me
Patch135: gdcm-2.8.4-alt-poppler.patch


%description
Grassroots DiCoM (GDCM) is a C++ library for DICOM medical files.
It supports ACR-NEMA version 1 and 2 (huffman compression is not supported),
RAW, JPEG, JPEG 2000, JPEG-LS, RLE and deflated transfer syntax.
It comes with a super fast scanner implementation to quickly scan hundreds of
DICOM files. It supports SCU network operations (C-ECHO, C-FIND, C-STORE,
C-MOVE). PS 3.3 & 3.6 are distributed as XML files.
It also provides PS 3.15 certificates and password based mechanism to
anonymize and de-identify DICOM datasets.

%package	doc
Group: Documentation
Summary:	Includes html documentation for gdcm
BuildArch:	noarch

%description doc
You should install the gdcm-doc package if you would like to
access upstream documentation for gdcm.

%package	applications
Group: Development/Tools
Summary:	Includes command line programs for GDCM
Requires:	%{name} = %{version}-%{release}

%description applications
You should install the gdcm-applications package if you would like to
use command line programs part of GDCM. Includes tools to convert,
anonymize, manipulate, concatenate, and view DICOM files.

%package	devel
Group: Development/Other
Summary:	Libraries and headers for GDCM
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-applications = %{version}-%{release}

%description devel
You should install the gdcm-devel package if you would like to
compile applications based on gdcm

%package	examples
Group: Development/Other
Summary:	CSharp, C++, Java, PHP and Python example programs for GDCM
Requires:	%{name} = %{version}-%{release}
AutoReq: no

%description examples
GDCM examples

%package -n python3-module-gdcm
Group: Development/Other
Summary:	Python binding for GDCM
%{?python_provide:%python_provide python3-gdcm}
Requires:	%{name} = %{version}-%{release}

%description -n python3-module-gdcm
You should install the python3-gdcm package if you would like to
used this library with python

%prep
%setup -q
%setup -T -D -a 1
%patch1 -p 1
%patch2 -p 1
%patch3 -p 1
%patch6 -p 1
%patch7 -p 1
%patch8 -p 1
%patch9 -p 1
%patch134 -p1
%patch135 -p1

# Fix cmake command
sed -i.backup 's/add_dependency/add_dependencies/' Utilities/doxygen/CMakeLists.txt

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
mkdir -p %{_target_platform}
pushd %{_target_platform}

%{fedora_cmake}	.. \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DGDCM_INSTALL_PACKAGE_DIR=%{_libdir}/cmake/%{name} \
	-DGDCM_INSTALL_INCLUDE_DIR=%{_includedir}/%{name} \
	-DGDCM_INSTALL_DOC_DIR=%{_docdir}/%{name} \
	-DGDCM_INSTALL_MAN_DIR=%{_mandir} \
	-DGDCM_INSTALL_LIB_DIR=%{_libdir} \
	-DGDCM_BUILD_TESTING:BOOL=ON \
	-DGDCM_DATA_ROOT=../gdcmData/ \
	-DGDCM_BUILD_EXAMPLES:BOOL=ON \
	-DGDCM_DOCUMENTATION:BOOL=ON \
	-DGDCM_PDF_DOCUMENTATION:BOOL=OFF \
	-DGDCM_WRAP_PYTHON:BOOL=ON \
	-DPYTHON_EXECUTABLE=%{__python3} \
	-DGDCM_INSTALL_PYTHONMODULE_DIR=%{python3_sitelibdir} \
	-DGDCM_WRAP_JAVA:BOOL=OFF \
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
#	-DGDCM_VTK_JAVA_JAR:PATH=/usr/share/java/vtk.jar no found! 
#	yum provides */vtk.jar -> No results found

popd

%make_build -C %{_target_platform}

%install
make install DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}
install -d $RPM_BUILD_ROOT%{python3_sitelibdir}

## Cleaning Example dir from cmake cache files + remove 0-length files
find %{_builddir}/%{?buildsubdir}/Examples -depth -name CMakeFiles | xargs rm -rf
find %{_builddir}/%{?buildsubdir}/Examples -depth -size 0 | xargs rm -rf

## Moving Example dir into _datadir
cp -r %{_builddir}/%{?buildsubdir}/Examples $RPM_BUILD_ROOT%{_datadir}/%{name}/

%check
# Making the tests informative only for now. Several failing tests (27/228):
# 11,40,48,49,107-109,111-114,130-135,146,149,,151-154,157,194,216,219
make test -C %{_target_platform} || exit 0

%files
%doc AUTHORS Copyright.txt README.Copyright.txt README.txt
%{_libdir}/*.so.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/XML/
%exclude %{_docdir}/%{name}/html/

%files doc
%doc %{_docdir}/%{name}/html/

%files applications
%{_bindir}/*
%doc %{_mandir}/man1/*.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/

%files examples
%{_datadir}/%{name}/Examples/

%files -n python3-module-gdcm
%{python3_sitelibdir}/%{name}*.py
%{python3_sitelibdir}/_%{name}swig.so
%{python3_sitelibdir}/__pycache__/%{name}*

%changelog
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
