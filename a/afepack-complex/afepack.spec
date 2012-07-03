%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname afepack
%define scalar_type complex
%define ldir %_libexecdir/petsc-%scalar_type

Name: %oname-%scalar_type
Version: 1.8
Release: alt12
Summary: C++ library for (adaptive) finite element developping (%scalar_type scalars)
License: GPLv2+
Group: Sciences/Mathematics
Url: http://dsec.pku.edu.cn/~rli/software_e.php
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://dsec.pku.edu.cn/~rli/AFEPack-snapshot.tar

BuildPreReq: python-module-petsc-config
BuildPreReq: %mpiimpl-devel libdealii-%scalar_type-devel libtbb-devel
BuildPreReq: doxygen boost-program_options-devel
BuildPreReq: texlive-latex-base chrpath

%description
AFEPack is a C++ library for adaptive finite element programming.

%package -n lib%name
Summary: Shared libraries of AFEPack
Group: System/Libraries

%description -n lib%name
AFEPack is a C++ library for adaptive finite element programming.

This package contains shared libraries of AFEPack of AFEPack.

%package templates
Summary: Set of Template elements for AFEPack
Group: Sciences/Mathematics
Requires: lib%name = %version-%release

%description templates
AFEPack is a C++ library for adaptive finite element programming.

This package contains a set of Template elements for AFEPack.

%package devel
Summary: Development files of AFEPack
Group: Development/C++
Requires: lib%name = %version-%release
Requires: %name-templates = %version-%release
Requires: libdealii-%scalar_type-devel
Requires: libtbb-devel boost-program_options-devel

%description devel
AFEPack is a C++ library for adaptive finite element programming.

This package contains development files of AFEPack.

%package examples
Summary: Examples for AFEPack
Group: Sciences/Mathematics
Requires: lib%name = %version-%release
Requires: %name-templates = %version-%release
Requires: libdealii-%scalar_type

%description examples
AFEPack is a C++ library for adaptive finite element programming.

This package contains examples for AFEPack.

%package -n %oname-devel-doc
Summary: Development documentation for AFEPack
Group: Development/Documentation
BuildArch: noarch

%description -n %oname-devel-doc
AFEPack is a C++ library for adaptive finite element programming.

This package contains development documentation AFEPack.

%prep
%setup -n AFEPack
rm -fR $(find ./ -name CVS)

pushd library/include
ln -s ../../../AFEPack/library AFEPack
pushd AFEPack/mpi
ln -s include/* ./
popd
popd
ln -s $PWD/library/include/*.h library/include/AFEPack

for i in $(find ./ -type f); do
	sed -i 's|\-O3|-O3 -g|g' $i
done

%build
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure
%make_build

TOPDIR=$PWD
pushd example
%make_build TOPDIR=$TOPDIR \
	ADDLIBS="-L$TOPDIR/library/lib -lAFEPack"
popd

%install
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%makeinstall_std prefix=%buildroot%ldir

# delete unreleased templates

rm -fR %buildroot%ldir/AFEPack/template/triangle/triangle.edge.Full.1*

# headers

mv %buildroot%ldir/include/AFEPack %buildroot%ldir/include/_
install -d %buildroot%ldir/include/AFEPack/mpi
mv %buildroot%ldir/include/_/*.h %buildroot%ldir/include/AFEPack/
rm -fR %buildroot%ldir/include/_
install -p -m644 library/mpi/include/*.h \
	%buildroot%ldir/include/AFEPack/mpi/

# examples

install -d %buildroot%ldir/examples/AFEPack
cp -fR example/* %buildroot%ldir/examples/AFEPack/
rm -f $(find %buildroot%ldir/examples/AFEPack -name '*.o') \
	$(find %buildroot%ldir/AFEPack -name '*.o')

# avoid mans' conflicts

pushd %buildroot%_man3dir
for i in details Functional std_map boost Geometry; do
	mv $i.3 %oname-$i.3
done
popd

for i in %buildroot%ldir/lib/*.so %buildroot%ldir/examples/AFEPack/*/*
do
	chrpath -r %mpidir/lib:%ldir/lib $i ||:
done

%files -n lib%name
%doc AUTHORS ChangeLog NEWS README TODO
%ldir/lib/*.so

%files templates
%ldir/AFEPack

%files devel
%ldir/include/*

%files examples
%dir %ldir/examples
%ldir/examples/*

%if "%scalar_type" == "real"
%files -n %oname-devel-doc
%doc %_docdir/AFEPack*
%doc %_man3dir/*
%endif

%changelog
* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt12
- New snapshot

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt11
- Fixed RPATH

* Sun Dec 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt10
- New snapshot

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt9
- Rebuilt with PETSc 3.2

* Tue Aug 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt8
- Rebuilt with new deal.II

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt7
- New snapshot

* Sun May 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt6
- New snapshot

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt5
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt4
- Restored optimization

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt3
- Rebuilt for debuginfo

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt2
- Initial build for Sisyphus

