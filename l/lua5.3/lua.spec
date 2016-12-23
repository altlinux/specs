%define oname lua
%global major_version 5.3

Name: lua5.3
Version: %major_version.3
Release: alt4
Summary: Powerful light-weight programming language
Group: Development/Other
License: MIT
Url: http://www.lua.org/
# repackaged tarball http://www.lua.org/ftp/lua-%version.tar.gz
Source0: lua-%version.tar
# repackaged tarball http://www.lua.org/tests/lua-%version-tests.tar.gz
Source1: lua-%version-tests.tar
Source2: lua.source0.watch
Source3: lua.source1.watch
# multilib
Source4: luaconf.h
# copied from readme.html
Source5: COPYRIGHT
Patch0: %oname-5.3.0-autotoolize.patch
Patch1: %oname-5.3.0-idsize.patch
#Patch2:         %%{oname}-5.3.0-luac-shared-link-fix.patch
Patch3: %oname-5.2.2-configure-linux.patch
Patch4: %oname-5.3.0-configure-compat-module.patch
# https://www.lua.org/bugs.html#5.3.3-1
Patch9: lua-5.3.3-upstream-bug-1.patch
# https://www.lua.org/bugs.html#5.3.3-2
Patch10: lua-5.3.3-upstream-bug-2.patch

BuildRequires: automake-common autoconf-common libtool-common readline-devel libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
Provides: lua(abi) = %major_version
Requires: liblua = %version
Source44: import.info
Conflicts: lua5 < %version
Obsoletes: lua5 < %version
Provides: lua = %EVR
Provides: lua5 = %EVR

%define common_descr \
Lua is a powerful light-weight programming language designed for\
extending applications. Lua is also frequently used as a\
general-purpose, stand-alone language. Lua is free software.\
Lua combines simple procedural syntax with powerful data description\
constructs based on associative arrays and extensible semantics. Lua\
is dynamically typed, interpreted from bytecodes, and has automatic\
memory management with garbage collection, making it ideal for\
configuration, scripting, and rapid prototyping.

%description
%common_descr

%package doc
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description doc
%common_descr

This package contains documantaion for %oname

%package -n liblua5-devel
Summary: Development files for %oname
Group: Development/C
Requires: %name = %version
Provides: lua-devel = %EVR
Provides: liblua-devel = %EVR
Provides: liblua5-devel = %EVR
Provides: liblua5.3-devel = %EVR
Conflicts: liblua5-devel < %version
Conflicts: liblua4-devel < %version
Conflicts: liblua-devel < %version

%description -n liblua5-devel
%common_descr

This package contains development files for %oname.

%package -n liblua5.3
Group: Development/Other
Summary: Libraries for %oname
Provides: liblua = %EVR
Provides: liblua5 = %EVR

%description -n liblua5.3
%common_descr

This package contains the shared libraries for %oname.

%package -n liblua5-devel-static
Summary: Static library for %oname
Group: Development/C
Requires: %name%{?_isa} = %version-%release
Provides: lua-static = %EVR
Provides: liblua5-devel-static = %EVR
Provides: liblua5.3-devel-static = %EVR
Conflicts: liblua5-devel-static < %version
Conflicts: liblua4-devel-static < %version

%description -n liblua5-devel-static
%common_descr

This package contains the static version of liblua for %oname.

%prep
%setup -n %oname-%version -a 1
cp %SOURCE5 .
mv src/luaconf.h src/luaconf.h.template.in
%patch0 -p1 -E -z .autoxxx
%patch1 -p1 -z .idsize
#%% patch2 -p1 -z .luac-shared
%patch3 -p1 -z .configure-linux
%patch4 -p1 -z .configure-compat-all
%patch9 -p1 -b .crashfix
%patch10 -p1 -b .readpast

%build
%autoreconf
%configure --with-readline --with-compat-module
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# Autotools give me a headache sometimes.
sed -i 's|@pkgdatadir@|%_datadir|g' src/luaconf.h.template

# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles
make %{?_smp_mflags} LIBS="-lm -ldl"
# only /usr/bin/lua links with readline now #luac_LDADD="liblua.la -lm -ldl"

%check
cd ./lua-%version-tests/

# Removing tests that fail under mock/koji
sed -i.orig -e '
    /db.lua/d;
    /errors.lua/d;
    ' all.lua
LD_LIBRARY_PATH=%buildroot/%_libdir %buildroot/%_bindir/lua -e"_U=true" all.lua

%install
make install DESTDIR=%buildroot
rm %buildroot%_libdir/*.la
mkdir -p %buildroot%_libdir/lua5
mkdir -p %buildroot%_datadir/lua5

# Rename luaconf.h to luaconf-<arch>.h to avoid file conflicts on
# multilib systems and install luaconf.h wrapper
mv %buildroot%_includedir/luaconf.h %buildroot%_includedir/luaconf-%_arch.h
install -p -m 644 %SOURCE4 %buildroot%_includedir/luaconf.h

%ifarch %ix86
if ! [ -e %buildroot/%_includedir/luaconf-i386.h ]; then
  pushd %buildroot/%_includedir/
  ln -s luaconf-%_arch.h  luaconf-i386.h
  popd
fi
%endif

%files
%_bindir/lua
%_bindir/luac
%_mandir/man1/lua*.1*

%files doc
%doc doc/*.html doc/*.css doc/*.gif doc/*.png

%files -n liblua5.3
%doc COPYRIGHT
%doc README
%_libdir/liblua-%major_version.so
%dir %_libdir/lua5
%dir %_datadir/lua5

%files -n liblua5-devel
%_includedir/l*.h
%_includedir/l*.hpp
%_libdir/liblua.so
%_libdir/pkgconfig/*.pc

%files -n liblua5-devel-static
%_libdir/*.a

%changelog
* Wed Dec 21 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.3-alt4
- added extra provides to devel packages
- fixed provides in liblua5-devel-static
- fixed groups in devel packages
- cleaned up spec file

* Tue Dec 20 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.3-alt3
- fixed liblua5-devel provides and conflicts

* Tue Dec 20 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.3-alt2
- separated doc package.
- added watch files.
- packaged updated COPYRIGHT instead of mit.txt.
- moved %%{_libdir}/lua5 and %%{_datadir}/lua5 to liblua5.3 package.
- moved lua/%%{major_version} to lua5 in %%{_libdir} and %%{_datadir}.
- renamed -devel and liblua5.3-devel-static packages.
- removed bootstrap.
- packaged repackaged tarballs.

* Wed Oct 05 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.3-alt1_3
- converted for ALT Linux by srpmconvert tools

