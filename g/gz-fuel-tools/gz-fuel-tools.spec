%define _unpackaged_files_terminate_build 1
%define soversion 11

Name: gz-fuel-tools
Version: 11.0.0
Release: alt2

Summary: A client library and command line tools for interacting with Gazebo Fuel servers
License: Apache-2.0
Group: Development/C++
Url: https://gazebosim.org/libs/fuel_tools/
Vcs: https://github.com/gazebosim/gz-fuel-tools

Source: %name-%version.tar

Conflicts: libgz-fuel-tools

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libtinyxml2-devel
BuildRequires: libgz-common-devel
BuildRequires: libgz-math-devel
BuildRequires: libgz-msgs-devel
BuildRequires: gz-tools-devel
BuildRequires: libyaml-devel
BuildRequires: libzip-devel
BuildRequires: libcurl-devel
BuildRequires: libpsl-devel
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libgsasl)
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: pkgconfig(libnghttp2)
BuildRequires: pkgconfig(libnghttp3)
BuildRequires: pkgconfig(libngtcp2)
BuildRequires: pkgconfig(libidn2)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libtasn1)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(mit-krb5-gssapi)
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: /proc
BuildRequires: ctest

%description
Gazebo Fuel Tools is composed by a client library and command line tools for
interacting with Gazebo Fuel servers.

%package -n libgz-fuel-tools%soversion
Summary: Library of gz-fuel-tools
Group: System/Libraries

%description -n libgz-fuel-tools%soversion
This package contains library libgz-fuel-tools of gz-fuel-tools.

%package -n libgz-fuel-tools-devel
Summary: Development files for gz-fuel-tools
Group: Development/C++

%description -n libgz-fuel-tools-devel
This package contains development files of gz-fuel-tools.

%prep
%setup

%build
%cmake \
    -GNinja \
    -Wno-dev \
    #
%cmake_build

%install
%cmake_install

%check
# Tests that try to download off the Internet are excluded.
%ctest \
  -E "UNIT_FuelClient_TEST|UNIT_Interface_TEST|gz_src_TEST" \
  #

%files
%doc AUTHORS README.md
%_libexecdir/ruby/gz/cmdfuel%soversion.rb
%_datadir/gz/fuel%soversion.yaml
%_datadir/gz/gz2.completion.d/fuel%soversion.bash_completion.sh

%files -n libgz-fuel-tools%soversion
%_libdir/libgz-fuel_tools.so.%soversion
%_libdir/libgz-fuel_tools.so.%version

%files -n libgz-fuel-tools-devel
%_includedir/gz/fuel_tools%soversion
%_cmakedir/gz-fuel_tools
%_cmakedir/gz-fuel_tools-all
%_pkgconfigdir/gz-fuel_tools.pc
%_libdir/libgz-fuel_tools.so

%changelog
* Tue Aug 11 2026 Pavel Petrykin <silverducks@altlinux.org> 11.0.0-alt2
- Update subpackage descriptions.

* Tue Dec 23 2025 Pavel Petrykin <silverducks@altlinux.org> 11.0.0-alt1
- New Version.

* Tue Jun 17 2025 Andrew A. Vasilyev <andy@altlinux.org> 10.0.0-alt2
- NMU: fix FTBFS.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 10.0.0-alt1
- New version.

* Wed Apr 03 2024 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- New version.

* Wed Dec 27 2023 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt3
- FTBFS: unified wildcard for sporadic naming.

* Mon Dec 18 2023 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt2
- Packaged gz-fuel_tools8/gz-fuel_tools8.tag.xml.

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 7.2.2-alt2
- Moved .so files to main package.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 7.2.2-alt1
- New version.

* Mon May 22 2023 Andrey Cherepanov <cas@altlinux.org> 4.9.0-alt1
- Initial build for Sisyphus.
