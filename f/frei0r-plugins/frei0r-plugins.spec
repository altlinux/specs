%define _unpackaged_files_terminate_build 1
%def_with opencv

Name: frei0r-plugins
Version: 2.3.3
Release: alt1

Summary: A free software collection of video effect plugins
License: GPL-2.0-or-later
Group: Video
Url: https://frei0r.dyne.org
Vcs: https://github.com/dyne/frei0r.git

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: libcairo-devel
%{?_with_opencv:BuildRequires: libopencv-devel}

%description
The frei0r project is a collection of free and open
source video effects plugins that can be used with
a variety of video editing and processing software.

%package -n frei0r-devel
Summary: Development files for %name
Group: Development/C

%description -n frei0r-devel
Frei0r - a minimalistic plugin API for video effects.

%package -n frei0r-devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description -n frei0r-devel-doc
This package contains development documentation for %name.

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

%build
%cmake \
	%{?_without_opencv:-DWITHOUT_OPENCV:BOOL=ON} \
	%nil
%cmake_build

pushd doc
doxygen Doxyfile
popd

%install
%cmake_install

%files
%dir %_libdir/frei0r-1
%_libdir/frei0r-1/*.so
%if_with opencv
%exclude %_libdir/frei0r-1/facebl0r.so
%exclude %_libdir/frei0r-1/facedetect.so
%endif

%files -n frei0r-devel
%_includedir/frei0r.h
%_pkgconfigdir/frei0r.pc

%files -n frei0r-devel-doc
%doc doc/html

%if_with opencv
%files opencv
%dir %_libdir/frei0r-1
%_libdir/frei0r-1/facebl0r.so
%_libdir/frei0r-1/facedetect.so
%endif

%changelog
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
- moved to %_libexecdir/%bname-%major_ver/
- fixed License

* Wed May 30 2007 Led <led@altlinux.ru> 1.1.19-alt1
- initial build
