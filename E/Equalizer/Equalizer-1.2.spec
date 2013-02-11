# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ perl(Env.pm)
BuildRequires: gcc4.6-c++
# END SourceDeps(oneline)
%define fedora 16
Name:		Equalizer
Version:	1.2.1
Release:	alt1.2
Summary:	Middleware to create and deploy parallel OpenGL-based applications

Group:		Development/C
License:	LGPLv2+
URL:		http://www.equalizergraphics.com/
Source0:	http://www.equalizergraphics.com/downloads/%{name}-%{version}.tar.gz

BuildRequires:	ctest cmake bison flex
BuildRequires:  boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel libglew-devel
BuildRequires:  libX11-devel libGL-devel
BuildRequires:  libOpenSceneGraph-devel >= 2.9.8

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


%package -n libSequel
Group: Development/C
Summary: libSequel

%description -n libSequel
libSequel provides a simple programming interface
to the Equalizer parallel rendering framework.

%package -n libSequel-devel
Group: Development/C
Requires: libSequel = %{version}-%{release}
Summary: Development files for libSequel

%description -n libSequel-devel
%{summary}


%prep
%setup -q
# Remove -Werror
sed -i -e 's, -Werror,,' CMakeLists.txt

# Fix bogus permissions
find \( -type f -a -executable \) -exec chmod -x {} \;

# Dlopen the runtime library, not the devel library.
sed -i -e 's,"libEqualizerServer.so","libEqualizerServer.so.%version",' libs/eq/client/client.cpp

# Hack around cmake configury bug
# Package doesn't build if system's GLEW is sufficiently new.
%if "%{fedora}" != "14"
#mkdir -p include/eq/GL
#cp /usr/include/GL/{glew,glxew,wglew}.h include/eq/GL
%endif
sed -i -e 's,<eq/GL/,<GL/,' `grep -rl 'include *<eq/GL/' .`

%build
export CC=gcc-4.6
export CXX=g++-4.6
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

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

if ! [ -e %buildroot%_libdir/libEqualizerServer.so.%version ]; then
	echo replace in sed: libEqualizerServer.so.%version with real soname
	exit 1
fi

%files
%doc LICENSE.txt README
%{_bindir}/*
%dir %{_datadir}/Equalizer
%{_datadir}/Equalizer/configs
%{_datadir}/Equalizer/data
%{_libdir}/libEqualizer*.so.*
#files -n libSequel
%{_libdir}/libSequel*.so.*

%files -n Collage
%{_libdir}/libCollage*.so.*

%files -n Collage-devel
%{_includedir}/co
%{_libdir}/libCollage*.so
%{_libdir}/pkgconfig/Collage.pc
%{_datadir}/CMake/Modules/FindCollage.cmake

%files -n Equalizer-devel
%{_includedir}/eq
%{_libdir}/libEqualizer*.so
%{_libdir}/pkgconfig/Equalizer.pc
%dir %{_datadir}/Equalizer
%doc %{_datadir}/Equalizer/examples
%{_datadir}/CMake/Modules/FindEqualizer.cmake
#files -n libSequel-devel
%{_includedir}/seq
%{_libdir}/libSequel*.so
#%{_libdir}/pkgconfig/Sequel.pc


%files -n vmmlib-devel
%{_includedir}/vmmlib

%changelog
* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1.2
- Rebuilt with Boost 1.53.0

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.1
- Rebuilt with Boost 1.52.0

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1
- updated to release-1.2.1 upstream git tag
- TODO: drop gcc4.6 and update to 1.3.7 git tag
  (requires http://eyescale.github.com/Lunchbox-1.4.0/index.html)

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt5_1.20110922.1
- rebuild with new boost

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

