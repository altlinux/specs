Name:    libleatherman
Version: 1.4.0
Release: alt1
Summary: A collection of C++ and CMake utility libraries
 
Group:   System/Libraries
License: Apache 2.0
Url:     https://github.com/puppetlabs/leatherman
Packager: Andrey Cherepanov <cas@altlinux.org>
 
Source: leatherman-%version.tar
 
BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-locale-devel
BuildRequires: boost-log-devel
BuildRequires: libcurl-devel

%description
A collection of C++ and CMake utility libraries.

%package devel
Summary: cpp-hocon development headers
Group: Development/Other
Provides: leatherman-devel = %version-%release
Obsoletes: leatherman-devel < %version-%release

%description devel
Development headers for leatherman.

%prep
%setup -n leatherman-%version
# Ruby 2.3 fix: replace rb_data_object_alloc symbol with rb_data_object_wrap
sed -i 's/rb_data_object_alloc/rb_data_object_wrap/g' \
	$( grep -rl rb_data_object_alloc ruby )

%build
%cmake -DLEATHERMAN_SHARED=TRUE
%cmake_build

%install
%cmakeinstall_std

%files
%doc *.md
%_libdir/leatherman_*.so.*
%_datadir/locale/*/LC_MESSAGES/leatherman_*.mo

%files devel
%_libdir/leatherman_*.so
%_includedir/boost/nowide/*.hpp
%_includedir/boost/nowide/integration/*.hpp
%_includedir/leatherman
%_libdir/cmake/leatherman

%changelog
* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Mon Nov 06 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version

* Sun Feb 19 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.0-alt1
- new version 0.11.0

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.2-alt1
- new version 0.10.2

* Tue Jan 17 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- Initial build in Sisyphus

