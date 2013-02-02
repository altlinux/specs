%ifarch x86_64
%define MODEL 64
%else
%define MODEL 32
%endif

Name: dmd
Version: 2.061
Release: alt2
Summary: The D Programming Language
Group: Development/Other
License: GPL
Url: http://dlang.org/

Source: %name-%version.tar
Patch0: dmd-lphobos2-alt.patch
Patch1: druntime-shared-alt.patch
Patch2: phobos-shared-alt.patch
BuildRequires: gcc-c++ curl-devel

Provides: libdruntime = %version libdruntime-devel = %version
Provides: libphobos = %version libphobos-devel = %version
Conflicts: ldc


%description
The D programming language is an object-oriented, imperative, multi-paradigm 
system programming language created by Walter Bright of Digital Mars. It 
originated as a re-engineering of C++, but even though it is mainly influenced 
by that language, it is not a variant of C++. D has redesigned some C++ features 
and has been influenced by concepts used in other programming languages, such as 
Java, Python, Ruby, C#, and Eiffel.

%prep
%setup -q
#%patch0
#%patch1
#%patch2



%build
cd dmd/src
%make_build -f posix.mak MODEL=%MODEL

export CFLAGS=-fPIC
export CXXFLAGS=-fPIC
cd ../../druntime
#sed -i 's|-m$(MODEL) -O|-m$(MODEL) -fPIC -O|g' posix.mak
%make_build -f posix.mak DMD=../dmd/src/dmd MODEL=%MODEL DRUNTIME_BASE=druntime PIC=1
#gcc lib/libdruntime.o obj/64/errno_c.o obj/64/complex.o -shared -o lib/libdruntime.so -m64 -lpthread -lm -lrt

cd ../phobos
#sed -i 's|DFLAGS += -O -release|DFLAGS += -fPIC -O -release|g' posix.mak
%make_build -f posix.mak DMD=../dmd/src/dmd MODEL=%MODEL ROOT=out PIC=1


cd ../tools
../dmd/src/dmd -c -O -w -d -fPIC -m%MODEL -property -release -I../druntime/import -I../phobos rdmd.d
gcc rdmd.o -o rdmd -m%MODEL -L../druntime/lib -L../phobos/out -ldruntime -lphobos2 -lpthread -lm -lrt
#../dmd/src/dmd -c -O -w -d -m%MODEL -property -release -I../druntime/import -I../phobos catdoc.d
#gcc catdoc.o -o catdoc -m%MODEL -L../phobos/out -lphobos2 -lpthread -lm -lrt

%install
mkdir -p %buildroot{%_bindir,%_sysconfdir,%_libdir,%_includedir/d/etc/c,%_mandir/man1}

cp dmd/src/dmd %buildroot%_bindir/

echo '; dmd.conf file for dmd' > %buildroot%_sysconfdir/dmd.conf
echo '; Names enclosed by %%%% are searched for in the existing environment' >> %buildroot%_sysconfdir/dmd.conf
echo '; and inserted. The special name %%@P%% is replaced with the path' >> %buildroot%_sysconfdir/dmd.conf
echo '; to this file.' >> %buildroot%_sysconfdir/dmd.conf
echo '[Environment]' >> %buildroot%_sysconfdir/dmd.conf
echo 'DFLAGS=-I%_includedir/d' >> %buildroot%_sysconfdir/dmd.conf -L-lrt

#druntime
cp -r druntime/import/* %buildroot%_includedir/d/
cp druntime/lib/libdruntime.a %buildroot%_libdir/

#phobos
cp phobos/out/libphobos2.a %buildroot%_libdir/
cp -r phobos/std %buildroot%_includedir/d/

cp phobos/etc/c/*.d %buildroot%_includedir/d/etc/c/

#tools

#cp tools/catdoc %buildroot%_bindir/
cp tools/rdmd %buildroot%_bindir/
cp -r dmd/docs/man/man1 %buildroot%_mandir/

%files
%doc druntime/doc
%_bindir/*
%_sysconfdir/*
%_mandir/man1/*
%dir %_includedir/d
%_includedir/d/core
%_includedir/d/*.di
%_libdir/libdruntime.a
%_includedir/d/std
%_includedir/d/etc
%_libdir/libphobos*

%changelog
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

