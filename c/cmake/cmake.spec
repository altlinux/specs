Name: cmake
Version: 2.8.8
Release: alt3

Summary: Cross-platform, open-source make system

License: BSD
Group: Development/Tools
Url: http://cmake.org/

Packager: Andrey Rahmatullin <wrar@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: bzlib-devel gcc-c++ libarchive-devel >= 2.8.4
BuildPreReq: libcurl-devel libexpat-devel libncurses-devel libqt4-devel libxml2-devel
BuildRequires(pre): shared-mime-info rpm-build-vim
%{?!_without_check:%{?!_disable_check:BuildRequires: /proc gcc-fortran java-devel cvs subversion mercurial git-core}}

Obsoletes: cpack < 2.4.5-alt3
Provides: cpack = %version-%release

Requires: %name-modules = %version-%release
Requires: rpm-macros-%name = %version-%release

%define _unpackaged_files_terminate_build 1

%add_findreq_skiplist %_datadir/CMake/Templates/cygwin-package.sh.in


%description
CMake is used to control the software compilation process using
simple platform and compiler independent configuration files.
CMake generates native makefiles and workspaces that can be
used in the compiler environment of your choice. CMake is quite
sophisticated: it is possible to support complex environments
requiring system configuration, pre-processor generation, code
generation, and template instantiation.


%package modules
Summary: Standard CMake modules
Group: Development/Tools
BuildArch: noarch

%description modules
CMake is used to control the software compilation process using
simple platform and compiler independent configuration files.

This package contains the standard modules from the CMake distribution.


%package -n ccmake
Summary: Curses interface for CMake
Group: Development/Tools
Requires: %name = %version-%release

%description -n ccmake
The "ccmake" executable is the CMake curses interface. Project
configuration settings may be specified interactively through this GUI.
Brief instructions are provided at the bottom of the terminal when the
program is running.


%package -n ctest
Summary: CMake test driver program
Group: Development/Tools
Requires: %name = %version-%release

%description -n ctest
The ctest executable is the CMake test driver program. CMake-generated
build trees created for projects that use the ENABLE_TESTING and
ADD_TEST commands have testing support. This program will run the tests
and report results.


%package gui
Summary: Qt interface for CMake
Group: Development/Tools
Requires: %name = %version-%release

%description gui
The "cmake-gui" executable is the CMake GUI.  Project configuration settings
may be specified interactively.  Brief instructions are provided at the
bottom of the window when the program is running.


%package doc
Summary: CMake docs
Group: Documentation
BuildArch: noarch

%description doc
This package contains CMake docs in DocBook, html and txt formats.


%package -n vim-plugin-%name
Summary: Vim plugins for CMake files
Group: Editors
BuildArch: noarch

%description -n vim-plugin-%name
This package contains updated indent and syntax Vim plugins for CMake files.


%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging applications that use cmake
Group: Development/Other
Conflicts: cmake = 2.8.0-alt1
Conflicts: rpm-build-compat <= 1.5.1-alt1

%description -n rpm-macros-%name
Set of RPM macros for packaging applications that use cmake.


%prep
%setup
%patch -p1
sed -i 's,SET(BUILD_SHARED_LIBS OFF),SET(BUILD_SHARED_LIBS ON),' CMakeLists.txt

%build
mkdir build
pushd build

CFLAGS="%optflags" CXXFLAGS="%optflags" ../bootstrap \
	--system-libs \
	--qt-gui \
	--prefix=%prefix \
	--datadir=/share/CMake \
	--mandir=/share/man \
	--docdir=/share/doc/%name-%version

export LD_LIBRARY_PATH=$PWD/Source:$PWD/Source/kwsys/:$PWD/Source/CursesDialog/form
%make_build VERBOSE=1
popd


%install
pushd build
export LD_LIBRARY_PATH=$PWD/Source:$PWD/Source/kwsys/:$PWD/Source/CursesDialog/form
%makeinstall_std
popd
install -m644 ChangeLog.manual %buildroot%_docdir/%name-%version
mv %buildroot/usr/lib %buildroot%_libdir || :
for i in 32 128; do
    install -pD -m644 Source/QtDialog/CMakeSetup$i.png %buildroot%_iconsdir/hicolor/${i}x$i/apps/CMakeSetup.png
done
mkdir -p %buildroot{%vim_indent_dir,%vim_syntax_dir}
install -m644 Docs/cmake-indent.vim %buildroot%vim_indent_dir/%name.vim
install -m644 Docs/cmake-syntax.vim %buildroot%vim_syntax_dir/%name.vim
install -pD -m644 %name.macros %buildroot%_rpmmacrosdir/%name

install -p  build/Source/kwsys/libcmsys.so  %buildroot%_libdir/libcmsys.so
install -p  build/Source/kwsys/libcmsys_c.so  %buildroot%_libdir/libcmsys_c.so

%check
# CTest.UpdateGIT fails, see #20884
unset GIT_DIR
unset GIT_INDEX_FILE
unset GIT_OBJECT_DIRECTORY
pushd build
export LD_LIBRARY_PATH=%buildroot%_libdir
%make test ARGS="--output-on-failure -E CTestTestUpload"
popd


%files
%_bindir/cmake
%_bindir/cpack
%_libdir/libCMakeLib.so
%_libdir/libCPackLib.so
%_libdir/libcmcompress.so
%_libdir/libcmsys.so
%_libdir/libcmsys_c.so
%_datadir/CMake/
%_aclocaldir/*
%_man1dir/cmake*.*
%_man1dir/cpack.*
%dir %_docdir/%name-%version/
%_docdir/%name-%version/ChangeLog.manual
%_docdir/%name-%version/Copyright.txt
%_docdir/%name-%version/cmcompress/
%_docdir/%name-%version/cmsys/
%exclude %_datadir/CMake/Modules/

%files modules
%dir %_datadir/CMake/
%_datadir/CMake/Modules/


%files -n ccmake
%_bindir/ccmake
%_libdir/libcmForm.so
%_man1dir/ccmake.*


%files -n ctest
%_bindir/ctest
%_libdir/libCTestLib.so
%_man1dir/ctest.*


%files gui
%_bindir/cmake-gui
%_desktopdir/CMake.desktop
%_xdgmimedir/packages/cmakecache.xml
%_iconsdir/*/*/*/CMakeSetup.png
%_pixmapsdir/*


%files doc
%dir %_docdir/%name-%version
%_docdir/%name-%version/ccmake.*
%_docdir/%name-%version/cmake*
%_docdir/%name-%version/cpack*
%_docdir/%name-%version/ctest.*


%files -n vim-plugin-%name
%vim_indent_dir/*
%vim_syntax_dir/*


%files -n rpm-macros-%name
%_rpmmacrosdir/*


%changelog
* Wed Jun 27 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.8-alt3
- Really fix FindPkgConfig.cmake regression (closes: #27499)

* Mon Jun 25 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.8-alt2
- Fix FindPkgConfig.cmake regression (closes: #27499)

* Sat Jun 23 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.8-alt1
- 2.8.8
- add %%cmake_build, %%cmake_install and %%cmakeinstall_std macros (closes: #24229)

* Tue Jan 24 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.7-alt1
- 2.8.7

* Sat Oct 08 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.6-alt1
- 2.8.6

* Sat Jul 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.5-alt1
- 2.8.5
- Disable test CTestTestUpload

* Sun Mar 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.4-alt1
- 2.8.4
- Update spec: add necessary LD_LIBRARY_PATH for build process (thanks real@)
- Remove build type and add flags for Fortran (thanks real@)

* Sat Jan 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.8.3-alt1
- 2.8.3

* Tue Jul 13 2010 Andrey Rahmatullin <wrar@altlinux.org> 2.8.2-alt1
- 2.8.2
- add/restore VCS tests by adding the necessary buildreqs
- add an additional #20884 workaround needed for new gear --commit

* Tue May 11 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.1-alt3
- fix %%cmake_insource (sin@, closes: #23459)

* Mon Mar 29 2010 Dmitry V. Levin <ldv@altlinux.org> 2.8.1-alt2
- Fixed and reenabled %%check.

* Sun Mar 28 2010 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.1-alt1
- 2.8.1
- disable tests (CTestTestTimeout fails in hasher)

* Tue Nov 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.0-alt2
- move macros to the separate package according to the policy

* Mon Nov 16 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.8.0-alt1
- 2.8.0
- add %%cmake and %%cmake_insource macros (closes: #22209)

* Sat Jul 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.4-alt2
- add workarounds for buffer overflows

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Fri Mar 13 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.3-alt2
- package Vim plugins (closes: #19158)

* Fri Mar 06 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.3-alt1
- 2.6.3
- fix Group:
- cmake-doc: don't require cmake

* Thu Dec 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.2-alt3
- package docdir into the main package (repocop)

* Mon Nov 17 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.2-alt2
- remove update_*/clean_* invocations

* Sat Sep 27 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sun Aug 03 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.1-alt1
- 2.6.1
- fix .desktop file according to desktop-file-validate
- move CMakeSetup.png from _pixmapsdir to _niconsdir
- make -doc subpackage noarch and split noarch -modules subpackage

* Sun May 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.6.0-alt1
- 2.6.0
- package html and txt docs separately

* Sat Feb 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Mon Jul 23 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.7-alt1
- 2.4.7

* Fri Mar 30 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.6-alt2
- rebuild with libcurl.so.4

* Sat Jan 13 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.6-alt1
- 2.4.6

* Wed Jan 03 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt4
- build in separate dir
- use optflags

* Wed Jan 03 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt3
- merge cpack package into cmake, since it is required by (almost?)
  all cmake builds (#10577)

* Sun Dec 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt2
- remove globbing of /usr/lib/qt-3* from FindQt3.cmake, which caused
  incorrect buildreq output for projects using FIND_PACKAGE(Qt3)

* Sat Dec 09 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt1
- 2.4.5
- fix x86_64 build (damir@)

* Sun Dec 03 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt0.2
- separate packages for ccmake, cpack and ctest

* Sat Dec 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.5-alt0.1
- 2.4.5 RC4
- fix search for libxmlrpc

* Thu Nov 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Wed Aug 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.3-alt2
- build with system libs
- build bundled libs as shared
- invoke make test

* Thu Aug 03 2006 Andrey Rahmatullin <wrar@altlinux.ru> 2.4.3-alt1
- new version

* Thu Jul 13 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt0.1
- new version 2.4.2 (with rpmrb script) (fix bug #9776)

* Tue May 09 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt0.1
- new version (2.4.1)

* Wed Jan 25 2006 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt0.1
- new version
- fix rpath using

* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version

* Sun Feb 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- first release for ALT Linux Sisyphus

* Tue Nov 23 2004 Gaetan LEHMANN <gaetan.lehmann@jouy.inra.fr> 2.0.5-1mdk
- 2.0.5

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.6.7-2mdk
- Rebuild

* Thu Jul 17 2003 Austin Acton <aacton@yorku.ca> 1.6.7-1mdk
- 1.6.7

* Thu Jan 9 2003 Austin Acton <aacton@yorku.ca> 1.4.7-1mdk
- initial package
