%ifarch x86_64
%define MODEL 64
%else
%define MODEL 32
%endif

Name: dmd
Version: 2.060
Release: alt4
Summary: The D Programming Language
Group: Development/Other
License: GPL
Url: http://dlang.org/

Source: %name-%version.tar
BuildRequires: gcc-c++

%description
The D programming language is an object-oriented, imperative, multi-paradigm 
system programming language created by Walter Bright of Digital Mars. It 
originated as a re-engineering of C++, but even though it is mainly influenced 
by that language, it is not a variant of C++. D has redesigned some C++ features 
and has been influenced by concepts used in other programming languages, such as 
Java, Python, Ruby, C#, and Eiffel.

%package -n libphobos
Summary: Phobos Runtime Library
Group: Development/Other
Requires: %name = %version

%description -n libphobos
Phobos is the standard runtime library that comes with the D language compiler.

%prep
%setup -q

%build
cd dmd/src
%make_build -f posix.mak MODEL=%MODEL

cd ../../druntime
%make_build -f posix.mak DMD=../dmd/src/dmd MODEL=%MODEL DRUNTIME_BASE=druntime

cd ../phobos
%make_build -f posix.mak DMD=../dmd/src/dmd MODEL=%MODEL ROOT=out

cd ../tools
../dmd/src/dmd -c -O -w -d -m%MODEL -property -release -I../druntime/import -I../phobos rdmd.d
gcc rdmd.o -o rdmd -m%MODEL -L../phobos/out -lphobos2 -lpthread -lm -lrt
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
ln -s libphobos2.a %buildroot%_libdir/libphobos.a
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

%files -n libphobos
%_includedir/d/std
%_includedir/d/etc
%_libdir/libphobos*

%changelog
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

