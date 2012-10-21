Name: libgit2
Version: 0.17.0
Release: alt1.c497a6

Summary: linkable library for Git
License: GPLv2 with linking exception

Group: System/Libraries
URL: http://libgit2.github.com

Source: %name-%version.tar

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake python-modules zlib-devel libssl-devel

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing you
to write native speed custom Git applications in any language which
supports C bindings.

%package devel
Group: Development/C
Summary: linkable library for Git - development files
Requires: %name = %version-%release

%description devel
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing you
to write native speed custom Git applications in any language which
supports C bindings.
This package contains development files.

%prep 
%setup -q
rm -rf deps/{regex,zlib}
sed -i 's/LIB_INSTALL_DIR lib/LIB_INSTALL_DIR lib${LIB_SUFFIX}/' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmakeinstall_std 

%files
%_libdir/%name.so.*
%doc README.md AUTHORS COPYING

%files devel
%_includedir/git2
# exclude headers for windows
%exclude %_includedir/git2/inttypes.h
%exclude %_includedir/git2/stdint.h
%_includedir/git2.h
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc

%changelog
* Sun Oct 21 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17.0-alt1.c497a6
- git snapshot c497a6

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17.0-alt1
- initial release
