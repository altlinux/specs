Name: telepathy-qt
Version: 0.14.1
Release: alt3

Group: System/Libraries
Summary: Telepathy framework - qt connection manager library
Url: http://telepathy.freedesktop.org/wiki/Telepathyqt
License: LGPL

Source0: http://telepathy.freedesktop.org/releases/telepathy-qt/%name-%version.tar.gz
Packager: Sergey V Turchin <zerg at altlinux dot org>

# Automatically added by buildreq on Fri Mar 14 2008 (-bi)
#BuildRequires: cmake gcc-c++ libqt3-devel libtelepathy-qt-devel
BuildRequires: cmake gcc-c++ libqt4-devel

%description
This package contains Qt-based library for Telepathy components.

%package -n lib%name
Summary: Telepathy framework - Qt connection manager library
Group: System/Libraries
%description -n lib%name
This package contains Qt-based library for Telepathy components.

%package -n lib%name-devel
Summary: Development libraries and header files for %name
Group: Development/KDE and QT
Requires: lib%name = %version-%release
%description -n lib%name-devel
Development libraries and header files for %name.


%prep
%setup -q


%build
%define _optlevel s
#add_optflags -DNDEBUG
%define lib_suffix %nil
%ifarch x86_64 ppc64
%define lib_suffix 64
%endif
mkdir -p %_target_platform
pushd %_target_platform
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DCMAKE_C_FLAGS_RELEASE:STRING='%optflags' \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING='%optflags' \
    -DLIB_DESTINATION=%_lib \
    -DLIB_SUFFIX=%lib_suffix
popd

%make_build -C %_target_platform VERBOSE=1

%install
%make -C %_target_platform DESTDIR=%buildroot install


%files -n lib%name
%doc AUTHORS
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_includedir/QtTelepathy/

%changelog
* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt3
- Rebuilt for debuginfo

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt2
- Rebuilt for soname set-versions

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.14.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libtelepathy-qt
  * postun_ldconfig for libtelepathy-qt
  * postclean-05-filetriggers for spec file

* Fri Mar 14 2008 Sergey V Turchin <zerg at altlinux dot org> 0.14.1-alt1
- initial specfile
