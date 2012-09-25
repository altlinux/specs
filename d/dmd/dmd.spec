%ifarch x86_64
%define MODEL 64
%else
%define MODEL 32
%endif

Name: dmd
Version: 2.060
Release: alt1
Summary: The D Programming Language
Group: Development/Other
License: GPL

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
%make_build -f posix.mak DMD=../dmd/src/dmd MODEL=%MODEL DRUNTIME_BASE=libdruntime.a

cd ../phobos
%make_build -f posix.mak DMD=../dmd/src/dmd MODEL=%MODEL ROOT=out

cd ../tools
../dmd/src/dmd -c -O -w -d -m%MODEL -property -release -I../druntime/import -I../phobos rdmd.d
gcc rdmd.o -o rdmd -m%MODEL -L../phobos/out -lphobos2 -lpthread -lm -lrt
../dmd/src/dmd -c -O -w -d -m%MODEL -property -release -I../druntime/import -I../phobos catdoc.d
gcc catdoc.o -o catdoc -m%MODEL -L../phobos/out -lphobos2 -lpthread -lm -lrt

%install
mkdir -p %buildroot{%_bindir,%_sysconfdir,%_libdir,%_includedir/d2,%_mandir/man1}

cp dmd/src/dmd %buildroot%_bindir/

echo '; dmd.conf file for dmd' > %buildroot%_sysconfdir/dmd.conf
echo '; Names enclosed by %%%% are searched for in the existing environment' >> %buildroot%_sysconfdir/dmd.conf
echo '; and inserted. The special name %%@P%% is replaced with the path' >> %buildroot%_sysconfdir/dmd.conf
echo '; to this file.' > %buildroot%_sysconfdir/dmd.conf

#druntime
cp -r druntime/import/* %buildroot%_includedir/d2/

#phobos
cp phobos/out/libphobos2.a %buildroot%_libdir/
cp -r phobos/std %buildroot%_includedir/d2/

#tools

cp tools/catdoc %buildroot%_bindir/
cp tools/rdmd %buildroot%_bindir/
cp -r dmd/docs/man/man1 %buildroot%_mandir/

%files
%doc dmd/docs
%doc druntime/doc
%_bindir/*
%_sysconfdir/*
%_mandir/man1/*
%_includedir/d2/core

%files -n libphobos
%_includedir/d2/std
%_libdir/*.a

%changelog
* Tue Sep 25 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.060-alt1
- Initial build

