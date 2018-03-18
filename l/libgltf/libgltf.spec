# BEGIN SourceDeps(oneline):
BuildRequires: boost-devel-headers gcc-c++ libpng-devel pkgconfig(cppunit) pkgconfig(gl) pkgconfig(x11)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global major 1
%define libname libgltf%{apiversion}%{major}
%define devname libgltf-devel
%global apiversion 0.1

Name: libgltf
Version: 0.1.0
Release: alt1_2
Summary: A library for rendering glTF models
Group: System/Libraries

License: MPLv2.0
URL: https://wiki.documentfoundation.org/Development/libgltf
Source: http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.gz

BuildRequires: boost-devel
BuildRequires: libglm-devel
BuildRequires: pkgconfig(epoxy)
Source44: import.info

%description
%{name} is a library for rendering glTF models -- development glTF, the GL
Transmission Format, is the runtime asset format for the GL APIs: WebGL,
OpenGL ES, and OpenGL. glTF bridges the gap between formats used by modeling
tools and the GL APIs.

%{name} provides methods to load the OpenGL scene from glTF format and render
it into an existing OpenGL context. %{name} also allows to change the camera
position so the scene can be displayed from different points of view.

%package -n %libname
Summary: A library for rendering glTF models
Group: System/Libraries
Obsoletes: %{_lib}gltf0 >= 0.1.0-1 

%description -n %libname
%{name} is a library for rendering glTF models -- development glTF, the GL
Transmission Format, is the runtime asset format for the GL APIs: WebGL,
OpenGL ES, and OpenGL. glTF bridges the gap between formats used by modeling
tools and the GL APIs.

%{name} provides methods to load the OpenGL scene from glTF format and render
it into an existing OpenGL context. %{name} also allows to change the camera
position so the scene can be displayed from different points of view.


%package -n %devname
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %devname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q


%build
%configure --disable-silent-rules --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/*.la


%files -n %libname
%doc AUTHORS COPYING NEWS
%{_libdir}/%{name}-%{apiversion}.so.%{major}
%{_libdir}/%{name}-%{apiversion}.so.%{major}.*

%files -n %devname
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_2
- new version

