%global        lua_version 5.5.1
%global        major_version %(echo %lua_version | cut -d. -f1,2)
%global        current_lua_version %major_version
%global        cmake_name lua%(echo %major_version | tr -d .)

Name:          lua
Version:       %lua_version
Release:       alt1
Summary:       Powerful light-weight programming language
License:       MIT
Group:         Development/Other

Url:           https://www.lua.org/
Vcs:           https://github.com/lua/lua.git
Source:        %name-%version.tar
Source1:       CMakeLists.txt
Source2:       lua.pc.in
Source3:       lua.1
Source4:       macros.rocks.in
Source5:       rocks-deps.lua.in
Source6:       rocks.files
Source7:       rpm-build-rocks.md
Patch:         lua-5.5-rock-paths.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-alternatives
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: alternatives
BuildRequires: pkgconfig(readline)

%description
Lua is a powerful light-weight programming language designed for
extending applications. Lua is also frequently used as a
general-purpose, stand-alone language.


%package       -n %{name}%{major_version}
Summary:       Lua %major_version interpreter
Group:         Development/Other
Requires:      liblua%major_version = %EVR
Requires(pre): alternatives >= 0:0.2.0-alt0.12
Provides:      lua = %EVR
# Earlier builds directly own /usr/bin/lua.
Conflicts:     lua5.4 < 5.4.7-alt3

%description   -n %{name}%{major_version}
This package contains the Lua %major_version interpreter.


%package       -n %{name}%{major_version}-doc
Summary:       Documentation for Lua %major_version
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %{name}%{major_version}-doc
This package contains documentation for Lua %major_version.


%package       -n liblua%major_version-devel
Summary:       Development files for Lua %major_version
Group:         Development/C
Requires:      liblua%major_version = %EVR
Requires:      %_bindir/lua%major_version

%description   -n liblua%major_version-devel
This package contains the headers and build metadata for Lua %major_version.


%package       -n liblua%major_version
Group:         Development/Other
Summary:       Shared library for Lua %major_version
Provides:      lua(abi) = %major_version

%description   -n liblua%major_version
This package contains the shared library for Lua %major_version.


%package       -n rpm-build-rocks
Summary:       RPM dependency generators for LuaRocks packages
Group:         Development/Tools
BuildArch:     noarch
Requires:      rpm-macros-rocks = %EVR

%description   -n rpm-build-rocks
Generate rocks() capabilities and runtime requirements from installed rockspecs.


%package       -n rpm-macros-rocks
Summary:       RPM macros for LuaRocks packaging
Group:         Development/Tools
BuildArch:     noarch

%description   -n rpm-macros-rocks
Define the LuaRocks installation directories and the buildroot install macro.


%prep
%setup
%autopatch -p1
cp %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7 .
sed -n '/^\* Copyright (C)/,/^\*\+\/$/p' lua.h | sed '$d; s/^\* \?//' > LICENSE
grep -q '^Permission is hereby granted' LICENSE

%build
%cmake \
   -DCMAKE_INSTALL_LIBDIR=%_libdir \
   -DCMAKE_INSTALL_LIBEXECDIR=%_libexecdir \
   -DCMAKE_INSTALL_MANDIR=%_mandir \
   -DLUA_INSTALL_RPMLIBDIR=%_rpmlibdir \
   -DLUA_INSTALL_ALTERNATIVESDIR=%_altdir
%cmake_build

%install
%cmakeinstall_std

%check
%ctest


%files         -n %{name}%{major_version}
%doc LICENSE
%_bindir/lua%major_version
%_bindir/lua-%major_version
%_man1dir/lua%major_version.1*
%_man1dir/lua-%major_version.1*
%_altdir/lua%major_version

%files         -n %{name}%{major_version}-doc
%doc README.md

%files         -n liblua%major_version
%doc LICENSE
%_libdir/liblua-%major_version.so.*

%files         -n liblua%major_version-devel
%_includedir/lua%major_version/
%_libdir/liblua-%major_version.so
%_pkgconfigdir/lua%major_version.pc
%_pkgconfigdir/lua-%major_version.pc
%_libdir/cmake/%cmake_name/

%files         -n rpm-build-rocks
%doc rpm-build-rocks.md
%_rpmlibdir/rocks.prov
%_rpmlibdir/rocks.prov.files
%_rpmlibdir/rocks.req
%_rpmlibdir/rocks.req.files

%files         -n rpm-macros-rocks
%_rpmmacrosdir/rocks


%changelog
* Wed Nov 18 2026 Pavel Skrylev <majioa@altlinux.org> 5.5.1-alt1
- + built lua 5.5.1 for Sisyphus.
- + added an alternative for /usr/bin/lua pointing to the versioned binary.
- + added CMake package exports and CTest coverage.
- + added the versioned man page to the interpreter package.
- + added RPM macros and dependency generators for rock packages.
- * required alternatives before installation.
- * set a numbered SONAME for liblua.
- ! moved the upstream MIT notice to package documentation to avoid a
    common-licenses intersection.
