%define sover 0

Name: gamerf
Version: 1
Release: alt1
Summary: Gamma / Error Functions
License: Free
Group: Sciences/Mathematics
Url: http://www.kurims.kyoto-u.ac.jp/~ooura/gamerf.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-fortran

%description
Gamma / Error Functions.

%package -n lib%name
Summary: Gamma / Error Functions
Group: System/Libraries

%description -n lib%name
Gamma / Error Functions.

%package -n lib%name-devel
Summary: Development files of lib%name
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
Gamma / Error Functions.

This package contains development files of lib%name.

%prep
%setup

%build
%add_optflags %optflags_shared
mkdir f
mv *.f f/

gcc -c *.c %optflags
gcc -shared *.o -Wl,-soname=lib%name.so.%sover -lm \
	-o lib%name.so.%sover
ln -s lib%name.so.%sover lib%name.so

pushd f
for i in *.f; do
	j=$(echo $i |sed 's|\.f$||')
	f95 -c $i %optflags
	f95 -shared $j.o -Wl,-soname=lib%name-f-$j.so.%sover \
		-o ../lib%name-f-$j.so.%sover
	ln -s lib%name-f-$j.so.%sover ../lib%name-f-$j.so
done
popd

%install
install -d %buildroot%_includedir
install -p -m644 *.h %buildroot%_includedir/

install -d %buildroot%_libdir
for i in lib*.so; do
	install -m644 $i.%sover %buildroot%_libdir/
	ln -s $i.%sover %buildroot%_libdir/$i
done

%files -n lib%name
%doc *.txt *.doc
%_libdir/*.so.*

%files -n lib%name-devel
%doc *.c f/*.f
%_includedir/*
%_libdir/*.so

%changelog
* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1-alt1
- Initial build for Sisyphus

