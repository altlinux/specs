%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

ExclusiveArch: %ix86 x86_64

%ifarch x86_64
%define MODEL 64
%else
%define MODEL 32
%endif

Name: dmd
Version: 2.098.1
Release: alt1
Summary: The D Programming Language
Group: Development/Other
License: BSL-1.0
Url: https://dlang.org/

# https://github.com/dlang/dmd.git
Source: %name-%version.tar
# https://github.com/dlang/druntime.git
Source2: druntime-%version.tar
# https://github.com/dlang/phobos.git
Source3: phobos-%version.tar
# https://github.com/dlang/tools.git
Source4: tools-%version.tar

Patch1: druntime-2.082.0-alt-build.patch
Patch2: druntime-2.082.0-alt-files-list.patch
Patch3: dmd-2.097.0-alt-build.patch
Patch4: phobos-2.082.0-alt-build.patch
Patch5: tools-2.095.1-alt-build.patch

BuildRequires: gcc-c++ curl-devel
BuildRequires: zlib-devel
# DMD now requires D compiler to build
BuildRequires: dmd
BuildRequires: /proc

Provides: libdruntime = %EVR
Conflicts: ldc
Requires: /proc

Requires: libdruntime-devel = %EVR
Requires: libdruntime-devel-static = %EVR
Requires: libphobos2 = %EVR
Requires: libphobos2-devel = %EVR
Requires: libphobos2-devel-static = %EVR

%description
The D programming language is an object-oriented, imperative, multi-paradigm
system programming language created by Walter Bright of Digital Mars. It
originated as a re-engineering of C++, but even though it is mainly influenced
by that language, it is not a variant of C++. D has redesigned some C++ features
and has been influenced by concepts used in other programming languages, such as
Java, Python, Ruby, C#, and Eiffel.

%package -n dmd-devel-common
Summary: Common development files for D language compiler.
Group: Development/Other

%description -n dmd-devel-common
Common development files for D language compiler.

%package -n libdruntime-devel
Summary: D runtime development files.
Group: Development/Other
Requires: dmd-devel-common = %EVR

%description -n libdruntime-devel
D runtime development files.

%package -n libdruntime-devel-static
Summary: Static D runtime development files.
Group: Development/Other
Requires: libdruntime-devel = %EVR

%description -n libdruntime-devel-static
Static D runtime development files.

%package -n libphobos2
Summary: Phobos is the standard runtime library that comes with the D language compiler.
Group: System/Libraries
Provides: libphobos = %EVR

%description -n libphobos2
Phobos is the standard runtime library that comes with the D language compiler.

%package -n libphobos2-devel
Summary: Phobos is the standard runtime library that comes with the D language compiler.
Group: Development/Other
Requires: dmd-devel-common = %EVR
Requires: libphobos2 = %EVR
Provides: libphobos-devel = %EVR

%description -n libphobos2-devel
Phobos is the standard runtime library that comes with the D language compiler.

%package -n libphobos2-devel-static
Summary: Phobos is the standard runtime library that comes with the D language compiler.
Group: Development/Other
Requires: libphobos2-devel = %EVR

%description -n libphobos2-devel-static
Phobos is the standard runtime library that comes with the D language compiler.

%prep
%setup -b2 -b3 -b4 -n %name

pushd ../druntime
%patch1 -p2
%patch2 -p2
popd

%patch3 -p2

pushd ../phobos
%patch4 -p2
popd

pushd ../tools
%patch5 -p2
popd

%build
pushd src
%make_build -f posix.mak MODEL=%MODEL PIC=1 BUILD=release ENABLE_RELEASE=1
popd

pushd ../druntime
#sed -i 's|-m$(MODEL) -O|-m$(MODEL) -fPIC -O|g' posix.mak
%make_build -f posix.mak MODEL=%MODEL DRUNTIME_BASE=druntime PIC=1 BUILD=release ENABLE_RELEASE=1
#gcc lib/libdruntime.o obj/64/errno_c.o obj/64/complex.o -shared -o lib/libdruntime.so -m64 -lpthread -lm -lrt
popd

pushd ../phobos
#sed -i 's|DFLAGS += -O -release|DFLAGS += -fPIC -O -release|g' posix.mak
%make_build -f posix.mak MODEL=%MODEL ROOT=out PIC=1 BUILD=release ENABLE_RELEASE=1
popd

pushd ../tools
%make_build -f posix.mak MODEL=%MODEL ROOT=out PIC=1 DFLAGS='-I../druntime/import -I../phobos -L-L../phobos/out' BUILD=release ENABLE_RELEASE=1
#../dmd/src/dmd -c -O -w -d -fPIC -m%MODEL -property -release -I../druntime/import -I../phobos rdmd.d
#gcc rdmd.o -o rdmd -m%MODEL -L../druntime/lib -L../phobos/out -ldruntime -lphobos2 -lpthread -lm -lrt
#../dmd/src/dmd -c -O -w -d -m%MODEL -property -release -I../druntime/import -I../phobos catdoc.d
#gcc catdoc.o -o catdoc -m%MODEL -L../phobos/out -lphobos2 -lpthread -lm -lrt
popd

%install
mkdir -p %buildroot{%_bindir,%_sysconfdir,%_libdir,%_includedir/d/etc/c,%_man1dir,%_man5dir}

cp generated/linux/release/%MODEL/dmd %buildroot%_bindir/

echo '; dmd.conf file for dmd' > %buildroot%_sysconfdir/dmd.conf
echo '; Names enclosed by %%%% are searched for in the existing environment' >> %buildroot%_sysconfdir/dmd.conf
echo '; and inserted. The special name %%@P%% is replaced with the path' >> %buildroot%_sysconfdir/dmd.conf
echo '; to this file.' >> %buildroot%_sysconfdir/dmd.conf
echo '[Environment]' >> %buildroot%_sysconfdir/dmd.conf
echo 'DFLAGS=-I%_includedir/d -L-lrt -L--export-dynamic -fPIC' >> %buildroot%_sysconfdir/dmd.conf

#druntime
cp -r ../druntime/import/* %buildroot%_includedir/d/
cp ../druntime/out/libdruntime.a %buildroot%_libdir/
rm -f ../druntime/out/libdruntime.so*.a
rm -f ../druntime/out/libdruntime.so*.o
cp ../druntime/out/libdruntime.so* %buildroot%_libdir/

#phobos
cp ../phobos/out/libphobos2.a %buildroot%_libdir/
rm -f ../phobos/out/libphobos2.so*.o
cp -a ../phobos/out/libphobos2.so* %buildroot%_libdir/
cp -r ../phobos/std %buildroot%_includedir/d/

cp ../phobos/etc/c/*.d %buildroot%_includedir/d/etc/c/

pushd ../tools
%make -f posix.mak MODEL=%MODEL ROOT=out PIC=1 DFLAGS='-I../druntime/import -I../phobos -L-L../phobos/out' BUILD=release ENABLE_RELEASE=1 install INSTALL_DIR=%buildroot%_prefix
popd

# catdoc conflicts with file from package 'catdoc'; rename it
mv %buildroot%_bindir/catdoc %buildroot%_bindir/dmd-catdoc

cp -r docs/man/man1/* %buildroot%_man1dir/
cp -r docs/man/man5/* %buildroot%_man5dir/

cp -r ../tools/man/man1/* %buildroot%_man1dir/

%files
%_bindir/*
%_sysconfdir/*
%_man1dir/*
%_man5dir/*
%_libdir/libdruntime.so

%files -n dmd-devel-common
%dir %_includedir/d

%files -n libdruntime-devel
%_includedir/d/core
%_includedir/d/*.d

%files -n libdruntime-devel-static
%_libdir/libdruntime.a

%files -n libphobos2
%_libdir/libphobos2.so.*

%files -n libphobos2-devel
%_libdir/libphobos2.so
%_includedir/d/std
%_includedir/d/etc

%files -n libphobos2-devel-static
%_libdir/libphobos2.a

%changelog
* Wed Jan 12 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2.098.1-alt1
- Updated to upstream version 2.098.1.

* Tue Jun 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.097.0-alt1
- Updated to upstream version 2.097.0.

* Tue Jun 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.096.1-alt1
- Updated to upstream version 2.096.1.

* Wed Mar 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.095.1-alt1
- Updated to upstream version 2.095.1.
- Fixed build with gcc-10.

* Mon Dec 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.094.2-alt1
- Updated to upstream version 2.094.2.
- Split package into multiple subpackages.

* Mon Oct 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.094.0-alt3
- Renamed catdoc to dmd-catdoc due to file conflicts (ALT #39060).

* Thu Oct 15 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.094.0-alt2
- Reworked %%install phase. More tools should be installed now (ALT #39060).

* Mon Sep 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.094.0-alt1
- Updated to upstream version 2.094.0.

* Tue Apr 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.091.0-alt1
- Updated to upstream version 2.091.0.

* Tue Jul 30 2019 Konstantin Rybakov <kastet@altlinux.org> 2.087.0-alt1
- Updated to upstream version 2.087.0.

* Tue Mar 26 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.082.0-alt2
- Linked dynamic libraries to system zlib (Closes: #36380)

* Mon Sep 17 2018 Pavel Moseev <mars@altlinux.org> 2.082.0-alt1
- Updated to upstream version 2.082.0.

* Wed Sep 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.076.0-alt1
- Updated to upstream version 2.076.0.
- Added %%ubt macro to release.

* Wed Sep 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.068.0-alt1
- Updated to upstream version 2.068.0.

* Fri Aug 16 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.063.2-alt1
- new bersion

* Sat Feb 02 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.061-alt2
- Rebuild with -fPIC

* Sat Jan 19 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.061-alt1
- New version (Closes: #28302)
- Fix includes (Closes: #28394)

* Sat Dec 22 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt5
- Added provides
- Phobos in dmd

* Wed Oct 31 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt4
- Added Url in spec
- Added missed headers
- Fix dmd.config

* Tue Oct 16 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt3
- Excluded catdoc(conflicts with the package catdoc-0.94.2-alt4)

* Sun Oct 07 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt2
- Fix dmd.conf

* Tue Sep 25 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt1
- Initial build

