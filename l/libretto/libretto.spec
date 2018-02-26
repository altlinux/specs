Name: libretto
Version: 2.1
Release: alt2
Summary: Library of easy-to-use generic container types for C
License: LGPL v2+
Group: Sciences/Mathematics
Url: http://pobox.com/~aaronc/tech/libretto/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://www.ibiblio.org/pub/linux/libs/libretto-2.1.tar.gz
Source: %name-%version.tar

BuildPreReq: libX11-devel

%description
Libretto is a library of easy-to-use generic container types for C,
together with some more-or-less random utility functions, though once
upon a time it thought it only had the utility functions, and back then
they were even more random than they are now.

%package -n lib%name
Summary: Library of easy-to-use generic container types for C
Group: System/Libraries

%description -n lib%name
Libretto is a library of easy-to-use generic container types for C,
together with some more-or-less random utility functions, though once
upon a time it thought it only had the utility functions, and back then
they were even more random than they are now.

%package -n lib%name-devel
Summary: Development files of Libretto
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Libretto is a library of easy-to-use generic container types for C,
together with some more-or-less random utility functions, though once
upon a time it thought it only had the utility functions, and back then
they were even more random than they are now.

This package contains development files of Libretto.

%package -n lib%name-devel-doc
Summary: Documentation for Libretto
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Libretto is a library of easy-to-use generic container types for C,
together with some more-or-less random utility functions, though once
upon a time it thought it only had the utility functions, and back then
they were even more random than they are now.

This package contains development documentation for Libretto.

%prep
%setup

touch AUTHORS

%build
%autoreconf
%configure \
	--enable-static=no
%make_build

%make -C doc %name.html

%install
%makeinstall_std

%files -n lib%name
%doc ANNOUNCE ChangeLog HISTORY NEWS README TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-doc
%doc doc/%name.html/*
%_infodir/*

%changelog
* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt2
- Rebuilt for debuginfo

* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1
- Initial build for Sisyphus

