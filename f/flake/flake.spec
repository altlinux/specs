%def_enable shared
%def_enable static

%define Name Flake
Name: flake
%define lname lib%name
Version: 0.11.5
Release: alt1.svn20090830
Summary: FLAC audio encoder
License: %lgpl2plus
Group: Sound
URL: http://%name-enc.sourceforge.net/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: cmake subversion libsndfile-devel

%description
The purpose of %Name is to be an alternative to the FLAC reference
encoder with the goal of increasing encoding speed and implementing
experimental features.


%if_enabled shared
%package -n %lname
Summary: %Name shared library
Group: System/Libraries

%description -n %lname
The purpose of %Name is to be an alternative to the FLAC reference
encoder with the goal of increasing encoding speed and implementing
experimental features.

This package includes shared %Name library.
%endif


%package -n %lname-devel
Summary: Development files of %Name
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
The purpose of %Name is to be an alternative to the FLAC reference
encoder with the goal of increasing encoding speed and implementing
experimental features.

This package includes files needed to develop %Name-based software.


%if_enabled static
%package -n %lname-devel-static
Summary: Static %Name library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
The purpose of %Name is to be an alternative to the FLAC reference
encoder with the goal of increasing encoding speed and implementing
experimental features.

This package includes static %Name library.
%endif


%prep
%setup


%build
%define _optlevel 3
mkdir -p BUILD-%_target_platform
pushd BUILD-%_target_platform
cmake \
%ifarch x86_64
		-DLIB_SUFFIX=64 \
%endif
    -DCMAKE_SKIP_RPATH=YES \
    -DCMAKE_C_FLAGS="%optflags" \
    -DCMAKE_INSTALL_PREFIX=%buildroot%_prefix \
    -DCMAKE_VERBOSE_MAKEFILE=TRUE \
		-DCMAKE_STRIP:FILEPATH="/bin/echo" \
%if_enabled shared
    -DSHARED=ON \
%else
    -DSHARED=OFF \
%endif
%if_enabled static
    -DSTATIC=ON \
%else
    -DSTATIC=OFF \
%endif
    ..
%make_build
popd


%install
pushd BUILD-%_target_platform
%make_install install
popd


%files
%doc README Changelog TODO doc/*
%_bindir/%name


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_includedir/*
%{?_enable_shared:%_libdir/*.so}


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%changelog
* Sun Sep 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.5-alt1.svn20090830
- New snapshot

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.11.5-alt0.2.qa1
- NMU: rebuilt for debuginfo.

* Sun Mar 08 2009 Led <led@altlinux.ru> 0.11.5-alt0.2
- SVN revision 243

* Sat Nov 08 2008 Led <led@altlinux.ru> 0.11.5-alt0.1
- SVN revision 232
- build with shared %lname

* Sat Sep 08 2007 Led <led@altlinux.ru> 0.11-alt1
- 0.11
- fixed License

* Wed Dec 06 2006 Led <led@altlinux.ru> 0.10-alt1
- initial build
