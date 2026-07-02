%define _unpackaged_files_terminate_build 1
%def_with opencv

# The gavl library is not available for i586:
# https://github.com/bplaum/gavl/issues/16
%ifarch %ix86
%def_without gavl
%else
%def_with gavl
%endif

Name: frei0r-plugins
Version: 3.2.3
Release: alt1

Summary: A free software collection of video effect plugins
License: GPL-2.0-or-later
Group: Video
Url: https://frei0r.dyne.org
Vcs: https://github.com/dyne/frei0r.git

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: libcairo-devel
%{?_with_opencv:BuildRequires: libopencv-devel}
%{?_with_gavl:BuildRequires: libgavl-devel}

%description
The frei0r project is a collection of free and open
source video effects plugins that can be used with
a variety of video editing and processing software.

%package -n frei0r-devel
Summary: Development files for %name
Group: Development/C

%description -n frei0r-devel
Frei0r - a minimalistic plugin API for video effects.

%if_with opencv
%package opencv
Summary: Frei0r plugins using OpenCV
Group: Video
Requires: libopencv-utils

%description opencv
Frei0r plugins that use the OpenCV computer vision framework.
%endif

%prep
%setup
%patch0 -p1

%ifarch %e2k
# error: incompatible types when assigning to type ‘__m128’ from type ‘__m128i’
# This code doesn't compile with -msse4.1 even using GCC on x86_64.
sed -i 's/defined(__SSE4_1__)/0/' src/filter/tint0r/tint0r.c
%endif

%build
%cmake \
	%{?_without_opencv:-DWITHOUT_OPENCV:BOOL=ON} \
	%{?_without_gavl:-DWITHOUT_GAVL:BOOL=ON} \
	%nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%dir %_libdir/frei0r-1
%_libdir/frei0r-1/*.so
%if_with opencv
%exclude %_libdir/frei0r-1/facebl0r.so
%exclude %_libdir/frei0r-1/facedetect.so
%endif

%files -n frei0r-devel
%_includedir/frei0r.h
%_includedir/frei0r.hpp
%_includedir/frei0r/
%_pkgconfigdir/frei0r.pc

%if_with opencv
%files opencv
%dir %_libdir/frei0r-1
%_libdir/frei0r-1/facebl0r.so
%_libdir/frei0r-1/facedetect.so
%endif

%changelog
* Thu Jul 02 2026 Anton Farygin <rider@altlinux.org> 3.2.3-alt1
- 3.2.2 -> 3.2.3

* Wed Jun 24 2026 Anton Farygin <rider@altlinux.org> 3.2.2-alt1
- 3.2.1 -> 3.2.2

* Thu Jun 18 2026 Anton Farygin <rider@altlinux.org> 3.2.1-alt1
- 3.1.3 -> 3.2.1

* Wed Apr 29 2026 Anton Farygin <rider@altlinux.org> 3.1.3-alt1
- 3.1.2 -> 3.1.3

* Thu Apr 16 2026 Ajrat Makhmutov <rauty@altlinux.org> 3.1.2-alt1
- New version.

* Wed Apr 09 2026 Ajrat Makhmutov <rauty@altlinux.org> 3.0.0-alt1
- New version.
- Add check section.

* Mon Apr 06 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.5.6-alt3
- e2k build fix

* Wed Mar 25 2026 Grant Makyan <karonus@altlinux.org> 2.5.6-alt2
- Use libgavl for non i586 build.

* Wed Mar 25 2026 Ajrat Makhmutov <rauty@altlinux.org> 2.5.6-alt1
- New version.

* Wed Feb 25 2026 Ajrat Makhmutov <rauty@altlinux.org> 2.5.4-alt1
- New version.

* Wed Dec 03 2025 Ajrat Makhmutov <rauty@altlinux.org> 2.5.1-alt1
- New version.

* Tue Oct 21 2025 Ajrat Makhmutov <rauty@altlinux.org> 2.5.0-alt1
- New version.

* Thu Sep 04 2025 Ajrat Makhmutov <rauty@altlinux.org> 2.4.0-alt1
- New version.

* Fri Jun 07 2024 Ajrat Makhmutov <rauty@altlinux.org> 2.3.3-alt1
- New version.
- Don't require plugins for frei0r-devel.
- Correct the summary of the frei0r-plugins.

* Thu May 02 2024 Ajrat Makhmutov <rauty@altlinux.org> 2.3.2-alt2
- Rename the facedetect subpackage to opencv.
- Don't require other plugins for frei0r-plugins-opencv.
- New code documentation in frei0r-devel-doc.
- Correct the descriptions of frei0r-plugins and frei0r-devel.

* Fri Apr 26 2024 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- updated to v2.3.2-16-gfdc9f32 (ported to CMake build system)

* Tue Apr 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.0-alt2
- Rebuilt with opencv-4.3.0.

* Fri Jan 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.7.0-alt1
- 1.7.0

* Wed Oct 03 2018 Alexey Shabalin <shaba@altlinux.org> 1.6.1-alt2
- fix build with opencv >= 3.4.2

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.1-alt1.2
- NMU: rebuilt with opencv-3.4.

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 1.6.1-alt1.1
- BOOTSTRAP: introduce opencv knob (on by default)
- minor spec cleanup

* Tue Jun 20 2017 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 1.5-alt1
- 1.5

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.4-alt2.qa1
- Rebuilt for gcc5 C++11 ABI.

* Tue Oct 08 2013 Alexey Shabalin <shaba@altlinux.ru> 1.4-alt2
- build plugins cairogradient, cairoimagegrid, cairoaffineblend, cairoblend
- fixed files for facedetect package

* Fri Oct 04 2013 Alexey Shabalin <shaba@altlinux.ru> 1.4-alt1
- 1.4

* Tue Oct 02 2012 Alexey Shabalin <shaba@altlinux.ru> 1.3-alt3
- rebuild with new libopencv

* Mon Dec 19 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3-alt2
- rebuild with new libopencv

* Mon Apr 04 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3-alt1
- 1.3
- rebuild with new libopencv

* Thu Nov 25 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- 1.2.1
- build with libopencv2 (tnx to real@)

* Wed Sep 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2-alt1
- 1.2

* Fri Dec 04 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.22-alt2.git7a5488
- split facedetect package

* Mon Nov 30 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.22-alt1.git7a5488
- 1.1.22 + git 2009-11-09
- update Summary, URL, description
- change Packager
- add frei0r-devel package
- add frei0r-devel-doc package
- update buildreq

* Mon Nov 10 2008 Led <led@altlinux.ru> 1.1.19-alt3
- fixed build with g++ 4.3

* Sat Mar 15 2008 Led <led@altlinux.ru> 1.1.19-alt2
- moved to %%_libexecdir/%%bname-%%major_ver/
- fixed License

* Wed May 30 2007 Led <led@altlinux.ru> 1.1.19-alt1
- initial build
