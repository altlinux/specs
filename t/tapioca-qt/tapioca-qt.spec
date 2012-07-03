Name: tapioca-qt
Version: 0.14.1
%define beta .2109
Release: alt2%beta.2

Summary: A framework for Voice over IP (VoIP) and Instant Messaging (IM)
Group: Networking/Instant messaging
License: LGPLv2+
Url: http://tapioca-voip.sourceforge.net/wiki/index.php/Tapioca
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: %name-%version%beta.tar.bz2


# Automatically added by buildreq on Fri Mar 14 2008 (-bi)
BuildRequires: cmake gcc-c++ libqt4-devel libtelepathy-qt-devel

%description
Tapioca is a framework for Voice over IP (VoIP) and
Instant Messaging (IM). Its main goal is to provide
an easy way for developing and using VoIP and IM
services in any kind of application. It was designed
to be cross-platform, lightweight, thread-safe, having
mobile devices and applications in mind.

Tapioca's main goals are:

* Create a solution that integrates all components
used by VoIP and IM applications in a single, reliable
and easy to use framework, which is able to work on different
platforms.

* Spare resources, providing central services for multiple
applications. Eg.: The control of all incoming and outgoing SIP
requests are managed by the SIP service, avoiding the creation of
one SIP stack and allocation of a network port for each SIP-based
application.

* Reduce the overhead of control layers and library dependencies.

%package -n lib%name
Summary: Development libraries and header files for %name
Group: System/Libraries
Requires: libtelepathy-qt >= 0.14.1
Requires: lib%name = %version-%release
%description -n lib%name
Development libraries and header files for %name.

%package -n lib%name-devel
Summary: Development libraries and header files for %name
Group: Development/KDE and QT
Requires: lib%name = %version-%release
%description -n lib%name-devel
Development libraries and header files for %name.


%prep
%setup -q -n %name-%version


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
%_includedir/QtTapioca/
%_pkgconfigdir/*.pc


%changelog
* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt2.2109.2
- Rebuilt for debuginfo

* Thu Nov 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt2.2109.1
- Rebuilt for soname set-versions

* Mon Mar 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt2.2109
- Snapshot 2109

* Wed Nov 12 2008 Sergey V Turchin <zerg at altlinux dot org> 0.14.1-alt2.2031
- snapshot r2031

* Fri Mar 14 2008 Sergey V Turchin <zerg at altlinux dot org> 0.14.1-alt1
- initial specfile
- remove binary from tarball
