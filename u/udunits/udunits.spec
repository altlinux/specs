Name: udunits
Version: 2.2.16
Release: alt1
Summary: Conversion of unit specifications between formatted and binary forms, etc
License: Open source
Group: Sciences/Physics
Url: http://www.unidata.ucar.edu/software/udunits/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libexpat-devel flex CUnit-devel gcc-fortran

Requires: lib%name = %version-%release

%description
UDUNITS supports conversion of unit specifications between formatted and
binary forms, arithmetic manipulation of units, and conversion of values
between compatible scales of measurement.

%package -n lib%name
Summary: Shared libraries of UDUNITS
Group: System/Libraries

%description -n lib%name
UDUNITS supports conversion of unit specifications between formatted and
binary forms, arithmetic manipulation of units, and conversion of values
between compatible scales of measurement.

This package contains shared libraries of UDUNITS.

%package -n lib%name-devel
Summary: Development files of UDUNITS
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
UDUNITS supports conversion of unit specifications between formatted and
binary forms, arithmetic manipulation of units, and conversion of values
between compatible scales of measurement.

This package contains development files of UDUNITS.

%package docs
Summary: Documentation for UDUNITS
Group: Documentation
BuildArch: noarch

%description docs
UDUNITS supports conversion of unit specifications between formatted and
binary forms, arithmetic manipulation of units, and conversion of values
between compatible scales of measurement.

This package contains documentation for UDUNITS.

%prep
%setup

rm -fR expat

%build
%autoreconf
%configure \
	--enable-static=no \
	--disable-udunits-1
%make_build

%install
%makeinstall_std

%check
%make check

%files
%doc ANNOUNCEMENT BACKLOG CHANGE_LOG COPYRIGHT README
%_bindir/*
%_datadir/%name
%_docdir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files docs
%doc *.html *.pdf */*.html */*.pdf
%_infodir/*

%changelog
* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.16-alt1
- Version 2.2.16

* Sat Jun 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.12-alt1
- Version 2.2.12

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.24-alt1
- Initial build for Sisyphus

