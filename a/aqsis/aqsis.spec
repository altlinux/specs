# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ python-devel
# END SourceDeps(oneline)
Name:		aqsis
Version:	1.8.1
Release:	alt2_1
Summary:	Open source 3D rendering solution adhering to the RenderMan standard
Group:		Video

License:	GPLv2+ and LGPLv2+
URL:		http://www.aqsis.org
Source0:	http://downloads.sourceforge.net/aqsis/aqsis-%{version}.tar.gz

BuildRequires:  desktop-file-utils

BuildRequires:  bison >= 1.35.0
BuildRequires:  boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel >= 1.34.0
BuildRequires:  ctest cmake >= 2.6.3
BuildRequires:  doxygen
BuildRequires:  flex >= 2.5.4
BuildRequires:  libfltk-devel >= 1.1.0 libfltk-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiffxx-devel libtiff-devel >= 3.7.1
BuildRequires:  libpng-devel
BuildRequires:  xsltproc libxslt
BuildRequires:  qt4-devel >= 4.6.2
#BuildRequires:  tinyxml-devel
BuildRequires:  openexr-devel
BuildRequires:  python-module-sphinx
BuildRequires:  zlib-devel >= 1.1.4

Requires: qt4
Requires: aqsis-core = %{version}-%{release}
Requires: aqsis-data = %{version}-%{release}
Source44: import.info


%description
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains graphical utilities and desktop integration.


%package core
Requires:	aqsis-libs = %{version}-%{release}
Summary:	Command-line tools for Aqsis Renderer
Group:		Video

%description core
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains a command-line renderer, a shader compiler
for shaders written using the RenderMan shading language, a texture
pre-processor for optimizing textures and a RIB processor.


%package libs
Summary:        Library files for Aqsis Renderer
Group:          System/Libraries

%description libs
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains the shared libraries for Aqsis Renderer.


%package data
Requires:	aqsis = %{version}-%{release}
Summary:	Example content for Aqsis Renderer
Group:		Video
BuildArch:      noarch
AutoReq: yes,nopython

%description data
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains example content, including additional
scenes, procedurals and shaders.


%package devel
Requires:	aqsis = %{version}-%{release}
Requires:	aqsis-core = %{version}-%{release}
Requires:	aqsis-libs = %{version}-%{release}
Requires:	aqsis-data = %{version}-%{release}
Summary:	Development files for Aqsis Renderer
Group:		Development/C

%description devel
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains various developer libraries to enable
integration with third-party applications.


%prep
%setup -q


%build
## Do not Enable pdiff=yes Because it will conflict with Printdiff :
## /usr/bin/pdiff  from package	a2ps
rm -rf build
mkdir -p build
pushd build
%{fedora_cmake} \
  -DSYSCONFDIR:STRING=%{_sysconfdir}/%{name} \
  -DAQSIS_MAIN_CONFIG_NAME=aqsisrc-%{_lib} \
  -DLIBDIR=%{_lib} \
  -DPLUGINDIR=%{_lib}/%{name} \
  -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
  -DCMAKE_SKIP_RPATH:BOOL=ON \
  -DAQSIS_USE_RPATH:BOOL=OFF \
  -DAQSIS_BOOST_FILESYSTEM_LIBRARY_NAME=boost_filesystem-mt \
  -DAQSIS_BOOST_REGEX_LIBRARY_NAME=boost_regex-mt \
  -DAQSIS_BOOST_THREAD_LIBRARY_NAME=boost_thread-mt \
  -DAQSIS_BOOST_WAVE_LIBRARY_NAME=boost_wave-mt \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS -DBOOST_FILESYSTEM_VERSION=2" \
  -DAQSIS_USE_EXTERNAL_TINYXML:BOOL=OFF ..

make VERBOSE=1 %{?_smp_mflags}

popd


%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd

# Move aqsisrc
mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/aqsisrc \
  $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/aqsisrc-%{_lib}

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/aqsis.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/aqsl.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/aqsltell.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/eqsl.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/piqsl.desktop


%files
%doc AUTHORS COPYING README
%{_bindir}/eqsl
%{_bindir}/piqsl
%{_bindir}/ptview
# Do not use the name pdiff for PerceptualDiff
# It is used by PrintDiff in a2ps
#{_bindir}/pdiff
%{_datadir}/applications/aqsis.desktop
%{_datadir}/applications/aqsl.desktop
%{_datadir}/applications/aqsltell.desktop
%{_datadir}/applications/eqsl.desktop
%{_datadir}/applications/piqsl.desktop
%{_datadir}/pixmaps/aqsis.png
%{_datadir}/icons/hicolor/192x192/mimetypes/aqsis-doc.png
%{_datadir}/mime/packages/aqsis.xml


%files core
%{_bindir}/aqsis
%{_bindir}/aqsl
%{_bindir}/aqsltell
%{_bindir}/miqser
%{_bindir}/teqser


%files libs
%dir %{_sysconfdir}/%{name}
## Do not use noreplace with aqsis release
## This may definitly change in future releases.
%config %{_sysconfdir}/%{name}/aqsisrc-%{_lib}
%{_libdir}/%{name}/
# Licensed under GPLv2+
%{_libdir}/libaqsis_*.so.*
# Licensed under LGPLv2+
#{_libdir}/libaqsis_ri2rib.so.*


%files devel
%{_includedir}/%{name}/
# Licensed under GPLv2+
%{_libdir}/libaqsis_*.so
# Licensed under LGPLv2+
#{_libdir}/libaqsis_ri2rib.so


%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples/
%{_datadir}/%{name}/plugins/
%{_datadir}/%{name}/scripts/
%{_datadir}/%{name}/shaders/



%changelog
* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2_1
- fixed build

* Thu May 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_1
- new version

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1_15.1
- Rebuilt with Boost 1.49.0

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_15
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_14
- update to new release by fcimport

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1_13.1
- Rebuilt with Boost 1.48.0

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_13
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_12
- update to new release by fcimport

* Sat Jul 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_11
- initial release by fcimport

