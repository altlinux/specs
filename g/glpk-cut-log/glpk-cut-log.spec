Name: glpk-cut-log
Version: 4.52
Release: alt1.git20140616
Summary: A fork of glpk with additional logging features for how cuts were generated
License: GPLv3
Group: Sciences/Mathematics
Url: https://github.com/timothy-king/glpk-cut-log
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/timothy-king/glpk-cut-log.git
Source: %name-%version.tar

BuildPreReq: zlib-devel libgmp-devel libltdl-devel

Conflicts: glpk glpk36
Requires: lib%name = %EVR

%description
A fork of glpk that includes additional logging features for how cuts
were generated.

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
A fork of glpk that includes additional logging features for how cuts
were generated.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Conflicts: libglpk-devel libglpk36-devel
Requires: lib%name = %EVR

%description -n lib%name-devel
A fork of glpk that includes additional logging features for how cuts
were generated.

This package contains development files of %name.

%prep
%setup

%build
%add_optflags %optflags_shared -fno-strict-aliasing
%autoreconf
%configure \
	--enable-static=no \
	--includedir=%_includedir/%name \
	--enable-dl \
	--with-gmp \
	--with-zlib
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README* THANKS
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.52-alt1.git20140616
- Initial build for Sisyphus

