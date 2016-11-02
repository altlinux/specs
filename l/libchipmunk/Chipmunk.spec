Name: libchipmunk
Version: 7.0.1
Release: alt1
Summary: Physics engine for 2D games

Group: System/Libraries
License: MIT
Url: http://chipmunk-physics.net
Source0: http://files.slembcke.net/chipmunk/release/Chipmunk-%version.tgz
Patch: Chipmunk-6.1.5-alt-build-shared-demos.patch

# Automatically added by buildreq on Sun Mar 03 2013
# optimized out: cmake-modules libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libstdc++-devel xorg-kbproto-devel xorg-xproto-devel
BuildRequires: cmake gcc-c++ libGLUT-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86vm-devel libxkbfile-devel xorg-xf86miscproto-devel libglew-devel libglfw-devel

%description
Chipmunk is a 2D rigid body physics library distributed under the MIT
license. Though not yet complete, it is intended to be fast, numerically
stable, and easy to use.

%package devel
Summary: Development tools for programs which will use the chipmunk library
Group: Development/C
Requires: %name = %version-%release

%description devel
Chipmunk is a 2D rigid body physics library distributed under the MIT
license. Though not yet complete, it is intended to be fast, numerically
stable, and easy to use.

This package contains the header files and  static libraries to develop
programs that will use the chipmunk library.  You should install this
package if you need to develop programs which will use the chipmunk
library functions.  You'll also need to install the chipmunk package.

%package demos
Summary: Demo binary and source for %name
Group: Development/C
%description demos
Demo binary and source for %name

%prep
%setup -n Chipmunk-%version
#patch -p1

%build
%add_optflags -DCHIPMUNK_FFI
sed -i 's@target_link_libraries(chipmunk m)@target_link_libraries(chipmunk m pthread)@' src/CMakeLists.txt

%cmake -DBUILD_STATIC=False -DINSTALL_STATIC=False -DINSTALL_DEMOS=True
%make_build -C BUILD

%install
%makeinstall -C BUILD DESTDIR=$RPM_BUILD_ROOT

%files
%doc *.txt README.*
%_libdir/*.so.*

%files devel
%doc doc/
%_includedir/chipmunk
%_libdir/*.so

%files demos
%doc demo/
%_bindir/*

%changelog
* Wed Nov 02 2016 Fr. Br. George <george@altlinux.ru> 7.0.1-alt1
- Autobuild version bump to 7.0.1
- Fix build

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 6.2.2-alt1
- Autobuild version bump to 6.2.2

* Thu Oct 17 2013 Fr. Br. George <george@altlinux.ru> 6.2.1-alt2
- Resurrect lost index.html

* Wed Oct 16 2013 Fr. Br. George <george@altlinux.ru> 6.2.1-alt1
- Autobuild version bump to 6.2.1
- Fix build

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 6.1.5-alt1
- Autobuild version bump to 6.1.5
- Fix patches

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 6.1.4-alt1
- Autobuild version bump to 6.1.4
- Fix cmake

* Sun Mar 03 2013 Fr. Br. George <george@altlinux.ru> 6.1.3-alt2
- Export some interlnal functions

* Sun Mar 03 2013 Fr. Br. George <george@altlinux.ru> 6.1.3-alt1
- Autobuild version bump to 6.1.3

* Sun Mar 03 2013 Fr. Br. George <george@altlinux.ru> 6.1.2-alt1
- Initial build from FC

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Jon Ciesla <limb@jcomserv.net> - 5.3.4-1
- latest upstream.

* Fri Aug 20 2010 Jon Ciesla <limb@jcomserv.net> - 5.3.1-1
- latest upstream.

* Thu Jul 15 2010 Jon Ciesla <limb@jcomserv.net> - 5.2.0-1
- Latest upstream, BZ 545475.
- Dropped cmake patch, updated dsolink patch.
- Dropped ruby extension for now, not up to date per upstream.

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 4.1.0-9
- Fix FTBFS, BZ 599950.

* Thu Oct  1 2009 Hans de Goede <hdegoede@redhat.com> - 4.1.0-8
- Fix FTBFS

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Jon Ciesla <limb@jcomserv.net> - 4.1.0-6
- ruby extension fix, BZ 489187.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 08 2009 Jon Ciesla <limb@jcomserv.net> - 4.1.0-4
- Attempted 64-bit fix.

* Wed Jan 07 2009 Jon Ciesla <limb@jcomserv.net> - 4.1.0-3
- Review fixes.

* Wed Jan 07 2009 Jon Ciesla <limb@jcomserv.net> - 4.1.0-2
- Review fixes.

* Mon Dec 01 2008 Jon Ciesla <limb@jcomserv.net> - 4.1.0-1
- New version.

* Mon Sep 15 2008 Jon Ciesla <limb@jcomserv.net> - 4.0.2-1
- Created package.
