%define oldname lua
%global major_version 5.3
# If you are incrementing major_version, enable bootstrapping and adjust accordingly.
# Version should be the latest prior build. If you don't do this, RPM will break and
# everything will grind to a halt.
%global bootstrap 0
%global bootstrap_major_version 5.2
%global bootstrap_version %{bootstrap_major_version}.3


Name:           lua5.3
Version:        %{major_version}.3
Release:        alt1_3
Summary:        Powerful light-weight programming language
Group:          Development/Other
License:        MIT
URL:            http://www.lua.org/
Source0:        http://www.lua.org/ftp/lua-%{version}.tar.gz
# copied from doc/readme.html on 2014-07-18
Source1:        mit.txt
%if 0%{?bootstrap}
Source2:        http://www.lua.org/ftp/lua-%{bootstrap_version}.tar.gz
%endif
Source3:        http://www.lua.org/tests/lua-%{version}-tests.tar.gz
# multilib
Source4:        luaconf.h
Patch0:         %{oldname}-5.3.0-autotoolize.patch
Patch1:         %{oldname}-5.3.0-idsize.patch
#Patch2:         %%{oldname}-5.3.0-luac-shared-link-fix.patch
Patch3:         %{oldname}-5.2.2-configure-linux.patch
Patch4:         %{oldname}-5.3.0-configure-compat-module.patch
%if 0%{?bootstrap}
Patch5:         %{oldname}-5.2.3-autotoolize.patch
Patch6:         %{oldname}-5.2.2-idsize.patch
Patch7:         %{oldname}-5.2.2-luac-shared-link-fix.patch
Patch8:         %{oldname}-5.2.2-configure-compat-module.patch
%endif
# https://www.lua.org/bugs.html#5.3.3-1
Patch9:		lua-5.3.3-upstream-bug-1.patch
# https://www.lua.org/bugs.html#5.3.3-2
Patch10:	lua-5.3.3-upstream-bug-2.patch

BuildRequires:  automake-common autoconf-common libtool-common readline-devel libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
Provides:       lua(abi) = %{major_version}
Requires:       liblua = %{version}
Source44: import.info
Conflicts: lua5 < %version
Obsoletes: lua5 < %version
Provides: lua = %version-%release
Provides: lua5 = %version-%release

%description
Lua is a powerful light-weight programming language designed for
extending applications. Lua is also frequently used as a
general-purpose, stand-alone language. Lua is free software.
Lua combines simple procedural syntax with powerful data description
constructs based on associative arrays and extensible semantics. Lua
is dynamically typed, interpreted from bytecodes, and has automatic
memory management with garbage collection, making it ideal for
configuration, scripting, and rapid prototyping.

%package devel
Summary:        Development files for %{oldname}
Group:          System/Libraries
Requires:       %{name}%{?_isa} = %{version}
Requires:       pkg-config
Conflicts: liblua5-devel
Provides: lua-devel = %version-%release
Provides: liblua5-devel = %version-%release
Conflicts: liblua5-devel < %version
Conflicts: liblua4-devel < %version

%description devel
This package contains development files for %{oldname}.

%package -n liblua5.3
Group: Development/Other
Summary:        Libraries for %{oldname}
Provides: liblua = %version-%release
Provides: liblua5 = %version-%release

%description -n liblua5.3
This package contains the shared libraries for %{oldname}.

%package -n liblua5.3-devel-static
Summary:        Static library for %{oldname}
Group:          System/Libraries
Requires:       %{name}%{?_isa} = %{version}
Provides: lua-static = %version
Provides: liblua5-devel-static = %version
Conflicts: liblua5-devel-static < %version
Conflicts: liblua4-devel-static < %version

%description -n liblua5.3-devel-static
This package contains the static version of liblua for %{oldname}.


%prep
%if 0%{?bootstrap}
%setup -n %{oldname}-%{version} -q -a 2 -a 3
%else
%setup -n %{oldname}-%{version} -q -a 3
%endif
cp %{SOURCE1} .
mv src/luaconf.h src/luaconf.h.template.in
%patch0 -p1 -E -z .autoxxx
%patch1 -p1 -z .idsize
#%% patch2 -p1 -z .luac-shared
%patch3 -p1 -z .configure-linux
%patch4 -p1 -z .configure-compat-all
%patch9 -p1 -b .crashfix
%patch10 -p1 -b .readpast
autoreconf -i

%if 0%{?bootstrap}
cd lua-%{bootstrap_version}/
mv src/luaconf.h src/luaconf.h.template.in
%patch5 -p1 -b .autoxxx
%patch6 -p1 -b .idsize
%patch7 -p1 -b .luac-shared
%patch3 -p1 -z .configure-linux
%patch8 -p1 -z .configure-compat-all
autoreconf -i
cd ..
%endif


%build
%configure --with-readline --with-compat-module
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# Autotools give me a headache sometimes.
sed -i 's|@pkgdatadir@|%{_datadir}|g' src/luaconf.h.template

# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles
make %{?_smp_mflags} LIBS="-lm -ldl"
# only /usr/bin/lua links with readline now #luac_LDADD="liblua.la -lm -ldl"

%if 0%{?bootstrap}
pushd lua-%{bootstrap_version}
%configure --with-readline --with-compat-module
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# Autotools give me a headache sometimes.
sed -i 's|@pkgdatadir@|%{_datadir}|g' src/luaconf.h.template

# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles
make %{?_smp_mflags} LIBS="-lm -ldl" luac_LDADD="liblua.la -lm -ldl"
popd
%endif

%check
cd ./lua-%{version}-tests/

# Dont skip the fully portable or ram-hungry tests:
# sed -i.orig -e '
#     /attrib.lua/d;
#     /files.lua/d;
#     /db.lua/d;
#     /errors.lua/d;
#     ' all.lua
# LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir} $RPM_BUILD_ROOT/%{_bindir}/lua all.lua

# Removing tests that fail under mock/koji
sed -i.orig -e '
    /db.lua/d;
    /errors.lua/d;
    ' all.lua
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir} $RPM_BUILD_ROOT/%{_bindir}/lua -e"_U=true" all.lua

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la
mkdir -p $RPM_BUILD_ROOT%{_libdir}/lua/%{major_version}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/lua/%{major_version}

# Rename luaconf.h to luaconf-<arch>.h to avoid file conflicts on
# multilib systems and install luaconf.h wrapper
mv %{buildroot}%{_includedir}/luaconf.h %{buildroot}%{_includedir}/luaconf-%{_arch}.h
install -p -m 644 %{SOURCE4} %{buildroot}%{_includedir}/luaconf.h

%if 0%{?bootstrap}
pushd lua-%{bootstrap_version}
mkdir $RPM_BUILD_ROOT/installdir
make install DESTDIR=$RPM_BUILD_ROOT/installdir
cp -a $RPM_BUILD_ROOT/installdir/%{_libdir}/liblua-%{bootstrap_major_version}.so $RPM_BUILD_ROOT%{_libdir}/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/lua/%{bootstrap_major_version}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/lua/%{bootstrap_major_version}
rm -rf $RPM_BUILD_ROOT/installdir
popd
%endif

%ifarch %{ix86}
if ! [ -e %buildroot/%_includedir/luaconf-i386.h ]; then
  pushd %buildroot/%_includedir/
  ln -s luaconf-%{_arch}.h  luaconf-i386.h
  popd
fi
%endif


%files
%{!?_licensedir:%global license %%doc}
%doc mit.txt

%doc README doc/*.html doc/*.css doc/*.gif doc/*.png
%{_bindir}/lua
%{_bindir}/luac
%if 0%{?bootstrap}
%dir %{_libdir}/lua/%{bootstrap_major_version}
%dir %{_datadir}/lua/%{bootstrap_major_version}
%endif
%{_mandir}/man1/lua*.1*
%dir %{_libdir}/lua
%dir %{_libdir}/lua/%{major_version}
%dir %{_datadir}/lua
%dir %{_datadir}/lua/%{major_version}

%files -n liblua5.3
%{_libdir}/liblua-%{major_version}.so
%if 0%{?bootstrap}
%{_libdir}/liblua-%{bootstrap_major_version}.so
%endif

%files devel
%{_includedir}/l*.h
%{_includedir}/l*.hpp
%{_libdir}/liblua.so
%{_libdir}/pkgconfig/*.pc

%files -n liblua5.3-devel-static
%{_libdir}/*.a


%changelog
* Wed Oct 05 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.3.3-alt1_3
- converted for ALT Linux by srpmconvert tools

