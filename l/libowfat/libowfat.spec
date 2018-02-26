Name: libowfat
Version: 0.28
Release: alt3

Summary: Reimplementation of libdjb

License: GPLv2
Group: System/Libraries
Url: http://www.fefe.de/libowfat/

Packager: Ilya Shpigor <elly@altlinux.org>

Source: http://dl.fefe.de/%name-%version.tar.bz2
Patch0: %name-0.28-shared.patch
Patch1: %name-0.28-no-dietlibc.patch
Patch2: %name-0.28-no-man.patch

%package devel
Summary: Headers and static lib for libowfat development
Group: Development/C
Requires: %name = %version-%release

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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%add_optflags %optflags_shared

%build
%make_build

%install
make -f GNUmakefile install \
        prefix="%buildroot%prefix" \
        LIBDIR="%buildroot%_libdir" \
        INCLUDEDIR="%buildroot%_includedir/%name"

ln -s libowfat.so.%version %buildroot%_libdir/libowfat.so.0
ln -s libowfat.so.0 %buildroot%_libdir/libowfat.so

%files
%doc README TODO COPYING CHANGES
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/%name/

%changelog
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
