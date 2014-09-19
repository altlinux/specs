%define sover 0

Name: bessel
Version: 1
Release: alt1
Summary: Bessel Functions - integer order
License: Free
Group: Sciences/Mathematics
Url: http://www.kurims.kyoto-u.ac.jp/~ooura/bessel.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-fortran

%description
Bessel Functions - integer order.

%package -n lib%name
Summary: Bessel Functions - integer order
Group: System/Libraries

%description -n lib%name
Bessel Functions - integer order.

%package -n lib%name-devel
Summary: Development files of lib%name
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
Bessel Functions - integer order.

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
f95 -c *.f %optflags
f95 -shared *.o -Wl,-soname=lib%name-f.so.%sover \
	-o ../lib%name-f.so.%sover
ln -s lib%name-f.so.%sover ../lib%name-f.so
popd

%install
install -d %buildroot%_libdir
for i in lib*.so; do
	install -m644 $i.%sover %buildroot%_libdir/
	ln -s $i.%sover %buildroot%_libdir/$i
done

%files -n lib%name
%doc *.txt
%_libdir/*.so.*

%files -n lib%name-devel
%doc *.c f/*.f
%_libdir/*.so

%changelog
* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1-alt1
- Initial build for Sisyphus

