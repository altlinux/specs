%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define _name lensfun
%define ver_major 0.3
%define beta %nil
%define api_ver 1
%define sover %api_ver
%define libname lib%_name%api_ver
%define db_ver %api_ver

%def_enable lenstool
%def_enable python
%def_enable tests
%def_enable check

Name: %_name
Version: %ver_major.3
Release: alt1%beta

Summary: Tools and library to rectifying the defects introduced by your photographic equipment.
Group: System/Libraries
License: LGPLv3 and CC-BY-SA-3.0
Url: https://lensfun.github.io

Vcs: https://github.com/lensfun/lensfun.git
Source: %_name-%version.tar

Patch1: lensfun-0.3.2-alt-pkexec.patch

%filter_from_provides /pkgconfig(lensfun)/d
%filter_from_provides /python3(lensfun)/d

Requires: %_name-tools = %EVR

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: cmake gcc-c++ libgomp-devel
BuildRequires: glib2-devel libpng-devel
BuildRequires: doxygen
BuildRequires: python3-devel python3-module-setuptools python3-module-docutils
%{?_enable_check:BuildRequires: ctest}

%description
Lensfun provides open source database of photographic lenses, tools and
library that also provides a way to read the database and search for
specific things in it, and provides a set of algorithms for correcting
images based on detailed knowledge of lens properties. Right now Lensfun
is designed to correct distortion, transversal (also known as lateral)
chromatic aberrations, and vignetting.

%package -n %libname
Summary: A library to rectifying the defects introduced by your photographic equipment.
Group: System/Libraries
Requires: %_name-data = %EVR

%description -n %libname
A library to rectifying the defects introduced by your photographic equipment.

%package -n %libname-devel
Summary: Development tools for programs which will use the Lensfun library
Group: Development/C++
Requires: %libname = %EVR
Conflicts: lib%_name > %version

%description -n %libname-devel
Development tools for programs which will use the Lensfun library.

%package -n %_name-data
Summary: Lensfun database (version %db_ver)
Group: Graphics
License: LGPLv3
BuildArch: noarch

%description -n %_name-data
This package contains lens data in XML format used by Lensfun.

%package tools
Summary: Lensfun tools for managing lens data
Group: Graphics
License: LGPLv3
BuildArch: noarch
Requires: %libname = %EVR
Conflicts: lib%_name-tools > %version

%description tools
This package contains tools to fetch lens database, updates and manage lens
adapters in Lensfun.

%package -n python3-module-%_name
Group: Development/Python3
Summary: Lensfun Python3 module
BuildArch: noarch
Requires: %_name-data = %EVR

%description -n python3-module-%_name
This is Lensfun Python3 module that provides common functionality for Python
scripts that want to find or read the Lensfun database.

%prep
%setup -n %_name-%version
%patch1 -p2

%build
%add_optflags %(getconf LFS_CFLAGS)

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
%ifnarch %ix86 x86_64
	-DBUILD_FOR_SSE:BOOL=OFF \
	-DBUILD_FOR_SSE2:BOOL=OFF \
%endif
	-DBUILD_DOC:BOOL=ON \
	%{?_enable_lenstool:-DBUILD_LENSTOOL=ON} \
	%{?_enable_tests:-DBUILD_TESTS:BOOL=ON} \
	%{?_disable_python:-DINSTALL_PYTHON_MODULE=OFF}
%nil

%cmake_build
%cmake_build -t man

%install
%cmake_install
pushd %_cmake__builddir/apps/
%python3_install
popd

%check
%cmake_build -t test

%files
%{?_enable_lenstool:%_bindir/lenstool}

%files tools
%_bindir/g-%_name-update-data
%_bindir/%_name-add-adapter
%_bindir/%_name-update-data
#%_bindir/%_name-convert-lcp
%python3_sitelibdir_noarch/%{_name}*
%_man1dir/*

%files -n %libname
%_libdir/lib%_name.so.%sover
%_libdir/lib%_name.so.%version
%doc ChangeLog README.*

%files -n %libname-devel
%_includedir/%_name/
%_libdir/lib%_name.so
%_pkgconfigdir/%_name.pc
%doc %_datadir/doc/%{_name}*/

%files -n %_name-data
%dir %_datadir/%_name/
%_datadir/%name/version_%api_ver/

%changelog
* Tue Feb 21 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- stable 0.3.3 from new srpm
- new lensfun-data subpackage
- enabled %%check

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.3.2-alt5.1
- NMU: spec: adapted to new cmake macros.

* Thu Apr 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt5
- Replaced gksudo with pkexec.

* Tue Feb 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt4
- Fixed build.

* Fri Aug 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt3
- NMU: rebuilt with new python3-module-docutils.

* Tue Apr 12 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.2-alt2
- fix build on non-x86 arches

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Fri Nov 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0
- removed obsolete patches
- new -tools subpackage

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.8-alt1
- 0.2.8
- removed old patches

* Fri Dec 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6 (ALT #28197)
- removed obsolete (fixed by upstream) patches

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt3.2
- Fixed build with libpng15

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt3.1
- Rebuilt for debuginfo

* Wed Dec 08 2010 Victor Forsiuk <force@altlinux.org> 0.2.5-alt3
- Apply PLD patch that fixes bug (broken vectorization) caused SIGSEGV in ufraw.
  SSE vectorization enabled in this build.

* Mon Aug 16 2010 Victor Forsiuk <force@altlinux.org> 0.2.5-alt2
- Disable SSE vectorization to avoid crashes until upstream fix this code.
- Add lens data for Nikkor 50mm F/1.8 D and Nikkor 18-105mm F/3.5-5.6.

* Fri Apr 02 2010 Victor Forsiuk <force@altlinux.org> 0.2.5-alt1
- 0.2.5

* Tue Dec 01 2009 Victor Forsyuk <force@altlinux.org> 0.2.4-alt1
- 0.2.4

* Fri Oct 09 2009 Victor Forsyuk <force@altlinux.org> 0.2.3-alt5
- Added patch by Dmitry Levin to fix problematic source that was
  compiled into wrong code by gcc 4.4.

* Fri Aug 07 2009 Victor Forsyuk <force@altlinux.org> 0.2.3-alt4
- Compile with gcc 4.3.

* Tue Jun 30 2009 Victor Forsyuk <force@altlinux.org> 0.2.3-alt3
- Fix FTBFS with GCC 4.4.

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 0.2.3-alt2
- Remove obsolete ldconfig calls.

* Mon Oct 20 2008 Victor Forsyuk <force@altlinux.org> 0.2.3-alt1
- 0.2.3

* Wed Sep 03 2008 Victor Forsyuk <force@altlinux.org> 0.2.2b-alt2
- Package lensfun.pc.

* Fri Aug 22 2008 Victor Forsyuk <force@altlinux.org> 0.2.2b-alt1
- Initial build.
