# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ perl(Env.pm)
# END SourceDeps(oneline)
%define fedora 16
Name:		Equalizer
Version:	1.0.1
Release:	alt4_1.20110922.1
Summary:	Middleware to create and deploy parallel OpenGL-based applications

Group:		Development/C
License:	LGPLv2+
URL:		http://www.equalizergraphics.com/
Source0:	http://www.equalizergraphics.com/downloads/%{name}-%{version}.tar.gz

BuildRequires:	ctest cmake bison flex
BuildRequires:  boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel libglew-devel
BuildRequires:  libX11-devel libGL-devel
BuildRequires:  libOpenSceneGraph-devel >= 2.9.8
Source44: import.info

%description
Equalizer is the standard middleware to create and deploy parallel OpenGL-based
applications. It enables applications to benefit from multiple graphics cards,
processors and computers to scale the rendering performance, visual quality and
display size. An Equalizer application runs unmodified on any visualization
system, from a simple workstation to large scale graphics clusters, multi-GPU
workstations and Virtual Reality installations.

%package -n Equalizer-devel
Group: Development/C
Requires: Equalizer = %{version}-%{release}
Summary: Development files for Equalizer

%description -n Equalizer-devel
%{summary}

%package -n vmmlib-devel
Group: Development/C
Summary: vmmlib

%description -n vmmlib-devel
%{summary}


%package -n Collage
Group: Development/C
Summary: libCollage

%description -n Collage
%{summary}

%package -n Collage-devel
Group: Development/C
Requires: Collage = %{version}-%{release}
Summary: Development files for libCollage

%description -n Collage-devel
%{summary}


%prep
%setup -q
# Remove -Werror
sed -i -e 's, -Werror,,' CMakeLists.txt

# Hack multilibs into cmake configury
find -name '*cmake' -exec grep -li 'DESTINATION lib' {} \; \
| xargs sed -i -e 's,DESTINATION lib,DESTINATION lib${LIB_SUFFIX},' \
libs/client/CMakeLists.txt libs/collage/CMakeLists.txt

# Fix bogus permissions
find \( -type f -a -executable \) -exec chmod -x {} \;

# Dlopen the runtime library, not the devel library.
sed -i -e 's,"libEqualizerServer.so","libEqualizerServer.so.1.0.0",' libs/client/client.cpp

# Hack around cmake configury bug
# Package doesn't build if system's GLEW is sufficiently new.
%if "%{fedora}" != "14"
#mkdir -p include/eq/GL
#cp /usr/include/GL/{glew,glxew,wglew}.h include/eq/GL
%endif
sed -i -e 's,<eq/GL/,<GL/,' `grep -rl 'include *<eq/GL/' .`

%build
%{fedora_cmake} .

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# Nothing much useful inside
rm -rf %{buildroot}%{_datadir}/Equalizer/doc

%if "%{fedora}" == "14"
# Remove bundled static GLEW
rm -f %{buildroot}%{_libdir}/lib*.a
%endif

# Some apps clash with apps provided by other packages
# prefix them with "eq"
for x in %{buildroot}%{_bindir}/*; do
case ${x} in
%{buildroot}%{_bindir}/e*) ;;
%{buildroot}%{_bindir}/osg*) ;;
*) b=$(basename ${x})
   mv ${x} %{buildroot}%{_bindir}/eq${b}
   ;;
esac
done

%files
%doc LICENSE.txt README
%{_bindir}/*
%dir %{_datadir}/Equalizer
%{_datadir}/Equalizer/configs
%{_datadir}/Equalizer/data
%{_libdir}/libEqualizer*.so.*

%files -n Collage
%{_libdir}/libCollage*.so.*

%files -n Collage-devel
%{_includedir}/co
%{_libdir}/libCollage*.so
%{_libdir}/pkgconfig/Collage.pc

%files -n Equalizer-devel
%{_includedir}/eq
%{_libdir}/libEqualizer*.so
%{_libdir}/pkgconfig/Equalizer.pc
%dir %{_datadir}/Equalizer
%doc %{_datadir}/Equalizer/examples

%files -n vmmlib-devel
%{_includedir}/vmmlib

%changelog
* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt4_1.20110922.1
- fixed build

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_1.20110922.1
- cleaned up remnants of eq/GL/* headers

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_1.20110922.1
- use native GL/glew.h instead of eq/GL/glew.h (hack around cmake bugs)

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1_1.20110922.2
- Rebuilt with Boost 1.49.0

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1.20110922.1
- imported from packman.iu-bremen.de

