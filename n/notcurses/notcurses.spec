%define _unpackaged_files_terminate_build 1
%define soversion 3
%define pypi_name notcurses
%define python3_name python3-module-notcurses

Name: notcurses
Version: 3.0.17
Release: alt1

Summary: Character graphics and TUI library
License: Apache-2.0
Group: Terminals
Url: https://nick-black.com/dankwiki/index.php/Notcurses
Vcs: https://github.com/dankamongmen/notcurses.git

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: doctest-devel
BuildRequires: libtinfo-devel
BuildRequires: libncursesw-devel
BuildRequires: libunistring-devel
BuildRequires: libdeflate-devel
BuildRequires: libgpm-devel
BuildRequires: libqrcodegen-devel
BuildRequires: pandoc
BuildRequires: libavcodec-devel
BuildRequires: libavdevice-devel
BuildRequires: libavformat-devel
BuildRequires: libavutil-devel
BuildRequires: libswscale-devel
BuildRequires: libswresample-devel
BuildRequires: libavfilter-devel
BuildRequires: python3-dev
BuildRequires: python3-module-cffi
BuildRequires: python3-module-pypandoc
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%package -n libnotcurses%soversion
Summary: Notcurses shared library
Group: System/Libraries

%package -n libnotcurses-core%soversion
Summary: Notcurses core shared library
Group: System/Libraries

%package -n libnotcurses-ffi%soversion
Summary: Notcurses FFI shared library
Group: System/Libraries

%package -n libnotcurses++%soversion
Summary: C++ bindings for Notcurses
Group: System/Libraries

%package -n libnotcurses-devel
Summary: Development files for Notcurses
Group: Development/C
Requires: libnotcurses%soversion = %EVR
Requires: libnotcurses-core%soversion = %EVR
Requires: libnotcurses-ffi%soversion = %EVR
Requires: libnotcurses++%soversion = %EVR

%package -n %python3_name
Summary: Python bindings for Notcurses
Group: Development/Python3
Requires: libnotcurses%soversion = %EVR

%description
Notcurses facilitates the creation of modern TUI programs,
making full use of Unicode and 24-bit TrueColor. It presents
an API similar to that of Curses, and rides atop Terminfo.

%description -n libnotcurses%soversion
The main Notcurses shared library.

%description -n libnotcurses-core%soversion
The Notcurses core shared library.

%description -n libnotcurses-ffi%soversion
The Notcurses FFI shared library.

%description -n libnotcurses++%soversion
C++ bindings for the Notcurses library.

%description -n libnotcurses-devel
Header files, pkg-config files and CMake files for Notcurses.

%description -n %python3_name
Python bindings and demonstration scripts for the Notcurses library.

%prep
%setup

%build
%cmake \
	-DUSE_QRCODEGEN=ON \
	-DDFSG_BUILD=ON \
	-DUSE_GPM=ON \
	-DUSE_STATIC=OFF \
	-DCMAKE_POSITION_INDEPENDENT_CODE=ON

%cmake_build
pushd cffi
CFLAGS="%optflags -I../include -L../%_cmake__builddir" \
%pyproject_build
popd

%install
%cmake_install
pushd cffi
CFLAGS="%optflags -I../include -L../%_cmake__builddir" \
%pyproject_install
popd

# Upstream CMake installs top-level markdown docs separately from rpm docs.
rm -rf %buildroot%_defaultdocdir/notcurses

%files
%doc README.md
%_bindir/ncls
%_bindir/ncneofetch
%_bindir/ncplayer
%_bindir/nctetris
%_bindir/notcurses-demo
%_bindir/notcurses-info
%_bindir/notcurses-input
%_bindir/notcurses-tester
%_bindir/tfman
%_man1dir/ncls.1*
%_man1dir/ncneofetch.1*
%_man1dir/ncplayer.1*
%_man1dir/nctetris.1*
%_man1dir/notcurses-demo.1*
%_man1dir/notcurses-info.1*
%_man1dir/notcurses-input.1*
%_man1dir/notcurses-tester.1*
%_man1dir/tfman.1*
%_datadir/%name/

%files -n libnotcurses%soversion
%_libdir/libnotcurses.so.%soversion
%_libdir/libnotcurses.so.%version

%files -n libnotcurses-core%soversion
%_libdir/libnotcurses-core.so.%soversion
%_libdir/libnotcurses-core.so.%version

%files -n libnotcurses-ffi%soversion
%_libdir/libnotcurses-ffi.so.%soversion
%_libdir/libnotcurses-ffi.so.%version

%files -n libnotcurses++%soversion
%_libdir/libnotcurses++.so.%soversion
%_libdir/libnotcurses++.so.%version

%files -n libnotcurses-devel
%_includedir/notcurses/
%_includedir/ncpp/
%_libdir/libnotcurses.so
%_libdir/libnotcurses-core.so
%_libdir/libnotcurses-ffi.so
%_libdir/libnotcurses++.so
%dir %_libdir/cmake
%_libdir/cmake/Notcurses/
%_libdir/cmake/Notcurses++/
%_libdir/cmake/NotcursesCore/
%_pkgconfigdir/notcurses.pc
%_pkgconfigdir/notcurses-core.pc
%_pkgconfigdir/notcurses-ffi.pc
%_pkgconfigdir/notcurses++.pc
%_man3dir/*.3*

%files -n %python3_name
%_bindir/notcurses-pydemo
%_bindir/ncdirect-pydemo
%_man1dir/notcurses-pydemo.1*
%_man1dir/ncdirect-pydemo.1*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/*.so

%changelog
* Wed Jun 03 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 3.0.17-alt1
- Initial build for ALT.
