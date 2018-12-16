Name: fuse-7z
Version: 0.2nggit
Release: alt1

Summary: A FUSE filesystem that uses the 7-zip library to interacts with all kind of archives

Group: System/Kernel and hardware
License: GPL v3
Url: https://github.com/kedazo/fuse-7z-ng

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/kedazo/fuse-7z-ng/archive/master.zip
Source: %name-%version.tar
Patch1: fuze-7z-fix.patch

Requires: %{get_dep fuse}

# TODO
%add_optflags -DFUSE_STAT="struct stat"

BuildRequires: cmake gcc-c++ libfuse-devel lib7zip-devel

%description
A FUSE filesystem that uses the 7-zip library to interacts with all kind
of archives, and in particular the .7z files.

Only reads are supported at the moment, and this is a work in progress (started 2011-09-05).

Contributions are welcome.

%prep
%setup
%patch1 -p2
# TODO
mv -v cmake/FindFuse.cmake cmake/FindFUSE.cmake
%__subst "s|fuse-7z-ng|%name|" CMakeLists.txt src/main.cpp

%build
%cmake_insource
%make_build

%install
install -D fuse_7z_ng %buildroot%_bindir/fuse-7z

%files
%doc README
%_bindir/fuse-7z
#_libexecdir/%name/

%changelog
* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2nggit-alt1
- new version (0.2nggit) with rpmgs script
- change upstream to fuse-7z-ng

* Fri Oct 07 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt3
- update Url, fix shell wrapper (against speces in name)

* Mon Sep 22 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt2
- fast hack for fix wchar_t to utf8 convert

* Mon Sep 22 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- build new version, fix build

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Completed linking

* Fri Aug 17 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
