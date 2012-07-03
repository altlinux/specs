%define somver 0
%define sover %somver.1.2
Name: otf
License: BSD
Group: Development/Tools
Summary: Tools and library for support the Open Trace Format (OTF)
Version: 1.2.18
Release: alt5
Url: http://www.paratools.com/otf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.paratools.com/otf/llnl/OTF-SRC-1.2.18.tar.gz

BuildPreReq: gcc-c++

%description
The Open Trace Format (OTF) is a new trace definition and representation for use
with large-scale parallel platforms. OTF addresses three objectives: openness,
flexibility, and performance.

%package doc
Summary: Documentation for OTF tools
Group: Documentation
BuildArch: noarch

%description doc
The Open Trace Format (OTF) is a new trace definition and representation for use
with large-scale parallel platforms. OTF addresses three objectives: openness,
flexibility, and performance.

This package contains documentation for OTF tools.

%package -n lib%name
Summary: Shared library of Open Trace Format (OTF)
Group: System/Libraries

%description -n lib%name
The Open Trace Format (OTF) is a new trace definition and representation for use
with large-scale parallel platforms. OTF addresses three objectives: openness,
flexibility, and performance.

This package contains static development files for OTF.

%package -n lib%name-devel
Summary: Development files for Open Trace Format (OTF)
Group: Development/C++
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
The Open Trace Format (OTF) is a new trace definition and representation for use
with large-scale parallel platforms. OTF addresses three objectives: openness,
flexibility, and performance.

This package contains development files for OTF.

%package -n lib%name-devel-static
Summary: Static library for Open Trace Format (OTF)
Group: Development/C++
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
The Open Trace Format (OTF) is a new trace definition and representation for use
with large-scale parallel platforms. OTF addresses three objectives: openness,
flexibility, and performance.

This package contains static library for OTF.

%package -n lib%name-devel-doc
Summary: Development documentation for Open Trace Format (OTF) library
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The Open Trace Format (OTF) is a new trace definition and representation for use
with large-scale parallel platforms. OTF addresses three objectives: openness,
flexibility, and performance.

This package contains development documentation for OTF library.

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure
%make_build

%install
%makeinstall_std

install -m755 tools/otfdump/otfdump %buildroot%_bindir

pushd tools/otfcompress
%make_build
install -m755 otfcompress %buildroot%_bindir
popd

install -d %buildroot%_docdir/%name
install -d %buildroot%_docdir/%name-api
install -p -m644 docu/tools/otftools.pdf %buildroot%_docdir/%name
install -p -m644 docu/api/specification.pdf %buildroot%_docdir/%name-api

# shared library

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
ar x ../lib%name.a
g++ -shared * \
	-Wl,-soname,lib%name.so.%somver -o ../lib%name.so.%sover
rm -f *
popd
rmdir tmp
ln -s lib%name.so.%sover lib%name.so.%somver
ln -s lib%name.so.%somver lib%name.so
popd

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%_bindir/*

%files doc
%_docdir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/%name-api

%changelog
* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt5
- Rebuilt for debuginfo

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt4
- Rebuilt without rpm-build-compat and with gcc4.4

* Tue Sep 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt3
- Added shared library

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt2
- Rebuild with PIC

* Tue May 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.18-alt1
- Initial build for Sisyphus

