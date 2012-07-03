Name: niftilib
Version: 0.20100720
Release: alt4
Summary: A set of i/o libraries for reading and writing nifti-1 files
License: Public
Group: File tools
Url: http://niftilib.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -z3 -d:pserver:anonymous@niftilib.cvs.sourceforge.net:/cvsroot/niftilib co -P Clibs
Source: %name-%version.tar.gz
Source1: CMakeCache.txt

Requires: lib%name = %version-%release

BuildPreReq: cmake gcc-c++ zlib-devel doxygen ctest

%description
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI
(fMRI) brain images.

%package -n lib%name
Summary: Shared libraries of Niftilib
Group: System/Libraries

%description -n lib%name
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI
(fMRI) brain images.

This package contains shared libraries of Niftilib.

%package -n lib%name-devel
Summary: Development files of Niftilib
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI
(fMRI) brain images.

This package contains development files of Niftilib.

%package -n lib%name-devel-doc
Summary: Documentation for Niftilib
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI
(fMRI) brain images.

This package contains development documentation for Niftilib.

%package examples
Summary: Examples for Niftilib
Group: Development/Documentation
Requires: lib%name = %version-%release

%description examples
Niftilib is a set of i/o libraries for reading and writing files in the
nifti-1 data format. nifti-1 is a binary file format for storing medical
image data, e.g. magnetic resonance image (MRI) and functional MRI
(fMRI) brain images.

This package contains examples for Niftilib.

%prep
%setup
install -m644 %SOURCE1 .

%build
ls examples >EXAMPLES_FILES

cmake \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	.
%make_build VERBOSE=1

pushd docs
doxygen Doxy_nifti.txt
popd

%install
%makeinstall_std

if [ ! -d %buildroot%_libdir ]; then
	install -d %buildroot%_libdir
	mv %buildroot%_libexecdir/* %buildroot%_libdir/
fi

install -d %buildroot%_docdir/lib%name-devel/examples
install -d %buildroot%_man3dir
cp -fR docs/html/* %buildroot%_docdir/lib%name-devel
install -m644 docs/man/man3/* %buildroot%_man3dir

pushd examples
cp $(cat ../EXAMPLES_FILES) \
	%buildroot%_docdir/lib%name-devel/examples/
popd
sed -i 's|^|%_docdir/lib%name-devel/examples/|' EXAMPLES_FILES

%files
%doc LICENSE Updates.txt
%_bindir/*
%exclude %_bindir/fsl_api_driver

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%_docdir/lib%name-devel
%exclude %_docdir/lib%name-devel/examples
%_man3dir/*

%files examples -f EXAMPLES_FILES
%_bindir/fsl_api_driver
%dir %_docdir/lib%name-devel/examples

%changelog
* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20100720-alt4
- Fixed build

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20100720-alt3
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20100720-alt2
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20100720-alt1
- New snapshot
- Rebuilt for soname set-versions

* Thu Jul 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20100428-alt1.cvs20100428
- New snapshot

* Thu Sep 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20090303.1-alt1.cvs20090924
- Initial build for Sisyphus

