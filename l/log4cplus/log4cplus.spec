Name: log4cplus
Version: 1.1.1
Release: alt1.rc3
Summary: Logging library to C++
License: Apache License
Group: Development/C++
Url: http://log4cplus.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ doxygen graphviz

%description
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

%package -n lib%name
Summary: Shared libraries of logging library to C++
Group: System/Libraries

%description -n lib%name
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains shared libraries of log4cplus.

%package -n lib%name-devel
Summary: Development files of logging library to C++
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains development files of log4cplus.

%package -n lib%name-devel-docs
Summary: Development documentation for logging library to C++
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration.  It is modeled after the Java log4j API.

This package contains development documentation and manpages for
log4cplus.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-static=no \
	--enable-threads=yes \
	--with-working-c-locale
%make_build

pushd docs
doxygen doxygen.config
popd

%install
%makeinstall_std

install -d %buildroot%_man3dir
install -m644 docs/man/man3/* %buildroot%_man3dir

%check
%make check

%files -n lib%name
%doc AUTHORS ChangeLog NEWS README TODO REVISION
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-docs
%doc docs/html/*
%_man3dir/*

%changelog
* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.rc3
- Version 1.1.1-rc3

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

