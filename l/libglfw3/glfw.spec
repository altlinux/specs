Name: libglfw3
Version: 3.2.1
Release: alt1
Summary: A cross-platform multimedia library
License: zlib
Group: System/Libraries
Url: http://www.glfw.org/index.html
Source: glfw-%version.tar.bz2
Obsoletes: libglfw = 3.0.2

# Automatically added by buildreq on Wed Oct 16 2013
# optimized out: cmake-modules libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel
BuildRequires: cmake doxygen glibc-devel-static libGLU-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxkbfile-devel libxkbcommon-devel
BuildRequires:  libvulkan-devel
BuildRequires:  libwayland-client-devel libwayland-cursor-devel libwayland-server-devel wayland-devel

%description
GLFW is a free, Open Source, multi-platform library for OpenGL
application development that provides a powerful API for handling
operating system specific tasks such as opening an OpenGL window,
reading keyboard, mouse, joystick and time input, creating threads, and
more.

%package devel
Summary: Support for developing C application
Requires: %name =  %version-%release
Group: Development/C
Obsoletes: libglfw-deevel = 3.0.2
Provides: libglfw-devel = %version
Provides: glfw-devel = %version
#Requires: xorg-x11-proto-devel

%description devel
The glfw-devel package contains header files for developing glfw
applications.

%prep
%setup -n glfw-%version
find . -type f | xargs sed -i 's/\r//'

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=ON
%make_build -C BUILD all

%install
%makeinstall -C BUILD DESTDIR=%buildroot PREFIX=%prefix LIBDIR=%_lib

%files
%doc README.md COPYING.txt
%_libdir/libglfw.so.*

%files devel
%_includedir/GLFW
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_libdir/cmake/glfw3/*.cmake

%changelog
* Sat Mar 17 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1
- NMU: updated to 3.2.1

* Wed Oct 16 2013 Fr. Br. George <george@altlinux.ru> 3.0.3-alt2
- Move include files into /usr/include/GL
- Rename package for 2.x version compatibility

* Wed Oct 16 2013 Fr. Br. George <george@altlinux.ru> 3.0.3-alt1
- Autobuild version bump to 3.0.3

* Wed Oct 16 2013 Fr. Br. George <george@altlinux.ru> 3.0.2-alt1
- Initial build from FC

* Sat Aug 10 2013 "Jonathan Mercier" <"Jonathan Mercier at gmail dot org"> - 3.0-0.27.20130807git735bc2d
- Update to rev 735bc2d

* Sun Aug 04 2013 "Jonathan Mercier" <"Jonathan Mercier at gmail dot org"> - 3.0-0.26.20130730git63a191e
- Update to rev 63a191e

* Mon Jul 29 2013 Ville Skyttä <ville.skytta@iki.fi> - 3.0-0.25.20130626git2656bf8
- Drop unnecessary doc dir removal from %%install.

* Wed Jun 26 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.24.20130626git2656bf8
- Update to rev 2656bf8

* Mon Jun 24 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.23.20130624git4883073
- Update to rev 4883073

* Sun Jun 23 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.22.20130621git6591579
- Update to rev 6591579

* Sun Jun 09 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.21.20130609git52354bf
- Update to rev 52354bf

* Sun Jun 09 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.20.20130609git68b7ea8
- Update to rev 68b7ea8

* Fri May 24 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.19.20130523git98cbf6f
- Update to rev 98cbf6f

* Sat May 18 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.18.20130517git673d5b5
- put  libXrandr as required

* Fri May 17 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.17.20130517git673d5b5
- Update to rev 673d5b5

* Fri May 17 2013  <bioinfornatics at fedoraproject dot org> - 3.0-0.16.20130514gite20e8f9
- Update to rev e20e8f9

* Thu May 16 2013  <bioinfornatics at fedoraproject dot org> - 3.0-0.15.20130514gite20e8f9
- Update to rev e20e8f9

* Thu May 16 2013  <bioinfornatics at fedoraproject dot org> - 3.0-0.14.20130514gite20e8f9
- Update to rev e20e8f9

* Wed May 15 2013  <bioinfornatics at fedoraproject dot org> - 3.0-0.13.20130514gite20e8f9
- Update to rev e20e8f9

* Wed May 15 2013 Jonathan MERCIER - 3.0-0.12.20130502git475d10d
- Install .cmake file

* Thu May 09 2013 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-0.11.20130502git475d10d
- Update to rev 475d10d

* Tue May 07 2013 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-0.10.20120703git14c6978
- Update to rev 14c6978

* Tue May 07 2013 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-0.9.20120703gita9ed5b1
- Update to rev 14c6978

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.8.20120812gita9ed5b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-0.7.20120812gita9ed5b1
- Fix both release/version format

* Fri Sep 21 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-6
- use %%{_prefix} instead of /usr
- remove this (debug?) line

* Fri Sep 21 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-5
- fix spec file

* Mon Aug 13 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-4
- update ti latest rev #a9ed5b1

* Mon Aug 13 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-3
- rebuilt

* Sat Aug 11 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-2
- Update and Fix glfw3

* Wed Apr 18 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0.0-1
- Initial release
