%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libowfat
Version: 0.32
Release: alt2
Summary: Reimplementation of libdjb
License: GPLv2
Group: System/Libraries
Url: http://www.fefe.de/libowfat/

Source: %name-%version.tar
Patch0: %name-%version-alt-build-flags.patch
Patch1: %name-%version-alt-no-dietlibc.patch
Patch2: %name-%version-alt-no-man.patch
Patch3: %name-%version-debian-fix-gcc10.patch
Patch4: %name-%version-alt-fno-common.patch
Patch5: %name-%version-alt-glibc-2.34-compat.patch

%package devel
Summary: Headers and static lib for libowfat development
Group: Development/C
Requires: %name = %EVR

%description
This library is a reimplementation of libdjb, which means that it provides
Daniel Bernstein's interfaces (with some extensions).

It contains wrappers around memory allocation, buffered I/O, routines for
formatting and scanning, a full DNS resolver, several socket routines,
wrappers for socket functions, mkfifo, opendir, wait, and an abstraction
around errno.  It also includes wrappers for Unix signal functions and a
layer of mmap and sendfile.

%description devel
Install this package if you want do compile applications using the
%name library.

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p1
%patch4 -p2
%patch5 -p2

%build
%add_optflags %optflags_shared
%add_optflags -D_FILE_OFFSET_BITS=64

%make -f GNUmakefile \
        havescope.h \
        CFLAGS="%optflags" \
        %nil

%make_build -f GNUmakefile \
        CFLAGS="%optflags" \
        %nil

%install
%add_optflags %optflags_shared

make -f GNUmakefile install \
        prefix="%buildroot%prefix" \
        LIBDIR="%buildroot%_libdir" \
        INCLUDEDIR="%buildroot%_includedir/%name" \
        CFLAGS="%optflags" \
        %nil

ln -s libowfat.so.%version %buildroot%_libdir/libowfat.so.0
ln -s libowfat.so.0 %buildroot%_libdir/libowfat.so

%files
%doc README TODO COPYING CHANGES
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/%name/

%changelog
* Tue Nov 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.32-alt2
- Fixed build with new glibc.

* Mon Dec 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.32-alt1
- Updated to upstream version 0.32.
- Fixed build with -fno-common.

* Mon Jul 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.31-alt1
- Updated to upstream version 0.31.

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.28-alt3.1
- Fixed build

* Wed Nov 18 2009 Ilya Shpigor <elly@altlinux.org> 0.28-alt3
- remove manuals from the devel package

* Wed Nov 11 2009 Ilya Shpigor <elly@altlinux.org> 0.28-alt2
- fix building development library

* Fri Nov 06 2009 Ilya Shpigor <elly@altlinux.org> 0.28-alt1
- initial build for ALT Linux Sisyphus

* Sat Oct 24 2009 Simon Wesp <cassmodiah@edoraproject.org> - 0.28-4
- Rebuild without dietlibc usage
- No package (in Fedora-Repo) requires libowfat at this time

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 19 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.28-2
- Honor optflags
- Add parallel build
- Correct libdir paths for dietlibc-integration
- Cosmetical Issues

* Tue Mar 17 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 0.28-1
- New upstream release

* Sun Aug 24 2008 Simon Wesp <cassmodiah@fedoraproject.org> - 0.27-1
- Initial release
