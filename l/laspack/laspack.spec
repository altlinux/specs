Name: laspack
Version: 1.12.2
Release: alt5
Summary: Solving large sparse systems of linear equations
License: BSD
Group: Sciences/Mathematics
Url: http://www.mgnet.org/mgnet/Codes/laspack/html/laspack.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

%description
LASPack is a package for solving large sparse systems of linear equations
like those which arise from discretization of partial differential equations.
It contains classical as well as selected state-of-the-art algorithms which
are commonly used for large sparse systems such as CG-like methods for
non-symmetric systems (CGN, GMRES, BiCG, QMR, CGS, and BiCGStab) and
multilevel methods such as multigrid and conjugate gradient method
preconditioned by multigrid and BPX preconditioners.

%package -n lib%name
Summary: Shared libraries of LASPack
Group: System/Libraries

%description -n lib%name
LASPack is a package for solving large sparse systems of linear equations
like those which arise from discretization of partial differential equations.
It contains classical as well as selected state-of-the-art algorithms which
are commonly used for large sparse systems such as CG-like methods for
non-symmetric systems (CGN, GMRES, BiCG, QMR, CGS, and BiCGStab) and
multilevel methods such as multigrid and conjugate gradient method
preconditioned by multigrid and BPX preconditioners.

This package contains shared libraries of LASPack.

%package -n lib%name-devel
Summary: Development files of LASPack
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
LASPack is a package for solving large sparse systems of linear equations
like those which arise from discretization of partial differential equations.
It contains classical as well as selected state-of-the-art algorithms which
are commonly used for large sparse systems such as CG-like methods for
non-symmetric systems (CGN, GMRES, BiCG, QMR, CGS, and BiCGStab) and
multilevel methods such as multigrid and conjugate gradient method
preconditioned by multigrid and BPX preconditioners.

This package contains development files of LASPack.

%package -n lib%name-devel-static
Summary: Static libraries of LASPack
Group: Development/C
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
LASPack is a package for solving large sparse systems of linear equations
like those which arise from discretization of partial differential equations.
It contains classical as well as selected state-of-the-art algorithms which
are commonly used for large sparse systems such as CG-like methods for
non-symmetric systems (CGN, GMRES, BiCG, QMR, CGS, and BiCGStab) and
multilevel methods such as multigrid and conjugate gradient method
preconditioned by multigrid and BPX preconditioners.

This package contains static libraries of LASPack.

%package -n lib%name-devel-doc
Summary: Documentation for LASPack
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
LASPack is a package for solving large sparse systems of linear equations
like those which arise from discretization of partial differential equations.
It contains classical as well as selected state-of-the-art algorithms which
are commonly used for large sparse systems such as CG-like methods for
non-symmetric systems (CGN, GMRES, BiCG, QMR, CGS, and BiCGStab) and
multilevel methods such as multigrid and conjugate gradient method
preconditioned by multigrid and BPX preconditioners.

This package contains development documentation for LASPack.

%package examples
Summary: Examples for LASPack
Group: Development/Documentation

%description examples
LASPack is a package for solving large sparse systems of linear equations
like those which arise from discretization of partial differential equations.
It contains classical as well as selected state-of-the-art algorithms which
are commonly used for large sparse systems such as CG-like methods for
non-symmetric systems (CGN, GMRES, BiCG, QMR, CGS, and BiCGStab) and
multilevel methods such as multigrid and conjugate gradient method
preconditioned by multigrid and BPX preconditioners.

This package contains examples for LASPack.

%prep
%setup

%build
%ifarch x86_64
sed -i 's|^\(ARCH_EXT\).*|\1 = 64|' \
	xc/makefile laspack/makefile
%endif

pushd xc
%make_build
popd
pushd laspack
%make_build
popd

%install
install -d %buildroot%_libdir
install -d %buildroot%_includedir/xc
install -d %buildroot%_includedir/laspack

pushd xc
%makeinstall_std
popd
pushd laspack
%makeinstall_std
popd

rmdir %buildroot%_includedir/*.old

for i in lastest matropt mlstest vectopt
do
	pushd laspack/examples/$i
%ifarch x86_64
	sed -i 's|^\(ARCH_EXT\).*|\1 = 64|' makefile
%endif
	%make_build DESTDIR=%buildroot
	popd
done

rm -f $(find laspack/examples -name '*.o')
install -d %buildroot%_libdir/%name
cp -fR laspack/examples %buildroot%_libdir/%name/

install -d %buildroot%_docdir/lib%name-devel-%version
cp -fR laspack/doc/* laspack/html \
	%buildroot%_docdir/lib%name-devel-%version/

# shared libraries

pushd %buildroot%_libdir
for i in xc laspack; do
	ar x lib$i.a
	gcc -shared *.o -lm \
		-Wl,-soname,lib$i.so.0 -o lib$i.so.0
	ln -s lib$i.so.0 lib$i.so
	rm -f *.o
done
popd

%files
%doc readme laspack/copyrght.h
%dir %_libdir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-devel-doc
%doc %_docdir/lib%name-devel-%version

%files examples
%dir %_libdir/%name
%_libdir/%name/examples

%changelog
* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.2-alt5
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.2-alt4
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.2-alt3
- Rebuilt for soname set-versions

* Thu Aug 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.2-alt2
- Added shared library

* Sat Jul 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.2-alt1
- Initial build for Sisyphus

