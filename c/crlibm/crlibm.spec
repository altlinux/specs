%define sover 1
Name: crlibm
Version: 1.0beta4
Release: alt2
Summary: Correctly Rounded mathematical library
License: LGPL
Group: Sciences/Mathematics
Url: http://lipforge.ens-lyon.fr/www/crlibm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libmpfr-devel libgmp-devel
BuildPreReq: texlive-latex-base texlive-base-bin texlive-publishers

%description
CRlibm, an efficient and proven correctly-rounded mathematical library.

CRlibm is a free mathematical library (libm) which provides:

* implementations of the double-precision C99 standard elementary
  functions,
* correctly rounded in the four IEEE-754 rounding modes,
* with a comprehensive proof of both the algorithms used and their
  implementation,
* sufficiently efficient in average time, worst-case time, and memory
  consumption to replace existing libms transparently.

%package -n lib%name
Summary: Correctly Rounded mathematical library
Group: System/Libraries

%description -n lib%name
CRlibm, an efficient and proven correctly-rounded mathematical library.

CRlibm is a free mathematical library (libm) which provides:

* implementations of the double-precision C99 standard elementary
  functions,
* correctly rounded in the four IEEE-754 rounding modes,
* with a comprehensive proof of both the algorithms used and their
  implementation,
* sufficiently efficient in average time, worst-case time, and memory
  consumption to replace existing libms transparently.

%package -n lib%name-devel
Summary: Development files of Correctly Rounded mathematical library
Group: Development/C
Requires: lib%name = %EVR
Conflicts: libscs-devel

%description -n lib%name-devel
CRlibm, an efficient and proven correctly-rounded mathematical library.

CRlibm is a free mathematical library (libm) which provides:

* implementations of the double-precision C99 standard elementary
  functions,
* correctly rounded in the four IEEE-754 rounding modes,
* with a comprehensive proof of both the algorithms used and their
  implementation,
* sufficiently efficient in average time, worst-case time, and memory
  consumption to replace existing libms transparently.

This package contains development files of CRlibm.

%package -n lib%name-devel-doc
Summary: Documentation for Correctly Rounded mathematical library
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
CRlibm, an efficient and proven correctly-rounded mathematical library.

CRlibm is a free mathematical library (libm) which provides:

* implementations of the double-precision C99 standard elementary
  functions,
* correctly rounded in the four IEEE-754 rounding modes,
* with a comprehensive proof of both the algorithms used and their
  implementation,
* sufficiently efficient in average time, worst-case time, and memory
  consumption to replace existing libms transparently.

This package contains documentation for CRlibm.

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure \
%ifarch x86_64
	--enable-sse2 \
%endif
	--enable-mpfr \
	--enable-gmp \
	--with-gmp-include=%_includedir \
	--with-gmp-lib=%_libdir \
	--with-mpfr-include=%_includedir \
	--with-mpfr-lib=%_libdir
%make_build
%make doc

%install
%makeinstall_std

# shared libraries
pushd %buildroot%_libdir
for i in crlibm scs; do
	gcc -shared -Wl,--whole-archive lib$i.a -Wl,--no-whole-archive \
		-lmpfr -lgmp \
		-Wl,-soname=lib$i.so.%sover -o lib$i.so.%sover
	ln -s lib$i.so.%sover lib$i.so
done
popd

%files -n lib%name
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-doc
%doc docs/*.pdf

%changelog
* Sat May 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0beta4-alt2
- Avoid conflict with libscs

* Fri May 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0beta4-alt1
- Initial build for Sisyphus

