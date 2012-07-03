Name: libface
Version: 0.1
Release: alt1.2
Summary: Face recognition library
License: GPLv2
Group: System/Libraries
Url: http://libface.sourceforge.net/
Packager: Aeliya Grevnyov <gray_graff@altlinux.org>

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ libopencv-devel doxygen

%description
Libface is a library aimed at bringing face recognition technology to the open source community.

%package devel
Group: Development/C++
Summary: Devel files for %name
%description devel
Devel files for %name

%prep
%setup

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_CXX_FLAGS:STRING='%optflags'
%make_build

%install
%makeinstall DESTDIR="%buildroot/" install

%files
%_libdir/%name.so*

%files devel
%_pkgconfigdir/%name.pc
%_includedir/%name
%_datadir/CMake/Modules/FindLibFace.cmake

%changelog
* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1.2
- rebuild with rpm optflags

* Sun Aug 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Rebuilt with OpenCV 2.3.1

* Thu Jun 30 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 0.1-alt1
- Initial build for sysiphus

